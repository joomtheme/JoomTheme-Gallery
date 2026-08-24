# Joomla update service

This directory is the public update endpoint for JoomTheme Gallery.

| File | Purpose |
| --- | --- |
| `update.xml` | Joomla extension update metadata and package checksums |
| `changelog.xml` | Changelog displayed by Joomla's extension manager |
| `pkg_jtgallery_vX.Y.Z.zip` | Installable component + module package |

Public endpoints:

- `https://raw.githubusercontent.com/joomtheme/JoomTheme-Gallery/main/updates/update.xml`
- `https://raw.githubusercontent.com/joomtheme/JoomTheme-Gallery/main/updates/changelog.xml`

## Publishing a release

1. Set the same semantic version in the package, component and module manifests.
2. Build the component and module archives, then place them in the unified package.
3. Add the package ZIP here without renaming it after checksum generation.
4. Update the version, download URL, compatibility rules and SHA-256/SHA-384/SHA-512 values in `update.xml`.
5. Add matching package, component and module records to `changelog.xml`.
6. Update the root `CHANGELOG.md` and download links.
7. Run `python3 tools/validate_release.py` and confirm the GitHub Actions check passes.
8. Test Joomla's **Check for Updates**, changelog display and update installation on a disposable site.

The download URL must stay on one line. The update feed intentionally advertises the unified package so the component and module cannot drift to different versions.
