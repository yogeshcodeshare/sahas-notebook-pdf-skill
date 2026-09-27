/* notebook.js — adds brand badge, footer (dots / n/N / swipe) and an overflow check
   to every <section class="page">. Configure on <body>:
     data-format   a4 | carousel | square | flow        (default a4)
     data-brand    "Sahas AI"          brand name   (omit → no badge)
     data-initials "SA"                monogram in the circle
     data-tagline  "AI Automation Notes"
     data-handle   "@yourhandle"       (optional)
     data-logo     "brown" | "cream"   show the brand logo (assets/brand) instead of text; cream = dark backgrounds only
     data-footer   "dots" | "count" | "swipe" | "dots+swipe" | "none"   (default dots)
   Per page: class="no-brand" hides the badge, class="no-foot" hides the footer. */
(function () {
  function el(tag, cls, html) { var e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  function build() {
    var b = document.body, d = b.dataset;
    var fmt = d.format || "a4";
    b.classList.add("fmt-" + fmt);
    document.documentElement.classList.add("fmt-" + fmt);
    if (fmt === "flow") return;

    var pages = Array.prototype.slice.call(document.querySelectorAll("section.page"));
    var total = pages.length, footer = d.footer || "dots";

    pages.forEach(function (p, i) {
      // wrap content so footer space is reserved
      if (!p.querySelector(":scope > .body")) {
        var body = el("div", "body");
        while (p.firstChild) body.appendChild(p.firstChild);
        p.appendChild(body);
      }
      if (d.brand && !p.classList.contains("no-brand")) {
        var badge = el("div", "brand",
          '<div class="mono">' + esc(d.initials || d.brand.slice(0, 2).toUpperCase()) + '</div>' +
          '<div><div class="name">' + esc(d.brand) + '</div>' +
          (d.tagline ? '<div class="tag">' + esc(d.tagline) + '</div>' : '') +
          (d.handle ? '<div class="handle">' + esc(d.handle) + '</div>' : '') + '</div>');
        if (d.logo) {
          badge.classList.add("logo-only");
          badge.style.setProperty("--brand-logo", "var(--brand-logo-" + d.logo + ")");
        }
        p.appendChild(badge);
      }
      if (footer !== "none" && !p.classList.contains("no-foot")) {
        var f = el("div", "foot"), left = "", right = "";
        if (footer.indexOf("dots") > -1) {
          var dots = ""; for (var j = 0; j < total; j++) dots += '<i class="' + (j === i ? "on" : "") + '"></i>';
          left = '<div class="dots">' + dots + '</div>';
        } else {
          left = '<div class="count muted">' + (i + 1) + ' / ' + total + '</div>';
        }
        if (footer.indexOf("swipe") > -1 && i < total - 1) right = '<div class="swipe">' + esc(d.swipe || "Swipe →") + '</div>';
        else if (footer.indexOf("dots") > -1 || footer === "count") right = '<div class="count">' + (i + 1) + '/' + total + '</div>';
        f.innerHTML = left + right;
        p.appendChild(f);
      }
    });
  }

  function checkOverflow() {
    var bad = [];
    document.querySelectorAll("section.page").forEach(function (p, i) {
      var body = p.querySelector(":scope > .body"); if (!body) return;
      var limit = p.getBoundingClientRect().bottom - (p.querySelector(":scope > .foot") ? p.querySelector(":scope > .foot").offsetHeight * 0.55 : 0);
      var maxBottom = 0;
      body.querySelectorAll("*").forEach(function (c) { var r = c.getBoundingClientRect(); if (r.height > 0 && r.bottom > maxBottom) maxBottom = r.bottom; });
      if (maxBottom > limit + 1) { p.setAttribute("data-overflow", Math.round(maxBottom - limit)); bad.push(i + 1); }
    });
    document.body.setAttribute("data-overflow-pages", bad.join(","));
    document.body.setAttribute("data-ready", "1");
  }

  function run() {
    build();
    var done = function () { requestAnimationFrame(function () { setTimeout(checkOverflow, 50); }); };
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(done); else done();
    // also check synchronously on window load: headless --dump-dom always waits for load,
    // so the result is present even if the async fonts.ready callback has not fired yet
    window.addEventListener("load", checkOverflow);
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", run); else run();
})();
