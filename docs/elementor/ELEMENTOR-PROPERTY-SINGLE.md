# Elementor — Single Property (Theme Builder)

Live theme is **Hello Elementor**, not Astra. Do not switch themes.

**Template:** Theme Builder → Single → CPT `property` → one template for every property.

Do **not** edit Header / Footer. Do **not** change Core, CPT, taxonomies, or ACF keys.

HTML reference: `property-single.html` + `property-single.css`  
Kit: Source Serif 4 + Inter · `#1A1A1A` `#725B2F` `#A68B5B` `#F9F7F2` (see `MAYFAIR-THEME-LOCKED.md`).

**Not** Arima / Mulish / Lora — those were a drift.

REST: `GET /wp-json/wp/v2/properties` — count **0** on last check. Publish one real property to preview the template. Do not invent Sector / ₹ values to fill it.

---

## Conditions (hide empty)

Every extra widget: Advanced → Dynamic / Display conditions → **hide if ACF empty**.

Never print `-` or `₹ —` on the live single. The HTML preview uses field *names* as chrome only.

| UI | Source |
|---|---|
| H1 | Post title |
| Eyebrow | `property-type` |
| Excerpt / overview | Post excerpt + post content — hide section if both empty |
| Gallery | Featured image + media gallery (Core / ACF if present) |
| Location | taxonomy `location` |
| Type | `property-type` |
| Configuration | `mpd_bedrooms` |
| Area | `mpd_area_sqft` |
| Status | `property-status` |
| Price | `mpd_price` + `mpd_price_label` |
| Verification | `mpd_verified` — hide if false/empty |
| ID / baths / floor / furnishing / possession / locality | matching `mpd_*` — hide if empty |
| Brochure button | `mpd_brochure` URL — hide if empty |
| Floor plan section | `mpd_floor_plan` |
| Video section | `mpd_video_url` |
| Map section | `mpd_latitude` + `mpd_longitude` — OpenStreetMap embed or Core map. No fake pin. |
| Related | Loop Grid `property`, same location or type, exclude current, 3. Hide section if empty. |

No amenities section — there is no amenities ACF.

---

## Layout

1. Parent boxed ~1120px (site 1280, inner editorial narrower). **No fixed height** on the parent.
2. Two columns desktop: media 1.15 / spec 0.85. Spec `sticky` under header.
3. Gallery: object-fit cover, 4:3, thumbs, radius 0–2px.
4. Spec = editorial sheet, thin `#E5E1D8` rules, Inter 11px labels, Source Serif values.
5. CTAs: Discuss → `/consult-with-us/` · Call `tel:+919873712902` · WhatsApp existing Core if present. **No new form plugin.**
6. On a single page do **not** use “View Property” (self-link). Use Discuss / Call.
7. Tablet: stack, spec after intro. Mobile: gallery → intro → spec → sections. Buttons full width.

---

## After publish

1. Add **one real** Property in WP (real photo, real fields you can stand behind).
2. Open the permalink — Theme Builder single should apply.
3. Empty ACF must not leave blank rows.
4. Header/footer unchanged.
5. Purge LiteSpeed.

Cannot apply Theme Builder from this sandbox (no wp-admin). Rebuild from this file on **Pages is wrong** — use **Theme Builder → Single**.
