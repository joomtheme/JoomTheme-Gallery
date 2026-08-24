#!/usr/bin/env python3
"""Validate the public JoomTheme Gallery Joomla update service."""

from __future__ import annotations

import argparse
import hashlib
import io
import re
import sys
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path, PurePosixPath
from xml.etree import ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
UPDATES_DIR = ROOT / "updates"
UPDATE_XML = UPDATES_DIR / "update.xml"
CHANGELOG_XML = UPDATES_DIR / "changelog.xml"
REQUIRED_UPDATE_FIELDS = ("name", "element", "type", "version", "downloads", "targetplatform")
HASHES = ("sha256",)
EXPECTED_ELEMENT = "pkg_jtgallery"
EXPECTED_TYPE = "package"
REPOSITORY_URL = "https://github.com/joomtheme/JoomTheme-Gallery"


class ValidationError(RuntimeError):
    """Raised when a release invariant is broken."""


def fail(message: str) -> None:
    raise ValidationError(message)


def parse_xml(path: Path) -> ET.Element:
    try:
        return ET.parse(path).getroot()
    except (OSError, ET.ParseError) as exc:
        fail(f"Cannot parse {path.relative_to(ROOT)}: {exc}")


def node_text(parent: ET.Element, tag: str) -> str:
    node = parent.find(tag)

    if node is None or node.text is None or not node.text.strip():
        fail(f"Missing or empty <{tag}> element")

    value = node.text.strip()

    if node.text != value:
        fail(f"Whitespace surrounds the <{tag}> value")

    return value


def safe_zip_members(archive: zipfile.ZipFile, label: str) -> None:
    names: set[str] = set()

    for item in archive.infolist():
        name = item.filename
        path = PurePosixPath(name)

        if not name or name in names:
            fail(f"{label} contains an empty or duplicate member: {name!r}")

        if path.is_absolute() or ".." in path.parts or "\\" in name:
            fail(f"{label} contains an unsafe member path: {name}")

        names.add(name)


def xml_from_zip(archive: zipfile.ZipFile, path: str, label: str) -> ET.Element:
    try:
        return ET.fromstring(archive.read(path))
    except KeyError:
        fail(f"{label} is missing {path}")
    except ET.ParseError as exc:
        fail(f"Cannot parse {path} in {label}: {exc}")


def verify_hashes(package_path: Path, update: ET.Element) -> None:
    payload = package_path.read_bytes()

    for algorithm in HASHES:
        expected = node_text(update, algorithm).lower()
        actual = hashlib.new(algorithm, payload).hexdigest()

        if expected != actual:
            fail(f"{algorithm.upper()} mismatch for {package_path.name}")


def verify_remote_package(download_url: str, package_path: Path) -> None:
    request = urllib.request.Request(download_url, headers={"User-Agent": "JoomTheme-Release-Validator"})

    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            payload = response.read()
    except OSError as exc:
        fail(f"Cannot download the published release asset: {exc}")

    if payload != package_path.read_bytes():
        fail("Published GitHub Release asset does not match the validated repository package")


def verify_changelog(version: str) -> None:
    root = parse_xml(CHANGELOG_XML)

    if root.tag != "changelogs":
        fail("changelog.xml root must be <changelogs>")

    entries: set[tuple[str, str, str]] = set()

    for item in root.findall("changelog"):
        entries.add((node_text(item, "element"), node_text(item, "type"), node_text(item, "version")))

    required = {
        ("pkg_jtgallery", "package", version),
        ("com_jtgallery", "component", version),
        ("mod_jtgallery", "module", version),
    }
    missing = required - entries

    if missing:
        fail(f"changelog.xml is missing current release entries: {sorted(missing)}")


def verify_package(package_path: Path, version: str) -> None:
    with zipfile.ZipFile(package_path) as package:
        safe_zip_members(package, package_path.name)
        manifest = xml_from_zip(package, "pkg_jtgallery.xml", package_path.name)

        if manifest.tag != "extension" or manifest.get("type") != "package":
            fail("Package manifest must be an <extension type='package'> document")

        if node_text(manifest, "packagename") != "jtgallery":
            fail("Package manifest <packagename> must be jtgallery")

        if node_text(manifest, "version") != version:
            fail("Package manifest version does not match update.xml")

        update_server = manifest.find("./updateservers/server")
        changelog_url = manifest.find("changelogurl")

        if update_server is None or (update_server.text or "").strip() != (
            "https://raw.githubusercontent.com/joomtheme/JoomTheme-Gallery/main/updates/update.xml"
        ):
            fail("Package manifest does not register the canonical update feed")

        if changelog_url is None or (changelog_url.text or "").strip() != (
            "https://raw.githubusercontent.com/joomtheme/JoomTheme-Gallery/main/updates/changelog.xml"
        ):
            fail("Package manifest does not register the canonical changelog")

        required_members = {
            "constituents/com_jtgallery.zip",
            "constituents/mod_jtgallery.zip",
            "language/en-GB/pkg_jtgallery.sys.ini",
            "language/tr-TR/pkg_jtgallery.sys.ini",
        }
        missing_members = required_members - set(package.namelist())

        if missing_members:
            fail(f"Package is missing required members: {sorted(missing_members)}")

        nested = (
            ("constituents/com_jtgallery.zip", "jtgallery.xml", "component", "com_jtgallery"),
            ("constituents/mod_jtgallery.zip", "mod_jtgallery.xml", "module", "mod_jtgallery"),
        )

        for archive_name, manifest_name, extension_type, element in nested:
            with zipfile.ZipFile(io.BytesIO(package.read(archive_name))) as child:
                safe_zip_members(child, archive_name)
                child_manifest = xml_from_zip(child, manifest_name, archive_name)

                if child_manifest.get("type") != extension_type:
                    fail(f"{manifest_name} has the wrong extension type")

                if node_text(child_manifest, "version") != version:
                    fail(f"{manifest_name} version does not match update.xml")

                if extension_type == "component" and node_text(child_manifest, "element") != element:
                    fail(f"{manifest_name} has the wrong element")

                if extension_type == "module" and child_manifest.find("files/folder[@module='mod_jtgallery']") is None:
                    fail("Module manifest does not identify mod_jtgallery")


def main(check_remote: bool = False) -> int:
    root = parse_xml(UPDATE_XML)

    if root.tag != "updates":
        fail("update.xml root must be <updates>")

    updates = root.findall("update")

    if len(updates) != 1:
        fail("update.xml must advertise exactly one unified package release")

    update = updates[0]

    for field in REQUIRED_UPDATE_FIELDS:
        if update.find(field) is None:
            fail(f"update.xml is missing <{field}>")

    if node_text(update, "element") != EXPECTED_ELEMENT or node_text(update, "type") != EXPECTED_TYPE:
        fail("update.xml must advertise pkg_jtgallery as a package")

    version = node_text(update, "version")
    download_url = node_text(update.find("downloads"), "downloadurl")
    parsed_url = urllib.parse.urlparse(download_url)
    expected_name = f"pkg_jtgallery_v{version}.zip"
    expected_release_url = f"{REPOSITORY_URL}/releases/tag/v{version}"
    expected_download_url = f"{REPOSITORY_URL}/releases/download/v{version}/{expected_name}"
    package_name = PurePosixPath(parsed_url.path).name

    if node_text(update, "infourl") != expected_release_url:
        fail(f"infourl must point to {expected_release_url}")

    if download_url != expected_download_url:
        fail(f"Primary download must point to {expected_download_url}")

    if package_name != expected_name:
        fail(f"Download filename must be {expected_name}")

    package_path = UPDATES_DIR / package_name

    if not package_path.is_file():
        fail(f"Referenced package does not exist: updates/{package_name}")

    platform = update.find("targetplatform")
    platform_pattern = platform.get("version", "") if platform is not None else ""

    try:
        if not re.match(platform_pattern, "6.1.3"):
            fail("targetplatform does not match Joomla 6.1.3")
    except re.error as exc:
        fail(f"Invalid targetplatform regular expression: {exc}")

    if node_text(update, "php_minimum") != "8.3.0":
        fail("php_minimum must remain 8.3.0 for this release line")

    verify_hashes(package_path, update)
    verify_package(package_path, version)
    verify_changelog(version)

    if check_remote:
        verify_remote_package(download_url, package_path)

    print(f"Validated JoomTheme Gallery {version}: XML, package manifests and SHA-256 checksum are correct.")

    if check_remote:
        print("Validated published GitHub Release asset: remote and repository packages are byte-for-byte identical.")

    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
