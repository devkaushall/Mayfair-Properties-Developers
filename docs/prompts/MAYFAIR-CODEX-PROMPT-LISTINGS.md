# Codex prompt — Properties / Projects / Insights listing templates

Copy everything below the line into Codex.

---

You are **not** redesigning the Mayfair homepage.

The split “Advisor’s desk” layout (sticky left rail + scrolling right canvas) from the V2 screenshot is **locked for listing/index pages only**. The stakeholder rejected it as Home. Home stays the existing 9-section editorial page. Do **not** overwrite `mayfair-home/homepage.html`.

Build **three** archive templates that share one layout system.

---

## Hard locks

### Site Settings (Elementor kit-6) — do not invent tokens

- Ink `#1A1A1A` · Bronze `#725B2F` · Accent `#A68B5B` · Text `#444748`
- Ivory `#F9F7F2` · Cream `#F5F0E7` · Surface `#FFFFFF` · Border `#E5E1D8`
- Utility bar type `#FFDEA7` on `#1A1A1A`
- Headings **Source Serif 4** · Body/UI **Inter**
- Accent labels: Inter uppercase, not italic
- Radius **2–4px** · container **1280px** · CTA min-height 48px
- Body buttons: `#1A1A1A` fill. Header Call now stays bronze. Consult outline → `/consult-with-us/`
- Forbidden: `#111111` `#D4A43A` `#F8F6F1` Arima Mulish Lora Playfair Poppins, fake gold, glassmorphism, counters, HOT DEAL

### Header + Footer = Heritage Concierge

Copy from `mayfair-home/homepage.html` (or the V2 screenshot chrome). Same 8 nav items, `tel:+919873712902`, WhatsApp `https://wa.me/919873712902`, NAP Sector 48, footer enquiry form, mobile dock. **Do not redesign chrome.** Only `<main>` differs per template.

### CMS

CPTs `property` / `project` / `insight` may be **0**. Empty states required. **No fake cards.**

Do not rename ACF.

Property: `mpd_price`, `mpd_price_label`, `mpd_area_sqft`, `mpd_bedrooms`, `mpd_bathrooms`, `mpd_possession_status`, `mpd_locality`, `mpd_verified`, `mpd_featured`, plus existing keys.

Project: `mpd_developer_name`, `mpd_min_price`, `mpd_max_price`, `mpd_possession_date`, `mpd_rera_number` (hide if empty).

Insight: `mpi_subtitle`, `mpi_reading_time`, `mpi_featured`, `insight-topic`.

Taxonomies: `property-type`, `property-status`, `location`, `project-type`, `insight-topic`.

---

## Layout to implement (from the screenshot — adapted)

**Desktop ≥1024**

- Left rail **~34%**, `position: sticky` under header, ivory, padding
- Right canvas **~66%**, scrolls
- Rail does **filters**, not a callback form (footer already has enquire)

**Tablet/mobile**

- H1 + filter `<details>` accordion on top
- Results below
- Dock unchanged; do not cover filters

Visual language from the screenshot to **keep**:

- Quiet ivory canvas, hairline cards, large Source Serif titles
- Empty modules as cream inset notes (like “PORTFOLIO BEING UPDATED”)
- Dark typographic location index **as a filter list**, not a Home chapter
- Three-door grouping is **not** required on listing pages (that was Home IA)

Visual language to **drop** on these pages:

- Homepage H1 “Find the Right Property…” in the rail
- Name/Phone/I am looking to form in the rail
- Stacking Approach + Why Mayfair + Consult banner on a listing URL
- Glass luxury-tower as a default hero (use `hero-editorial.jpg` / `gurugram-street.jpg` / no hero)

---

## Page 1 — Properties (`properties.html`)

**H1:** Properties in Gurugram  
**Lede:** A shortlist of residential and commercial opportunities. Published only when the file is ready.  
**Eyebrow:** Portfolio

**Rail filters (Inter):**

- Type → `property-type`
- Location → `location` (Golf Course Road, Golf Course Extension, Dwarka Expressway, Southern Peripheral Road, New Gurugram, Sohna Road, South Gurugram — only show terms that exist; if taxonomy empty, show the list as **links to the same page** disabled/honest “Filters appear when listings are published”)
- Status → `property-status`
- Configuration → `mpd_bedrooms` (1–5+)
- Reset

**Canvas:**

- Chip row of active filters
- Loop: up to 12, then pagination
- Card hierarchy: image · name · location · type · beds · area · status · price + `mpd_price_label` · verified badge · View Property
- Desktop: **horizontal** card (image 280–340px left) — listing density like Transaction Point **fields**, no badges saying HOT
- Empty: cream note “We’re currently updating our property portfolio.” + Discuss / Call. **No specimen fake 3 BHK.**

Elementor: Archive template or Page `/properties/` + Loop Grid query `property`. Filter with Loop Grid taxonomy + Query, or URL params `?property-type=` if no extra plugin. **Do not install a new filter plugin** unless Hello/Elementor Pro Query already can do it. If filters cannot run without a plugin, render them as **links to taxonomy archives** and document that.

---

## Page 2 — Projects (`projects.html`)

**H1:** Projects in Gurugram  
**Lede:** Developments with verified fields only — name, location, developer, type, price range, possession, RERA when it exists.

**Rail filters:** project-type · location · developer (if field) · possession grouping only from real dates

**Canvas:** more editorial than property cards — larger image, fewer items (6–9). Hide RERA if empty. Empty: “Developments are being reviewed.” No invented HRERA.

Live slug: `/project/`

---

## Page 3 — Insights (`insights.html`)

**H1:** Market insights  
**Lede:** Notes on buying, Gurugram micro-markets, valuation, regulations and location — to help you decide, not to fill a blog.

**Rail:** `insight-topic` list + optional “Featured”

**Canvas:** journal rows (not a 3-column magazine mash): topic · title · excerpt · `mpi_reading_time` · Read Insight. Empty: “Market notes are being prepared.”

Live slug: `/insights-2/`

---

## Shared behaviour

- One H1 per page
- `aria-current` on the matching header nav item
- Title/meta:
  - Properties: `Properties in Gurugram | Mayfair Properties & Developers`
  - Projects: `Projects in Gurugram | Mayfair Properties & Developers`
  - Insights: `Market insights | Mayfair Properties & Developers`
- Photography from `mayfair-home/img/` editorial set only if needed for empty-state atmosphere — not as fake listing photos
- Footer form stays; rail **filters only** + text links Discuss / Call
- `prefers-reduced-motion`

---

## Files

```
mayfair-home/listings/properties.html
mayfair-home/listings/projects.html
mayfair-home/listings/insights.html
mayfair-home/listings/listings.css   ← shared desk layout, kit tokens, local fonts ../fonts
mayfair-home/listings/ELEMENTOR-LISTINGS.md
```

Do not modify `homepage.html` / `index.html` / `home-prod.css`.

Preview: `python3 -m http.server 8000 --bind 0.0.0.0` from `mayfair-home/listings`.

---

## Verify

- Header/footer identical to Home chrome
- No homepage H1 or lead-form in the rail
- No forbidden colours/fonts
- Empty states, zero fake inventory
- Three HTML pages + one CSS + Elementor notes (Loop Grid, query, hide-on-empty, taxonomy links)
- Cannot log into wp-admin — do not claim you published

Build the three listing templates now.

---
