#!/usr/bin/env python3
"""Render a notebook-style HTML file to PDF with local headless Chrome / Edge / Chromium.

Usage:
    python render.py notes.html                 # -> notes.pdf next to it
    python render.py notes.html -o out.pdf --png  # also write page PNG previews (needs PyMuPDF)
    python render.py notes.html --format carousel

The HTML only needs <section class="page"> blocks (or free-flowing content with
data-format="flow"). This script injects assets/notebook.css + notebook.js, sets the
@page size for the chosen format, checks every page for overflow, then prints to PDF.
Everything runs locally; nothing is uploaded anywhere.
"""
import argparse, os, re, shutil, subprocess, sys, tempfile
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
ASSETS = SKILL_DIR / "assets"

PAGE_SIZES = {
    "a4": "@page { size: 210mm 297mm; margin: 0; }",
    "carousel": "@page { size: 1080px 1350px; margin: 0; }",
    "square": "@page { size: 1080px 1080px; margin: 0; }",
    "flow": "@page { size: 210mm 297mm; margin: 0; }",
}

CANDIDATES = [
    os.environ.get("CHROME_PATH", ""),
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
]


def find_browser():
    for c in CANDIDATES:
        if c and Path(c).exists():
            return c
    for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "chrome", "msedge", "microsoft-edge"):
        p = shutil.which(name)
        if p:
            return p
    sys.exit("No Chrome/Edge/Chromium found. Install one or set CHROME_PATH.")


def detect_format(html):
    m = re.search(r'<body[^>]*data-format\s*=\s*["\'](\w+)["\']', html, re.I)
    return (m.group(1).lower() if m else "a4")


def brand_vars():
    """CSS variables pointing at the bundled brand assets (used by data-logo)."""
    b = ASSETS / "brand"
    # vector SVGs stay sharp at every zoom level; PNGs are kept only as a fallback
    files = {"brown": "sahas-logo-horizontal-brown", "cream": "sahas-logo-horizontal-cream", "seal": "sahas-seal",
             "stacked-dark": "sahas-logo-stacked-dark", "stacked-cream": "sahas-logo-stacked-cream"}
    files = {k: (f + ".svg" if (b / (f + ".svg")).exists() else f + ".png") for k, f in files.items()}
    return ":root{" + "".join(f"--brand-logo-{k}:url('{(b / f).as_uri()}');" for k, f in files.items() if (b / f).exists()) + "}"


def build_html(src_html, fmt):
    css = (ASSETS / "notebook.css").as_uri()
    js = (ASSETS / "notebook.js").as_uri()
    head = (f'<link rel="stylesheet" href="{css}">\n'
            f'<style>{PAGE_SIZES[fmt]}\n{brand_vars()}</style>\n'
            f'<script src="{js}"></script>\n')
    # drop any author-side link to notebook.css/js so they are not loaded twice
    src_html = re.sub(r'<link[^>]+notebook\.css[^>]*>', '', src_html, flags=re.I)
    src_html = re.sub(r'<script[^>]+notebook\.js[^>]*>\s*</script>', '', src_html, flags=re.I)
    if not re.search(r'data-format', src_html, re.I):
        src_html = re.sub(r'<body', f'<body data-format="{fmt}"', src_html, count=1, flags=re.I)
    else:
        src_html = re.sub(r'(<body[^>]*data-format\s*=\s*["\'])\w+', rf'\g<1>{fmt}', src_html, count=1, flags=re.I)
    if re.search(r'<head[^>]*>', src_html, re.I):
        return re.sub(r'(<head[^>]*>)', lambda m: m.group(1) + "\n" + head, src_html, count=1, flags=re.I)
    return "<!doctype html><html><head><meta charset='utf-8'>" + head + "</head>" + src_html + "</html>"


def chrome(browser, args, profile, budget=8000):
    base = [browser, "--headless=new", "--disable-gpu", "--no-first-run", "--no-default-browser-check",
            "--allow-file-access-from-files", f"--user-data-dir={profile}", f"--virtual-time-budget={budget}"]
    return subprocess.run(base + args, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=180)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("html")
    ap.add_argument("-o", "--out")
    ap.add_argument("--format", choices=list(PAGE_SIZES), help="override body data-format")
    ap.add_argument("--png", action="store_true", help="write page PNG previews next to the PDF")
    ap.add_argument("--keep-html", action="store_true", help="keep the built HTML (for debugging)")
    a = ap.parse_args()

    src = Path(a.html).resolve()
    out = Path(a.out).resolve() if a.out else src.with_suffix(".pdf")
    raw = src.read_text(encoding="utf-8")
    fmt = a.format or detect_format(raw)
    built = build_html(raw, fmt)

    browser = find_browser()
    tmpdir = Path(tempfile.mkdtemp(prefix="nbpdf_"))
    # build file sits next to the source so relative <img src> paths keep working
    build_path = src.parent / f".{src.stem}.build.html"
    build_path.write_text(built, encoding="utf-8")
    try:
        uri = build_path.as_uri()
        # 1) overflow check
        if fmt != "flow":
            m = None
            for attempt in range(4):  # layout script occasionally reports after the DOM dump; retry with more time
                r = chrome(browser, ["--dump-dom", uri], tmpdir / f"p1_{attempt}", budget=10000 + 5000 * attempt)
                m = re.search(r'data-overflow-pages="([^"]*)"', r.stdout)
                if m is not None:
                    break
            if m is None:
                print("warning: could not verify page overflow (layout script did not report)")
            elif m.group(1):
                print(f"WARNING: content overflows on page(s) {m.group(1)} -- split or trim those pages.")
            else:
                print("overflow check: all pages fit")
        # 2) print
        r = chrome(browser, ["--no-pdf-header-footer", "--print-to-pdf-no-header",
                             f"--print-to-pdf={out}", uri], tmpdir / "p2")
        if not out.exists():
            print(r.stderr[-2000:])
            sys.exit("PDF was not produced.")
        print(f"PDF: {out}")
        if a.png:
            try:
                import pymupdf
            except ImportError:
                try:
                    import fitz as pymupdf
                except ImportError:
                    print("PyMuPDF not installed — skipping PNG previews (pip install pymupdf)")
                    return
            doc = pymupdf.open(str(out))
            prev = out.parent / (out.stem + "_preview")
            prev.mkdir(exist_ok=True)
            for i, pg in enumerate(doc):
                pg.get_pixmap(dpi=80).save(str(prev / f"page-{i + 1:02d}.png"))
            print(f"previews: {prev} ({doc.page_count} pages)")
    finally:
        if not a.keep_html:
            build_path.unlink(missing_ok=True)
        shutil.rmtree(tmpdir, ignore_errors=True)


if __name__ == "__main__":
    main()
