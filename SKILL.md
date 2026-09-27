---
name: notebook-notes-pdf
description: Create Sahas AI's hand-lettered "grid-paper notebook" PDFs — study notes, Instagram/LinkedIn carousels, guides, cheat-sheets and explainers that look handwritten (Kalam titles + Patrick Hand body, red ink text, navy ✱ underlined headings, black underlined keywords, circled callouts with arrows, colour-coded flow diagrams with real logos/icons, ruled tables, pastel note boxes, Sahas AI logos on cover, corner badge and a dark thank-you page). Use whenever the user asks for notes, a PDF, a carousel or a cheat-sheet "in my notes style", "notebook style", "Sahas style", "handwritten style", or wants any topic turned into these visual notes — in English, Hinglish, Hindi or Marathi. Renders locally with headless Chrome/Edge; no web services.
---

# Notebook Notes PDF (Sahas AI style)

You write **plain HTML using the component classes below**. `scripts/render.py` injects the
stylesheet, fonts, logos, brand badge, page dots, page size and an overflow check, then prints a PDF
with local Chrome/Edge. Every rule in this file was approved by the owner; don't improvise a new look.

```
notebook-notes-pdf/
├── SKILL.md                  ← this file (workflow + rules)            READ FIRST
├── references/style-guide.md ← visual DNA, voice, component cookbook   READ BEFORE WRITING
├── references/languages.md   ← English / Hinglish / Marathi rules, labels, examples
├── assets/template.html      ← starter with cover, inner pages, flow, table, thank-you page — COPY THIS
├── assets/notebook.css       ← the style system (don't restyle per document)
├── assets/notebook.js        ← badge, footer dots/count/swipe, overflow detector
├── assets/fonts/             ← Kalam, Patrick Hand, Caveat, Shantell Sans (OFL, bundled)
├── assets/brand/             ← Sahas AI logos (vector SVG, PNG fallback) + round seal
├── scripts/render.py         ← HTML → PDF (+ PNG previews)
└── examples/                 ← finished demo (HTML + PDF)
```

## Workflow

1. **Get the brief:** topic, audience, **language** (English · Hinglish · Marathi), **mode** (Light / Dark) and format.
   Defaults: `carousel` (1080×1350, 6–10 pages), English, Light mode. For Hinglish or Marathi read
   `references/languages.md` first.
2. **Read `references/style-guide.md`.**
3. **Plan the pages:** one idea per page.
   - **Page 1** is the centred cover.
   - **Inner pages:** each is tab → h2 → intro → one main component → optional note.
   - **Last page** is the dark thank-you page.
   - **Budget per carousel page:** 1 heading, an intro line, and max ~6 list items, or one diagram/table plus ~3 bullets.
4. **Copy `assets/template.html`** next to the output and fill it in. Keep the `<body>` attributes as they are.
5. **Render:**
   ```bash
   python scripts/render.py path/to/notes.html --png
   ```
   Options: `-o out.pdf`, `--format a4|carousel|square|flow`, `--keep-html`.
   Needs Chrome, Edge or Chromium (auto-detected, or set `CHROME_PATH`). `--png` needs `pip install pymupdf`.
6. **Verify (mandatory):**
   - If it prints `WARNING: content overflows on page(s) N`, split or trim those pages.
   - Look at **every** preview PNG against the checklist below. Fix and re-render until it's clean.
7. **Deliver** the PDF, and mention the HTML source so it can be edited later.

## Two approved themes: Light mode and Dark mode (ask which one if the user doesn't say)

| Theme | `<body>` class | Look |
|---|---|---|
| **Light mode** (default) | `body-patrick` | plain off-white paper (**no grid lines**), red body text, navy headings, black keywords |
| **Dark mode** | `body-patrick theme-dark` | dark brown `#1B1714` on every page; **gold `#E0A843` replaces red, cream `#F3EEDB` replaces black/navy**; never red on brown |

Both themes share the same structure, components, logo rules and thank-you page. In Dark mode the cover
automatically switches to the cream stacked logo, and the yellow corner badge keeps the brown logo.

## The approved Sahas style: non-negotiable rules

### Fonts
- **Kalam:** titles, subtitles, headings, box titles, underlined keywords, circled words, callout statements, labels.
- **Patrick Hand:** only normal paragraph, list and description text (`<body class="body-patrick">`).

### Text colour
- **Paper:** plain, **no grid lines** on any page.
- **Red body text** (original scheme; Dark mode uses gold instead).
- **Navy:** section headings.
- **Black bold + underline:** keywords (2–4 per block).
- **Green:** only the conclusion ("In short…").
- **Exception: no red text inside tables and flow diagrams.** Table cells and flow-box descriptions use dark ink. CSS handles this automatically.

### Colour and icons (restraint)
- **How many:** colour boxes and icons go only on genuinely important spots, about **2–3 per page**. Some pages have none.
- **Plain by default:** normal text and ordinary bullet lists stay plain (em-dash list, no icons, no box).
- **Where icons are allowed:**
  - flow step boxes (brand logos like `<i class="logo whatsapp">` or colour emoji like 🤖 📋 🤝)
  - circled callouts (`.ring.fill` + one icon, e.g. 📞 Voice AI)
  - card grids where each icon identifies the item (🦷 clinic, 🏠 real estate…)
- **Never an icon on:** note/tip/warning/money boxes, table headers or comparison-box titles. Those get colour and a highlighted label only.
- **Each icon must carry meaning** and must not repeat on a page.

### Logos (all in `assets/brand/`, vector SVG so they stay sharp)
| Logo | Where | Markup |
|---|---|---|
| Horizontal **brown** | top-right badge on every inner page (rounded yellow box, curled corner, logo only) | `<body data-logo="brown">` (automatic) |
| Stacked **dark** | **cover** on a light background, centred | `<div class="logo-stacked dark"></div>` |
| Stacked **cream** | **thank-you page** on a dark background | `<div class="logo-stacked cream center"></div>` |
| Round **seal** | only where a stamp fits naturally (thank-you page) | `<div class="seal"></div>` |

- Cream logos go **only on dark backgrounds**, never on white or yellow.
- The cover and thank-you page use `no-brand` (no corner badge; the big logo is already there).
- The agency's full name is **"Sahas AI Business Automation Agency"**. Use it on the thank-you page.

### Cover and thank-you page
- **Cover:** `class="page center cover-center no-brand"`. Logo, kicker, title, subtitle and chips are all centred, and the red wave runs the full title width.
- **Thank-you page:** `class="page center dark-page no-brand"`. Cream stacked logo, "Thank you!", gold wave, a save/share line, the seal and the full agency name.
  - No phone numbers or personal contact details unless the user provides a published business line.

## Component quick reference (snippets in the style guide)

| Need | Markup |
|---|---|
| Page | `<section class="page">…</section>` |
| Breadcrumb tab | `<div class="tab">✎ Topic name</div>` (first element on inner pages) |
| Kicker | `<p class="kicker">Method 3</p>` |
| Section heading | `<h2><span>Heading text</span></h2>` → ✱ + navy underline |
| Keyword | `<span class="k">word</span>` |
| Circled callout | `<div class="callout"><span class="ring">Word</span><span class="arrow"></span><span class="said">statement</span></div>`; filled: `ring fill` (+ `blue` / `green` / `yellow`) |
| Dash list | `<ul class="dash"><li>…</li></ul>` |
| Numbered steps | `<ol class="steps"><li><h3>Title</h3><p>desc</p></li></ol>` (`tight`) |
| Coloured note | `<div class="note tip"><span class="label">Tip:</span> …</div>`, kinds `tip good warn info money fact` (plain `note` = dashed navy) |
| Takeaway | `<p class="takeaway">In short — …</p>` |
| Divider | `<hr class="rule">` |
| Table | `<table class="ink">`; coloured headers `th-red th-green th-blue` |
| Colour-coded flow | `<div class="flow steps-flow"><div class="box step s-green" data-n="1"><div class="ic">…icon…</div><span class="t">Title</span><span class="d">desc</span></div><div class="arr a-green"></div>…</div>`, colours `s-green s-blue s-purple s-orange s-pink s-teal` |
| Plain flow / vertical flow | `.flow` + `.box` + `.arr` · `.vflow` + `.arr-down` |
| Cards / compare | `.grid2` `.grid3` of `.box` · `<div class="vs"><div class="box red fill-red">…</div><div class="mid">vs</div><div class="box green fill-green">…</div></div>` |
| Timeline | `<div class="timeline"><div><span class="when">Now →</span> …</div></div>` |
| Bars | `<div class="bars"><div class="bar"><span class="lbl">X</span><span class="trk"><i style="--v:70"></i></span><span class="val">70%</span></div></div>` |
| UI sketches | `.wire-input` `.wire-chip` `.wire-btn` `.wire-line` inside a `.box` |
| Source line | `<p class="src">Source: …</p>` |

## Writing rules
- **Tone:** short, practical, first-hand. One line per point, em-dash asides, concrete numbers and real examples. Talk to the reader ("you").
- **Visuals over paragraphs:** prefer a diagram, table or steps whenever there's a process, comparison or list.
- **Facts:** never invent statistics. Unsourced numbers must be framed as examples or estimates, and real ones get a `.src` line.
- **Languages:** English, Hinglish (Roman-script Hindi + English tech words) and Marathi (Devanagari). Follow `references/languages.md` for voice, fixed labels, `<html lang>` and `data-swipe`.
- **Never include:** PAN, Aadhaar, bank/UPI details, API keys, passwords or client personal contact details.

## Quality checklist (check on the PNGs)
- [ ] No overflow warning, and nothing touches the footer dots or the corner badge
- [ ] Carousel headings fit on one line (shorten them if not)
- [ ] 0–3 colour/icon accents per page; plain lists are plain; no icons on note boxes or table headers
- [ ] No red text inside tables or flows
- [ ] Cover is centred with the dark stacked logo; the last page is the dark thank-you page with the cream logo and full agency name
- [ ] Brown badge on every inner page; no cream logo on a light background
- [ ] Facts are correct and sourced; no personal data
