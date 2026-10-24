# Atharva OS / System 01

The profile uses GitHub-compatible Markdown, native links, script-free SVGs and one finite GIF. No external image services, remote fonts, JavaScript, embedded HTML in SVG, or fake metrics are required. Every SVG is fully visible without animation. The GIF plays once; all information is also available in static art or text. The design uses system monospace fonts with phosphor green, warm gold, and a dark forest background.

`scripts/build_profile.py` is the shared source for all artwork, including the root compatibility assets. The three original generator entry points remain usable and delegate to it. Mobile picture sources switch at 600px; the narrow activity view shows recent weeks, with a link to GitHub's complete calendar. Text project descriptions and contact links stay native Markdown/HTML for keyboard navigation and screen readers. GIF text is decorative and repeated elsewhere.

## Regenerate

```sh
python -m pip install -r scripts/requirements.txt
python scripts/fetch_contributions.py
python scripts/build_profile.py
python -m unittest discover -s scripts -p 'test_*.py'
python scripts/validate_profile.py
```

Run from the repository root. `GH_PROFILE_USER` defaults to Atharvanh. GitHub Actions sets it to the repository owner. The Pillow GIF renderer uses Consolas on Windows and DejaVu Sans Mono on Ubuntu. Glyph shapes can differ between these systems.

## Daily refresh

The scheduled workflow runs daily at 06:17 UTC (11:47 IST), and can also be started manually. GitHub may delay scheduled jobs or disable them after repository inactivity; see the Actions tab for actual status. Invalid or incomplete calendar data fails the job before replacing the stored JSON. Existing checked-in assets remain available. This is a public-HTML integration, so future GitHub markup changes may require parser maintenance.

Validation and pull requests use read-only repository permissions. Only the update job gets `contents: write`, commits an explicit generated-file allowlist, and pushes through the standard GitHub token. Checkout/setup actions are pinned to commit SHAs. No personal access token is stored in this repository. Push filters prevent generated-only commits from starting another update.

## Content evidence (checked 24 October 2026)

- [ZeroLabs](https://github.com/Atharvanh/new-zerolabs): public, non-fork; README documents JavaScript, Express, Gemini, Tailwind CSS and Three.js.
- [WelNest](https://github.com/Atharvanh/cep_project): public, non-fork; README and package describe React Native, Expo, TypeScript, barcode lookup, nutrition logging and reporting.
- [CETPredict](https://cetpredict.in): featured at the owner’s request, replacing AgriEdge. Description and Python, JavaScript, HTML/CSS, and JSON/data-parsing tags follow the portfolio screenshot supplied by the owner. The live URL is explicitly supplied by the owner.
- Python is also used by this profile's generators. No Next.js or GSAP claim is made without project evidence.
- [Canonical LinkedIn profile](https://in.linkedin.com/in/atharvaharale) is publicly indexed as Atharva Harale. The supplied path without `/in/` returns 404; LinkedIn may return anti-bot status 999 for automated direct requests.
- Portfolio and email were explicitly supplied by the owner. Portfolio HTTP response was 200 during validation; email is a mailto link, not a delivery claim.
- Contribution values come from [GitHub's public calendar](https://github.com/users/Atharvanh/contributions); they are contributions, not an invented commit count or skill rating.

## Rendering validation

The GitHub Markdown API preserves the picture elements, mobile media queries, images and real links. Validate the live profile after pushing because cache propagation and client rendering can vary. GitHub's [non-code-file documentation](https://docs.github.com/en/repositories/working-with-files/using-files/working-with-non-code-files) states that SVG scripting and animation are unsupported; therefore essential visibility never relies on either.
