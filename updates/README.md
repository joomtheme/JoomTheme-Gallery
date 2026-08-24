# Joomla update service

This directory is the public update endpoint for JoomTheme Gallery.

| File | Purpose |
| --- | --- |
| `update.xml` | Joomla extension update metadata and package checksums |
| `changelog.xml` | Changelog displayed by Joomla's extension manager |
| `pkg_jtgallery_vX.Y.Z.zip` | Exact local mirror of the installable GitHub Release asset |

Public endpoints:

- `https://raw.githubusercontent.com/joomtheme/JoomTheme-Gallery/main/updates/update.xml`
- `https://raw.githubusercontent.com/joomtheme/JoomTheme-Gallery/main/updates/changelog.xml`
- `https://github.com/joomtheme/JoomTheme-Gallery/releases/latest`

## Publishing a release

1. Set the same semantic version in the package, component and module manifests.
2. Build the component and module archives, then place them in the unified package.
3. Generate SHA-256, SHA-384 and SHA-512 values, then keep the exact package ZIP in this directory for repository-side validation.
4. Create the `vX.Y.Z` Git tag and GitHub Release, and attach the same package ZIP as a release asset.
5. Update the version, release information URL, release-asset download URL, compatibility rules and checksums in `update.xml`.
6. Add matching package, component and module records to `changelog.xml`.
7. Update the root `CHANGELOG.md` and both README download links.
8. Run `python3 tools/validate_release.py --check-remote` and confirm the GitHub Actions check passes.
9. Test Joomla's **Check for Updates**, changelog display and update installation on a disposable site.

The download URL must stay on one line and point to the immutable asset below `/releases/download/vX.Y.Z/`. The update feed intentionally advertises the unified package so the component and module cannot drift to different versions.
