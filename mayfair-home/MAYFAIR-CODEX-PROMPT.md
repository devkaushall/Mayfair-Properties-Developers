# Codex prompt — Mayfair Properties & Developers (copy everything below the line)

---

You are implementing **production web work** for **Mayfair Properties & Developers**, a **Gurugram-focused real estate advisory** (not a luxury developer, not a portal, not a Mumbai ultra-luxury firm).

Work like a senior front-end + WordPress/Elementor implementer. Do not invent a new architecture, palette, or type system. Do not “improve” the brand into luxury gold, Dubai, Sotheby’s, or Magicbricks.

---

## 0. What this job is

**Polish and implement** the already-locked homepage and design system.

**Not** this job:

- Inventing a 10th homepage section
- Changing Header / Footer Theme Builder templates (Heritage Concierge is locked)
- Changing CPT registrations or ACF field **names/types**
- Filling empty loops with fake listings, fake RERA, fake testimonials, fake counters
- Copying Blue Vistas / Savills / Transaction Point / AARKA / Looops visuals

References exist **only** to explain tone, information architecture, and property-card hierarchy.

---

## 1. Company (facts only — do not invent more)

- **Name:** Mayfair Properties & Developers
- **Positioning (lock this sentence):** Mayfair Properties & Developers is a Gurugram-focused real estate advisory and property services platform helping buyers, sellers and investors make confident property decisions through verified opportunities, local market expertise and transparent guidance.
- **Audience:** families, first-time buyers, sellers, investors, NRIs — broader than HNI-only
- **Official site:** `https://mayfairpropertiesdevelopers.com`
- **Phone:** `+91 98737 12902` · `tel:+919873712902` · WhatsApp `https://wa.me/919873712902`
- **Hours:** Mon–Sun 10:00–18:00
- **NAP:** P-106, Sohna–Gurgaon Road, near Parsvnath Green Ville, Uppal Southend, Sector 48, Gurugram, Haryana 122018
- **GMB category should be** Real Estate Agency (currently Construction company — do not “fix” GMB from code)
- **Do not use** the dead domain `myfairpropertiesdevelopers.com`
- **Do not use** Mumbai / Nariman Point / “Established 1997” / ₹48,000 Cr / 2,400 homes / MH RERA / `+91 22…` / fake awards

**Never invent:** years in business, ₹ volumes, listing counts, awards, RERA numbers, testimonials, yields, “India’s leading”, “dream home”, “world-class”, “exclusive opportunity”, “act now”, “hurry”.

Live WordPress (Hostinger, Hello Elementor, Elementor + Pro, ACF, Royal Addons). Theme is **Hello Elementor**, not Astra.

---

## 2. Locked visual system (Elementor kit-6)

**Source of truth = live Site Settings**, not any parallel “editorial” mock palette.

### Colour — use only these

| Token | Hex | Use |
|---|---|---|
| Primary / ink | `#1A1A1A` | headings, charcoal CTAs, dark sections |
| Secondary / bronze | `#725B2F` | header Call now, bronze UI |
| Text | `#444748` | body |
| Accent | `#A68B5B` | links, hairlines, numbers — **this is the only gold** |
| Ivory | `#F9F7F2` | page canvas |
| Cream | `#F5F0E7` | tinted bands, enquiry card |
| Surface | `#FFFFFF` | cards, inputs |
| Border | `#E5E1D8` | rules |
| Muted line | `#C4C7C7` | input borders |
| Utility | `#FFDEA7` | top bar text only |
| Error | `#BA1A1A` | |
| Success | `#2A9F4D` | |

**Forbidden (previous drift — never use again):** `#111111` `#D4A43A` `#F8F6F1` `#D8C7B2` `#8C847C` `#2A1E17`.

Gold ratio: mostly ivory/charcoal/cream. Accent `#A68B5B` sparingly. **No gold-heavy luxury aesthetic.**

Links: `#A68B5B` → hover `#725B2F`.

### Type — use only these

- **Headings (Primary / Secondary):** `Source Serif 4`
- **Body / UI / nav / buttons / forms (Text / Accent):** `Inter`
- Editorial italic (Why Mayfair pull-quote only): **Source Serif 4 italic** — not a third family

**Forbidden:** Playfair Display (except leftover kit H4 until reset), Arima, Mulish, Lora, Poppins, Montserrat, DM Serif Display, Cormorant, Cinzel.

| Global | Family | Desktop / Tablet / Mobile | Weight | LH | Tracking |
|---|---|---|---|---|---|
| Primary | Source Serif 4 | 64 / 48 / 40 | 600 | 1.12 / 1.2 / 1.2 | −0.02em |
| Secondary | Source Serif 4 | 42 / 40 / 32 | 500 | 1.2 / 1.2 / 1.3 | −0.015 |
| Text | Inter | 16 | 400 | 1.6 | — |
| Accent | Inter | 12 / 14 / 13 | 700 | 1 | uppercase, **not italic**, ~0.14em |

- Homepage **one H1** → Primary
- Section titles **H2** → Secondary
- Nav/buttons → Inter
- Kit leftover: `h4` may still be Playfair 24px — **reset H4 to Source Serif 4** so Playfair stops loading from Google Fonts

### Layout

- Container **1280px** (tablet 1024, mobile 767)
- Side padding 24px (mobile 20px)
- Widget gap 16px
- Radius **2–4px** only
- No glassmorphism, no heavy shadows, no oversized radii (12–16px), no gradients except image overlays for type readability
- No animation that interferes with reading
- Buttons min-height **48px**
- Body CTA: `#1A1A1A` fill, ivory type
- Header **Call now**: `#725B2F`, Inter, uppercase
- Header **Consult**: charcoal outline → `/consult-with-us/`

---

## 3. Locked chrome (do not rebuild unless broken)

**Heritage Concierge** header + footer already live in Elementor Theme Builder. Preserve them.

Header:

- Utility bar: Gurugram line + `tel:+919873712902` + Mon–Sun 10:00–18:00; utility type `#FFDEA7` on `#1A1A1A`
- Cream ~76px bar, light logo, 8 items: Home, About Us, Properties, Services, Projects, Gallery, Insights, Contact us
- Outline Consult → `/consult-with-us/`
- Bronze Call now → `tel:+919873712902`
- Mobile: hamburger + dock Call · WhatsApp · Enquire (`wa.me/919873712902`)

Footer:

- Dark full wordmark (not MF submark)
- Positioning sentence
- NAP Sector 48
- Portfolio + Advisory columns (“Buy a property” sentence case)
- Enquiry: name, phone, email, best time, consent → **Mayfair Forms & Leads** on WP (HTML mocks may `preventDefault` only)
- Radius 2–4px

**Edit Pages → Home canvas only.** Do not replace Header/Footer templates.

Live Insights URL in nav is `/insights-2/` — keep until redirects exist. Prefer one Insights URL long-term; do not invent new slugs.

---

## 4. Locked homepage architecture — 9 sections, this order, no extras

Do not reorder. Do not add a 10th primary section.

| # | Type | Section |
|---|---|---|
| 01 | Static | Hero |
| 02 | Static | Mayfair Approach |
| 03 | Dynamic | Featured Properties |
| 04 | Static | Services |
| 05 | Static | Why Mayfair |
| 06 | Dynamic | Featured Projects |
| 07 | Static | Gurugram |
| 08 | Dynamic | Market Insights |
| 09 | Static | Consultation CTA |

Personality in one line:

> A well-designed real estate advisory office translated into a website — not a luxury property showroom and not a property portal.

Feeling: architecture magazine × trusted local advisor × modern consultancy.

**Not:** Dubai developer, Sotheby’s, flashy broker, MLS wall of cards.

Avoid: luxury black+gold everywhere, huge ₹50 Cr numbers, “India’s No.1”, “500+ Happy Families”, animated counters, glassmorphism, huge gradients, gold borders, floating luxury cards, cinematic video, excessive parallax, Exclusive/Elite/Ultra Luxury/Unparalleled, fake listings/testimonials/stats.

---

## 5. Section specs

### 01 Hero — static

- Strong Gurugram architectural photo (overcast/street, not sunset villa + pool + Range Rover)
- Ivory caption plate, not a full dark luxury wash
- Eyebrow: `Gurugram real estate advisory`
- **H1 (only H1 on page):** Find the Right Property. Make the Right Decision.
- Support: Mayfair helps buyers, sellers and investors navigate Gurugram real estate through local knowledge, transparent guidance and long-term thinking.
- Primary CTA: Explore Properties → `/properties/`
- Secondary: Speak With an Advisor → `/consult-with-us/`
- Micro: You are not here to be sold a property. You are here to make a property decision with better information.
- No search bar, no urgency

SEO title: `Mayfair Properties & Developers | Real Estate Advisor in Gurugram`  
Meta: `Navigate Gurugram real estate with clear advice, verified property opportunities and local market expertise from Mayfair Properties & Developers.`

### 02 Mayfair Approach — static

- Editorial split: material/architecture image | copy
- **H2:** A property decision deserves more than a sales pitch.
- Four principles only: **01 Local Knowledge · 02 Transparent Guidance · 03 Suitability First · 04 Long-Term Thinking**
- Hairline list, not icon cards
- Belief: suitability first; willing to say when a property is not right

### 03 Featured Properties — dynamic

- **H2:** Properties worth taking a closer look at.
- **3** cards when CPT has posts. Curated collection, not a portal grid.
- WordPress: `property` CPT → Elementor **Loop Grid** → property card template → existing ACF only
- Card hierarchy (Transaction Point density, **no hype**):

  - Image (featured)
  - Property name (title)
  - Location (`location` taxonomy)
  - Type (`property-type`)
  - Configuration (`mpd_bedrooms`)
  - Area (`mpd_area_sqft`)
  - Status (`property-status` if present)
  - Price (`mpd_price` + `mpd_price_label`)
  - Verification (`mpd_verified` — hide if empty)
  - CTA: View Property → permalink

- Desktop: **horizontal** cards (image left, facts right). Tablet collapse. Mobile single column, scannable. Do not shrink the desktop layout.
- **If query empty:** hide Loop Grid. Show designed empty state: “We’re currently updating our property portfolio.” + “Tell us what you’re looking for…” + Discuss / Call.
- A **format specimen** (labels + `₹ —` only) is allowed if clearly “not a listing”. **Never** invent “Modern 3 BHK, Sector 57, ₹x Cr”.
- No HOT DEAL, ONLY 2 LEFT, fake %, giant discount badges

ACF on property (do not rename): `mpd_property_id`, `mpd_price`, `mpd_price_label`, `mpd_area_sqft`, `mpd_bedrooms`, `mpd_bathrooms`, `mpd_floor_level`, `mpd_furnishing`, `mpd_possession_status`, `mpd_locality`, `mpd_latitude`, `mpd_longitude`, `mpd_floor_plan`, `mpd_brochure`, `mpd_video_url`, `mpd_featured`, `mpd_verified`

### 04 Services — static

- **H2:** Advice built around the problem you actually have.
- **Inside this section (not a new section),** Savills-style pathways:

  - **Find a property** → Residential `/residential/` · Commercial `/commercial/` · Projects `/project/`
  - **Need advice** → Buy `/buy-property/` · Sell `/sell-property/` · Invest `/want-to-invest-in-property/` · Consult `/consult-with-us/`
  - **Understand the market** → Gurugram `#gurugram` · Insights `/insights-2/`

- Then editorial **directory** (not icon cards), six rows: Buy · Sell / Valuation · Invest · Commercial · NRI Advisory · Consultation
- Each row = real customer problem + how Mayfair helps (copy already in `homepage.html`)

### 05 Why Mayfair — static

- Full-width `#1A1A1A`, split copy | quiet interior photo
- **H2** (Source Serif 4 italic): A property can look right on paper and still be wrong for you.
- Not a “Why Choose Us” six-icon grid. No counters.
- Include: brochures/prices/pins are incomplete; the difference is not louder marketing; integrity to walk away
- CTA → `/about-us/`

### 06 Featured Projects — dynamic

- **H2:** Developments shaping Gurugram.
- 2–3 cards. More editorial than property cards.
- CPT `project` Loop Grid
- Fields: image, title, location, `mpd_developer_name`, `project-type`, `mpd_min_price`–`mpd_max_price`, `mpd_possession_date`, `mpd_rera_number` (**hide if empty**)
- **Never invent** RERA, possession, prices, developer claims
- Empty: designed vacant state + format specimen with labels only

### 07 Gurugram — static / taxonomy-ready

- **H2:** One city. Different markets.
- Corridors (no appreciation / future prices / guaranteed returns): Golf Course Road, Golf Course Extension, Dwarka Expressway, Southern Peripheral Road, New Gurugram, Sohna Road
- Informational one-liners. Link `/properties/` until location landings exist

### 08 Market Insights — dynamic

- **H2:** Know the market before you buy into it.
- Latest **3** `insight` posts
- Image · topic (`insight-topic`) · title · excerpt · Read Insight
- Purpose: Mayfair understands the market — not a generic blog wall
- Empty: vacant state. **Do not invent posts**

Insight ACF (do not rename): `mpi_subtitle`, `mpi_reading_time`, `mpi_author_name`, `mpi_author_image`, `mpi_featured`, `mpi_source_name`, `mpi_source_url`, `mpi_cta_text`, `mpi_cta_url`

### 09 Consultation CTA — static

- Architectural image, restrained overlay
- **H2:** Not sure what the right move is?
- Discuss Your Requirement → `/consult-with-us/`
- Call Mayfair → `tel:+919873712902`
- No urgency. Ivory/ink CTA on dark, not `#111111`

---

## 6. References — study, do not copy

1. **Blue Vistas India** (`https://www.bluevistasindia.com/`) — **primary tone + hierarchy:** selected → verified → advisory → insights. Sell information and advice, not inventory. Not their visuals, not their cities, not their listings.
2. **Savills India** — IA / pathways only (Find a property / Need advice / Understand the market). Not their chrome.
3. **Transaction Point** — property **card information hierarchy** only. Not counters, not “hot deal”, not their numbers.
4. **AARKA** — confidence without shouting. Do not copy HNI/₹5–50 Cr framing; Mayfair’s audience is broader.
5. **Looops boutique RE template** — muted, editorial, curated collection vs wall of cards. Do not copy their track-record figures.

---

## 7. WordPress / Elementor implementation rules

- Theme: Hello Elementor. Builder: Elementor Pro Flexbox containers. No extra page builder.
- **Site Settings** already locked (kit-6). Do not create a second global palette in Custom CSS.
- Custom CSS in kit may keep:

```
--mpd-primary: #1A1A1A;
--mpd-bronze: #A68B5B;
--mpd-bronze-dark: #725B2F;
--mpd-bg: #F9F7F2;
--mpd-surface: #FFFFFF;
--mpd-border: #E5E1D8;
```

- Google Fonts: Source Serif 4 + Inter only; load **swap**. Remove unused Playfair.
- Dynamic = Loop Grid on CPTs. Hide grid when 0 posts; show empty state.
- Do not change Mayfair Core CPT code or ACF keys.
- Forms on production → Mayfair Forms & Leads, not a demo `preventDefault` (HTML preview may demo).
- REST user `gangafoods893@gmail.com` is a live-site hygiene issue — do not print it in front-end.
- Site URL may still be `http` in REST — do not hardcode `http://` in new links; use `https://mayfairpropertiesdevelopers.com/...` or relative permalinks.
- No Yoast required for this task unless already installed; still set page title/meta/H1 as specified.
- Accessibility: skip link, focus-visible 2px accent/bronze, `prefers-reduced-motion`, real `tel:` links, one H1.

---

## 8. Repo / files (if working in this workspace)

Canonical HTML/CSS:

- `mayfair-home/homepage.html` — production homepage reference
- `mayfair-home/home-prod.css` — locked kit tokens
- `mayfair-home/MAYFAIR-THEME-LOCKED.md` — theme lock
- `mayfair-home/ELEMENTOR-HOMEPAGE.md` — Elementor section map
- `mayfair-home/ELEMENTOR-SITE-SETTINGS.md` — kit map
- Fonts: `fonts/source-serif-4-*.woff2`, `fonts/inter-*.woff2` (local preview). Live site uses Elementor Google Fonts.

GitHub `devkaushall/Mayfair-Properties-Developers` is **not** a WordPress tree. Do not dump 58 webps at repo root. Do not treat Stitch/HTML luxury mocks as company fact.

If you change HTML, keep `index.html` in sync with `homepage.html` for the local preview server (`python3 -m http.server` in `mayfair-home`, bind `0.0.0.0`).

---

## 9. Quality bar

Visitor should think: **“I can trust these people to help me understand a property decision.”**  
Not: **“This is another flashy broker trying to sell me something.”**

Calm, credible, local, modern, editorial, human, premium, practical.

When CPT counts are **0 / 0 / 0**, the page must still look **designed and complete** via empty states — never a blank hole, never fake cards presented as inventory.

---

## 10. Deliverables

1. Homepage HTML/CSS (or Elementor-equivalent) matching the 9 sections and locked kit
2. Property, project, insight **Loop item templates** with ACF mappings
3. Empty-state UI for all three loops
4. Elementor implementation notes: widgets, queries, hide-on-empty
5. No new fonts, no new colours, no new primary sections, no fake data
6. Brief note of anything you could not do (e.g. cannot log into wp-admin from sandbox)

Start from existing `homepage.html` + `home-prod.css`. Diff against the lock files. Do not start from a luxury real-estate template.

---
