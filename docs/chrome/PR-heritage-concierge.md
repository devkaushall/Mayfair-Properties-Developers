# Lock Gurugram positioning and Heritage Concierge global chrome

**Repo:** `devkaushall/Mayfair-Properties-Developers`  
**Suggested title:** `Lock Gurugram-focused positioning and Heritage Concierge header/footer`  
**Suggested base:** `main`  
**Suggested labels:** `design-system`, `wordpress`, `elementor`, `content`

---

## Summary

This PR records the **locked product and design decisions** for Mayfair Properties & Developers and the **Heritage Concierge** header/footer that is now the global Theme Builder chrome.

Mayfair is a **Gurugram real-estate advisory** for buyers, sellers, and investors — not a Mumbai ultra-luxury brokerage. The Stitch/HTML homepage mock (`mayfair-properties-html-homepage.html`) remains a **visual reference only**. Its copy (1997 founding, Nariman Point, ₹48,000 Cr, Maharashtra RERA) must **not** be treated as company fact and must **not** ship on the live site.

Heritage Concierge is the approved site-wide header and footer. It uses the locked Heritage tokens, the repo logos, the **eight live top-level pages**, Gurugram NAP, and an enquiry form in the footer.

---

## Motivation

Three things were colliding:

1. **Live WordPress** already has Gurugram taxonomies, CPTs (`property`, `project`, `insight`), and an 8-item mega menu — but empty pages and dead `#` CTAs.
2. **The HTML design mock** looks premium but tells a different (incorrect) brand story.
3. **Five chrome options** were explored. We need one global pair so Theme Builder, plugins, and copy stay aligned.

Without a written lock, the next Elementor edit or AI-generated page will drift back to luxury-Mumbai copy or a 19-item flat menu.

---

## What changed (product lock)

### Positioning (source of truth)

> Mayfair Properties & Developers is a Gurugram-focused real estate advisory and property services platform helping buyers, sellers and investors make confident property decisions through verified opportunities, local market expertise and transparent guidance.

| In scope | Out of scope |
|---|---|
| Gurugram corridors: Sohna Road, South Gurugram, Golf Course Extension, Dwarka Expressway, New Gurgaon | Mumbai / national ultra-luxury story |
| Residential: apartments, builder floors, villas, independent houses, plots | Invented stats (₹48,000 Cr, 2,400 homes, 27 years) |
| Commercial / investment properties | Nariman Point HQ, `+91 22…` numbers, `mayfairproperties.in` |
| Projects: residential, commercial, mixed-use, plotted | Maharashtra RERA `P51800047631` |
| Services: buy, sell, rent, invest, consult | Fake listing counts (120+ / 45+ / 80+ / 65+) until `WP_Query` is real |
| Insights: buying/selling guides, Gurugram market, investment, legal | |

### Navigation (eight top-level pages)

These are the live WPR mega-menu roots. Do not flatten children into the top bar.

1. Home  
2. About Us  
3. Properties → Commercial, Residential  
4. Services → Buy, Sell, Rent, Consult, Invest  
5. Projects → Upcoming  
6. Gallery  
7. Insights → Blogs, Articles  
8. Contact us  

### Chrome choice

| Pair | Role | Status |
|---|---|---|
| **1 Heritage Concierge** | Global header + footer | **Locked** |
| 2 Conversion Strip | Mobile dock (Call / WhatsApp / Enquire) only | Follow-up |
| 3 Inventory Portal | Mega panel + search | After real listings exist |
| 4 Editorial Journal | Insights templates only | Optional later |
| 5 Evening Desk | Consult / Contact / form pages | Optional later |

---

## What reviewers should look at

### Header (Heritage Concierge)

- Charcoal **utility bar**: Gurugram line (buyers, sellers, investors, verified listings) + `+91 98737 12902` + hours `Mon–Sun 10:00–18:00`.
- Cream **76px bar**: primary light logo, eight pages, outline **Consult**, bronze **Call now**.
- Tokens: `#1A1A1A`, `#725B2F`, `#F9F7F2`, Playfair + Inter, 2–4px radii.

### Footer (Heritage Concierge)

- Secondary / dark logo + Gurugram positioning sentence.  
- NAP: P-106, Sohna–Gurgaon Road, Uppal Southend, Sector 48, Gurugram 122018.  
- **Portfolio:** property types (Apartment, Villa, Plot, Builder floor, Independent house, Commercial).  
- **Advisory:** Buy, Sell / valuation, Rent, Invest, Consult.  
- **Enquiry card:** name, phone, email, best time, consent, Submit — must hit **Mayfair Forms & Leads** (or a working mailer), not `#`.  
- Legal row: © 2026 · Privacy · Terms · RERA (label only until a Haryana number exists).

Live Elementor template under review: Footer `post=574` (and the matching Header template assigned to Entire Site).

---

## Reviewer checklist

**Content**

- [ ] No 1997 / Mumbai / ₹48k Cr / MH RERA copy in header, footer, or homepage.
- [ ] Utility and footer lines match the Gurugram positioning sentence.
- [ ] Eight top-level items only; children stay in dropdowns or footer columns.

**Links (block Publish if any fail)**

- [ ] Logo → `/`
- [ ] Call now + utility/footer phone → `tel:+919873712902`
- [ ] Consult → `/consult-with-us/`
- [ ] Each of the eight nav items → its real permalink (not `#`)
- [ ] Portfolio / Advisory links → real archives or service pages
- [ ] Enquiry form creates a lead (Mayfair Forms inbox or email)
- [ ] Privacy / Terms are real pages or plain text — no 404s
- [ ] RERA is not a fake registration number

**Design system**

- [ ] Enquiry card and inputs use **2–4px** radius (not large pills)
- [ ] Utility bar type contrast on charcoal (prefer `#A68B5B` / `#FFDEA7`)
- [ ] “Buy a property” sentence case
- [ ] Prefer taxonomy types over a redundant “Residential” sibling of Apartments/Villas

**Responsive (if not in this PR, open a follow-up)**

- [ ] Header sticky after ~60px (hairline shadow only)
- [ ] Tablet/mobile: hamburger; Call now remains visible
- [ ] Mobile sticky dock: Call · WhatsApp · Enquire

---

## How to test

1. Elementor → Theme Builder → Header / Footer → preview **desktop**.  
2. Click every nav item and both CTAs in an unpublished preview.  
3. Submit the footer form with a test name/phone; confirm a row in **Mayfair Forms → Submissions** (or the notification email).  
4. Resize to 768px and 375px: menu must collapse; hit areas ≥ 44px.  
5. View page source on the front end: **no API keys**, no Stitch Mumbai copy.

---

## Risk and follow-up (not this PR)

- Inner pages (About, Properties, Services, …) are still empty Elementor shells. New chrome will send traffic into blank canvases until those templates have content.  
- Do **not** enable Mayfair Arena AI Bridge **public widget** until the prompt is resolved server-side.  
- Google Business still lists `myfairpropertiesdevelopers.com` (dead). Fix NAP outside git.  
- Plugin zips in this repo are not a substitute for versioned source; a later PR should unzip `mayfair-arena-ai-bridge` (and Core, if missing) into folders.

---

## Notes for maintainers

- Design tokens and template map: `mayfair-elementor-implementation-package-locked.zip` (`01-design-system.md`, `03-wordpress-template-map.md`).  
- Logos: `Primary_original_Logo_for_Light_theme-*.webp` (header), `Secondary_Logo_for_Dark_theme-*.webp` (footer).  
- Forms plugin: `mayfair-forms-leads.zip` — system of record for enquiries.  
- Arena plugin: `mayfair-arena-ai-bridge.zip` — official `https://api.preview.arena.ai` only; keys stay in **WP Admin → Mayfair AI → Connection**, never in this repo.

**Please do not merge if Consult, Call, or the enquiry form still point at `#`.**
