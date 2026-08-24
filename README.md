# JoomTheme Gallery

[Türkçe](README.tr-TR.md) · [Download 0.7.3](https://raw.githubusercontent.com/joomtheme/JoomTheme-Gallery/main/updates/pkg_jtgallery_v0.7.3.zip) · [Support](https://github.com/joomtheme/JoomTheme-Gallery/issues) · [JoomTheme](https://joomtheme.com)

JoomTheme Gallery is a native Joomla 6 gallery extension distributed as one installable package:

- `com_jtgallery` — gallery, category and image management with an Atum-aligned administrator interface.
- `mod_jtgallery` — a responsive site module for publishing selected gallery images.

The current stable release is **0.7.3**.

## Requirements

- Joomla 6.1.x (tested with Joomla 6.1.3)
- PHP 8.3 or later
- A Joomla-supported image processing environment with JPEG, PNG and WebP support

## Highlights

- Native Joomla MVC architecture, ACL, categories, access levels and multilingual filtering
- Responsive gallery layouts for Joomla's frontend template environment
- Atum-compatible administrator dashboard and list views
- Original, large, medium and thumbnail image variants
- Optional EXIF/GPS and appended metadata removal, enabled by default
- Keyboard- and touch-friendly lightbox with a softer Bootstrap-style backdrop
- Component and site module delivered in one Joomla package
- Joomla update-server and changelog integration

## Installation

1. Download [`pkg_jtgallery_v0.7.3.zip`](https://raw.githubusercontent.com/joomtheme/JoomTheme-Gallery/main/updates/pkg_jtgallery_v0.7.3.zip).
2. In Joomla Administrator, open **System → Install → Extensions**.
3. Upload the package. Joomla installs both the component and the site module.
4. Create a gallery, add images, then publish it through a menu item or a **JoomTheme Gallery** module.

Installing a newer package over an existing installation performs an in-place upgrade.

## Automatic updates

The package registers the following public Joomla services:

- Update feed: [`updates/update.xml`](https://raw.githubusercontent.com/joomtheme/JoomTheme-Gallery/main/updates/update.xml)
- Joomla changelog: [`updates/changelog.xml`](https://raw.githubusercontent.com/joomtheme/JoomTheme-Gallery/main/updates/changelog.xml)

Joomla checks the feed from **System → Update → Extensions** and validates the published package against SHA-256, SHA-384 and SHA-512 checksums before installation.

## Documentation and support

- [Release history](CHANGELOG.md)
- [Support guide](SUPPORT.md)
- [Contributing](CONTRIBUTING.md)
- [Security policy](SECURITY.md)
- [Issue tracker](https://github.com/joomtheme/JoomTheme-Gallery/issues)

Please report security vulnerabilities privately as described in the security policy.

## License

GNU General Public License version 2 or later. See [LICENSE](LICENSE).
