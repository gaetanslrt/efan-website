# -*- coding: utf-8 -*-
"""Render the FAQ as a PDF in the site's visual language."""

"""Run:  python3 _source/faq/faq_pdf.py
Edit the questions and answers in faq_data.py, then run this script.
Needs Python 3.8+, Playwright and pypdf:
    pip install playwright pypdf && playwright install chromium
"""

import os, re, sys, base64, tempfile
from pathlib import Path

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from faq_data import DATA, ENROLMENT, ADDRESSES

SITE = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(SITE, "media", "documents")


NB = "\u00a0"


def fr_typo(x):
    """French spacing: no-break space before : ; ? ! % $ and inside « », in 8 h 05."""
    if isinstance(x, str):
        x = re.sub(r" ([:;?!»%$])", NB + r"\1", x)
        x = re.sub(r"« ", "«" + NB, x)
        return re.sub(r"(\d) h (\d)", r"\1" + NB + "h" + NB + r"\2", x)
    if isinstance(x, (list, tuple)):
        return type(x)(fr_typo(i) for i in x)
    if isinstance(x, dict):
        return {k: (v if k in ("lang", "site", "contact") else fr_typo(v)) for k, v in x.items()}
    return x


def text(lang):
    return fr_typo(DATA[lang]) if lang == "fr" else DATA[lang]


def paras(x):
    return [] if not x else ([x] if isinstance(x, str) else list(x))


def b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("ascii")


CSS = """
@page { size: A4; }

* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body {
  margin: 0;
  font-family: Inter, "Public Sans", "DejaVu Sans", sans-serif;
  font-size: 9.6pt;
  line-height: 1.52;
  color: #161616;
}
h1, h2, h3, h4 { margin: 0; font-weight: 700; letter-spacing: -.01em; }
p { margin: 0 0 .5em; }
ul { margin: 0; padding: 0; list-style: none; }

/* ------------------------------------------------------------------ cover */
.cover {
  position: relative;
  page-break-after: always;
  height: 297mm;
  padding: 26mm 20mm 20mm;
  display: flex;
  flex-direction: column;
  background: #f5f5fe;
}
.cover::before {
  content: "";
  position: absolute; inset: 0;
  background-image:
    linear-gradient(to right, rgba(0,0,145,.06) .4mm, transparent .4mm),
    linear-gradient(to bottom, rgba(0,0,145,.06) .4mm, transparent .4mm);
  background-size: 10mm 10mm;
}
.cover > * { position: relative; }
.cover__mark {
  display: inline-block; align-self: flex-start;
  padding: 6mm 7mm; background: #fff; margin-bottom: 20mm;
  box-shadow: 0 0 0 .35mm #cacafb;
}
.cover__logo { display: block; width: 70mm; }
.cover__eyebrow {
  font-size: 8.5pt; font-weight: 700; letter-spacing: .14em;
  text-transform: uppercase; color: #000091; margin-bottom: 5mm;
}
.cover__eyebrow span {
  display: inline-block; width: 12mm; height: .7mm;
  background: #e1000f; vertical-align: .9mm; margin-right: 3mm;
}
.cover h1 {
  font-size: 34pt; line-height: 1.08; color: #000091; margin-bottom: 7mm;
}
.cover__sub { font-size: 12.5pt; color: #3a3a3a; max-width: 120mm; }
.cover__rule {
  width: 60mm; height: 1.4mm; margin: 12mm 0;
  background: linear-gradient(90deg, #000091 0 50%, #e1000f 50% 100%);
}
.cover__inside { margin-top: 14mm; }
.cover__inside p {
  font-size: 7.8pt; font-weight: 700; letter-spacing: .12em;
  text-transform: uppercase; color: #666; margin-bottom: 3mm;
}
.cover__inside li {
  display: flex; gap: 4mm; padding: 2mm 0;
  border-top: .3mm solid #cacafb; font-size: 9.6pt; color: #161616;
}
.cover__inside li span { color: #e1000f; font-weight: 700; width: 4mm; }
.cover__foot { margin-top: auto; font-size: 9pt; color: #3a3a3a; }
.cover__foot strong { display: block; font-size: 10.5pt; color: #161616; }
.cover__edition {
  display: inline-block; margin-top: 3mm; padding: 1.4mm 3.5mm;
  background: #000091; color: #fff; font-size: 8pt; font-weight: 700;
  letter-spacing: .09em; text-transform: uppercase;
}

/* --------------------------------------------------------------- headings */
.band {
  display: flex; align-items: baseline; gap: 4mm;
  margin: 0 0 6mm;
  padding-bottom: 2.5mm;
  border-bottom: .5mm solid #000091;
  page-break-after: avoid;
}
.band h2 { font-size: 15pt; color: #000091; }
.band__n {
  font-size: 9pt; font-weight: 700; color: #e1000f;
  letter-spacing: .1em;
}

.section { page-break-inside: auto; }
.section + .section { margin-top: 9mm; }

/* --------------------------------------------------------------------- QA */
.qa { margin-bottom: 6mm; }
/* Long answers may span two pages; a question never ends a page on its own. */
.qa__q { break-after: avoid; page-break-after: avoid; }
.qa p, .qa li { break-inside: avoid; page-break-inside: avoid; }
.qa__q {
  font-size: 10.4pt; font-weight: 700; color: #161616;
  margin-bottom: 2mm; line-height: 1.35;
}
.qa__lead {
  display: inline-block;
  padding: .8mm 2.4mm; margin-bottom: 2mm;
  background: #e3e3fd; color: #000091;
  font-weight: 700; font-size: 9.2pt;
}
.qa__lead--long { display: block; background: none; padding: 0; color: #161616; font-weight: 600; }
.qa__text { color: #3a3a3a; max-width: 165mm; }
.qa__text + .qa__text, .qa ul + .qa__text { margin-top: 2mm; }
.addr { margin-top: 2mm; }
.addr li { font-size: 8.8pt; color: #3a3a3a; margin-bottom: 1mm; }
.qa ul { margin-top: 1mm; }
.qa li {
  position: relative; padding-left: 5mm; margin-bottom: 1.4mm; color: #3a3a3a;
}
.qa li::before {
  content: ""; position: absolute; left: 0; top: 1.7mm;
  width: 1.6mm; height: 1.6mm; background: #e1000f;
}

/* ----------------------------------------------------------------- blocks */
.figures {
  display: grid; grid-template-columns: repeat(4, 1fr);
  gap: .4mm; background: #dddddd; border: .4mm solid #dddddd;
  margin-bottom: 4mm;
}
.fig { background: #fff; padding: 4mm 3.5mm; }
.fig__v { font-size: 19pt; font-weight: 700; color: #000091; line-height: 1; }
.fig__l { font-size: 8pt; color: #3a3a3a; margin-top: 1.5mm; line-height: 1.35; }

.chart { margin: 2mm 0 3mm; }
.bar { display: flex; align-items: center; gap: 3mm; margin-bottom: 1.6mm; }
.bar__y { width: 20mm; font-size: 8pt; color: #666; flex: none; }
.bar__t { flex: 1; height: 5mm; background: #f6f6f6; display: block; }
.bar__f { display: block; height: 5mm; background: #000091; }
.bar__n { width: 8mm; font-size: 8pt; font-weight: 700; color: #000091; text-align: right; flex: none; }

.note { font-size: 7.6pt; color: #666; margin-top: 2mm; }

.callout {
  padding: 5mm 5mm; background: #f5f5fe;
  border: .35mm solid #cacafb; border-left: 1.6mm solid #000091;
  page-break-inside: avoid;
}
.callout h3 { font-size: 11pt; color: #000091; margin-bottom: 2mm; }
.callout p { color: #3a3a3a; margin: 0; }

.toc { margin-bottom: 8mm; }
.toc li {
  display: flex; gap: 3mm; padding: 1.8mm 0;
  border-bottom: .3mm solid #eeeeee; font-size: 9.4pt;
}
.toc li span:first-child { color: #e1000f; font-weight: 700; width: 5mm; }

.sources {
  margin-top: 7mm; padding-top: 3mm;
  border-top: .3mm solid #dddddd;
  font-size: 7.6pt; color: #666;
}
sup { font-size: .7em; }
"""


def chart(rows):
    top = max(n for _, n in rows)
    out = ['<div class="chart">']
    for year, n in rows:
        out.append(
            f'<div class="bar"><span class="bar__y">{year}</span>'
            f'<span class="bar__t"><span class="bar__f" style="width:{n / top * 100:.1f}%"></span></span>'
            f'<span class="bar__n">{n}</span></div>')
    out.append("</div>")
    return "".join(out)


def build_cover(lang, logo_b64):
    d = text(lang)
    return (f'<!DOCTYPE html><html lang="{d["lang"]}"><head><meta charset="utf-8">'
            f"<style>{CSS}</style></head><body style='margin:0'>"
            f'<section class="cover">'
            f'<span class="cover__mark">'
            f'<img class="cover__logo" src="data:image/png;base64,{logo_b64}" alt=""></span>'
            f'<p class="cover__eyebrow"><span></span>{d["school"]}</p>'
            f'<h1>{d["title"]}</h1>'
            f'<p class="cover__sub">{d["sub"]}</p>'
            f'<div class="cover__rule"></div>'
            f'<div class="cover__inside"><p>{d["toc_title"]}</p><ul>'
            + "".join(f'<li><span>{x["n"]}</span>{x["t"]}</li>' for x in d["sections"])
            + '</ul></div>'
            f'<div class="cover__foot">'
            f'<strong>{d["site"]}</strong>{d["contact"]}'
            f'<br><span class="cover__edition">{d["edition"]}</span>'
            f'</div></section></body></html>')


def build_html(lang, logo_b64):
    d = text(lang)
    parts = [f'<!DOCTYPE html><html lang="{d["lang"]}"><head><meta charset="utf-8">',
             f"<title>{d['title']} — {d['school']}</title><style>{CSS}</style></head><body>"]

    # figures + contents
    figs = "".join(f'<div class="fig"><div class="fig__v">{v}</div>'
                   f'<div class="fig__l">{l}</div></div>' for v, l in d["figures"])
    toc = "".join(f'<li><span>{s["n"]}</span><span>{s["t"]}</span></li>' for s in d["sections"])
    parts.append(
        f'<div class="band"><h2>{d["figures_title"]}</h2></div>'
        f'<div class="figures">{figs}</div>'
        f'<p class="note">{d["figures_note"]}</p>'
        f'<h3 style="font-size:10.5pt;margin:7mm 0 2mm">{d["chart_title"]}</h3>'
        f'{chart(ENROLMENT)}'
        f'<p class="note">{d["chart_note"]}</p>'
        f'<div class="band" style="margin-top:10mm"><h2>{d["toc_title"]}</h2></div>'
        f'<ul class="toc">{toc}</ul>')

    # sections
    for s in d["sections"]:
        parts.append('<section class="section">')
        parts.append(f'<div class="band"><span class="band__n">{s["n"].zfill(2)}</span>'
                     f'<h2>{s["t"]}</h2></div>')
        for q, bullets, lead, *after in s["qa"]:
            parts.append('<div class="qa">')
            parts.append(f'<p class="qa__q">{q}</p>')
            for para in paras(lead):
                cls = "qa__text" if len(para) > 40 else "qa__lead"
                parts.append(f'<p class="{cls}">{para}</p>')
            if bullets:
                parts.append("<ul>" + "".join(f"<li>{b}</li>" for b in bullets) + "</ul>")
            for para in paras(after[0] if after else None):
                parts.append(f'<p class="qa__text">{para}</p>')
            parts.append("</div>")
        parts.append("</section>")

    parts.append(
        f'<div class="callout" style="margin-top:9mm">'
        f'<h3>{d["closing_title"]}</h3><p>{d["closing"]}</p>'
        f'<p style="margin-top:3mm"><em>{d["addresses_title"]}</em></p><ul class="addr">'
        + "".join(f"<li><strong>{n}</strong> — {a} ({w})</li>" for n, a, w in ADDRESSES)
        + '</ul></div>'
        f'<p class="sources">{d["sources"]}</p>')

    parts.append("</body></html>")
    return "".join(parts)


HEADER = """<div style="width:100%;font-size:7pt;font-family:Inter,sans-serif;color:#929292;
 padding:0 16mm;display:flex;justify-content:space-between;">
 <span>{school} — {title}</span><span>{edition}</span></div>"""

FOOTER = """<div style="width:100%;font-size:7pt;font-family:Inter,sans-serif;color:#929292;
 padding:0 16mm;display:flex;justify-content:space-between;align-items:center;">
 <span>{site}</span>
 <span style="font-weight:700;color:#000091;">
   <span class="pageNumber"></span>/<span class="totalPages"></span></span></div>"""


def render(lang, logo_b64):
    from playwright.sync_api import sync_playwright
    from pypdf import PdfWriter, PdfReader
    d = text(lang)
    # Ces noms doivent rester ceux de la constante FAQ de build.py.
    name = "faq-efan-2026-2027.pdf" if lang == "fr" else "faq-fasn-2026-2027-en.pdf"
    dest = os.path.join(OUT, name)

    tmp = Path(tempfile.mkdtemp(prefix="faq-"))
    cover_html, body_html = tmp / f"faq-cover-{lang}.html", tmp / f"faq-body-{lang}.html"
    cover_html.write_text(build_cover(lang, logo_b64), encoding="utf-8")
    body_html.write_text(build_html(lang, logo_b64), encoding="utf-8")
    cover_pdf, body_pdf = str(tmp / f"faq-cover-{lang}.pdf"), str(tmp / f"faq-body-{lang}.pdf")

    with sync_playwright() as pw:
        b = pw.chromium.launch()
        p = b.new_page()
        # cover: full bleed, no running header or footer
        p.goto(cover_html.as_uri(), wait_until="load")
        p.pdf(path=cover_pdf, format="A4", print_background=True,
              margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
        # body: running header and footer, page x of y
        p.goto(body_html.as_uri(), wait_until="load")
        p.pdf(path=body_pdf, format="A4", print_background=True,
              display_header_footer=True,
              header_template=HEADER.format(**d),
              footer_template=FOOTER.format(**d),
              margin={"top": "20mm", "bottom": "20mm", "left": "16mm", "right": "16mm"})
        b.close()

    w = PdfWriter()
    for f in (cover_pdf, body_pdf):
        for page in PdfReader(f).pages:
            w.add_page(page)
    w.add_metadata({"/Title": f"{d['title']} — {d['school']}",
                    "/Author": d["school"],
                    "/Subject": d["sub"],
                    "/Language": d["lang"]})
    with open(dest, "wb") as f:
        w.write(f)
    return dest


if __name__ == "__main__":
    logo = b64(os.path.join(SITE, "media", "site", "logo-efan.png"))
    for lang in ("fr", "en"):
        p = render(lang, logo)
        print(f"{lang}: {p}  ({os.path.getsize(p)/1024:.0f} KB)")
