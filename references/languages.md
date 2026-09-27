# Languages: English · Hinglish · Marathi

The layout, components, colours and logos are identical in every language. Only three things change:
the words, `<html lang="…">`, and the footer swipe text (`data-swipe` on `<body>`).

| Language | `<html lang>` | `data-swipe` | Script | Fonts |
|---|---|---|---|---|
| English | `en` | *(omit → "Swipe →")* | Latin | Kalam titles + Patrick Hand body |
| Hinglish | `hi-Latn` | `Swipe karo →` | Latin (Roman Hindi) | same as English |
| Marathi | `mr` | `पुढे पाहा →` | Devanagari | Kalam renders Devanagari for titles *and* body (Patrick Hand has no Devanagari, so it falls back automatically) |

Keep these in English in **every** language: brand and tool names (WhatsApp, n8n, Meta, CRM, AI, API),
numbers, ₹ amounts, dates, and the agency name **Sahas AI Business Automation Agency**.

## English

Short, practical, first-hand. One line per point, em-dash asides, concrete numbers. See the style guide.

## Hinglish (Roman-script Hindi + English)

Based on the owner's approved Hinglish notes (e.g. *"Meta approval, pricing aur setup — poora funda"*).

**Voice**
- Sentence structure is Hindi and written in Roman letters; all tech words stay English: *"Approval ke baad agent, bulk, marketing — sab chalega."*
- Address the reader as **aap**, with friendly imperatives: *karo, becho, lo, bhejo, check kar lena*. Never *tu*.
- Everyday, spoken words: *poora funda, jhanjhat khatam, seedhi baat, asli baat ye hai, isi wajah se, fir*.
- Keep it simple. Avoid heavy Sanskrit Hindi (write *zaroorat*, not *aavashyakta*).
- **Headings:** short and mixed, e.g. *"4 tarah ke message aur cost"*, *"Raasta 1 — WhatsApp Business API"*.
- **Keywords** (`.k`) are usually the English term: *"AI **qualify** karta hai, owner **close** karta hai"*.

**Spelling:** use one consistent Roman spelling per document. *hai, hain, nahi, mein, ke liye, kya, kyun, kaise, abhi, pehle, baad, sirf, sab, aap, karo, hota, chahiye, zaroorat, paisa*.

**Fixed labels**
| English | Hinglish |
|---|---|
| Tip: | Tip: |
| Good to know: | Yaad rakho: |
| Note: | Note: |
| Catch: / Limitation: | Catch: |
| Rule of thumb: | Seedha rule: |
| In short — | Seedhi baat — |
| Thank you! | Thank you! |
| Save this and share… | Save karo, aur … ko bhejo |

## Marathi (मराठी, Devanagari)

**Voice**
- Standard, conversational Marathi, as spoken in Karad, Satara or Pune: clear and friendly, not literary.
- Address the reader as **तुम्ही**, with verbs like *करा, विका, पाठवा, तपासा*.
- **English tech words** are either written in Devanagari the way they're spoken (*क्लायंट, लीड, फॉलो-अप, बिझनेस, सेटअप, रिटेनर*) or kept in Latin letters for brand names (WhatsApp, CRM, AI, API, n8n). Don't force pure-Marathi coinages that owners wouldn't use.
- **Headings:** short, e.g. *"एजन्सीचं स्वरूप बदलतंय"*. Spoken contractions like *बदलतंय, खरं, चाललंय* are fine and sound natural.
- **Punctuation:** the full stop is `.` (not `।`). Keep em-dashes — for asides.
- Numbers stay in Western digits (2026, ₹15,000).

**Fixed labels**
| English | Marathi |
|---|---|
| Tip: | टीप: |
| Good to know: | लक्षात ठेवा: |
| Note: | नोंद: |
| Warning / Catch: | लक्ष द्या: |
| Rule of thumb: | साधा नियम: |
| In short — | थोडक्यात — |
| Old / New | जुनी / नवी |
| Thank you! | धन्यवाद! |
| Save this and share… | हे सेव्ह करा, आणि … ला पाठवा |

**Checks for Marathi pages**
- Devanagari is taller than Latin. Keep carousel headings to one line (≈ 26 characters), and titles to at most 3 lines.
- Proof-read the matras. If unsure about a word, prefer the simpler common one.

## Examples in `examples/`
- `sample-hinglish-light.html / .pdf`: Hinglish, Light mode
- `sample-marathi-dark.html / .pdf`: Marathi, Dark mode
- `future-of-ai-automation-agency-india-light.html / .pdf`: English, Light mode
- `future-of-ai-automation-agency-india-dark.html / .pdf`: English, Dark mode
