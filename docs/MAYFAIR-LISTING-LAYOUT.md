# Listing layout — LOCKED (not homepage)

Codex V2 screenshot (Advisor’s desk: sticky left rail + scrolling canvas) is **attractive** and **wrong as Home**.

**Home** stays the editorial 9-section page (`homepage.html` / live Pages → Home). Do not replace Home with the desk layout.

**Use the desk layout only for:**

| WP template | URL (live) | Rail job | Canvas job |
|---|---|---|---|
| Properties archive | `/properties/` | Filters | Property Loop Grid |
| Projects archive | `/project/` | Filters | Project Loop Grid |
| Insights archive | `/insights-2/` | Topics | Insight Loop Grid |

Also usable later for taxonomy landings (`location`, `property-type`) with the same chrome.

---

## Why not Home

- First action is a form (Name / Phone). That is a **tool**, not a welcome.
- Split rail + long module stack reads as a **dashboard / CRM**, not an advisory office front door.
- Duplicate enquire (rail + footer) on Home is noise.
- The glass-tower hero is showroom, not Gurugram street advisory.

Home must still make a visitor think: *I can trust these people to help me understand a decision.*  
This layout makes them think: *I am already inside a listing machine.*

## Why it works for listings

- Sticky rail = **filters** (Transaction Point density, Blue Vistas “selected not random”).
- Canvas = **results**, 3–12 items, not a portal wall.
- Empty CPT (0/0/0) still looks designed.
- Same Heritage Concierge header/footer so it is clearly one site.
- Insights as a journal column + topic rail is closer to Savills research than a blog grid.

The dark **One city. Different markets.** type index can be reused as a **location filter** on Properties/Projects — not as the Home canvas.

---

## Chrome + kit (unchanged)

Header / Footer = Heritage Concierge. Site Settings = kit-6.

Source Serif 4 + Inter. `#1A1A1A` `#725B2F` `#A68B5B` `#444748` `#F9F7F2` `#F5F0E7` `#FFFFFF` `#E5E1D8` `#FFDEA7`. Radius 2–4px. Container 1280px.

No fake listings, RERA, counters, HOT DEAL.

---

## Rail vs canvas (all three archives)

**Left rail (~32–38%, sticky desktop)**

- Page eyebrow + **one H1**
- Short Inter lede (what this index is)
- **Filters** (not a callback form — footer already has enquire)
- Result count when CPT > 0 (“12 properties”) — never invent a number when empty
- Discuss / Call as secondary, after filters

**Right canvas**

- Active filter chips
- Loop Grid
- Pagination or “load more” (Elementor)
- Designed empty state when query = 0

Mobile: H1 + filters collapse (details/accordion), then results, dock unchanged.

---

## Per-page filters (ACF/tax only)

**Properties**

- `property-type` (Apartment, Builder Floor, Villa, Independent House, Plot, Commercial)
- `location`
- `property-status` (Available, Under Offer, Sold, On Hold) — default Available if that helps
- Configuration: `mpd_bedrooms`
- Optional: possession `mpd_possession_status`
- Do not add fake budget sliders until real `mpd_price` data exists

Card: image, name, location, type · beds · area, price + label, verified, View Property. Horizontal on desktop or vertical snap — **listing density**, not Home editorial chapters.

**Projects**

- `project-type`
- `location`
- Possession (`mpd_possession_date` / grouped: Ready / Ongoing / Upcoming only if field exists)
- Developer (`mpd_developer_name`) as facet when ≥2 values
- RERA shown **only if** `mpd_rera_number` filled

**Insights**

- `insight-topic`
- Optional featured (`mpi_featured`)
- Card: topic, title, excerpt, reading time, Read Insight — journal, not magazine masonry

---

## Empty copy (honest)

- Properties: We’re currently updating our property portfolio. Tell us what you’re looking for.
- Projects: Developments are being reviewed. No invented RERA or prices.
- Insights: Market notes are being prepared.

CTA: Discuss your requirement → `/consult-with-us/` · Call `tel:+919873712902`
