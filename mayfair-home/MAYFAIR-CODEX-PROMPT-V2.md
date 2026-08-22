# Codex prompt V2 — new homepage from scratch (copy below the line)

---

You are building a **brand-new homepage** for **Mayfair Properties & Developers**.

This is **not** a restyle of the current preview. Do **not** clone `mayfair-home/homepage.html` layout (ivory caption-plate hero, numbered services directory, vacant+label specimen stacked the same way). Invent a **different composition, rhythm, and interaction model**.

You **must not** invent a different brand.

---

## Hard locks (never violate)

### A. Site Settings = live Elementor kit-6

Use **only** these tokens. If you need a colour that is not here, stop.

| Token | Hex | Use |
|---|---|---|
| Primary / ink | `#1A1A1A` | headings, charcoal CTAs, dark bands |
| Secondary / bronze | `#725B2F` | header Call now only + bronze UI |
| Text | `#444748` | body |
| Accent | `#A68B5B` | links, hairlines, numbers — **only gold** |
| Ivory | `#F9F7F2` | page canvas |
| Cream | `#F5F0E7` | alt bands, forms |
| Surface | `#FFFFFF` | cards, inputs |
| Border | `#E5E1D8` | rules |
| Muted line | `#C4C7C7` | input borders |
| Utility | `#FFDEA7` | top bar type only |
| Error | `#BA1A1A` | |
| Success | `#2A9F4D` | |

**Forbidden:** `#111111` `#D4A43A` `#F8F6F1` `#D8C7B2` `#8C847C` `#2A1E17` and any new gold.

**Type**

- Headings: **Source Serif 4** (Primary 64/48/40 · 600 · lh 1.12; Secondary 42/40/32 · 500 · lh 1.2)
- Body / UI / nav / buttons / forms: **Inter** 16/400/lh 1.6
- Accent labels: Inter 12–13, 700, uppercase, **not italic**
- Why-Mayfair pull only: Source Serif 4 **italic**
- **Forbidden:** Playfair, Arima, Mulish, Lora, Poppins, Montserrat, DM Serif, Cormorant

**Layout kit**

- Max width **1280px**, padding 24px (mobile 20px)
- Radius **2–4px**
- Body CTA: `#1A1A1A` fill, ivory type, min-height 48px
- Header Call now stays `#725B2F` uppercase Inter
- Header Consult stays charcoal outline → `/consult-with-us/`
- `prefers-reduced-motion: reduce` must disable motion
- Focus-visible 2px Accent/bronze
- One **H1** only

### B. Header + Footer = Heritage Concierge (do not redesign)

Copy the **existing** header/footer markup and behaviour from `mayfair-home/homepage.html` (or live Theme Builder). Do not invent a new nav, a new logo treatment, or a new dock.

**Header**

- Utility: Gurugram line + `tel:+919873712902` + Mon–Sun 10:00–18:00; type `#FFDEA7` on `#1A1A1A`
- ~76px ivory bar, `img/logo-light.webp`, 8 links: Home, About Us, Properties, Services, Projects, Gallery, Insights (`/insights-2/`), Contact us
- Consult outline → `/consult-with-us/`
- Call now bronze → `tel:+919873712902`
- Mobile hamburger + dock: Call · WhatsApp (`https://wa.me/919873712902`) · Enquire

**Footer**

- `img/logo-dark.webp` full wordmark (not MF submark)
- Positioning: Gurugram-focused advisory for buyers, sellers and investors — verified opportunities, local market expertise and transparent guidance.
- NAP: P-106, Sohna–Gurgaon Road, Uppal Southend, Sector 48, Gurugram 122018 · +91 98737 12902
- Portfolio + Advisory columns; “Buy a property” sentence case
- Enquiry form: name, phone, email, best time, consent. HTML may `preventDefault`; comment that WP wires to Mayfair Forms & Leads
- © 2026

You may only restyle **`<main>`**. Header/footer CSS classes should keep working.

### C. Brand facts (do not invent)

- Name: Mayfair Properties & Developers
- Gurugram advisory for buyers, sellers, investors — not Mumbai luxury, not a portal, not a developer showroom
- Official: `https://mayfairpropertiesdevelopers.com`
- No fake years, ₹ volumes, listing counts, awards, RERA, testimonials, yields, “India’s leading”, “dream home”, “world-class”, “HOT DEAL”, counters (120+/45+/80+/65+)

### D. CMS (dynamic means WordPress, not fake JS data)

CPTs: `property`, `project`, `insight` — counts may be **0**. Design **empty states** that look finished.

Do not rename ACF:

**property:** `mpd_property_id`, `mpd_price`, `mpd_price_label`, `mpd_area_sqft`, `mpd_bedrooms`, `mpd_bathrooms`, `mpd_floor_level`, `mpd_furnishing`, `mpd_possession_status`, `mpd_locality`, `mpd_latitude`, `mpd_longitude`, `mpd_floor_plan`, `mpd_brochure`, `mpd_video_url`, `mpd_featured`, `mpd_verified`

**project:** `mpd_developer_name`, `mpd_possession_date`, `mpd_min_price`, `mpd_max_price`, `mpd_rera_number`, `mpd_project_brochure`, lat/long, featured

**insight:** `mpi_subtitle`, `mpi_reading_time`, `mpi_author_name`, `mpi_author_image`, `mpi_featured`, `mpi_source_name`, `mpi_source_url`, `mpi_cta_text`, `mpi_cta_url`

Taxonomies: `property-type`, `property-status`, `location`, `project-type`, `insight-topic`

Mark Loop Grid hooks in HTML comments. Hide loops when empty.

---

## What “absolutely different & dynamic” means

The current v1 page is a **calm vertical editorial stack**: caption-plate hero → split approach → vacant panel → numbered directory → charcoal why → corridor list → consult banner.

V2 must feel like a **different product surface**, still professional.

**Required new model (use this, do not mix with v1):**

### “Advisor’s desk” — split-canvas homepage

**Desktop (≥1024)**

- **Left ~38% sticky rail** (below the locked header, above the locked footer/dock):
  - Same H1 and support copy
  - Live enquiry mini-form (name, phone, I am looking to: Buy / Sell / Invest / Consult, consent)
  - `tel:` and WhatsApp
  - Hours
  - This rail **does not** replace the footer form
- **Right ~62% scrolling canvas** of **chapters** (not the v1 section templates)

**Tablet/mobile:** rail stacks **after** the first chapter image, form remains easy to reach; mobile dock unchanged.

**Motion (dynamic, not luxury):**

- Chapter images may fade/slide **8–16px** on scroll
- Sticky chapter index (01–09) on the canvas edge, Inter 11px uppercase
- Property/project cards: horizontal **snap** row on desktop (3 visible-ish), swipe on mobile
- Corridor names: large type; hover reveals one honest sentence (no ROI claims)
- `prefers-reduced-motion`: static

No parallax circus, no glassmorphism, no video hero, no animated counters, no gold particles.

---

## Content chapters on the scrolling canvas (same jobs as the business, new shapes)

Keep these **jobs** (the business still needs them). **Change the shapes.**

1. **Opening image chapter** — full-bleed Gurugram architecture in the canvas (not a caption plate). H1 lives in the **left rail**, not on the photo.
2. **Approach** — one long italic Source Serif sentence + four short Inter lines **without** 01–04 gold numbers in a vertical rule list. Try a 2×2 quiet grid or a single flowing paragraph with four bold lead-ins.
3. **Properties (dynamic, 3)** — snap row of **vertical** cards (image top, facts below). Hierarchy: image, name, location, type · beds · area, price/`mpd_price_label`, verified badge, View Property. Empty: one unfinished folder UI (“Portfolio being updated”) + Discuss CTA. No fake Sector 57 homes.
4. **Services** — **not** a 6-row numbered directory. Use three **large doors**: Find a property / Need advice / Understand the market, each opening a short stack of links (Residential, Commercial, Projects · Buy, Sell, Invest, Consult · Gurugram, Insights). NRI + Commercial still reachable.
5. **Why Mayfair** — full-canvas cream or ink **quote page**. H2: *A property can look right on paper and still be wrong for you.* Photo as a narrow vertical strip, not a 50/50 split like v1.
6. **Projects (dynamic, 2–3)** — editorial **one-at-a-time** slide or stacked full-width bands: image, name, location, developer, type, price range, possession, RERA if present. Hide empty RERA. Empty: honest vacant, no invented HRERA.
7. **Gurugram** — typographic index, huge corridor names, no map pins, no “Explore” chips like v1. Honest one-liners only. Corridors: Golf Course Road, Golf Course Extension, Dwarka Expressway, Southern Peripheral Road, New Gurugram, Sohna Road.
8. **Insights (dynamic, 3)** — newspaper column: topic, title, 2-line excerpt, Read Insight. No blog-card grid like a magazine template clone of v1’s three-up.
9. **Close** — short, no second hero banner clone. “Not sure what the right move is?” + Discuss / Call. The left rail already has the form; this is a quiet end-stop.

SEO

- Title: Mayfair Properties & Developers | Real Estate Advisor in Gurugram
- Meta: Navigate Gurugram real estate with clear advice, verified property opportunities and local market expertise from Mayfair Properties & Developers.
- H1: Find the Right Property. Make the Right Decision.

---

## Tone (study, don’t copy)

- Blue Vistas: selected, verified, advisory — sell clarity not inventory
- Savills: pathways Find / Advice / Market
- Transaction Point: card **fields**, not hype
- AARKA: no shouting (do not copy HNI/₹5–50 Cr)
- Not Dubai, not Sotheby’s, not Magicbricks

Photography: existing `mayfair-home/img/hero-editorial.jpg`, `consult-facade.jpg`, `gurugram-street.jpg`, `material-detail.jpg`, `why-interior.jpg`. Do not use `villa.webp` / `apt.webp` / `comm.webp` (too showroom).

---

## Files — new tree, do not overwrite v1

Create:

```
mayfair-home/v2/index.html      ← new homepage (header/footer copied)
mayfair-home/v2/home-v2.css     ← new CSS, kit tokens only
mayfair-home/v2/ELEMENTOR-V2.md ← how to rebuild Pages → Home only
```

Serve from `mayfair-home/v2` on **8000** or **8081** (`python3 -m http.server 8000 --bind 0.0.0.0`). Do not replace `mayfair-home/homepage.html` (v1 lock).

Local fonts: `../fonts/source-serif-4-*.woff2`, `../fonts/inter-*.woff2`.

---

## Verify before you stop

- Header + footer match v1 chrome (same links, tel, dock)
- No forbidden colours/fonts in CSS
- Exactly one H1
- 0 listings still looks designed
- Desktop split rail + canvas; mobile single column; dock not covering the form
- `index.html` in v2 is the new page
- Cannot log into wp-admin — document Elementor, don’t pretend you published

Build V2 now.

---
