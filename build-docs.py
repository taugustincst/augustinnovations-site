#!/usr/bin/env python3
"""Render the public-safe business documents (Markdown) into styled site pages."""
import re
import sys
from pathlib import Path

sys.path.insert(0, "/tmp/mdenv/lib/python3.12/site-packages")
import markdown  # noqa: E402

SRC = Path.home() / "workspace" / "augustinnovations-site" / "documents-src"
OUT = Path.home() / "workspace" / "augustinnovations-site" / "documents"
OUT.mkdir(parents=True, exist_ok=True)

DOCS = [
    ("capability-statement", "Capability Statement",
     "Entity facts, core competencies, products, and differentiators for AugustInnovations LLC."),
    ("suds-vendor-overview", "SUDS — Vendor Overview for Buyers",
     "What SUDS is, its deployment and isolation model, security posture, published pricing, and status."),
    ("cseed-product-sheet", "CSeed — Product Sheet",
     "Local-only clinical de-identification for Windows: formats, safeguards, license terms, and pricing."),
    ("clinical-perimeter-services", "Clinical Perimeter — Services",
     "Web application penetration tests for healthcare software vendors: scope, price, guardrails, and deliverables."),
    ("rules-of-engagement-template", "Rules of Engagement — Template",
     "The standard rules governing every Clinical Perimeter engagement, executed before testing begins."),
    ("testing-authorization-template", "Testing Authorization — Template",
     "The written client authorization under which Clinical Perimeter performs security testing."),
]

SHELL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — AugustInnovations LLC</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://augustinnovations.io/documents/{slug}.html">
<link rel="icon" type="image/svg+xml" href="../logo.svg">
<style>
  :root{{--navy:#16324A; --navy-deep:#0F2436; --teal:#177A6B; --teal-dark:#11604F;
    --gold:#C9902E; --ink:#1C2733; --muted:#5A6B7A; --paper:#F7F5F0; --card:#FFFFFF; --line:#E2DDD2}}
  *{{box-sizing:border-box}}
  body{{margin:0;font-family:Georgia,'Times New Roman',serif;background:var(--paper);color:var(--ink);line-height:1.65}}
  h1,h2,h3,.sans{{font-family:-apple-system,'Segoe UI',Helvetica,Arial,sans-serif}}
  a{{color:var(--teal-dark)}}
  .wrap{{max-width:860px;margin:0 auto;padding:0 24px}}
  header{{background:var(--navy);color:#fff}}
  .topbar{{display:flex;align-items:center;justify-content:space-between;padding:14px 0;flex-wrap:wrap;gap:8px}}
  .brand{{display:flex;align-items:center;gap:11px}}
  .brand img{{width:34px;height:34px}}
  .brand .mark{{font-family:-apple-system,'Segoe UI',Helvetica,Arial,sans-serif;font-weight:800;font-size:20px;color:#fff}}
  .brand .mark span{{color:var(--gold)}}
  nav a{{color:#E7EEF3;text-decoration:none;margin-left:20px;font-size:14.5px;font-family:-apple-system,'Segoe UI',Helvetica,Arial,sans-serif}}
  nav a:hover{{color:var(--gold)}}
  main{{padding:38px 0 10px}}
  main h1{{font-size:31px;color:var(--navy);margin:0 0 14px;line-height:1.25}}
  main h2{{font-size:22px;color:var(--navy);margin:30px 0 8px}}
  main h3{{font-size:18px;color:var(--navy);margin:22px 0 6px}}
  table{{border-collapse:collapse;width:100%;margin:14px 0;font-size:15.5px}}
  th,td{{border:1px solid var(--line);padding:8px 12px;text-align:left;vertical-align:top}}
  th{{background:#EFECE3}}
  .crumb{{font-family:-apple-system,'Segoe UI',Helvetica,Arial,sans-serif;font-size:13.5px;color:var(--muted);margin-bottom:18px}}
  footer{{background:var(--navy-deep);color:#B9C9D6;margin-top:56px;padding:28px 0 34px;font-size:14px}}
  footer a{{color:#E7EEF3}}
  .doclist{{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:8px 26px 18px}}
  .doclist h3{{margin:20px 0 2px}}
  .doclist p{{margin:0 0 6px;color:var(--muted);font-size:15.5px}}
</style>
</head>
<body>
<header><div class="wrap topbar">
  <div class="brand"><img src="../logo.svg" alt=""><div class="mark">August<span>Innovations</span></div></div>
  <nav><a href="../index.html">Home</a><a href="index.html">Documents</a><a href="../index.html#contact">Contact</a></nav>
</div></header>
<main><div class="wrap">
<p class="crumb"><a href="../index.html">AugustInnovations LLC</a> · <a href="index.html">Documents</a> · {crumb}</p>
{body}
</div></main>
<footer><div class="wrap">
<p>© 2026 AugustInnovations LLC · Plumas Lake, California · D-U-N-S® 12-343-3746 · <a href="mailto:info@suds.systems">info@suds.systems</a></p>
</div></footer>
<script src="../lead.js" data-inbox="info@suds.systems" data-brand="AugustInnovations LLC" data-site="augustinnovations.io" data-interests="General inquiry|SUDS|Clinical Perimeter|CSeed|ReleaseReaper|Consulting" data-interest="General inquiry" data-head="#16324A" data-accent="#C9902E" data-accent-ink="#0F2436"></script>
</body>
</html>
"""


def clean(md_text: str) -> str:
    # Public renders: no street address, no draft status line.
    md_text = md_text.replace("1347 Meadow Ranch St, Plumas Lake, CA 95961", "Plumas Lake, California")
    md_text = re.sub(r" · \*\*Status:\*\* Draft for owner review", "", md_text)
    return md_text


for slug, title, desc in DOCS:
    raw = (SRC / f"{slug}.md").read_text(encoding="utf-8")
    body = markdown.markdown(clean(raw), extensions=["tables"])
    html = SHELL.format(title=title, desc=desc, slug=slug, crumb=title, body=body)
    (OUT / f"{slug}.html").write_text(html, encoding="utf-8")
    print("rendered", slug)

items = "\n".join(
    f'<h3><a href="{slug}.html">{title}</a></h3><p>{desc}</p>' for slug, title, desc in DOCS
)
index_body = f"""<h1>Business documents</h1>
<p>The public document set for AugustInnovations LLC and its products — SUDS, CSeed, and Clinical Perimeter.
Documents not listed here (including Form W-9 and executed agreements) are provided on request:
<a href="mailto:info@suds.systems">info@suds.systems</a>.</p>
<div class="doclist">{items}</div>"""
index_html = SHELL.format(
    title="Business Documents", desc="Public business documents for AugustInnovations LLC: capability statement, product sheets, service terms, and engagement templates.",
    slug="index", crumb="Documents", body=index_body)
(OUT / "index.html").write_text(index_html, encoding="utf-8")
print("rendered index")
