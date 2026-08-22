# Repository contents — what went where

Organised 22 Aug 2026. Everything new from the Arena workspace that was **not** already in GitHub `main`, plus a clean-up of files that were dumped at the repo root.

Nothing was pushed to GitHub from this environment (no write remotes / no `gh` login). The tree below is the local project, ready to commit and push.

---

## Root (kept small)

| Path | Role |
|---|---|
| `README.md` | How to preview, locks, apply order |
| `.gitignore` | Stock WordPress ignore (unchanged) |
| `docs/REPO-CONTENTS.md` | This file |

---

## `brand/` — logos (moved off root)

| File | Source |
|---|---|
| `logo-light.webp` | Copy of light-theme primary mark |
| `logo-dark.webp` | Copy of dark-theme secondary mark |
| `submark-light.webp` / `submark-dark.webp` | Submarks |
| `Primary_original_Logo_for_Light_theme-removebg-preview.webp` | Original filename, preserved |
| `Secondary_Logo_for_Dark_theme-removebg-preview.webp` | Original filename, preserved |
| `Submark_original_for_Light_theme-.webp` | Original filename, preserved |
| `Submark_for_Dark_theme-.webp` | Original filename, preserved |

---

## `site/` — production HTML website (new)

Preview this folder. Relative links; locked fonts only (Source Serif 4 + Inter).

### Pages

| File | Purpose |
|---|---|
| `index.html` | Same as homepage (server default) |
| `homepage.html` | Home — 9-section editorial |
| `about.html` | About (no invented decades) |
| `services.html` | Full services |
| `buy.html` `sell.html` `rent.html` `invest.html` `consult.html` | Service landings |
| `properties.html` | Property archive (desk + filters) |
| `property-single.html` | Single property Theme Builder ref |
| `projects.html` | Project archive |
| `project-single.html` | Single project |
| `upcoming.html` | Upcoming = filter note, not fake inventory |
| `insights.html` | Insight archive |
| `insight-single.html` | Single insight |
| `residential.html` `commercial.html` | Type landings |
| `gallery.html` | Gallery empty / Media-driven |
| `contact.html` | NAP + hours |
| `search.html` | Search results empty state |
| `404.html` | 404 |

### CSS / JS / assets

| File | Purpose |
|---|---|
| `home-prod.css` | Global kit + Home + chrome |
| `pages.css` | Inner pages, archives, 404, search |
| `services.css` | Services extras |
| `property-single.css` | Single property |
| `site.js` | Drawer + form demo |
| `fonts/source-serif-4-*.woff2` | Locked headings |
| `fonts/inter-*.woff2` | Locked UI |
| `img/hero-editorial.jpg` `consult-facade.jpg` `gurugram-street.jpg` `material-detail.jpg` `why-interior.jpg` | Editorial photography |
| `img/logo-light.webp` `logo-dark.webp` | Marks used by HTML |
| `img/hero.webp` `interior.webp` | Older stills |
| `img/villa.webp` `apt.webp` `comm.webp` | **Do not use on Home** (showroom). Kept only so old option files still resolve if copied. |

---

## `docs/` — decisions and Elementor handoff (new)

| File | Purpose |
|---|---|
| `MAYFAIR-THEME-LOCKED.md` | Colour + type lock (kit-6) |
| `PRODUCTION-AUDIT.md` | Honest WP vs HTML status; apply order |
| `MAYFAIR-LISTING-LAYOUT.md` | Desk layout = archives, not Home |
| `Mayfair-Properties-Developers-Digital-Assessment.md` | GMB / NAP / repo / live audit |
| `REPO-CONTENTS.md` | This map |

### `docs/elementor/`

| File | Purpose |
|---|---|
| `ELEMENTOR-HOMEPAGE.md` | Pages → Home only |
| `ELEMENTOR-SITE-SETTINGS.md` | Kit-6 globals |
| `ELEMENTOR-PROPERTY-SINGLE.md` | Theme Builder Single `property` |

### `docs/chrome/`

| File | Purpose |
|---|---|
| `Mayfair-Heritage-Concierge.html` | Locked header/footer preview |
| `Mayfair-Header-Footer-Gallery.html` | Five chrome options (historical) |
| `Mayfair-Header-Footer-Design-References.md` | Chrome notes |
| `PR-heritage-concierge.md` | PR body for chrome |

### `docs/prompts/`

Codex / agent prompts (copy-paste). Not production CSS.

| File | Purpose |
|---|---|
| `MAYFAIR-CODEX-PROMPT.md` | Implement locked Home |
| `MAYFAIR-CODEX-PROMPT-V2.md` | Alternate desk Home (rejected as Home) |
| `MAYFAIR-CODEX-PROMPT-LISTINGS.md` | Use desk layout on archives |

### `docs/references/`

Stakeholder screenshots (Elementor footer, mobile dock, Codex V2 desk page).

### `docs/type-specimen/`

Font comparison page (Playfair vs Source Serif 4 vs Arima). **Not** the production stack. Extra `.woff2` / `.ttf` live only here so `site/fonts` stays locked.

---

## `packages/` — already in GitHub, moved off root

| File | Notes |
|---|---|
| `mayfair-elementor-implementation-package-locked.zip` | Earlier locked Elementor pack |
| `mayfair-forms-leads.zip` | Mayfair Forms & Leads |
| `mayfair-implementation-assistant.zip` | Assistant |
| `mayfair-runtime-diagnostics.zip` | Diagnostics |

Unzip into WordPress plugins as before. Do not treat zips as the HTML source of truth (`site/` is).

---

## `archive/` — old root / studies

| Path | What |
|---|---|
| `mayfair-properties-html-homepage.html` | Previous GitHub homepage dump |
| `root-dump/` | `image.png`, `Screenshot 2026-08-19 165225.png` |
| `homepage-options/` | Options B–D + `styles.css` (consult-first / corridors / chapters) |

---

## `tools/`

| File | What |
|---|---|
| `build_pages.py` | Regenerates inner HTML pages with shared chrome |

---

## Not copied into the repo

| Item | Why |
|---|---|
| `mayfair-chrome-gallery/*.b64` | Raw base64; logos already in `brand/` |
| Live wp-admin / CPT posts | None exist; nothing to export |
| API keys | Never store keys in Git |

---

## Naming conventions going forward

- HTML/CSS for the public preview → `site/`
- Human docs → `docs/` (`SCREAMING-KEBAB` for locks, `ELEMENTOR-*` for builder maps)
- Logos → `brand/` (`logo-light`, `logo-dark`, `submark-*`)
- Plugin binaries → `packages/`
- Retired files → `archive/` (do not delete history, do not put back on root)
- No new files on the repository root except `README.md` and `.gitignore`
