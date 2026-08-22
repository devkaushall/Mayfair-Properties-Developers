# Production audit — 21 Aug 2026

## What this environment can and cannot do

**Cannot:** log into `wp-admin`, publish Elementor Theme Builder templates, wire Mayfair — Save Lead on the live Hostinger site, or flip Astra (the live theme is **Hello Elementor**).

**Did:** build a **complete, linked HTML website** in `mayfair-home/` that is the production design + IA + empty-state system. Apply it in Elementor from the map below. That is the deploy path.

A template file existing here ≠ live WordPress complete. Do not tell stakeholders the live site is finished until Theme Builder is published and one real property/project/insight exist.

---

## Live WordPress (inspected)

| Item | State |
|---|---|
| Theme | Hello Elementor (prompt said Astra — **do not switch**) |
| Kit-6 fonts | Source Serif 4 + Inter (prompt’s Arima/Mulish/Lora is **drift — ignore**) |
| Kit-6 colour | `#1A1A1A` `#725B2F` `#A68B5B` `#F9F7F2` (prompt’s `#111111` `#D4A43A` is **drift — ignore**) |
| Pages | 19 published (Home, About, Properties, Services, inner services, Projects, Gallery, Insights×3, Contact, etc.) |
| CPT `property` / `project` / `insight` | **0 / 0 / 0** |
| Posts | 0 |
| Header / Footer | Elementor Theme Builder — **do not replace** |
| Duplicate Insights URLs | `/insights/`, `/insights-2/`, `/blogs/`, `/articles/` — 301 to one URL in WP |
| Lead engine | Mayfair Core — use existing form actions only |

**Positioning lock (overrides the “decades / Luxury values” block in the last prompt):** Gurugram advisory. No invented decades, awards, volumes, RERA, luxury-developer claims.

---

## HTML site (this folder) — complete user journeys

| Journey | Files |
|---|---|
| Home → discover | `homepage.html` |
| Properties index → single | `properties.html` → `property-single.html` |
| Projects index → single | `projects.html` → `project-single.html` |
| Insights index → single | `insights.html` → `insight-single.html` |
| Services | `services.html` + `buy.html` `sell.html` `rent.html` `invest.html` `consult.html` |
| About / Contact / Gallery | `about.html` `contact.html` `gallery.html` |
| Search / 404 | `search.html` `404.html` |
| Type landings | `residential.html` `commercial.html` `upcoming.html` |

Header/footer identical chrome. Forms: `preventDefault` + note to bind **Mayfair — Save Lead / Save Site Visit**.

---

## Elementor apply order (you, in wp-admin)

1. Site Settings already kit-6 — do not paste the gold/Arima prompt.
2. **Do not touch** Header / Footer templates.
3. Pages → Home: rebuild from `homepage.html` / `ELEMENTOR-HOMEPAGE.md`.
4. Pages → Services: `services.html`.
5. Pages → About, Contact, Gallery, Consult, Buy, Sell, Rent, Invest: matching HTML.
6. Theme Builder **Single** `property` / `project` / `insight`.
7. Theme Builder **Archive** or page + Loop Grid for Properties / Projects / Insights (`MAYFAIR-LISTING-LAYOUT.md`).
8. Theme Builder Search + 404.
9. Loop items: editorial spec card (`ELEMENTOR-PROPERTY-SINGLE.md` + listing prompt). Hide empty ACF. No `-`.
10. Forms → existing Core actions only.
11. 301 `/insights/`, `/blogs/`, `/articles/` → `/insights-2/` (or the one URL you keep).
12. Publish **one real** property, project, insight — then test loops.
13. Reset kit H4 if still Playfair.
14. Purge LiteSpeed.

---

## Blockers (not invented around)

| Blocker | Why | Continue without |
|---|---|---|
| No wp-admin from this sandbox | Cannot click Publish | HTML + this map |
| CPT counts 0 | Cannot verify real cards | Empty states designed |
| `mpd_gallery` named in last prompt | Core may use featured + gallery; do not rename fields | Featured image + hide extra |
| No amenities ACF | Cannot build Features grid | Omit section |
| Duplicate insight pages | SEO | 301, don’t invent posts |
| Prompt vs locked kit | Conflicting fonts/colours | Kit-6 wins |

---

## Production-ready definition (honest)

**Ready as a design/implementation package:** yes.  
**Ready as a live WordPress site without human Elementor publish + real CPT content:** no.

That is the architecture constraint, not unfinished HTML.
