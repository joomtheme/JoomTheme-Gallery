# Contributing

Thank you for helping improve JoomTheme Gallery.

## Before you start

- Use GitHub Issues for confirmed bugs and focused feature proposals.
- Keep security reports private; follow [SECURITY.md](SECURITY.md).
- Keep pull requests small enough to review and test independently.

## Development expectations

- Target Joomla 6.1.x and PHP 8.3 or later.
- Follow Joomla's MVC, Web Asset Manager, ACL, routing, language and coding conventions.
- Do not modify Joomla core files or depend on a specific third-party template.
- Preserve English (`en-GB`) and Turkish (`tr-TR`) language-key parity.
- Keep administrator output compatible with Atum and frontend output compatible with Joomla's core template environment.
- Preserve keyboard use, visible focus, meaningful labels and reduced-motion behavior.

## Testing a change

Test clean installation, upgrade installation and uninstall behavior on a disposable Joomla site. Exercise administrator galleries, images and categories; frontend menu views; the site module; ACL/access/language filtering; responsive layouts; and the lightbox.

For release-feed changes, run:

```bash
python3 tools/validate_release.py
```

The validator parses both XML files, inspects the package and nested extension manifests, and verifies all published checksums.

## Pull requests

Describe the problem, the chosen solution and the test environment. Link the relevant issue and include before/after screenshots for visible UI changes. Do not commit credentials, production data or generated local configuration.
