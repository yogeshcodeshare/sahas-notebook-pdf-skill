# Style guide — the Sahas AI "grid-paper notebook" look

The goal: any model using this skill produces pages a reader would mistake for the same author.
Every rule here was approved page by page by the owner — follow it, don't reinvent it.

## 1. Visual DNA

| Element | Spec |
|---|---|
| Paper | plain off-white `#fbfbf8`, **no grid lines** (Dark mode: plain dark brown `#1b1714`) |
| Body font | **Patrick Hand** for normal paragraph / list / description text only (`body.body-patrick`) |
| Title font | **Kalam** 700 for titles, subtitles, headings, box titles, keywords, circled words, callouts, labels |
| Script font | **Caveat** 700 for cover titles, kickers ("Method 3"), "Swipe →" |
| Red `#d7392b` | explanatory body text, kickers, callout statements, ring words — **but never inside tables or flow diagrams** (dark ink there) |
| Navy `#1f2d6e` | section headings (underlined) and dashed note-box text |
| Black `#161616` | cover title, h3 step titles, keywords (bold + underline), number dots, rules, table borders |
| Green `#1d8a3a` | the conclusion / "In short" / "No theory…" line, "Swipe →" |
| Grey `#8b909b` | page count, sources |
| Brand badge | rounded yellow box top-right, black border, slight tilt, curled bottom-right corner, **brown horizontal Sahas logo only** (`data-logo="brown"`) |
| Breadcrumb tab | dashed red rounded pill across the top: "✎ Section name" |
| Footer | page dots `●○○○` bottom-left, `n/N` or green "Swipe →" bottom-right |

Hand-drawn feel comes from: the fonts, the imperfect oval ring, curvy arrows, wavy red underline,
white cards with offset shadow, dotted separators. Keep everything else clean and aligned.

## 2. Page anatomy

```
[✎ tab ....................................]  [brand badge]
Kicker (red script, optional)
✱ Section Heading (navy, underlined)
Intro line in red with one keyword underlined.
( Ring ) ⟶ The one big idea in red bold
❶ Step title (black)
   red description with a keyword — em-dash aside
─────────────────────────────── (thick black rule between two topics)
┆ Good to know: navy note in a dashed box ┆
In short — green conclusion.
●○○○○○                                              Swipe →
```

Two topics may share a page, separated by `<hr class="rule">`, each with its own `h2`
(and optional kicker like "Method 3" / "Method 4").

## 3. Writing voice

- Practitioner, not professor. "No theory. Only what I have actually done."
- One point per line. Lines start with an em dash (`ul.dash`) or a number dot (`ol.steps`).
- Formula: **keyword** — plain consequence/example. e.g. "— **No link in the first message** — it reads as spam."
- Concrete numbers ("20 connection requests a day", "30–40 emails, never cross 50"), named tools, Indian context (₹, GST, Udyam, tier-2 cities) where relevant.
- Parenthetical tags on step titles: "WhatsApp API Method *(the old way)*" → `<h3>… <small>(the old way)</small></h3>`.
- Note-box labels: **Good to know:**, **Limitation:**, **Tip:**, **Note:**, **Small correction:**, **What is technically happening:**.
- Ring words are 1–3 words: a label ("Pick a niche", "Only abroad", "₹15,000", "POV RULE").
- Close with a green summary that restates the whole page/deck in 2–3 sentences.
- Hinglish variant: same structure, Roman Hindi sentences, English for tech terms and keywords.

## 4. Component cookbook

### Cover (carousel)
```html
<section class="page center">
  <svg class="icon-doodle" viewBox="0 0 100 100">…simple 2-colour line icon…</svg>
  <p class="kicker">Make money with AI</p>
  <h1 class="title xl">How to close clients for AI automation</h1>
  <div class="wave"></div>
  <p class="subtitle">7 ways to find them + the pitch that actually closes</p>
  <div class="chips"><span>Cold calling</span><span>Cold email</span><span>LinkedIn</span></div>
  <hr class="rule mt2">
  <p class="takeaway">No theory. Only what I have actually done.</p>
</section>
```
Alternative cover line: `<div class="callout"><span class="ring ink">7 ways</span><span class="arrow"></span><span class="said">to find them + the pitch that closes</span></div>`.

### Steps with titles
```html
<ol class="steps">
  <li><h3>Go to Facebook Business Manager</h3>
      <p>Log in. <span class="k">Condition:</span> the account must be 3+ months old.</p></li>
</ol>
```
Titles-only list: `<ol class="steps tight"><li><h3>WhatsApp Support Agent</h3></li>…</ol>`.
Inline numbered keyword list (like "❶ One niche — real estate, clinics…"):
`<ol class="steps tight"><li><p><span class="k">One niche</span> — real estate, clinics. Just one.</p></li></ol>`.

### Ring + arrow statement
```html
<div class="callout"><span class="ring">Dashboard</span><span class="arrow squiggle"></span>
  <span class="said">WhatsApp has no built-in inbox — you build your own.</span></div>
```
`.callout.soft` = normal-weight statement (for longer sentences).

### Table
```html
<table class="ink">
  <tr><th>Method</th><th>Meaning</th><th>When</th></tr>
  <tr><td>GET</td><td>Read data</td><td>Fetch a list</td></tr>
</table>
```

### Hand-drawn UI sketch (e.g. "LinkedIn → Companies → About")
```html
<div class="flow">
  <div class="box" data-n="1"><div class="wire-input">real estate</div><span class="d">search icon</span></div>
  <div class="arr"></div>
  <div class="box" data-n="2"><span class="wire-chip">Companies</span><span class="wire-line"></span><span class="wire-line w60"></span></div>
  <div class="arr"></div>
  <div class="box" data-n="3"><span class="t nv">About</span><span class="wire-line w80"></span><span class="wire-btn">Call</span></div>
</div>
```
Profile grid: `<div class="wire-row"><i class="on"></i><i></i><i class="on"></i><i></i></div>`.

### Compare
```html
<div class="vs">
  <div class="box red"><span class="t">BSP</span><span class="d">Handles billing, adds 5–20% margin</span></div>
  <div class="mid">vs</div>
  <div class="box green"><span class="t">Tech Provider</span><span class="d">Client pays Meta directly</span></div>
</div>
```

### Custom inline SVG diagrams
When a kit component doesn't fit, draw a small inline `<svg>` using only the palette colours,
`stroke-width` 3–4, `stroke-linecap="round"`, no fills except black arrowheads / light tints,
and label with `font-family="Kalam"`.

## 5. Do / Don't

Do: keep margins generous · align everything left · one accent per page · white space between blocks.
Don't: use emoji clutter (one small symbol in the tab is fine) · paragraphs over 3 lines · more than
2 green lines per page · colours outside the palette · stock photos · centred body text.

## 6. Colour & icon restraint (owner's rule)

- Colour boxes and icons only at the **2–3 most important spots per page**; some pages get none.
- **Icons allowed:** flow step boxes (brand logos / colour emoji), circled callouts (`.ring.fill` + one icon), item-identifying card grids.
- **No icons on:** note/tip/warn/money boxes, table headers, comparison-box titles — those get colour + highlighted label only.
- Normal paragraphs and ordinary bullet lists stay plain. Each icon must mean something and appear once per page.
- Colour-coded flow: one pastel colour per step (`s-green → s-blue → s-purple → s-orange`), matching arrows (`a-*`), numbered circle on top, icon, Kalam title in the step colour, small dark description.

## 7. Logos & bookend pages

| Asset (assets/brand) | Use |
|---|---|
| `sahas-logo-horizontal-brown.svg` | corner badge on every inner page (automatic with `data-logo="brown"`) |
| `sahas-logo-stacked-dark.svg` | cover page, light background, centred |
| `sahas-logo-stacked-cream.svg` | thank-you page, dark background |
| `sahas-seal.svg` | round stamp — only where it fits naturally (thank-you page) |
| `*-cream.*` | **dark backgrounds only** |

- Agency name in full: **Sahas AI Business Automation Agency**.
- Cover = `page center cover-center no-brand`: everything centred, wave spans the title.
- Thank-you = `page center dark-page no-brand`: cream stacked logo, "Thank you!", gold wave, save/share line, seal + full agency name.
- SVG logos are vector → sharp at every zoom; PNGs exist only as fallback.

## 8. Dark mode (`body.theme-dark`)

Same pages and components as Light mode, but on the thank-you page's dark brown `#1b1714`:
- **Gold `#e0a843`:** every place Case 1 uses red (body text, callouts, kickers, tab, wave, timeline dots).
- **Cream `#f3eedb`:** titles, headings, keywords, number dots, rules, table borders, ring and arrow strokes.
- **Heading and keyword underlines** are gold. The green takeaway becomes a soft green `#8fd49b`.
- **Boxes, flow steps and notes** switch to dark tinted versions of their colours.
- **Logos:** the cover uses the cream stacked logo automatically. The corner badge stays yellow with the brown logo.
- **Never** put red text on the brown background.
