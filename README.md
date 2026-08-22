# Mayfair Properties & Developers

Gurugram-focused real estate **advisory** — WordPress (Hello Elementor + Elementor Pro + ACF + Mayfair Core), design system, and HTML source of truth.

Live site: [mayfairpropertiesdevelopers.com](https://mayfairpropertiesdevelopers.com)

**Not** a luxury developer showroom, not a property portal, not a Mumbai 1997 firm. Do not invent years, ₹ volumes, RERA, awards, or listings.

---

## Start here

| If you need… | Open |
|---|---|
| Locked colours & fonts | [`docs/MAYFAIR-THEME-LOCKED.md`](docs/MAYFAIR-THEME-LOCKED.md) |
| What is done vs what WP still needs | [`docs/PRODUCTION-AUDIT.md`](docs/PRODUCTION-AUDIT.md) |
| HTML website (preview) | [`site/`](site/) — `python3 -m http.server 8080` inside `site/` |
| Elementor Home | [`docs/elementor/ELEMENTOR-HOMEPAGE.md`](docs/elementor/ELEMENTOR-HOMEPAGE.md) |
| Elementor Single Property | [`docs/elementor/ELEMENTOR-PROPERTY-SINGLE.md`](docs/elementor/ELEMENTOR-PROPERTY-SINGLE.md) |
| Archives / filters layout | [`docs/MAYFAIR-LISTING-LAYOUT.md`](docs/MAYFAIR-LISTING-LAYOUT.md) |
| Folder map of this repo | [`docs/REPO-CONTENTS.md`](docs/REPO-CONTENTS.md) |

### Locked kit (do not drift)

- Type: **Source Serif 4** (headings) + **Inter** (body/UI)
- Colour: `#1A1A1A` · `#725B2F` · `#A68B5B` · `#444748` · `#F9F7F2` · `#F5F0E7`
- Header / Footer: Heritage Concierge — do not replace Theme Builder chrome
- Theme on live: **Hello Elementor** (not Astra)

Forbidden: `#111111` `#D4A43A` `#F8F6F1` Arima Mulish Lora Playfair as production type.

---

## Preview the HTML site

```bash
cd site
python3 -m http.server 8080 --bind 0.0.0.0
```

Then open `/` (Home), `/services.html`, `/properties.html`, `/property-single.html`, `/404.html`, etc.

Forms are front-end demos (`preventDefault`). On WordPress use **Mayfair — Save Lead** / **Save Site Visit** only.

---

## WordPress apply (short)

1. Do not change CPTs, ACF keys, or Core.
2. Do not replace Header / Footer templates.
3. Rebuild **Pages → Home** from `site/homepage.html`.
4. Theme Builder singles + archives from `site/*-single.html` and listing pages.
5. 301 duplicate Insights URLs (`/insights/`, `/blogs/`, `/articles/`) to one slug.
6. Publish real Property / Project / Insight posts — loops stay empty until then.

Full checklist: `docs/PRODUCTION-AUDIT.md`.

---

## Repo layout

```
brand/          Logos (canonical)
site/           Production HTML/CSS/JS preview
docs/           Locks, Elementor maps, audits, prompts
packages/       Plugin zips (Forms, Core-related packages)
archive/        Old root homepage + option studies
tools/          Page generator
```

Existing root clutter (zips, long logo filenames, stray screenshots) has been moved into these folders.
