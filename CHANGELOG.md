# Changelog

All notable changes to JoomTheme Gallery are documented here. The machine-readable Joomla changelog is published at [`updates/changelog.xml`](updates/changelog.xml).

## [0.7.3](https://github.com/joomtheme/JoomTheme-Gallery/releases/tag/v0.7.3) — 2026-08-24

### Fixed

- Added the package system-language files required by JED validation.
- Added package author email and website metadata.
- Removed leading whitespace from external-link accessibility translations while preserving spoken separation in markup.

### Changed

- Aligned the component, module and unified package at version 0.7.3.

## 0.7.2 — 2026-08-24

### Added

- Added accessible Developer and GitHub Issues links to the administrator dashboard.
- Published the Joomla update and changelog feeds.

### Fixed

- Removed Joomla's unrelated generic Help button only from the JoomTheme Gallery Categories context.

## 0.7.1 — 2026-08-24

### Added

- Introduced the unified Joomla package containing the component and site module.

### Fixed

- Removed administrator-menu quick-task parameters rejected by the JED Checker manifest schema while retaining dashboard quick actions.

## 0.7.0 — 2026-08-24

### Added

- Rebuilt the administrator dashboard with Atum cards, metrics, ACL-aware quick actions and recent-item views.
- Added Joomla-native empty states, responsive list tables, access/language filters and category integration.

### Changed

- Moved dashboard queries and storage aggregation into a dedicated Joomla MVC model.

## 0.6.28 — 2026-08-24

### Fixed

- Fixed the administrator **New Gallery** action by removing duplicate list-form control fields.

## 0.6.27 — 2026-08-24

### Fixed

- Hardened administrator actions with Joomla CSRF tokens and POST-only cover selection.
- Added accessible control labels and fallback image-link labels.
- Changed the component lightbox to a softer Bootstrap-style 50% backdrop.
- Completed GPL file headers and synchronized Web Asset Manager versions.

## Earlier development releases

Versions 0.6.19–0.6.26 introduced secure image storage, image processing, metadata removal, categories, frontend routing and upload workflow fixes. The detailed historical component changelog remains included inside the component archive.
