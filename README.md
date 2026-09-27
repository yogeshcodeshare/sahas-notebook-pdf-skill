# notebook-notes-pdf — Sahas AI notes-PDF skill

An agent skill that turns any topic into Sahas AI's **hand-lettered grid-paper notes PDFs**:
Kalam titles + Patrick Hand body, red ink text, navy ✱ headings, circled callouts, colour-coded
flow diagrams with real logos/icons, ruled tables, pastel note boxes, Sahas AI logos on the cover,
a corner badge on every page and a dark thank-you page. Formats: Instagram/LinkedIn carousel
(1080×1350), square, A4 pages and long A4 flowing notes.

## Install

**Claude Code (recommended):** copy or clone this folder to

```bash
git clone <your-repo-url> ~/.claude/skills/notebook-notes-pdf
```

(or into a project's `.claude/skills/notebook-notes-pdf/`). Then ask for notes "in my notebook style"
and the skill triggers automatically.

**Claude.ai / Claude desktop:** zip this folder and upload it under *Settings → Capabilities → Skills*.

**Other AI tools (ChatGPT, Codex, Gemini…):** give them this folder and tell them to follow `SKILL.md`.

## Requirements

- Python 3.8+
- Google Chrome, Microsoft Edge or Chromium (auto-detected; or set `CHROME_PATH`)
- Optional: `pip install pymupdf` for PNG page previews

Runs fully offline — nothing is uploaded anywhere.

## Use

```bash
python scripts/render.py examples/future-of-ai-automation-agency-india-light.html --png
```

Start new documents from `assets/template.html`. The rules are in `SKILL.md`,
`references/style-guide.md` and `references/languages.md`.

**Modes:** Light mode (default, `class="body-patrick"`) · Dark mode (`class="body-patrick theme-dark"`).
**Languages:** English · Hinglish · Marathi. Examples of each are in `examples/`.

## Licences

- Fonts in `assets/fonts/`: Kalam (Indian Type Foundry), Patrick Hand (Patrick Wagesreiter),
  Caveat (Impallari Type), Shantell Sans (Arrow Type), all under the SIL Open Font License 1.1
  (`assets/fonts/OFL.txt`), from github.com/google/fonts.
- Logos in `assets/brand/` are **© Sahas AI Business Automation Agency, all rights reserved**. They are not
  open-licensed. Keep the repository **private**, or remove `assets/brand/` before making anything public.
- Colour emoji come from the operating system's emoji font, so they look slightly different on Windows,
  macOS and Linux.
