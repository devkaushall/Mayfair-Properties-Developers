# Elementor Home — implementation map

Rebuild **Pages → Home** only. Do **not** replace Header / Footer Theme Builder templates (Heritage Concierge).

Live theme: **Hello Elementor**. CPTs `property` / `project` / `insight`. Counts at last inspect: **0 / 0 / 0**. Keep Core + ACF field names.

Replace the current Home canvas (`MAYFAIR ACQUISITIONS`, fake counters, “uncompromising quality”). **One H1 only.**

HTML reference: `mayfair-home/homepage.html`  
Styles: `mayfair-home/home-prod.css`

---

## SEO

| Field | Value |
|---|---|
| Title | Mayfair Properties & Developers \| Real Estate Advisor in Gurugram |
| Meta | Navigate Gurugram real estate with clear advice, verified property opportunities and local market expertise from Mayfair Properties & Developers. |
| H1 | Find the Right Property. Make the Right Decision. |

Exactly **one H1** (hero). Section titles **H2**. Footer column labels stay styled headings or divs — do not add another H1.

---

## Global styles (Site Settings)

Locked kit only — see `MAYFAIR-THEME-LOCKED.md`. Do not use `#111111` `#D4A43A` `#F8F6F1` or Arima/Mulish/Lora.

| Token | Value | Use |
|---|---|---|
| Primary | `#1A1A1A` | headings, charcoal CTAs |
| Secondary | `#725B2F` | Call now |
| Text | `#444748` | body |
| Accent | `#A68B5B` | links, hairlines |
| Ivory | `#F9F7F2` | canvas |
| Cream | `#F5F0E7` | tinted bands |
| Headings | **Source Serif 4** | H1–H3 |
| Body | **Inter** | UI, nav, copy |
| Editorial italic | **Source Serif 4 italic** | Why Mayfair H2 |

Radius **2–4px**. Gold = Accent `#A68B5B` only. Header buttons stay bronze / outline.

---

## Sections (top → bottom)

### 01 Hero — static
- Full-width container, min-height ~88vh.
- Background: calm Gurugram architecture (not sunset-villa / luxury brochure). Reference: `img/hero-editorial.jpg`.
- Light bottom overlay only. **Ivory content panel** bottom-left — not a full dark wash.
- Eyebrow: `Gurugram real estate advisory`
- **H1:** Find the Right Property. Make the Right Decision.
- Support: buyers, sellers and investors; local knowledge; transparent guidance; long-term thinking.
- Buttons: Explore Properties → `/properties/` · Speak With an Advisor → `/consult-with-us/`
- Micro line (not a second H1): “You are not here to be sold a property…”

### 02 Mayfair Approach — static
- Split: material/architecture image | copy.
- **H2:** A property decision deserves more than a sales pitch.
- Four principles, numbered 01–04: Local Knowledge · Transparent Guidance · Suitability First · Long-Term Thinking.
- Editorial list with hairline rules. Not icon cards.

### 03 Featured Properties — **dynamic**
- **H2:** Properties worth taking a closer look at.
- **Loop Grid** → Query: `property`, posts per page **3**. Prefer `mpd_featured` if used.
- Loop item (horizontal card on desktop):
  - Image: Featured image
  - Title: Post title
  - Location: taxonomy `location`
  - Type: `property-type`
  - Beds: ACF `mpd_bedrooms`
  - Area: `mpd_area_sqft`
  - Price: `mpd_price` + `mpd_price_label`
  - Badge: `mpd_verified` (hide if empty)
  - CTA: View Property → permalink
- If query empty: **hide the grid**. Show the designed empty state:
  - “We’re currently updating our property portfolio.”
  - “Tell us what you’re looking for and our advisory team can help.”
  - Discuss your requirement → `/consult-with-us/`
- **Do not** hard-code listing names, prices or fake cards.

### 04 Services — static directory
- **H2:** Advice built around the problem you actually have.
- Six rows (not icon cards): Buy · Sell / Valuation · Invest · Commercial · NRI Advisory · Consultation
- Links: `/buy-property/` `/sell-property/` `/want-to-invest-in-property/` `/commercial/` `/consult-with-us/` `/consult-with-us/`
- Each row: customer problem + how Mayfair helps. Copy from `homepage.html`.

### 05 Why Mayfair — static
- Full-width charcoal `#1A1A1A`. Split copy | interior photograph.
- **H2** (Source Serif 4 italic): A property can look right on paper and still be wrong for you.
- Not a “Why Choose Us” icon grid. No counters.
- Button → `/about-us/`

### 06 Featured Projects — **dynamic**
- **H2:** Developments shaping Gurugram.
- Loop Grid → `project`, 2–3 items.
- Tags: image, title, `mpd_developer_name`, `location`, `project-type`, `mpd_min_price`–`mpd_max_price`, `mpd_possession_date`, `mpd_rera_number` (**hide if empty**).
- Never invent RERA, possession, prices or developer claims.
- Empty: designed vacant state, not a blank hole. CTA → `/consult-with-us/` and `/project/`.

### 07 Gurugram — static / taxonomy-ready
- **H2:** One city. Different markets.
- Corridors (link to `/properties/` until location landings exist):
  - Golf Course Road
  - Golf Course Extension
  - Dwarka Expressway
  - Southern Peripheral Road
  - New Gurugram
  - Sohna Road
- Informational one-liners only. **No** appreciation, future prices or guaranteed returns.

### 08 Market Insights — **dynamic**
- Loop Grid → `insight`, latest 3.
- Image, title, excerpt, taxonomy `insight-topic`, `mpi_reading_time`, Read more.
- CTA → `/insights-2/`
- Empty: designed vacant state. Do **not** invent posts.

### 09 Final consultation — static
- Background architecture (`img/consult-facade.jpg`), restrained overlay.
- **H2:** Not sure what the right move is?
- Discuss Your Requirement → `/consult-with-us/`
- Call Mayfair → `tel:+919873712902`
- No urgency language.

---

## Do not

- Invent years, ₹ volumes, listing counts, awards, RERA numbers, testimonials or yields.
- Keep the old 120+ / 45+ / 80+ / 65+ counters.
- Use “dream home”, “world-class”, “unmatched”, “exclusive opportunity”, “act now”, “hurry”.
- Change CPT registrations or ACF field names.
- Install another page builder.
- Touch Header / Footer templates except the existing punch list (`tel:`, Consult → `/consult-with-us/`, form → Mayfair Forms, 2–4px radius).

## After publish

Add real **Properties**, **Projects** and **Insights** in WP admin when they exist. The loops fill without touching the Home canvas. Until then, empty states stay.
