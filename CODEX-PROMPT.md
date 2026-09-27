# Prompt for Codex: Sahas AI notebook-notes PDF skill

Paste everything below the line into Codex once, at the start of a session. After that, just ask:
"Make notes on <topic>, <language>, <light/dark> mode".

---

You have a local skill on this laptop called **notebook-notes-pdf**. It creates Sahas AI's notes and
carousel PDFs in a fixed, owner-approved style. Use the local files only. Do NOT fetch anything from
GitHub or the internet to use this skill.

**Skill folder (absolute path):**
`C:\Yogesh - personal\Claude\Cluade Projects\Ai Automation\.claude\skills\notebook-notes-pdf\`

**Before your first document, read these files fully, in this order:**
1. `SKILL.md`: workflow, the approved rules, the component reference and the quality checklist
2. `references/style-guide.md`: visual DNA, voice, snippets for every component
3. `references/languages.md`: English / Hinglish / Marathi rules and fixed labels
4. `assets/template.html`: the starter file you copy for every new document
5. One finished example that matches the request, in `examples/`:
   - English, Light mode: `future-of-ai-automation-agency-india-light.html`
   - English, Dark mode: `future-of-ai-automation-agency-india-dark.html`
   - Hinglish: `sample-hinglish-light.html`
   - Marathi: `sample-marathi-dark.html`

**When I ask for notes on a topic:**
1. **Fill the gaps.** If I don't say, ask once for:
   - language: English, Hinglish or Marathi
   - mode: Light mode (default) or Dark mode
   - format: carousel 1080×1350 is the default
2. **Plan.** One idea per page: page 1 is the centred cover, then the inner pages, then the dark thank-you page last. Keep to the per-page budget in SKILL.md.
3. **Write the HTML.** Copy `assets/template.html` to my output folder and write the pages using ONLY the skill's CSS classes.
   - Don't add new CSS and don't change the design.
   - Keep the `<body>` attributes. Add `theme-dark` for Dark mode, and set `<html lang>` plus `data-swipe` for Hinglish or Marathi, as `languages.md` says.
4. **Render** with the skill's own script (it injects the CSS, fonts and logos automatically):
   ```
   python "C:\Yogesh - personal\Claude\Cluade Projects\Ai Automation\.claude\skills\notebook-notes-pdf\scripts\render.py" "<my-file>.html" --png
   ```
   It needs Chrome or Edge, which is already installed; PyMuPDF is used for the PNG previews.
5. **Verify.** If it prints `WARNING: content overflows`, split or trim those pages and re-render.
   - Then open EVERY preview PNG and check it against the checklist at the end of SKILL.md.
   - Fix and re-render until it's clean.
6. **Report.** Give me the PDF path and the HTML path.

**Rules you must never break** (details in SKILL.md):
- **Fonts:** Kalam for titles, headings, keywords and callouts; Patrick Hand only for normal text.
- **Light mode:** red body text, navy headings, no grid lines. **No red text inside tables or flow diagrams.**
- **Dark mode:** brown `#1B1714` background, gold instead of red, cream instead of black. Never red on brown.
- **Icons:** only in flow step boxes and circled callouts, 2–3 accents per page at most. Never on note boxes, table headers or comparison titles. Normal lists stay plain.
- **Logos (automatic from `assets/brand/`):**
  - brown horizontal logo in the top-right badge on inner pages
  - stacked logo only on the cover and the thank-you page
  - cream logos only on dark backgrounds
  - round seal only on the thank-you page
- **Agency name:** always "Sahas AI Business Automation Agency".
- **Facts:** never invent statistics; source real numbers with a `.src` line.
- **Privacy:** never include PAN, Aadhaar, bank/UPI details, API keys, passwords or client personal contact details.
- **Output location:** save outputs next to where I ask, or in the current project folder. Never write outputs inside the skill folder.
- **Skill files:** don't edit anything in the skill folder unless I explicitly ask you to change the skill.
- **Confidentiality:** everything here is private Sahas AI work. Keep it on this machine; don't upload it anywhere.
