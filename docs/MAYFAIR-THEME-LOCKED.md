# Mayfair theme — LOCKED

**Source of truth:** live Elementor Site Settings, kit `elementor-kit-6`.  
**Not** the HTML mock palettes (`#111111`, `#D4A43A`, `#F8F6F1`, Arima, Mulish, Lora). Those were a drift. Do not use them again.

Inspected 21 Aug 2026 after the font update.

---

## Type (locked)

- Headings **Primary / Secondary:** Source Serif 4
- Body / UI **Text / Accent:** Inter
- No Playfair, Arima, Mulish, Lora, Poppins, Montserrat

| Global | Family | Size (D / T / M) | Weight | Line-height | Tracking |
|---|---|---|---|---|---|
| Primary | Source Serif 4 | 64 / 48 / 40 | 600 | 1.12 / 1.2 / 1.2 | −0.02em |
| Secondary | Source Serif 4 | 42 / 40 / 32 | 500 | 1.2 / 1.2 / 1.3 | −0.015 |
| Text | Inter | 16 | 400 | 1.6 | — |
| Accent | Inter | 12 / 14 / 13 | 700 | 1 / 1 / 1.2 | uppercase, **not italic** |

- H1 on the homepage should use **Primary**. Section H2/H3 use **Secondary**.
- Editorial italic (Why Mayfair pull) = Source Serif 4 italic — not a third family.
- Nav, buttons, forms, body = Inter only.

**Leftover:** kit `h4` is still hard-coded **Playfair Display** 24px. That is why Playfair still loads. Reset H4 to Source Serif 4 so it stops.

---

## Colour (locked — kit only)

| Token | Hex | Use |
|---|---|---|
| Primary | `#1A1A1A` | ink, headings, charcoal CTAs, dark sections |
| Secondary | `#725B2F` | Call now, bronze UI |
| Text | `#444748` | body |
| Accent | `#A68B5B` | links, hairlines, numbers |
| Ivory | `#F9F7F2` | page canvas |
| Cream | `#F5F0E7` | tinted bands, enquiry card |
| Surface | `#FFFFFF` | cards, inputs |
| Border | `#E5E1D8` | rules |
| Muted line | `#C4C7C7` | input borders |
| Utility | `#FFDEA7` | top bar text only |
| Error | `#BA1A1A` | |
| Success | `#2A9F4D` | |

**Do not use:** `#111111` `#D4A43A` `#F8F6F1` `#D8C7B2` `#8C847C` `#2A1E17`. Gold is **`#A68B5B`**, not a yellow gold.

Link colour Accent `#A68B5B`, hover Secondary `#725B2F`.

---

## Layout (locked)

- Container **1280px** (tablet 1024, mobile 767)
- Side padding 24px (mobile 20px)
- Widget gap 16px
- Radius **2–4px**
- Theme **Hello Elementor**
- Header / Footer = Heritage Concierge (do not rebuild unless a technical issue)

---

## Buttons (locked)

- Body CTA: `#1A1A1A` fill, ivory type
- Header Call now: `#725B2F`, Inter, uppercase
- Header Consult: charcoal outline
- Min-height 48px

---

## Custom CSS in kit (keep)

```
--mpd-primary: #1A1A1A
--mpd-bronze: #A68B5B
--mpd-bronze-dark: #725B2F
--mpd-bg: #F9F7F2
--mpd-surface: #FFFFFF
--mpd-border: #E5E1D8
```

Focus-visible 2px Accent. Respect `prefers-reduced-motion`.

---

## Rule for every future reference design

1. Open this file first.
2. Use only the tokens above.
3. If a mock needs a colour that is not in the kit, **stop** — do not invent one.
4. HTML previews must match kit-6, not a parallel “editorial” palette.
