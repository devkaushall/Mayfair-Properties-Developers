#!/usr/bin/env python3
"""Generate remaining Mayfair inner pages with shared chrome. Preview only."""
from pathlib import Path

ROOT = Path(__file__).parent

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <link rel="stylesheet" href="home-prod.css" />
  <link rel="stylesheet" href="pages.css" />
  {extra_css}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="util"><div class="util-inner">
  <span class="util-left">Gurugram real estate · Buyers, sellers &amp; investors</span>
  <span><a href="tel:+919873712902">+91 98737 12902</a> &nbsp;·&nbsp; Mon–Sun 10:00–18:00</span>
</div></div>
<header class="site-header"><div class="bar">
  <a class="logo" href="homepage.html" aria-label="Mayfair Properties &amp; Developers home"><img src="img/logo-light.webp" alt="Mayfair Properties &amp; Developers" /></a>
  <nav class="nav-d" aria-label="Primary">
    <a href="homepage.html"{cur_home}>Home</a>
    <a href="about.html"{cur_about}>About Us</a>
    <a href="properties.html"{cur_prop}>Properties</a>
    <a href="services.html"{cur_svc}>Services</a>
    <a href="projects.html"{cur_proj}>Projects</a>
    <a href="gallery.html"{cur_gal}>Gallery</a>
    <a href="insights.html"{cur_ins}>Insights</a>
    <a href="contact.html"{cur_con}>Contact us</a>
  </nav>
  <div class="actions">
    <a class="btn btn-consult" href="consult.html">Consult</a>
    <a class="btn btn-bronze" href="tel:+919873712902">Call now</a>
    <button class="ham" id="ham" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="drawer"><span></span><span></span><span></span></button>
  </div>
</div></header>
<div class="backdrop" id="backdrop"></div>
<aside class="drawer" id="drawer" aria-hidden="true"><nav aria-label="Mobile">
  <a href="homepage.html">Home</a><a href="about.html">About Us</a><a href="properties.html">Properties</a>
  <a href="services.html">Services</a><a href="projects.html">Projects</a><a href="gallery.html">Gallery</a>
  <a href="insights.html">Insights</a><a href="contact.html">Contact us</a>
</nav></aside>
<main id="main">
"""

FOOT = """
</main>
<footer class="site-footer"><div class="foot">
  <div class="foot-brand">
    <img class="foot-logo" src="img/logo-dark.webp" alt="Mayfair Properties &amp; Developers" />
    <p>Gurugram-focused advisory for buyers, sellers and investors — verified opportunities, local market expertise and transparent guidance.</p>
    <div class="nap">P-106, Sohna–Gurgaon Road<br />Uppal Southend, Sector 48<br />Gurugram 122018<br />
    <a href="tel:+919873712902">+91 98737 12902</a></div>
  </div>
  <div class="col"><h2 class="col-title">Portfolio</h2>
    <a href="residential.html">Apartments</a><a href="residential.html">Villas</a>
    <a href="residential.html">Plots</a><a href="residential.html">Builder floors</a>
    <a href="commercial.html">Commercial</a><a href="residential.html">Residential</a>
  </div>
  <div class="col"><h2 class="col-title">Advisory</h2>
    <a href="buy.html">Buy a property</a><a href="sell.html">Sell / valuation</a>
    <a href="rent.html">Rent</a><a href="invest.html">Invest</a><a href="consult.html">Consult</a>
  </div>
  <form class="enquiry" id="enquiryForm" action="#" method="post">
    <h3>Request a callback</h3>
    <label for="fn">Full name *</label><input id="fn" name="name" required autocomplete="name" />
    <label for="ph">Phone *</label><input id="ph" name="phone" type="tel" required autocomplete="tel" />
    <label for="em">Email *</label><input id="em" name="email" type="email" required autocomplete="email" />
    <label for="tm">Best time to call</label>
    <select id="tm" name="best_time"><option value="">Select…</option>
      <option>Morning (10:00–13:00)</option><option>Afternoon (13:00–16:00)</option><option>Evening (16:00–18:00)</option></select>
    <label class="consent"><input type="checkbox" name="consent" required />
      <span>I agree to be contacted by Mayfair Properties &amp; Developers about my enquiry.</span></label>
    <button class="btn btn-bronze" type="submit">Submit enquiry</button>
    <p style="font-size:11px;color:#5c574f;margin-top:8px;">On WordPress: Mayfair — Save Lead. This preview does not store data.</p>
  </form>
</div>
<div class="legal"><span>© 2026 Mayfair Properties &amp; Developers</span><span><a href="homepage.html">Home</a> · <a href="search.html">Search</a></span></div>
</footer>
<nav class="dock" aria-label="Mobile actions">
  <a href="tel:+919873712902">Call</a>
  <a href="https://wa.me/919873712902">WhatsApp</a>
  <a href="#enquiryForm">Enquire</a>
</nav>
<script src="site.js"></script>
</body></html>
"""

def chrome(title, desc, current="", extra_css=""):
    flags = {k: "" for k in ("cur_home","cur_about","cur_prop","cur_svc","cur_proj","cur_gal","cur_ins","cur_con")}
    if current:
        flags[current] = ' aria-current="page"'
    return HEAD.format(title=title, desc=desc, extra_css=extra_css, **flags)

def write(name, html):
    (ROOT / name).write_text(html, encoding="utf-8")
    print("wrote", name)

# --- pages ---

write("about.html", chrome(
    "About Us | Mayfair Properties &amp; Developers",
    "Gurugram-focused real estate advisory — local knowledge, transparent guidance, suitability first.",
    "cur_about"
) + """
<section class="page-hero"><div class="wrap">
  <p class="eyebrow">About</p>
  <h1>A Gurugram advisor, not a catalogue.</h1>
  <p class="support">Mayfair Properties &amp; Developers helps buyers, sellers and investors make property decisions with verified opportunities, local market reading and plain communication. We do not claim decades we cannot show, and we will say when a file is not right for you.</p>
</div></section>
<section class="block"><div class="wrap approach-grid" style="min-height:0">
  <div class="approach-visual" style="min-height:320px"><img src="img/why-interior.jpg" alt="Quiet interior, Gurugram" /></div>
  <div class="approach-copy" style="padding:0 0 0 40px">
    <p class="lede">The work is simple to say and careful to do: listen to the requirement, shortlist what fits, check what can be checked, and leave you able to explain the decision.</p>
    <p class="belief">Integrity here means walking away from a transaction that does not fit — not decorating a weak file with better adjectives.</p>
    <p class="lede">Office: P-106, Sohna–Gurgaon Road, Uppal Southend, Sector 48, Gurugram 122018. Mon–Sun 10:00–18:00.</p>
    <p class="btn-row"><a class="btn btn-ink" href="consult.html">Speak with an advisor</a><a class="btn btn-line" href="services.html">See services</a></p>
  </div>
</div></section>
""" + FOOT)

def archive(fname, title, desc, cur, h1, lede, empty_h, empty_p, filters_html):
    write(fname, chrome(title, desc, cur) + f"""
<div class="wrap desk">
  <aside class="rail">
    <p class="eyebrow">Index</p>
    <h1>{h1}</h1>
    <p class="support">{lede}</p>
    <form class="filter" action="{fname}" method="get">
      {filters_html}
      <button class="btn btn-ink" type="submit">Apply</button>
      <p style="font-size:12px;color:var(--text);margin-top:12px;">Filters become live when CPT records exist. Elementor: taxonomy query / URL params. No extra plugin required if you link term archives.</p>
    </form>
    <p class="btn-row"><a class="btn btn-line" href="consult.html">Discuss your requirement</a></p>
  </aside>
  <div class="canvas">
    <p class="count">0 published · nothing invented to fill the page</p>
    <div class="vacant" role="status"><div class="vacant-copy" style="padding:36px 0">
      <h3>{empty_h}</h3>
      <p>{empty_p}</p>
      <div class="btn-row"><a class="btn btn-ink" href="consult.html">Discuss your requirement</a>
      <a class="btn btn-line" href="tel:+919873712902">Call Mayfair</a></div>
    </div></div>
  </div>
</div>
""" + FOOT)

archive("properties.html", "Properties in Gurugram | Mayfair Properties &amp; Developers",
        "Curated Gurugram property listings when files are ready to publish.",
        "cur_prop", "Properties in Gurugram",
        "A shortlist, not a portal. Cards fill from the Property CPT. Empty fields hide.",
        "We’re currently updating our property portfolio.",
        "Tell us location, configuration and budget. An advisor can help identify suitable options.",
        """<label for="ft">Type</label><select id="ft" name="property-type"><option value="">All types</option>
        <option>Apartment</option><option>Builder Floor</option><option>Villa</option>
        <option>Independent House</option><option>Plot</option><option>Commercial</option></select>
        <label for="fl">Location</label><select id="fl" name="location"><option value="">All corridors</option>
        <option>Golf Course Road</option><option>Golf Course Extension</option><option>Dwarka Expressway</option>
        <option>Southern Peripheral Road</option><option>New Gurugram</option><option>Sohna Road</option></select>
        <label for="fs">Status</label><select id="fs" name="property-status"><option value="">Any</option>
        <option>Available</option><option>Under Offer</option><option>Sold</option><option>On Hold</option></select>
        <label for="fb">Bedrooms</label><select id="fb" name="beds"><option value="">Any</option>
        <option>1</option><option>2</option><option>3</option><option>4</option><option>5+</option></select>""")

archive("projects.html", "Projects in Gurugram | Mayfair Properties &amp; Developers",
        "Selected Gurugram developments — verified fields only.",
        "cur_proj", "Projects in Gurugram",
        "Name, location, developer, type, price range, possession, RERA when the field is filled.",
        "Developments are being reviewed.",
        "We will not invent RERA numbers, possession dates or prices to fill this index.",
        """<label for="pt">Project type</label><select id="pt" name="project-type"><option value="">All</option>
        <option>Residential</option><option>Commercial</option><option>Mixed-use</option><option>Plotted</option></select>
        <label for="pl">Location</label><select id="pl" name="location"><option value="">All corridors</option>
        <option>Golf Course Road</option><option>Golf Course Extension</option><option>Dwarka Expressway</option>
        <option>Southern Peripheral Road</option><option>New Gurugram</option><option>Sohna Road</option></select>""")

archive("insights.html", "Market insights | Mayfair Properties &amp; Developers",
        "Gurugram buying notes, micro-markets, valuation and regulations — when published.",
        "cur_ins", "Market insights",
        "Written to help you decide, not to fill a blog. Loop Grid on CPT insight.",
        "Market notes are being prepared.",
        "When published, this index will list topic, title, excerpt and reading time.",
        """<label for="it">Topic</label><select id="it" name="insight-topic"><option value="">All topics</option>
        <option>Buying</option><option>Selling</option><option>Gurugram market</option>
        <option>Investment</option><option>Legal</option></select>""")

write("contact.html", chrome(
    "Contact us | Mayfair Properties &amp; Developers",
    "Visit or call Mayfair in Sector 48, Gurugram. Mon–Sun 10:00–18:00.",
    "cur_con"
) + """
<section class="page-hero"><div class="wrap">
  <p class="eyebrow">Contact</p>
  <h1>Come in, or start with a call.</h1>
  <p class="support">The same number for buyers, sellers, renters and investors. No urgency script.</p>
</div></section>
<div class="wrap contact-grid">
  <div class="nap-block">
    <p class="eyebrow">Studio</p>
    <p>P-106, Sohna–Gurgaon Road<br />near Parsvnath Green Ville<br />Uppal Southend, Sector 48<br />Gurugram, Haryana 122018</p>
    <p><a href="tel:+919873712902">+91 98737 12902</a><br />
    <a href="https://wa.me/919873712902">WhatsApp</a><br />Mon–Sun 10:00–18:00</p>
    <p><a class="btn btn-ink" href="consult.html">Consult with us</a></p>
  </div>
  <div>
    <p class="eyebrow">Write</p>
    <p class="lede">Use the footer form on this page, or call during hours. On WordPress the form posts to Mayfair — Save Lead.</p>
  </div>
</div>
""" + FOOT)

write("consult.html", chrome(
    "Consult with us | Mayfair Properties &amp; Developers",
    "A focused conversation about a Gurugram property decision.",
    "cur_svc"
) + """
<section class="page-hero"><div class="wrap">
  <p class="eyebrow">Consultation</p>
  <h1>Tell us the situation.</h1>
  <p class="support">Buy, sell, rent, invest, or not sure. We will say if a conversation is useful — including if the right move is to wait.</p>
  <p class="btn-row"><a class="btn btn-ink" href="tel:+919873712902">Call +91 98737 12902</a>
  <a class="btn btn-line" href="https://wa.me/919873712902">WhatsApp</a></p>
</div></section>
<section class="block tint"><div class="wrap">
  <p class="lede">Hours Mon–Sun 10:00–18:00. Sector 48 studio. Footer form → Mayfair — Save Lead / Save Site Visit on production. This HTML preview does not store submissions.</p>
</div></section>
""" + FOOT)

write("gallery.html", chrome(
    "Gallery | Mayfair Properties &amp; Developers",
    "Photographs of Gurugram property and places Mayfair works — published media only.",
    "cur_gal"
) + """
<section class="page-hero"><div class="wrap">
  <p class="eyebrow">Gallery</p>
  <h1>Pictures we can stand behind.</h1>
  <p class="support">This page should pull from the Media library / a gallery field — not stock luxury towers. Live site has media; this preview does not invent a portfolio wall.</p>
</div></section>
<div class="wrap gallery-empty">
  <div class="vacant" role="status"><div class="vacant-copy" style="padding:24px 0">
    <h3>Gallery images load from WordPress Media.</h3>
    <p>In Elementor: Gallery widget → dynamic or selected Media. Do not paste unrelated developer renders.</p>
  </div></div>
</div>
""" + FOOT)

write("search.html", chrome(
    "Search | Mayfair Properties &amp; Developers",
    "Search Mayfair pages, properties, projects and insights."
) + """
<section class="page-hero"><div class="wrap">
  <p class="eyebrow">Search</p>
  <h1>Find a page or a published record.</h1>
  <form class="search-box" action="search.html" method="get">
    <input type="search" name="s" placeholder="Search…" aria-label="Search" />
    <button class="btn btn-ink" type="submit">Search</button>
  </form>
</div></section>
<div class="wrap" style="padding:40px 0 80px">
  <div class="vacant" role="status"><div class="vacant-copy" style="padding:24px 0">
    <h3>No results yet.</h3>
    <p>Theme Builder → Search Results. Query the search term across pages + property + project + insight. Empty: this message + links below.</p>
    <div class="btn-row"><a class="btn btn-ink" href="properties.html">Properties</a>
    <a class="btn btn-line" href="insights.html">Insights</a>
    <a class="btn btn-line" href="homepage.html">Home</a></div>
  </div></div>
</div>
""" + FOOT)

write("404.html", chrome(
    "Page not found | Mayfair Properties &amp; Developers",
    "That address is not on this site."
) + """
<div class="wrap zero">
  <p class="eyebrow">404</p>
  <h1>This page is not here.</h1>
  <p class="lede">The link may be old, or the page has not been published. Nothing is wrong with your requirement — just this URL.</p>
  <div class="btn-row">
    <a class="btn btn-ink" href="homepage.html">Home</a>
    <a class="btn btn-line" href="properties.html">Properties</a>
    <a class="btn btn-line" href="consult.html">Consult</a>
  </div>
</div>
""" + FOOT)

# thin service/type pages
for fname, cur, eye, h1, body, cta_href, cta in [
    ("residential.html","cur_prop","Residential","Homes in Gurugram",
     "Apartments, builder floors, villas, independent houses and plots — when a file is ready to share. This page can query property-type residential terms. Empty until CPT posts exist.",
     "properties.html","Browse properties"),
    ("commercial.html","cur_prop","Commercial","Work and retail space",
     "Office, shop and mixed-use briefs. Same advisory standard as a home: suitability, access, paperwork. Loop Grid filtered to Commercial when data exists.",
     "properties.html","Browse properties"),
    ("buy.html","cur_svc","Buy","Buy with a shortlist, not a feed",
     "We help you match Gurugram property to location, configuration, budget and use, then walk what should be checked before you commit.",
     "consult.html","Discuss a purchase"),
    ("sell.html","cur_svc","Sell","Price is not a strategy",
     "A grounded reading of where the property sits and who may pay for it — without a loud campaign.",
     "consult.html","Talk about selling"),
    ("rent.html","cur_svc","Rent","A lease is still a decision",
     "Homes and commercial space for occupiers, or a brief if you have space to let.",
     "consult.html","Discuss renting"),
    ("invest.html","cur_svc","Invest","Use, risk, time — not a yield slogan",
     "Residential and commercial opportunities read through hold period, occupancy and exit. No guaranteed returns.",
     "consult.html","Investment conversation"),
    ("upcoming.html","cur_proj","Upcoming","Projects still being checked",
     "Upcoming is a filter on the Project CPT (possession / status), not a second inventory. Empty until records exist.",
     "projects.html","All projects"),
]:
    write(fname, chrome(f"{eye} | Mayfair Properties &amp; Developers", body[:150], cur) + f"""
<section class="page-hero"><div class="wrap">
  <p class="eyebrow">{eye}</p>
  <h1>{h1}</h1>
  <p class="support">{body}</p>
  <p class="btn-row"><a class="btn btn-ink" href="{cta_href}">{cta}</a>
  <a class="btn btn-line" href="services.html">All services</a></p>
</div></section>
""" + FOOT)

write("project-single.html", chrome(
    "Project | Mayfair Properties &amp; Developers",
    "A single Gurugram development — fields from the Project CPT only."
) + """
<p class="prop-note wrap" style="display:block;padding-top:20px">Theme Builder → Single · CPT project. Hide empty ACF. Never invent RERA.</p>
<article class="wrap" style="padding:32px 0 64px">
  <p class="eyebrow" data-dynamic="project-type">Project type</p>
  <h1 data-dynamic="post_title">Project title</h1>
  <p class="lede">Developer, location, price range, possession and RERA print only when saved on the post.</p>
  <dl class="detail-grid" style="margin-top:28px">
    <div class="spec-row"><dt>Location</dt><dd>Location</dd></div>
    <div class="spec-row"><dt>Developer</dt><dd data-dynamic="mpd_developer_name">Developer</dd></div>
    <div class="spec-row is-empty"><dt>Price range</dt><dd data-dynamic="mpd_min_price"></dd></div>
    <div class="spec-row is-empty"><dt>Possession</dt><dd data-dynamic="mpd_possession_date"></dd></div>
    <div class="spec-row is-empty"><dt>RERA</dt><dd data-dynamic="mpd_rera_number"></dd></div>
  </dl>
  <p class="btn-row"><a class="btn btn-ink" href="consult.html">Discuss this project</a>
  <a class="btn btn-line" href="tel:+919873712902">Call Mayfair</a></p>
</article>
<section class="consult"><img src="img/consult-facade.jpg" alt="" /><div class="shade"></div>
<div class="consult-inner wrap"><p class="eyebrow light">Conversation</p>
<h2>Want the file read with you?</h2>
<div class="btn-row"><a class="btn btn-ink" href="consult.html" style="background:#F9F7F2;color:#1A1A1A;">Discuss requirement</a>
<a class="btn btn-ghost" href="tel:+919873712902">Call Mayfair</a></div></div></section>
""" + FOOT)

write("insight-single.html", chrome(
    "Insight | Mayfair Properties &amp; Developers",
    "A market note from Mayfair — published insight only."
) + """
<article class="article">
  <p class="meta"><span data-dynamic="insight-topic">Topic</span> · <span data-dynamic="date">Date</span> · <span data-dynamic="mpi_reading_time"></span></p>
  <h1 data-dynamic="post_title">Insight title</h1>
  <p class="lede" data-dynamic="mpi_subtitle">Subtitle if present; hide if empty.</p>
  <img class="cover" src="img/gurugram-street.jpg" alt="" data-dynamic="featured_image" />
  <div class="body" data-dynamic="post_content">
    <p>Article body from the Insight CPT. Related insights: Loop Grid exclude current, same topic, hide if empty.</p>
  </div>
  <p class="btn-row"><a class="btn btn-ink" href="insights.html">All insights</a>
  <a class="btn btn-line" href="consult.html">Talk this through</a></p>
</article>
""" + FOOT)

print("done")
