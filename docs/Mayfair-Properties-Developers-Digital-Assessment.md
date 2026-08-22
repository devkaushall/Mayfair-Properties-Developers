# Mayfair Properties & Developers
## Technical and Digital Presence Assessment

**Prepared for:** Stakeholders reviewing the company’s code repository, official website, and Google Business presence  
**Assessment date:** 19 August 2026  
**Scope:** GitHub repository `devkaushall/Mayfair-Properties-Developers`, live site [mayfairpropertiesdevelopers.com](https://mayfairpropertiesdevelopers.com), and Google Business Profile / Maps listing [share.google/9O02RJ2wWQ4oTVS3A](https://share.google/9O02RJ2wWQ4oTVS3A)

---

## 1. Executive summary

Mayfair Properties & Developers is a **Gurugram / Sohna Road real-estate advisory and construction-adjacent business**, not the national ultra-luxury brokerage portrayed in the design mock. The company is mid-rebuild: a credible WordPress architecture has been started, a distinctive heritage visual system exists, and the Google listing is claimed and well-rated — but the public website is still an empty shell, the repository is not yet a real source of truth, and the online identity is fragmented across directories.

| Channel | Maturity | Headline verdict |
|---|---|---|
| GitHub repository | Day-zero / design system | Ambitious plugins and a locked design system, stored as zip dumps. Not a deployable WordPress site. Untested. Missing the Core plugin that the live site already uses. |
| Official website | Scaffold only | Hello Elementor + Elementor Pro + custom CPTs are in place. **0 properties, 0 projects, 0 insights, 0 blog posts.** 18 of 19 pages have no body content. Primary CTAs go nowhere. |
| Google Business Profile | Claimed, thin | **4.8 / 5 from 4 reviews.** Listing is managed, but the website URL is a **dead misspelling**, the category is “Construction company”, NAP data conflicts with other directories, and review volume is too small to be a trust asset. |

**Single most important finding:** there are now **three competing brand stories** — (1) a local Gurugram advisor on the live site and Google, (2) a fabricated 1997 Mumbai ultra-luxury house in the HTML design reference, and (3) inconsistent name/address/phone records on Justdial, TradeIndia, IndiaMART and RealEstateIndia. Until those are unified, every extra page, plugin, or ad spend will leak trust.

**Recommended posture for the next 30 days:** freeze fictional luxury copy, populate the already-built CMS with real Gurugram inventory, fix Google’s website URL, and stop publishing unverifiable statistics.

---

## 2. Who the company actually is

Evidence from the live site, Google listing, and third-party directories is consistent on geography and inconsistent on almost everything else.

### 2.1 Confirmed facts

- Trading name: **Mayfair Properties & Developers** (Hindi on Google: मेफेयर प्रॉपर्टीज एंड डेवलपर्स).
- Market: **Gurugram**, with emphasis on Sohna Road / South Gurugram.
- Live site positioning: “Buyer Focused · Verified Properties · Local Gurugram Expertise · Transparent Guidance.”
- Google category: **Construction company**.
- Google address: **P-106, Sohna–Gurgaon Road, near Parsvnath Green Ville, Uppal Southend, Sector 48, Gurugram, Haryana 122018**.
- Google phone: **+91 98737 12902**.
- Hours on Google: **10:00–18:00, seven days**.
- Listing last updated by the business: **about three weeks before this assessment**.
- TradeIndia (registered 2017) names proprietor **Mr. Ram Avatar Yadav**, address Plot No. 1, Vigyan Vihar, Sohna Road, Opp. Vatika City, Gurugram 122101, and describes the firm as a **service provider / real-estate agent** for plots, flats, homes and land. [3](https://www.tradeindia.com/mayfair-properties-developers-11233471/)
- RealEstateIndia lists **Vikash Yadav**, Sec-69 Opp. Vatika City, Sohna Road; **RERA status: Not Available**. [4](https://www.realestateindia.com/profile/mayfair-properties-in-sohna-road-gurgaon-332480/)
- A Google review names advisor **Hemchand Ji** as “a true person and very knowledgeable property guide.”

### 2.2 Identity collisions (do not ignore)

| Source | What it says | Risk |
|---|---|---|
| Official website | Gurugram advisor; no address, phone, or legal entity on the public homepage | Visitors cannot verify or contact the firm from the homepage |
| Google Business | Sector 48 / Uppal Southend; website `myfairpropertiesdevelopers.com` | Wrong URL; address differs from Vatika City listings |
| Justdial — “Mayfair Properties & Developers” | Opp. Vatika City, Sohna Road 122001; **0 ratings, unclaimed**; stock photo only | Duplicate / stale listing |
| Justdial — “Mayfair Properties & Developers (Closed Down)” | Opposite Southend Floors, Sohna Road | Signals a closed business to local searchers |
| Justdial — “Mayfair Properties” Palam Vihar | Different address, 4.0 from 4 ratings, est. 2009 | Likely a **different firm** with a colliding name |
| IndiaMART | Construction + “bridge construction” + real-estate services; different phone | Category sprawl, looks like a generic seller profile |
| Design HTML in the repo | “Established 1997”, Mumbai Nariman Point HQ, ₹48,000 Cr transacted, 2,400 homes, MH RERA `P51800047631` | **Not supported by any public record of this Gurugram firm** |

The design mock is a high-end *visual* reference. It is not a factual company profile. Publishing those numbers, the 1997 founding, the Mumbai head office, or a Maharashtra RERA number would be a serious compliance and reputation problem.

---

## 3. Repository inspection

**Repository:** [github.com/devkaushall/Mayfair-Properties-Developers](https://github.com/devkaushall/Mayfair-Properties-Developers)  
**Owner:** `devkaushall` (Dev) — WordPress / Elementor designer based in Gurugram. Commit author email: `devkaushal8923@gmail.com`.  
**Visibility:** Public. **Stars / forks:** 0 / 0.  
**Created:** 19 August 2026. **Commits on `main`:** 8, all on the same day.  
**Stated purpose:** “WordPress, Elementor, ACF, custom plugins, design system and implementation source of truth.”

### 3.1 What is actually in the repo

The repository is **not a WordPress installation**. It is a flat folder of brand assets, one HTML mock, and four zip archives.

```
README.md                                          165 bytes, two lines
.gitignore                                         stock WordPress.gitignore
Primary / Secondary / Submark logos                4 × WebP
Screenshot 2026-08-19 165225.png                   design-mock screenshot (~1.5 MB)
image.png                                          second design-mock screenshot (~2.6 MB)
mayfair-properties-html-homepage.html              1,574-line Stitch/Studio mock
mayfair-elementor-implementation-package-locked.zip   12 markdown/css/json spec files
mayfair-forms-leads.zip                            full custom plugin (~7.7k PHP lines)
mayfair-implementation-assistant.zip               full custom plugin
mayfair-runtime-diagnostics.zip                    single-file read-only admin plugin
```

**Branches:** `main`, `plugins` (merged via PR #1), `Refrence` (typo; open as PR #2).  
**Tags / releases / CI / license / tests:** none.

The `.gitignore` is a full WordPress core ignore file, which implies an intended future WP tree that has not been committed. Tracking compiled zip files instead of source is the opposite of a “source of truth.”

### 3.2 Architecture the documents describe

The locked Elementor package is internally consistent and unusually specific for a brochure site:

| Layer | Specified target |
|---|---|
| CMS | WordPress 6.x |
| Theme | Hello Elementor |
| Page builder | Elementor Pro 3.24+ (Flexbox containers) |
| Fields | ACF Free only — 35 fields (17 property / 9 project / 9 insight) |
| CPTs | `property`, `project`, `insight` |
| Taxonomies | `property-type`, `property-status`, `location` (shared), `project-type`, `insight-topic` |
| Forms | Custom plugin **Mayfair Forms & Leads**, not Elementor Forms as the system of record |
| Theme Builder | 10+ templates: header, footer, front page, three singles, three archives, two conversion pages, three loop items |
| Visual system | “Architectural Sharp / Mayfair Heritage”: charcoal `#1A1A1A`, bronze `#725B2F` / `#A68B5B`, canvas `#F9F7F2`, Playfair Display + Inter, 2–4 px radii |

That is a **real product architecture**, not a random Elementor dump. The data-model audit even records fields that were *removed* (amenities repeater, parking, carpet area, gallery) because they would have required ACF Pro. That kind of constraint discipline is a strength.

### 3.3 Plugin-by-plugin evaluation

#### A. Mayfair Forms & Leads (v1.0.0) — strongest artefact

A complete lead platform: form builder, 12 real-estate templates, independent `$wpdb` tables, inbox with statuses/notes/assignment, CSV/XLSX/JSON/PDF/TXT export, `wp_mail` notifications, optional HTTPS webhook, Elementor widget + `[mayfair_form]` shortcode.

**Code quality (reviewed, not executed in WordPress):**

- Clean class map (`MPFL_*`), `ABSPATH` guards, uninstall opt-in, capability split (`manage_mayfair_forms`, `view/edit/export/delete_mayfair_leads`).
- Security is better than typical agency form plugins: per-form nonce, honeypot, HMAC-signed timing token, transient rate limit, type-based sanitisation, server-side validation including **choice whitelisting**, `wp_check_filetype_and_ext()` for uploads, isolated `uploads/mayfair-leads/` with `.htaccess` denying PHP, **raw IP never stored** (salted hash or nothing).
- REST namespace `mpfl/v1` is **read-only and capability-gated**. Confirmed live: unauthenticated `GET /wp-json/mpfl/v1/forms` returns **401**.
- SQL uses `$wpdb->prepare` / `insert` / `update`; table names are prefix + fixed suffix. phpcs ignores are annotated, not hidden.
- Output escaping is systematic (`esc_html` / `esc_attr` / `esc_url` / `wp_kses_post`).
- Honest README: *“generated and statically validated only… not tested inside a live WordPress installation.”*

**Weaknesses:**

- Spec documents say **10** form scenarios; the plugin seeds **12**. Drift has already started.
- No automated tests in the repo (docs claim  CLI tests that are not committed).
- Rate limiting via transients will not hold on multi-node hosts without a shared object cache.
- `wp_mail()` without SMTP will be unreliable on Hostinger.
- Admin UI is functional PHP views, not a modern SPA — acceptable, but the form-builder UX will feel dated next to Gravity Forms / Fluent Forms.
- Shipping as a zip rather than a versioned plugin directory makes code review and security scanning harder.

#### B. Mayfair Implementation Assistant (v1.0.0) — clever, correctly constrained

Analyses pasted/uploaded AI output (Google Stitch, Studio, agents) against the locked design system, flags off-palette colours, foreign fonts, invented ACF fields and Pro-only features, then emits a click-by-click Elementor guide. **It never mutates the live site.** PHP in uploads is refused; ZIPs are inspected in memory with zip-bomb and path-traversal guards.

This is a thoughtful answer to “AI generated a beautiful page that would destroy our design system.” It is an internal tool, not a customer-facing feature. Same honesty clause: not tested in WordPress.

#### C. Mayfair Runtime Diagnostics (v1.0.0) — small and useful

A single 496-line read-only admin page (`Tools → Mayfair Diagnostics`) that PASS/FAIL-checks CPTs, taxonomies, ACF groups and permalinks against the locked spec. Well written. Should be run on the live site immediately; the output would tell the team, in one screenshot, what is actually installed.

#### D. Missing: Mayfair Properties Core

The blueprint, the diagnostics plugin, and the **live site** all depend on a Core plugin that registers `property` / `project` / `insight`. **That plugin is not in this repository.** The live REST API already exposes those types, so Core (or an equivalent) exists in production and is not under version control here. That is the largest completeness gap.

### 3.4 HTML homepage mock — design quality vs. factual risk

`mayfair-properties-html-homepage.html` is a polished single-file landing page (Tailwind v4 CDN, Playfair + Inter, bronze/cream palette, sticky nav, mobile menu, property cards, testimonials, insights, contact form). Visually it is in the same family as Sotheby’s / Knight Frank brochure sites.

It is **not** the live site, and it should not be treated as approved copy.

| Mock claim | Problem |
|---|---|
| “Established 1997 · India’s Premier Luxury Real Estate Firm” | TradeIndia registration is 2017; no public 27-year record |
| ₹48,000 Cr+ assets transacted; 2,400+ homes curated | Unsourced. Dangerous if published |
| Head office: Mayfair House, 14th Floor, Nariman Point, Mumbai 400 021 | Contradicts every Gurugram listing |
| Phones `+91 22 6888 0000` / `+91 11 4681 0000` | Not the Google number |
| Email `acquisitions@mayfairproperties.in` | Different domain from the live site |
| MH RERA `P51800047631` | Wrong state for a Haryana business; number not verified |
| Featured homes at ₹96 Cr – ₹420 Cr in Worli / Lutyens / Sadashivanagar | Stock Pexels photography; no evidence these are Mayfair listings |
| Testimonials “R. Singhania”, “A. Nair”, “V. Kapoor” | Unattributed, almost certainly placeholder |
| Contact / newsletter JS | `preventDefault()` only — no backend |

The mock also loads Tailwind from a CDN and Material Symbols from Google Fonts. Fine for a prototype; not a production dependency map.

### 3.5 Repository scorecard

| Criterion | Score | Notes |
|---|---|---|
| Stated vs. actual contents | 3 / 10 | Claims to be the WP/Elementor source of truth; is a zip drop + mock |
| Information architecture | 8 / 10 | CPT / taxonomy / ACF / Theme Builder map is coherent |
| Plugin code quality | 7.5 / 10 | Security-aware, documented, honest about untested status |
| Completeness | 4 / 10 | Core plugin absent; no theme templates; no sample content; no CI |
| Repo hygiene | 2 / 10 | 4 MB of screenshots, binary zips, 165-byte README, typo branch `Refrence` |
| Alignment with the live brand | 3 / 10 | Mock sells a fictional national luxury house; live brand is Gurugram |
| Production readiness | 2 / 10 | Authors say so themselves |

---

## 4. Official website assessment

**URL:** [https://mayfairpropertiesdevelopers.com](https://mayfairpropertiesdevelopers.com)  
**Stack (observed 19 August 2026):**

| Item | Observed |
|---|---|
| CMS | WordPress (REST `wp/v2`, `xmlrpc.php` exposed) |
| Theme | Hello Elementor |
| Builders / add-ons | Elementor **4.2.2**, Elementor Pro **4.2.1**, Royal Elementor Addons **1.7.1065** |
| Custom plugins live | Mayfair Forms & Leads (`mpfl/v1` namespace present), plus a Core-equivalent that registered the three CPTs |
| Other namespaces | LiteSpeed, Hostinger Image Optimizer, Elementor AI, `cowboy-mcp/v1`, `wpvibe/v1` |
| Hosting | Hostinger (`platform: hostinger`, `hcdn`, LiteSpeed cache, PHP **8.3.30**) |
| Fonts | Playfair Display + Inter (full weight series loaded from Google Fonts) |
| Homepage last modified | **19 August 2026, 14:26 IST** — same day as the GitHub repo |

HTTP → HTTPS redirect works. `www` and apex resolve to different Hostinger addresses, which is normal for that host but should be watched for certificate / canonical drift. WordPress `home` / `url` in the REST index is still **`http://`**, not `https://`.

### 4.1 Information architecture

Nineteen published pages exist. **Eighteen have zero rendered body content** in the WordPress REST API. They are empty Elementor documents wearing a global header and footer.

| Page | Content? | Notes |
|---|---|---|
| Home | Partial (~475 visible characters) | Only populated page |
| About Us, Services, Contact, Gallery, Project, Upcoming | Empty | Header/footer only |
| Properties, Residential, Commercial | Empty | No loop, no listings |
| Buy / Sell / Rent / Invest / Consult | Empty | Conversion pages with no form |
| Insights, Insights-2, Blogs, Articles | Empty **and duplicated** | Three competing “content” URLs |

Navigation is oversized for a site with nothing behind it: Home, About, Properties, Commercial, Residential, Services, Buy, Sell, Rent, Consult, Invest, Projects, Upcoming, Gallery, Insights, Blogs, Insights (again), Articles, Contact.

### 4.2 Custom data model on the live site

This is the good news. The locked architecture **is already registered in production**:

| Object | REST | Published items | Seeded terms (all count = 0) |
|---|---|---|---|
| `property` | `/wp/v2/properties` | **0** | Types: Apartment, Builder Floor, Commercial, Independent House, Plot, Villa. Statuses: Available, On Hold, Sold, Under Offer |
| `project` | `/wp/v2/projects` | **0** | Commercial, Mixed Use, Plotted Development, Residential |
| `insight` | `/wp/v2/insights` | **0** | Buying Guide, Gurugram, Investment, Legal & Property Knowledge, Market Trends, Selling Guide |
| `location` (shared) | yes | **0** | Central / Golf Course Extension vicinity, Dwarka Expressway, Golf Course Extension Road, New Gurgaon, Sohna Road, South Gurugram |
| Blog `post` | `/wp/v2/posts` | **0** | — |
| Media | `/wp/v2/media` | **11** | Logos + generic category/hero images (`property-apartment`, `property-villa`, `property-plots`, `hero-main`, `cta-interior`, …) |

The taxonomy vocabulary is correctly **Gurugram-shaped**. Someone has already rejected the Mumbai / Lutyens fantasy at the data-model layer. Inventory simply has not been entered.

### 4.3 Design, usability, content, UX

**Design.** The live homepage uses the locked tokens (bronze `#725B2F`, near-black `#131316`, cream canvas, Playfair headings, Inter UI). Category tiles and a dark CTA band are in the right visual family. Compared with the HTML mock, the live page is thinner, less photographic, and less “editorial.” That is appropriate for a local advisor — if the page were finished.

**Usability failures (homepage):**

1. **No `<h1>`.** The document outline starts at `h2` (“Curated Portfolio”). Bad for accessibility and SEO.
2. **Primary CTAs are dead.** Header “enquire now”, “View All”, and the footer-band **“Enquiere Now”** all point to `href="#"`.
3. **No telephone, WhatsApp, email, address, or map** in the rendered homepage. A real-estate site that cannot be called from the first screen will lose every mobile visitor.
4. **No working form** on Home or Contact. The custom forms plugin is installed and its REST is locked down, but no form is placed on any public page.
5. **Featured Properties** is a heading without cards. The CMS has nothing to loop.
6. **Inflated counters** presented as fact: Apartments 120+, Villas 45+, Plots 80+, Commercial 65+. Combined claim: 310+ listings. Live inventory: **zero**. This is worse than an empty state — it is a credibility trap.
7. **Typography / copy errors:** “Enquiere Now”; tagline “each **clients** specific needs”; “Insights” appears twice in the menu.
8. Mega-menu (Royal Addons) plus a 19-item information architecture on a one-page site creates a “Potemkin” feeling: lots of doors, no rooms.

**Content clarity.** The four value props (Buyer Focused, Verified Properties, Local Gurugram Expertise, Transparent Guidance) are the right promise for this firm. There is no supporting proof: no about story, no team, no RERA, no case studies, no process, no service definitions, no legal pages (Privacy, Terms).

**User experience, end-to-end.**

```
Land on homepage
  → cannot identify a real listing
  → cannot submit an enquiry
  → cannot tap-to-call
  → click any inner URL
      → identical empty chrome
  → leave
```

That is not a conversion funnel. It is a bounce funnel.

### 4.4 SEO, performance, and hardening

| Check | Result |
|---|---|
| Title | Over-long, grammatical error (“each clients specific needs…”) |
| Meta description | **Missing** |
| Open Graph / Twitter cards | **Missing** |
| JSON-LD / LocalBusiness schema | **Missing** |
| Canonical | Present on homepage |
| Robots | Default WP `robots.txt` only |
| Analytics / ads pixels | **No GTM, gtag, Meta Pixel, Clarity, or Hotjar** |
| H1 | **Missing** |
| Image `alt` / lazy-load | Weak; no `loading="lazy"` on homepage |
| Fonts | Entire Inter + Playfair weight series requested — heavier than needed |
| Scripts | 17 external scripts (Elementor + Pro + Royal particles/jarallax/parallax) for a nearly empty page |
| Preload / critical CSS | None observed |
| Security headers | `upgrade-insecure-requests` only. No `X-Frame-Options`, no meaningful CSP |
| User enumeration | `GET /wp-json/wp/v2/users/1` returns **`gangafoods893@gmail.com`** as the public author name |
| xmlrpc.php | Reachable |
| Forms REST | Correctly 401 when anonymous |

The public author slug `gangafoods893gmail-com` is a professional and security defect. It looks like a leftover Hostinger / previous-site account and should be renamed immediately.

### 4.5 Website scorecard

| Criterion | Score | Notes |
|---|---|---|
| Visual design system | 7 / 10 | Tokens and type are in place; page is unfinished |
| Information architecture | 3 / 10 | Too many empty URLs; duplicate Insights |
| Content clarity | 2 / 10 | Slogan-level copy; no proof, no people, no properties |
| Conversion UX | 1 / 10 | Dead CTAs, no form, no click-to-call |
| SEO / discoverability | 2 / 10 | No meta, no schema, no content, no analytics |
| Trust & compliance | 2 / 10 | No RERA, no address, fake listing counts, leftover admin identity |
| Technical foundation | 7 / 10 | Modern stack, CPTs live, forms plugin live, PHP 8.3, HTTPS |
| Completeness vs. IA | 1 / 10 | 1 of 19 pages has any body copy |

---

## 5. Google Business Profile and online reputation

**Listing resolved from** [https://share.google/9O02RJ2wWQ4oTVS3A](https://share.google/9O02RJ2wWQ4oTVS3A)  
**Maps entity:** Mayfair Properties & Developers · Knowledge Graph `/g/12hn96bqh`  
**Direct Maps search:** [Google Maps — Mayfair Properties & Developers, Gurugram](https://www.google.com/maps/search/Mayfair+Properties+%26+Developers+Gurugram)

### 5.1 Listing snapshot

| Field | Value | Assessment |
|---|---|---|
| Rating | **4.8 / 5** | Excellent average, statistically fragile |
| Review count | **4** | Far below the threshold that moves Gurugram property searchers |
| Category | Construction company | Misaligned with the website’s buyer/seller/investor positioning. Should be **Real Estate Agency** (primary) with Construction / Property Consultant as additional |
| Address | P-106, Sohna–Gurgaon Rd, near Parsvnath Green Ville, Uppal Southend, Sector 48, 122018 | Precise, but **does not match** Vatika City / Vigyan Vihar directory addresses |
| Phone | +91 98737 12902 | Consistent with the RealEstateIndia masked number |
| Website | `http://www.myfairpropertiesdevelopers.com/` | **Critical defect.** Domain does not resolve (NXDOMAIN). Every Maps click is a dead end |
| Hours | 10:00–18:00 daily | Recently maintained |
| Photos | 3 | Thin for a property business; no interiors, no team, no listings |
| Claim / management | Updated by the business ~3 weeks ago; owner replies present | Listing is actively managed — good |

### 5.2 Reviews

Publicly extracted reviews:

1. **Nitin Sharma — 5★ — ~3 weeks ago**  
   *“Hemchand ji true person and very knowledgeable property guide.”*  
   Owner reply: timely, named, gracious. This is the right response pattern.

2. **officail Naqvi — ~4 years ago**  
   No visible review body in the public extract. Owner replied **three weeks ago** with a generic thank-you. Late replies on old reviews are better than silence, but they read as a recent cleanup rather than an always-on habit.

Two further reviews contribute to the 4.8 average but did not yield usable text in this pass. The rating bar is dominated by 5-star ratings.

**How to read 4.8 from 4 reviews:** it is a compliment to the advisors (Hemchand Ji in particular), not a reputation moat. A single 1-star review drops the average to 4.0. Competitors on Sohna Road typically show tens to hundreds of ratings.

### 5.3 Broader presence

| Channel | Signal |
|---|---|
| Google Business | 4.8 / 4; claimed; **wrong website** |
| Official website | Live but empty; not linked from Google |
| Justdial (exact name) | 0 ratings, unclaimed, stock image |
| Justdial (same name, “Closed Down”) | Actively harmful |
| Justdial (Palam Vihar “Mayfair Properties”) | Different business, 4.0 / 4 |
| TradeIndia | 2017 proprietor profile; no reviews |
| RealEstateIndia | Agent profile; **RERA not available**; no reviews |
| IndiaMART | Generic service tiles; different phone |
| Instagram / Facebook / LinkedIn from the live site | No working profile URLs extracted from the homepage |
| Organic search | Thin; directory pages outrank the official site for branded queries |

There is **no meaningful review corpus** anywhere except Google’s four ratings. There is also no contradiction that would suggest a hidden scandal for *this* Gurugram firm. (Unrelated “Mayfair” entities in Mumbai, Guwahati, Australia and the US dominate generic web search and should not be confused with this business.)

### 5.4 Reputation scorecard

| Criterion | Score | Notes |
|---|---|---|
| Rating quality | 8 / 10 | 4.8 with a specific, human review |
| Rating quantity | 2 / 10 | Four reviews |
| Listing completeness | 4 / 10 | Hours and phone yes; website broken; photos thin; category wrong |
| NAP consistency | 2 / 10 | At least three addresses and two phones in circulation |
| Review response | 7 / 10 | Recent, polite owner replies |
| Brand distinctiveness online | 3 / 10 | Name collision + empty official site |

---

## 6. Cross-channel strengths, weaknesses, opportunities

### Strengths

1. **A real CMS backbone already exists.** CPTs, taxonomies, ACF-shaped vocabulary, Elementor Pro, and the custom forms plugin are on the server. The hard platform work is started.
2. **Design system is distinctive and locked.** Bronze / charcoal / cream + Playfair / Inter is ownable in the Gurugram broker market, which is full of blue-and-white templates.
3. **Forms plugin is thoughtfully engineered.** Security, privacy (hashed IP), capability model, and export formats are above typical freelance WordPress work.
4. **Google listing is claimed and recently tended.** Owner replies and updated hours mean someone is paying attention.
5. **Clients who do leave reviews speak well of the people.** “True person” / “knowledgeable property guide” is the right raw material for a trust brand.
6. **The live taxonomy is honest about geography.** Sohna Road, Dwarka Expressway, Golf Course Extension — not Malabar Hill.

### Weaknesses

1. **The public website cannot convert.** Dead buttons, no form, no phone, no listings.
2. **Google sends traffic to a domain that does not exist** (`myfair…` vs `mayfair…`).
3. **Content vacuum plus fake counts (120+ / 45+ / 80+ / 65+)** will be noticed by any serious buyer.
4. **Three brand stories** (local advisor vs. 1997 Mumbai luxury house vs. mixed directory records).
5. **Repository is not a source of truth.** Binary zips, missing Core plugin, 165-byte README, untested plugins, typo branch.
6. **NAP chaos** across Google, Justdial, TradeIndia, IndiaMART.
7. **No SEO, analytics, schema, or legal pages.**
8. **Public WP user is `gangafoods893@gmail.com`.**
9. **RERA is “Not Available”** on RealEstateIndia; the HTML mock invents a Maharashtra number.
10. **Name collision** with other “Mayfair Properties” businesses, including a Justdial “Closed Down” listing.

### Opportunities (highest leverage first)

| Priority | Action | Why it matters | Effort |
|---|---|---|---|
| P0 | Change the Google website to `https://mayfairpropertiesdevelopers.com` | Every Maps click is currently wasted | 10 minutes |
| P0 | Put a real phone + WhatsApp + working enquiry form on header, homepage, and contact | Restores the only conversion path that matters | 0.5–1 day |
| P0 | Remove or replace the 120+ / 45+ / 80+ / 65+ counters until they are true | Stops an avoidable honesty problem | 1 hour |
| P0 | Rename the public WP author; set site URL to HTTPS | Hygiene and security | 30 minutes |
| P1 | Publish 8–15 **real** Gurugram listings into the `property` CPT (even if “call for price”) | The entire Theme Builder stack is waiting for this | 2–5 days |
| P1 | Write About, Services, Contact with one address, one phone, one RERA/entity line | Matches Google; kills the empty-page bounce | 1–2 days |
| P1 | Collapse Insights / Insights-2 / Blogs / Articles into **one** journal | Stops IA self-sabotage | 2 hours |
| P1 | Fix Justdial: claim the live listing, request removal/merge of “Closed Down” | Local pack hygiene | 1 day + wait |
| P2 | Ask 15 closed clients for Google reviews (QR at handover, WhatsApp template) | 4 → 25 reviews changes the listing’s commercial value | Ongoing |
| P2 | Recategorise Google to Real Estate Agency; add Services, products, more photos | Matches actual business | 1 hour |
| P2 | Unzip plugins into versioned folders; add Core plugin to git; write a real README | Makes the repo what it claims to be | 1–2 days |
| P2 | Run Runtime Diagnostics on production; install SMTP; add GTM + LocalBusiness schema | Operability | 1 day |
| P3 | Decide, in writing, that the 1997 Mumbai / ₹48k Cr story is **not** approved copy | Prevents a future legal/reputation incident | One meeting |
| P3 | Harmonise NAP on TradeIndia, IndiaMART, RealEstateIndia | Local SEO | 1 day |
| P3 | Add Haryana RERA registration if the firm is brokering/developing as required | Trust + compliance | Legal |

---

## 7. What “good” looks like in 60 days

A realistic target, given that the platform is already half-built:

1. Google, the website header, and the Contact page all show **the same** name, Sector 48 (or Vatika) address, and +91 98737 12902.
2. Homepage has an H1, a working form, click-to-call, and 6–12 live property cards from the CPT — no invented portfolio sizes.
3. About page names the principals (Ram Avatar Yadav / Vikash Yadav / Hemchand) and states what the firm actually does in Gurugram.
4. Inner IA reduced to: Home, About, Properties, Projects, Insights, Contact, plus Buy / Sell as form pages.
5. Google category corrected; website URL corrected; ≥20 reviews; 15+ original photos.
6. Repository contains plugin **source**, the missing Core plugin, a Theme Builder export or documented template IDs, and a README that a second developer can follow.
7. No public page still claims 1997, Nariman Point, ₹48,000 Cr, or a Maharashtra RERA number unless those claims are independently documented.

---

## 8. Risk register (for sponsors)

| Risk | Severity | Likelihood | Mitigation |
|---|---|---|---|
| Publishing the HTML mock’s financial / heritage claims | High (misrepresentation) | High if the mock is treated as copy deck | Legal review; lock the Gurugram fact sheet as the only approved source |
| Google website typo persists | High (lost demand) | Certain today | Edit GBP immediately |
| Fake listing counts noticed by a client or journalist | Medium | High once traffic grows | Delete counters or bind them to real `WP_Query` counts |
| Empty site indexed as the official brand | Medium | Already happening | `noindex` empty URLs until they have content; or do not link them |
| Unrelated “Mayfair” scandals (e.g. foreign entities) attach by name | Medium | Low–medium | Distinct Gurugram NAP, team photos, RERA, Google reviews |
| Custom plugins untested in WP | Medium | High | Staging QA using the bundled checklists before any more feature work |
| Public user `gangafoods893@gmail.com` | Low–medium | Certain | Rename; review role; disable REST user listing |
| Plugin zips only in a public repo | Low | Certain | Move to source; consider making the repo private until launch |

---

## 9. Method and sources

This assessment is based on primary inspection on 19 August 2026:

- Clone of `https://github.com/devkaushall/Mayfair-Properties-Developers` (`main` at `f5d2ac9`); unzip and static review of all four packages; full read of the 1,574-line HTML mock and the locked design-system documents.
- Live HTTP / HTML / WordPress REST inspection of `mayfairpropertiesdevelopers.com` (pages, CPTs, taxonomies, media, users, `mpfl/v1`, headers, robots, sitemap).
- Google Business / Maps listing resolved from the supplied share link, plus Justdial, TradeIndia, RealEstateIndia and IndiaMART records.

Plugins were **not** executed inside WordPress. Findings about code quality are from source review; findings about the live site are from what the server actually emits.

---

## 10. Bottom line

The technical team has built **the right kind of foundation** for a Gurugram property firm: a locked design system, a serious forms/leads plugin, and a CMS that already knows the difference between a villa on Sohna Road and a blog post. That work is real.

What stakeholders are looking at today, however, is not a launched digital presence. It is a **half-connected system**:

- a repository that documents a luxury fantasy and stores plugins as zip files;
- a website that wears the new brand but cannot show a single property or take a single lead;
- a Google profile that likes the business (4.8) but sends visitors to a domain that does not exist.

The gap is not talent or taste. It is **truth, inventory, and conversion**. Close those three and the architecture already on Hostinger will start earning its keep.

---

*End of assessment.*
