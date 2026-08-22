# Mayfair Properties & Developers
## Header & Footer Design References

Five distinct header/footer pairings, drawn from the locked design system, Theme Builder map, live WordPress information architecture, and brand assets in [devkaushall/Mayfair-Properties-Developers](https://github.com/devkaushall/Mayfair-Properties-Developers).

These are **implementation references**, not live pages. They use the repository’s real brand and content vocabulary — Gurugram advisory, bronze/charcoal/cream tokens, Playfair Display + Inter, 2–4px “Architectural Sharp” radii — and they **collapse** the current 19-item menu (duplicate Insights, empty Buy/Sell/Rent/Articles doors) into navigable groups.

**Shared constraints (from the locked spec)**

| Token / rule | Value |
|---|---|
| Primary charcoal | `#1A1A1A` |
| Secondary bronze | `#725B2F` |
| Accent bronze | `#A68B5B` |
| Canvas / cream | `#F9F7F2` / `#F5F0E7` |
| Border subtle | `#E5E1D8` |
| Type | Playfair Display (wordmark, headings) · Inter (nav, UI, legal) |
| Shape | 0–4px radii; 200–250ms ease; hover lift ≤ 2px |
| Desktop frame | 1280px boxed, 24px gutter |
| Touch | Minimum 44px targets; mobile ≤ 767px gets an off-canvas menu |
| Logos in repo | Primary (light), Secondary (dark), Submark light, Submark dark |
| Spec components | CMP-01 Global Header · CMP-02 Global Footer · callback / enquiry shortcode |

**Content that belongs in every serious pair**

- Wordmark: **Mayfair** + overline **Properties & Developers**
- Honest primary nav — the **8 live top-level pages**: Home · About Us · Properties · Services · Projects · Gallery · Insights · Contact us  
  (Commercial / Residential sit under Properties; Buy / Sell / Rent / Consult / Invest under Services; Blogs / Articles under Insights.)
- One visible conversion action: **Enquire** or **Call** (`+91 98737 12902` from the Google listing)
- Footer must include: property-type + location taxonomies, advisory links (Buy / Sell / Rent / Invest / Consult), legal (Privacy, Terms, RERA when available), and a callback / enquiry form — matching Theme Builder item 2 (“Taxonomy Links, Advisory Links, Callback Shortcode”)

---

## Example 1 — Heritage Concierge
*Closest to the locked “Architectural Sharp & Mayfair Heritage” system and the Stitch homepage mock. Best default for the whole site.*

### Header

**Structure (two rows, sticky after the first)**

1. **Utility bar** — 32px, charcoal `#1A1A1A`, Inter 11px uppercase, letter-spacing 0.12em.  
   Left: “Local Gurugram expertise · Verified listings”.  
   Right: `+91 98737 12902` (tap-to-call) · `Enquire` text link · hours “Mon–Sun 10:00–18:00”. Hidden on small phones except the phone number.

2. **Primary bar** — 76px (spec), cream `#F9F7F2` at 95% with a 1px `#E5E1D8` hairline. On scroll, a 4px soft shadow only — no colour change.

**Key components**

- **Brand, left:** Primary light logo (or the light submark in a 36×36 charcoal square + Playfair “Mayfair” / Inter bronze “Properties & Developers”). Links home.
- **Nav, centre (desktop ≥1025px):** Home · About · Properties · Projects · Services · Insights. Active item: bronze underline 2px, not a pill.
- **Utilities, right:** Outline button **Consult** (`#1A1A1A` 1px) + filled bronze **Call now**. On tablet, keep Call now and collapse the rest into a three-line hamburger (last bar bronze).
- **Mobile:** Off-canvas cream drawer, same order, phone and Enquire pinned to the drawer footer. No mega-menu.

**Style notes**

Editorial, quiet, hotel-concierge. No icons except the phone glyph. No search in this variant — search lives on the Properties archive (CMP-08). This pairing is what Theme Builder “Mayfair Global Header” is describing.

### Footer

**Structure — four columns, 1280px, charcoal field `#1A1A1A`, cream type**

| Col 1 — Brand | Col 2 — Portfolio | Col 3 — Advisory | Col 4 — Callback |
|---|---|---|---|
| Secondary (dark) logo | Apartments | Buy a property | Short heading “Request a callback” |
| One-line promise: buyer-focused Gurugram guidance | Villas | Sell / valuation | Mayfair Forms shortcode: name, phone, consent |
| Address: Sector 48 / Sohna–Gurgaon Road | Plots | Rent | Bronze submit |
| Phone + email | Builder floors · Commercial | Invest · Consult | “We reply within one business day” |

**Below the grid:** hairline `#2E2D2D`. Left: © Mayfair Properties & Developers. Right: Privacy · Terms · RERA (placeholder until a Haryana number exists). No invented Maharashtra RERA.

**Style notes**

Dark, sharp corners, bronze rules 32×2px above each column title. Social row (optional, only if real profiles exist): small 36px squares, bronze on hover — do not ship empty Facebook/Instagram hrefs.

**Best for:** Site-wide default; matches the locked tokens and CMP-01/CMP-02.

---

## Example 2 — Conversion Strip
*Built for a firm that currently has no inventory online. Phone and WhatsApp do the work the empty property loop cannot.*

### Header

**Structure — single 64px sticky bar + a mobile-only bottom dock**

- Full-bleed cream bar, logo left (light submark + wordmark).
- **No centre nav on mobile.** Desktop nav is only four items: Properties · Services · About · Contact.
- Right cluster is the hero of the bar: green-neutral **WhatsApp** (outline) + bronze **Call +91 98737 12902**. The number is always visible from 768px up; below that it becomes a phone icon with the full number in the bottom dock.

**Mobile sticky dock (spec: “sticky bottom action bar”)**

Three equal 48px-tall cells: **Call** · **WhatsApp** · **Enquire**. Fixed above the iOS home indicator. This is the conversion layer; the top bar only brands and opens the menu.

**Style notes**

More product than brochure. Inter-heavy, Playfair only in the wordmark. Slightly denser than Example 1. Utility colour (WhatsApp) is the only departure from the locked palette — keep it to that one button so the bronze system still reads as Mayfair.

### Footer

**Structure — compact two-band, not four tall columns**

1. **Action band** on cream `#F5F0E7`: left-aligned “Looking for the right property in Gurugram?” + bronze **Enquire now** (this is the working form page, never `href="#"`).
2. **Link band** on charcoal: three short lists in one row — Company (About, Contact, Insights), Help (Buy, Sell, Rent, Consult), Legal — then a single line of NAP (name, Sector 48 address, phone).

No newsletter until there is something to send. No fake listing counts.

**Best for:** Launch / “scaffold” phase; pairs with the current empty CPT state without pretending there are 120+ apartments.

---

## Example 3 — Inventory Portal
*For when `property` / `project` / `location` actually have terms and posts. Uses the taxonomy map already registered on WordPress.*

### Header

**Structure — 76px bar + full-width mega panel**

- Cream bar, primary light logo left.
- Nav items that open **mega panels** (not a 12-link flat list):
  - **Properties** — two columns: *Type* (Apartment, Villa, Plot, Builder Floor, Independent House, Commercial) and *Corridor* (Sohna Road, Golf Course Extension, Dwarka Expressway, New Gurgaon, South Gurugram). Footer of the panel: “View all listings →”.
  - **Projects** — Residential / Commercial / Mixed Use / Plotted (the `project-type` terms).
  - **Services** — Buy, Sell, Rent, Invest, Consult (the conversion pages).
  - **Insights** — one column of `insight-topic` terms (Buying Guide, Market Trends, Legal, Gurugram).
- **Search field** in the header (desktop only), 240px, Inter 14px, placeholder “Locality or property ID”. Submits to the Property archive (CMP-08), not a dead `#`.
- Right: bronze **Enquire**. Phone moves to the utility line above, 28px charcoal.

**Mobile**

Mega panels become accordion sections inside the off-canvas drawer. Search sits at the top of the drawer. Sticky bottom bar: Call · Enquire.

**Style notes**

Still sharp and cream, but the mega panel is white `#FFFFFF` with a 1px `#E5E1D8` border and 24px padding. Type labels are 10px Inter bold uppercase bronze. This is the only variant that should feel like a listing portal.

### Footer

**Structure — five columns on charcoal**

1. Brand + NAP + “Verified by Mayfair” line (only if the ACF flag is in use).
2. **Browse by type** — live `property-type` term links (counts optional, only if real).
3. **Browse by location** — live `location` terms.
4. **Projects & Insights** — archive roots + two latest insight titles (dynamic).
5. **Callback shortcode** — same Mayfair Forms widget as Example 1.

Legal bar includes a sitemap link. No “120+ listings” unless `WP_Query` says so.

**Best for:** Post-launch, once inventory exists. Directly implements Theme Builder header (“Dynamic Menu”) and footer (“Taxonomy Links”).

---

## Example 4 — Editorial Journal
*Quieter chrome for Insights, Articles, and Buying Guides. Treats Mayfair as an advisor who publishes, not a classifieds board.*

### Header

**Structure — centred, non-sticky until 80px of scroll, then condenses**

- Top: centred light submark (32px) over Playfair “Mayfair” and a thin bronze rule 48px wide. No utility bar.
- Beneath: a single Inter 12px uppercase row — Insights · Guides · Market · About · Contact — centred, 32px gaps.
- Far right, absolutely positioned: text link **Subscribe** (jumps to footer) and a small **Enquire** ghost button. On mobile these join a bottom sheet.

**On scroll**

Header collapses to 56px, logo left, three links (Insights, About, Enquire), cream bar with hairline. Feels like a review or magazine masthead (Kinfolk / estate journal), still using Playfair + bronze.

**What it deliberately omits**

Property mega-menu, WhatsApp, listing search. Those belong on Properties, not on a guide about title due diligence.

### Footer

**Structure — cream canvas, not charcoal** (the only light footer)

- Wide top: “Mayfair Insights” in Playfair 28px + one-line description + email field + bronze arrow button (newsletter; only if you will actually send one).
- Then a three-column link row in muted `#444748`: Topics (the six `insight-topic` terms), Company, Legal.
- Bottom: small dark submark, address, phone, © line.

**Style notes**

More paper than nightclub. Borders `#E5E1D8`. Social icons only if the journal is the public voice. Pair this header/footer **only** on Insight singles and the Insights archive (Theme Builder items 6 and 9); keep Example 1 or 3 on the rest of the site via Theme Builder conditions.

**Best for:** Thought-leadership templates; stops Insights from wearing a property-portal hat.

---

## Example 5 — Evening Desk
*Uses the repo’s **Secondary logo for dark theme**. A dusk, in-office feel for Consult / Contact / Enquire — high contrast, fewer links, stronger phone.*

### Header

**Structure — one 72px charcoal bar, secondary logo, no cream at all**

- Background `#1A1A1A`. Bottom edge: 1px `#725B2F` bronze rule (not a thick gold slab).
- Left: **Secondary_Logo_for_Dark_theme** (or dark submark). Wordmark in `#E6E2D9`, overline in `#A68B5B`.
- Nav in `#C4C7C7` Inter 12px uppercase: About · Properties · Services · Contact. Hover: `#FFDEA7`.
- Right: outline-white **Consult** + filled bronze **Call now**.
- Mobile: hamburger in bronze-light; drawer is charcoal, not cream.

**Style notes**

This is the “after 6pm meeting” header. Do not mix it with the cream utility bar of Example 1 — pick one atmosphere per template. Ideal for Consult with us, Contact, and the enquiry thank-you state.

### Footer

**Structure — charcoal continuing from the header (no seam)**

- Full-bleed `#1A1A1A`. A 64px-tall **enquiry ribbon** at the top of the footer: Playfair 22px “Speak with an advisor” + the callback shortcode in a 480px white card (2px radius) sitting on the dark field — the only light object.
- Under the ribbon, three columns in `#858383`: Office (Sector 48 address, map link, hours 10:00–18:00), Services (Buy / Sell / Rent / Invest / Consult), Fine print (Privacy, Terms, RERA).
- No taxonomy clouds here — this footer is for conversion pages, not browsing.

**Best for:** Consult, Contact, Buy, Sell, Rent, Invest. Theme Builder can assign this pair to those pages only.

---

## How the five differ (quick chooser)

| | Atmosphere | Nav density | Conversion emphasis | When to use |
|---|---|---|---|---|
| **1 Heritage Concierge** | Cream, editorial, locked tokens | Medium, flat | Call + Consult | Global default |
| **2 Conversion Strip** | Compact, utility-first | Very low | WhatsApp + Call + bottom dock | Pre-inventory launch |
| **3 Inventory Portal** | Cream + mega panel + search | High, taxonomy-driven | Enquire + search | After listings exist |
| **4 Editorial Journal** | Paper, centred masthead | Low, topics | Subscribe / Enquire | Insights only |
| **5 Evening Desk** | Charcoal + secondary logo | Low | Call + callback card | Consult / Contact / forms |

---

## Implementation notes (Elementor Pro)

1. Build **two Theme Builder headers and two footers** at most to start: Example 1 (Entire Site) + Example 5 (Consult/Contact/Buy/Sell/Rent). Add Example 3 only when CPTs have posts. Add Example 4 only on Insight archives/singles.
2. Bind logo widgets to the four repo assets: light primary / light submark on cream; secondary / dark submark on charcoal.
3. Enquire / callback must use **Mayfair Forms & Leads** shortcodes (`[mayfair_form …]`), not Elementor Forms as the system of record, and never `href="#"`.
4. Do not put “120+ / 45+ / 80+ / 65+” or the Stitch mock’s Mumbai / ₹48,000 Cr claims in any footer metric strip.
5. Keep one NAP everywhere: the Google listing’s Sector 48 / Sohna–Gurgaon Road address and `+91 98737 12902`, until directories are unified.
6. Respect the responsive spec: off-canvas from 1024px down; sticky bottom action bar at ≤767px; 44px minimum hit areas.

---

*References: locked files `01-design-system.md`, `02-component-library.md`, `03-wordpress-template-map.md`, `08-responsive-spec.md`; brand logos in the repository root; live IA and taxonomies on mayfairpropertiesdevelopers.com.*
