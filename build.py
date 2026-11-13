#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EFAN / FASN — générateur du site bilingue
=========================================

Une seule source, deux langues, de vraies pages statiques.

    python3 build.py

Ce que vous modifiez
--------------------
_source/content/<page>.html   le contenu d'une page, en anglais (HTML simple)
_source/i18n/fr.json          la traduction de chaque phrase
_source/i18n/ui.json          les libellés d'interface (menus, boutons, pied de page)
_source/i18n/home.json        les textes de la page d'accueil
_source/structure.json        l'arborescence du site et les titres de pages

Le script réécrit ensuite index.html et les 36 pages françaises à la racine,
/en/ et les 36 pages anglaises, ainsi que les redirections des anciennes
adresses /fr/…. Les dossiers assets/, media/ et docs/ ne sont pas touchés.

Prérequis : Python 3.8+ et BeautifulSoup   (pip install beautifulsoup4 lxml)
"""

import os, re, json, html as H, sys

try:
    from bs4 import BeautifulSoup
except ImportError:
    sys.exit("Il manque BeautifulSoup :  pip install beautifulsoup4 lxml")

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "_source")
LANGS = ("fr", "en")
# Langue servie à la racine du site ; l'autre est publiée sous /<code>/.
DEFAULT = "fr"
# Avant le passage du français à la racine, il vivait sous /fr/ : ces
# anciennes adresses sont conservées sous forme de redirections.
LEGACY_PREFIX = "fr"


def sub(lang):
    """Sous-dossier d'une langue : "" pour la langue par défaut, "en/" sinon."""
    return "" if lang == DEFAULT else lang + "/"

PHONE = "(757) 230-7569"
TEL = "+17572307569"
MAIL = "efan.norfolk@gmail.com"
CREDIT_NAME = "Gaëtan SUILLEROT"
CREDIT_MAIL = "gaetan.slt@gmail.com"
FAQ = {"fr": "docs/FAQ-EFAN-2026-2027.pdf", "en": "docs/FAQ-FASN-2026-2027-EN.pdf"}
# La FAQ (PDF) s'ouvre dans un nouvel onglet : le visiteur garde le site ouvert.
NEW_TAB = 'target="_blank" rel="noopener"'


def new_tab_hint(lang):
    """Annonce aux lecteurs d'écran l'ouverture dans un nouvel onglet."""
    return f'<span class="sr-only">, {UI[lang]["new_tab"]}</span>'

# Pages retirées du site : leur ancienne adresse redirige vers la page qui
# reprend désormais leur contenu, pour ne pas casser les liens déjà envoyés.
REMOVED = {
    # Les bulletins se fournissent désormais en français (VBCPS les traduit).
    "21-high-school-translation-of-reports-ns2": "36-enrollment-in-the-american-schools",
}
# Conditions d'utilisation : une page du site (_source/content/terms-of-service.html).
TOS = "terms-of-service"

# Réglages d'affichage (contrastes, police dyslexie), mémorisés dans le
# navigateur. Ce script, placé dans <head>, les applique avant le premier
# affichage : la page ne « clignote » pas entre deux styles. Sans choix
# enregistré, on suit la préférence « contraste élevé » du système.
A11Y_BOOT = ("<script>(function(){try{var d=document.documentElement,"
             "s=JSON.parse(localStorage.getItem('efan-a11y')||'{}'),"
             "c=s.contrast||(window.matchMedia&&matchMedia('(prefers-contrast: more)').matches?'high':'');"
             "if(c==='high')d.setAttribute('data-contrast','high');"
             "if(s.font==='dyslexic')d.setAttribute('data-font','dyslexic');"
             "}catch(e){}})();</script>")


def a11y_control(lang):
    """Bouton « Accessibilité » du bandeau et son panneau de réglages.

    Masqué tant que le JavaScript ne l'a pas activé : sans script, il ne
    servirait à rien. Les réglages sont de simples boutons radio, utilisables
    au clavier et annoncés correctement par les lecteurs d'écran."""
    t = UI[lang]

    def option(group, value, label, hint=None, extra_cls=""):
        checked = " checked" if value == "standard" else ""
        hint_html = f'<span class="a11y-option__hint">{hint}</span>' if hint else ""
        return (f'<label class="a11y-option{extra_cls}">'
                f'<input type="radio" name="a11y-{group}" value="{value}"{checked}>'
                f'<span class="a11y-option__text"><span class="a11y-option__label">{label}</span>'
                f'{hint_html}</span></label>')

    return f"""<li class="a11y">
          <button type="button" class="util-link a11y__toggle" data-icon="a11y" aria-expanded="false" aria-controls="a11y-panel" hidden><span class="a11y__label">{t['a11y_button']}</span></button>
          <div class="a11y-panel" id="a11y-panel" role="group" aria-labelledby="a11y-title" hidden>
            <p class="a11y-panel__title" id="a11y-title">{t['a11y_title']}</p>
            <fieldset class="a11y-panel__group">
              <legend>{t['a11y_contrast']}</legend>
              {option("contrast", "standard", t['a11y_standard'])}
              {option("contrast", "high", t['a11y_contrast_high'], t['a11y_contrast_high_hint'])}
            </fieldset>
            <fieldset class="a11y-panel__group">
              <legend>{t['a11y_font']}</legend>
              {option("font", "standard", t['a11y_standard'])}
              {option("font", "dyslexic", t['a11y_font_dys'], t['a11y_font_dys_hint'], " a11y-option--dys")}
            </fieldset>
            <p class="a11y-panel__note">{t['a11y_note']}</p>
            <div class="a11y-panel__foot">
              <button type="button" class="btn btn--tertiary a11y-panel__reset">{t['a11y_reset']}</button>
              <button type="button" class="btn btn--secondary a11y-panel__close">{t['close']}</button>
            </div>
          </div>
        </li>"""


BLOCKS = ["p", "li", "h2", "h3", "h4", "h5", "h6", "td", "th",
          "caption", "figcaption", "blockquote", "footer"]


def load(name):
    with open(os.path.join(SRC, name), encoding="utf-8") as f:
        return json.load(f)


ST = load("structure.json")
UI = load(os.path.join("i18n", "ui.json"))
HOME_S = load(os.path.join("i18n", "home.json"))
FR_RAW = load(os.path.join("i18n", "fr.json"))

PAGES = ST["pages"]
SLUG_SET = set(PAGES)
MISSING = []


# --------------------------------------------------------------------------
# translation
# --------------------------------------------------------------------------
def norm(s):
    return re.sub(r"\s+", " ", s).strip()


FR = {norm(k): v for k, v in FR_RAW.items() if v}


def leaf_blocks(root):
    out = []
    for el in root.find_all(BLOCKS):
        if el.find(BLOCKS):
            continue
        if not el.get_text(strip=True):
            continue
        out.append(el)
    return out


def translate(html, slug):
    soup = BeautifulSoup(html, "lxml")
    body = soup.find("body") or soup
    for el in leaf_blocks(body):
        key = norm("".join(str(c) for c in el.contents).strip())
        tr = FR.get(key)
        if tr is None:
            if key:
                MISSING.append((slug, key))
            continue
        # html.parser : contrairement à lxml récent, il n'enveloppe pas un
        # texte nu dans un <p> (ce qui sortait le texte des <h2>, <li>…).
        nb = BeautifulSoup(tr, "html.parser")
        el.clear()
        for child in list(nb.contents):
            el.append(child)
    for img in body.find_all("img"):
        if img.get("alt"):
            tr = FR.get(norm(img["alt"]))
            if tr:
                img["alt"] = BeautifulSoup(tr, "lxml").get_text(" ", strip=True)
    return "".join(str(c) for c in body.contents)


# --------------------------------------------------------------------------
# paths
# --------------------------------------------------------------------------
def rel(path, asset_depth):
    if path.startswith(("http://", "https://", "mailto:", "tel:", "#")):
        return path
    return ("../" * asset_depth) + path.lstrip("/")


def page_href(slug, page_depth):
    if slug.startswith(("http", "/?")):
        return slug
    return ("../" * page_depth) + slug + "/"


def home_href(page_depth):
    return ("../" * page_depth) + "index.html" if page_depth else "index.html"


def other_url(lang, slug):
    other = "en" if lang == "fr" else "fr"
    if lang == DEFAULT:
        return sub(other) if slug is None else f"../{sub(other)}{slug}/"
    return "../" if slug is None else f"../../{slug}/"


def variant_for(media_path, want):
    """Use the lighter copy of an image when one was generated."""
    inner = media_path[len("/media/"):]
    stem, ext = os.path.splitext(inner)
    cand = f"media/_{want}/{stem}{ext}"
    return cand if os.path.exists(os.path.join(ROOT, cand)) else media_path.lstrip("/")


def localise(html, a_depth, p_depth):
    """Canonical links -> links relative to this page, in this language."""
    soup = BeautifulSoup(html, "lxml")
    body = soup.find("body") or soup

    for img in body.find_all("img"):
        src = img.get("src", "")
        if not src.startswith("/media/"):
            continue
        classes = set(img.get("class") or [])
        pc = set((img.parent.get("class") or []) if img.parent is not None else [])
        gp = img.parent.parent if img.parent is not None else None
        gc = set((gp.get("class") or []) if gp is not None else [])
        want = 480 if ("person__photo" in classes or "gallery__item" in pc
                       or "gallery__item" in gc) else 1400
        target = variant_for(src, want)
        img["src"] = rel(target, a_depth)
        if target != src.lstrip("/") and img.get("width") and img.get("height"):
            try:
                w, hgt = int(img["width"]), int(img["height"])
                img["height"] = str(round(hgt * want / w))
                img["width"] = str(want)
            except ValueError:
                del img["width"]
                del img["height"]

    for a in body.find_all("a", href=True):
        href = a["href"].strip()
        if href.startswith("/media/"):
            a["href"] = rel(href, a_depth)
            if href.lower().endswith(".pdf") and "is-pdf" not in (a.get("class") or []):
                a["class"] = (a.get("class") or []) + ["is-pdf"]
            continue
        if href.startswith(("http://", "https://")):
            a["rel"] = "noopener"
            if "is-external" not in (a.get("class") or []):
                a["class"] = (a.get("class") or []) + ["is-external"]
            continue
        if href.startswith(("mailto:", "tel:", "#")):
            continue
        m = re.match(r"^/([^/?#]+)/$", href)
        if m and m.group(1) in SLUG_SET:
            a["href"] = page_href(m.group(1), p_depth)
            continue
        if href == "/":
            a["href"] = home_href(p_depth)
    return "".join(str(c) for c in body.contents)


# --------------------------------------------------------------------------
# labels
# --------------------------------------------------------------------------
def L(d, lang):
    return d[lang] if isinstance(d, dict) else d


def siblings_of(sec):
    out = []
    group_slugs = {i["slug"] for g in sec["groups"] for i in g["items"]}
    if sec["feature"] and sec["feature"]["slug"] not in group_slugs:
        out.append((sec["feature"]["label"], sec["feature"]["slug"], None))
    for g in sec["groups"]:
        for i in g["items"]:
            out.append((i["label"], i["slug"], g["label"]))
    if sec["footer_link"]:
        out.append((sec["footer_link"]["label"], sec["footer_link"]["slug"], None))
    seen, uniq = set(), []
    for lbl, s, gl in out:
        if s in seen:
            continue
        seen.add(s)
        uniq.append((lbl, s, gl))
    return uniq


def page_info(slug):
    for sec in ST["nav"]:
        for lbl, s, gl in siblings_of(sec):
            if s == slug:
                return {"section": sec, "group": gl, "label": lbl, "siblings": siblings_of(sec)}
    for e in ST["flat"]:
        if e["slug"] == slug:
            return {"section": None, "group": None, "label": e["label"], "siblings": [],
                    "flat_label": e["label"]}
    for e in ST["extra"]:
        if e["slug"] == slug:
            return {"section": None, "group": None, "label": e["label"], "siblings": []}
    return {"section": None, "group": None, "label": slug, "siblings": []}


# --------------------------------------------------------------------------
# chrome
# --------------------------------------------------------------------------
def head(title, description, lang, a_depth, other, extra=""):
    t = UI[lang]
    other_lang = "fr" if lang == "en" else "en"
    return f"""<!DOCTYPE html>
<html lang="{t['html_lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — {t['site_title']}</title>
<meta name="description" content="{description}">
<meta name="theme-color" content="#000091">
<link rel="icon" href="{rel('assets/img/favicon-32.png', a_depth)}" sizes="32x32">
<link rel="apple-touch-icon" href="{rel('assets/img/favicon-180.png', a_depth)}">
<link rel="alternate" hreflang="{other_lang}" href="{other}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Public+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap">
<link rel="stylesheet" href="{rel('assets/css/efan.css', a_depth)}">
{A11Y_BOOT}
{extra}
<noscript><style>
  .nav {{ position: static !important; transform: none !important; visibility: visible !important;
         width: auto !important; border-left: 0 !important; }}
  .nav__list {{ display: block; }}
  .nav__btn, .burger, .nav__panel-head {{ display: none !important; }}
  .megamenu {{ position: static !important; box-shadow: none; }}
  .megamenu[hidden] {{ display: block !important; }}
</style></noscript>
</head>
<body>

<ul class="skiplinks">
  <li><a href="#content">{t['skip_content']}</a></li>
  <li><a href="#main-nav">{t['skip_nav']}</a></li>
  <li><a href="#footer">{t['skip_footer']}</a></li>
</ul>
"""


def header(lang, a_depth, p_depth, other, cur_sec=None, cur_slug=None):
    t = UI[lang]
    h = lambda s: page_href(s, p_depth)
    tabs = []
    for sec in ST["nav"]:
        is_cur = cur_sec == sec["id"]
        tabs.append(
            f'<li class="nav__item has-menu">'
            f'<button type="button" class="nav__btn{" is-current" if is_cur else ""}" '
            f'aria-expanded="false" aria-controls="menu-{sec["id"]}">{L(sec["label"], lang)}</button>'
            f'<div class="megamenu" id="menu-{sec["id"]}" hidden>'
            f'<div class="container megamenu__inner">'
            f'<div class="megamenu__intro">'
            f'<p class="megamenu__title">{L(sec["title"], lang)}</p>'
            f'<p class="megamenu__text">{L(sec["intro"], lang)}</p>'
            + (f'<p class="megamenu__text"><a class="link link--arrow" '
               f'href="{h(sec["feature"]["slug"])}">{L(sec["feature"]["label"], lang)}</a></p>'
               if sec["feature"] else "")
            + "</div>")
        cols = []
        for g in sec["groups"]:
            links = "".join(
                f'<li><a href="{h(i["slug"])}"'
                f'{" aria-current=&quot;page&quot;" if i["slug"] == cur_slug else ""}>'
                f'{L(i["label"], lang)}</a></li>' for i in g["items"])
            gl = L(g["label"], lang) if g["label"] else None
            group = f'<p class="megamenu__group">{gl}</p>' if gl else ""
            cols.append(f'<div class="megamenu__col">{group}'
                        f'<ul class="megamenu__links">{links}</ul></div>')
        tabs.append(f'<div class="megamenu__cols megamenu__cols--{min(len(sec["groups"]), 3)}">'
                    f'{"".join(cols)}</div>')
        if sec["footer_link"]:
            tabs.append(f'<div class="megamenu__foot"><a class="link link--arrow" '
                        f'href="{h(sec["footer_link"]["slug"])}">'
                        f'{L(sec["footer_link"]["label"], lang)}</a></div>')
        tabs.append("</div></div></li>")

    for e in ST["flat"]:
        cur = ' aria-current="page"' if e["slug"] == cur_slug else ""
        cls = " is-current" if e["slug"] == cur_slug else ""
        tabs.append(f'<li class="nav__item"><a class="nav__link{cls}" href="{h(e["slug"])}"{cur}>'
                    f'{L(e["label"], lang)}</a></li>')
    tabs.append(f'<li class="nav__item"><a class="nav__link" href="{rel(FAQ[lang], a_depth)}" {NEW_TAB}>'
                f'{t["faq"]} <span class="nav__meta">PDF</span>{new_tab_hint(lang)}</a></li>')

    # --- sélecteur de langue : ordre fixe EN puis FR -------------------------
    # La position ne dépend plus de la langue de la page. Pour chaque langue,
    # c'est son rôle qui change : repère si c'est celle de la page, lien sinon.
    LANG_LABELS = {"en": "EN", "fr": "FR"}

    def lang_item(code):
        if code == lang:
            return (f'<span class="lang-switch__current" aria-current="true" '
                    f'lang="{code}">{LANG_LABELS[code]}</span>')
        return (f'<a href="{other}" lang="{code}" hreflang="{code}" '
                f'title="{t["lang_other_title"]}">{LANG_LABELS[code]}</a>')

    lang_switch = lang_item("en") + lang_item("fr")
    # ------------------------------------------------------------------------

    return f"""
<header class="header" role="banner">

  <div class="header__utility">
    <div class="container header__utility-inner">
      <p class="header__tagline">{t['tagline']}</p>
      <ul class="header__utility-links">
        <li><a href="tel:{TEL}" class="util-link" data-icon="phone">{PHONE}</a></li>
        <li><a href="mailto:{MAIL}" class="util-link" data-icon="mail">{MAIL}</a></li>
        {a11y_control(lang)}
        <li class="lang-switch">
          {lang_switch}
        </li>
      </ul>
    </div>
  </div>

  <div class="header__main">
    <div class="container header__main-inner">
      <div class="brand-wrap">
        <a class="brand" href="{home_href(p_depth)}" aria-label="{t['home_aria']}">
          <img src="{rel('assets/img/logo-efan.png', a_depth)}" alt="{t['brand_alt']}" width="1148" height="376">
        </a>
        <p class="brand__desc">
          <strong>{t['brand_strong']}</strong>
          {t['brand_sub']}
        </p>
      </div>

      <div class="header__actions">
        <a class="btn btn--primary header__cta" href="{page_href('enrollment-french-american-school-of-norfolk', p_depth)}">
          {t['cta_enroll']}
        </a>
        <button type="button" class="burger" id="burger" aria-expanded="false" aria-controls="main-nav">
          <span class="burger__bars" aria-hidden="true"></span>
          <span class="burger__label">{t['menu']}</span>
        </button>
      </div>
    </div>
  </div>

  <nav class="nav" id="main-nav" aria-label="{t['nav_aria']}">
    <div class="container">
      <div class="nav__panel-head">
        <span class="nav__panel-title">{t['menu']}</span>
        <button type="button" class="nav__close" id="nav-close">{t['close']}</button>
      </div>
      <ul class="nav__list">
        {"".join(tabs)}
      </ul>
    </div>
  </nav>
</header>

<div class="nav-overlay" id="nav-overlay" hidden></div>
"""


def footer(lang, a_depth, p_depth, other):
    t = UI[lang]
    h = lambda s: page_href(s, p_depth)
    cols = []
    for sec in ST["nav"]:
        items = []
        for g in sec["groups"]:
            items += [(i["label"], i["slug"]) for i in g["items"]]
        if sec["feature"]:
            items.append((sec["feature"]["label"], sec["feature"]["slug"]))
        if sec["footer_link"]:
            items.append((sec["footer_link"]["label"], sec["footer_link"]["slug"]))
        seen, uniq = set(), []
        for lbl, s in items:
            if s in seen:
                continue
            seen.add(s)
            uniq.append((lbl, s))
        links = "".join(f'<li><a href="{h(s)}">{L(lbl, lang)}</a></li>' for lbl, s in uniq)
        cols.append(f'<div class="footer__col"><p class="footer__title">{L(sec["label"], lang)}</p>'
                    f'<ul>{links}</ul></div>')
    more = "".join(f'<li><a href="{h(e["slug"])}">{L(e["label"], lang)}</a></li>'
                   for e in ST["flat"] + ST["extra"])
    cols.append(f'<div class="footer__col"><p class="footer__title">{t["information"]}</p><ul>'
                + more
                + f'<li><a href="{rel(FAQ[lang], a_depth)}" {NEW_TAB}>{t["faq"]} '
                  f'<span class="footer__meta">PDF</span>{new_tab_hint(lang)}</a></li></ul></div>')

    return f"""
<footer class="footer" id="footer" role="contentinfo">
  <div class="container">

    <div class="footer__top">
      <div class="footer__brand">
        <img src="{rel('assets/img/logo-efan.png', a_depth)}" alt="{t['brand_alt']}" width="1148" height="376">
        <p class="footer__desc">{t['footer_desc']}</p>
        <ul class="footer__contact">
          <li><a href="tel:{TEL}">{PHONE}</a></li>
          <li><a href="mailto:{MAIL}">{MAIL}</a></li>
          <li>{t['hours_inline']}</li>
        </ul>
      </div>

      <nav class="footer__nav" aria-label="{t['sitemap_aria']}">
        {"".join(cols)}
      </nav>
    </div>

    <div class="footer__bottom">
      <div>
        <p class="footer__copy">{t['copyright']}</p>
        <p class="footer__credit">{t['credit']} {CREDIT_NAME} · <a href="mailto:{CREDIT_MAIL}">{CREDIT_MAIL}</a></p>
      </div>
      <ul class="footer__legal">
        <li><a href="{page_href(TOS, p_depth)}">{t['terms']}</a></li>
        <li><a href="{other}">{t['other_version']}</a></li>
        <li><a href="#content">{t['back_to_top']}</a></li>
      </ul>
    </div>

  </div>
</footer>

<script src="{rel('assets/js/efan.js', a_depth)}" defer></script>
</body>
</html>
"""


def contact_strip(lang, p_depth, grey=True):
    t = UI[lang]
    return f"""
<section class="section{' section--grey' if grey else ''}" aria-labelledby="contact-title">
  <div class="container">
    <h2 class="section__title" id="contact-title">{t['contacts']}</h2>
    <div class="contact">
      <div class="contact__item">
        <p class="contact__label">{t['phone_label']}</p>
        <p class="contact__value"><a href="tel:{TEL}">{PHONE}</a></p>
      </div>
      <div class="contact__item">
        <p class="contact__label">{t['email_label']}</p>
        <p class="contact__value"><a href="mailto:{MAIL}">{MAIL}</a></p>
      </div>
      <div class="contact__item">
        <p class="contact__label">{t['hours_label']}</p>
        <p class="contact__value">{t['hours_value']}</p>
      </div>
      <div class="contact__item">
        <p class="contact__label">{t['useful_label']}</p>
        <p class="contact__value"><a class="link link--arrow" href="{page_href('38-useful-contacts', p_depth)}">{t['full_directory']}</a></p>
      </div>
    </div>
  </div>
</section>
"""


def breadcrumb(slug, lang, p_depth):
    t = UI[lang]
    info = page_info(slug)
    crumbs = [f'<a href="{home_href(p_depth)}">{t["home"]}</a>']
    if info["section"]:
        crumbs.append(f'<span>{L(info["section"]["label"], lang)}</span>')
    if info["group"]:
        crumbs.append(f'<span>{L(info["group"], lang)}</span>')
    crumbs.append(f'<span aria-current="page">{L(ST["titles"][slug], lang)}</span>')
    return (f'<nav class="breadcrumb" aria-label="{t["breadcrumb_aria"]}"><div class="container">'
            f'<ol>{"".join(f"<li>{c}</li>" for c in crumbs)}</ol></div></nav>')


def sidenav(slug, lang, p_depth):
    t = UI[lang]
    info = page_info(slug)
    sibs = info["siblings"]
    if len(sibs) < 2 or not info["section"]:
        return ""
    label = L(info["section"]["label"], lang)
    out = [f'<nav class="sidenav" aria-label="{t["section_aria"] % H.escape(label)}">',
           f'<p class="sidenav__title">{H.escape(label)}</p>', "<ul>"]
    last = "__start__"
    for lbl, s, gl in sibs:
        if gl != last:
            if gl:
                out.append(f'<li class="sidenav__group">{H.escape(L(gl, lang))}</li>')
            last = gl
        cur = ' class="is-current" aria-current="page"' if s == slug else ""
        out.append(f'<li><a href="{page_href(s, p_depth)}"{cur}>{H.escape(L(lbl, lang))}</a></li>')
    out.append("</ul></nav>")
    return "".join(out)


def pager(slug, lang, p_depth):
    t = UI[lang]
    info = page_info(slug)
    sibs = [(l, s) for l, s, g in info["siblings"] if not s.startswith(("/", "http"))]
    slugs = [s for _, s in sibs]
    if len(sibs) < 2 or slug not in slugs:
        return ""
    i = slugs.index(slug)
    prev_ = sibs[i - 1] if i > 0 else None
    next_ = sibs[i + 1] if i < len(sibs) - 1 else None
    if not prev_ and not next_:
        return ""
    parts = [f'<nav class="pager" aria-label="{t["pager_aria"]}"><div class="container">'
             f'<div class="pager__inner">']
    if prev_:
        parts.append(f'<a class="pager__link pager__link--prev" href="{page_href(prev_[1], p_depth)}">'
                     f'<span class="pager__dir">{t["previous"]}</span>'
                     f'<span class="pager__label">{H.escape(L(prev_[0], lang))}</span></a>')
    else:
        parts.append("<span></span>")
    if next_:
        parts.append(f'<a class="pager__link pager__link--next" href="{page_href(next_[1], p_depth)}">'
                     f'<span class="pager__dir">{t["next"]}</span>'
                     f'<span class="pager__label">{H.escape(L(next_[0], lang))}</span></a>')
    parts.append("</div></div></nav>")
    return "".join(parts)


def eyebrow_of(slug, lang):
    info = page_info(slug)
    en = ST["eyebrows"].get(slug)
    if not en:
        if info["group"]:
            return L(info["group"], lang)
        if info["section"]:
            return L(info["section"]["label"], lang)
        return ""
    return ST["eyebrows_fr"].get(en, en) if lang == "fr" else en


# --------------------------------------------------------------------------
# pages
# --------------------------------------------------------------------------
def build_page(slug, lang):
    t = UI[lang]
    a_depth = 1 + (0 if lang == DEFAULT else 1)
    p_depth = 1

    with open(os.path.join(SRC, "content", slug + ".html"), encoding="utf-8") as f:
        body = f.read()
    if lang == "fr":
        body = translate(body, slug)
    body = localise(body, a_depth, p_depth)

    info = page_info(slug)
    title = L(ST["titles"][slug], lang)
    desc = L(ST["blurbs"].get(slug, {"en": "", "fr": ""}), lang) or H.unescape(title)
    eyebrow = eyebrow_of(slug, lang)
    side = sidenav(slug, lang, p_depth)
    other = other_url(lang, slug)
    empty = f'<div class="notice"><p>{t["empty_page"]}</p></div>'

    out = [
        head(H.unescape(title), H.escape(desc, quote=True), lang, a_depth, other),
        header(lang, a_depth, p_depth, other,
               info["section"]["id"] if info["section"] else None, slug),
        '<main id="content" role="main">',
        breadcrumb(slug, lang, p_depth),
        '<div class="page-head"><div class="container">',
        (f'<p class="eyebrow">{H.escape(eyebrow)}</p>' if eyebrow else ""),
        f"<h1>{title}</h1>",
        "</div></div>",
        f'<div class="page-body{" page-body--with-side" if side else ""}">'
        f'<div class="container page-body__inner">',
        side,
        f'<article class="prose">{body.strip() or empty}</article>',
        "</div></div>",
        pager(slug, lang, p_depth),
        contact_strip(lang, p_depth),
        "</main>",
        footer(lang, a_depth, p_depth, other),
    ]
    d = os.path.join(ROOT, sub(lang), slug)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(x for x in out if x))


HOME_EXTRA = """<meta property="og:type" content="website">
<meta property="og:locale" content="{og_locale}">
<meta property="og:locale:alternate" content="{og_alt}">
<meta property="og:site_name" content="{og_site}">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{og_desc}">
<meta property="og:image" content="assets/img/classroom-1280.jpg">
<meta name="twitter:card" content="summary_large_image">"""

HOME_JSONLD = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "School",
  "name": "French American School of Norfolk",
  "alternateName": ["\\u00c9cole Franco-Am\\u00e9ricaine de Norfolk", "FASN", "EFAN"],
  "description": "The French American School of Norfolk teaches the French Ministry of National Education curriculum, Kindergarten through 12th grade, in partnership with Norfolk Public Schools and Virginia Beach City Public Schools.",
  "telephone": "+1-757-230-7569",
  "email": "efan.norfolk@gmail.com",
  "logo": "assets/img/logo-efan.png",
  "image": "assets/img/classroom-1280.jpg",
  "areaServed": ["Norfolk, Virginia", "Virginia Beach, Virginia"],
  "openingHours": "Mo-Fr 09:00-17:00"
}
</script>"""


def build_home(lang):
    t = UI[lang]
    k = HOME_S[lang]
    a_depth, p_depth = (0 if lang == DEFAULT else 1), 0
    A = lambda p: rel(p, a_depth)
    h = lambda s: page_href(s, p_depth)
    faq = A(FAQ[lang])
    other = other_url(lang, None)

    main = f"""
<main id="content" role="main">

  <section class="hero">
    <div class="container hero__inner">
      <div class="hero__body">
        <p class="eyebrow">{k['eyebrow']}</p>
        <h1>{k['h1']}</h1>
        <p class="hero__lead">{k['lead']}</p>
        <p class="hero__sub">{k['sub']}</p>
        <div class="hero__actions">
          <a class="btn btn--primary" href="{h('enrollment-french-american-school-of-norfolk')}">{k['cta1']}</a>
          <a class="btn btn--secondary" href="{h('a-propos-2-projet-detablissement')}">{k['cta2']}</a>
        </div>
      </div>
      <figure class="hero__figure">
        <img src="{A('assets/img/classroom-980.jpg')}"
          srcset="{A('assets/img/classroom-480.jpg')} 480w, {A('assets/img/classroom-980.jpg')} 980w, {A('assets/img/classroom-1280.jpg')} 1280w"
          sizes="(max-width: 62rem) 100vw, 44vw"
          alt="{k['hero_alt']}" width="980" height="920" loading="eager">
      </figure>
    </div>
  </section>

  <section class="section section--tight" aria-labelledby="enrollment-title">
    <div class="container">
      <div class="callout">
        <p class="callout__tag">{k['enr_tag']}</p>
        <h2 class="callout__title" id="enrollment-title">{k['enr_title']}</h2>
        <p>{k['enr_p1']}</p>
        <p>{k['enr_p2']}</p>
        <p class="callout__action">
          <a class="btn btn--primary" href="{h('enrollment-french-american-school-of-norfolk')}">{k['enr_btn1']}</a>
          <a class="btn btn--tertiary" href="{h('tuition-and-payment-terms')}">{k['enr_btn2']}</a>
        </p>
      </div>
    </div>
  </section>

  <section class="section section--grey" aria-labelledby="figures-title">
    <div class="container">
      <h2 class="section__title" id="figures-title">{k['fig_title']}</h2>
      <p class="section__intro">{k['fig_intro']}</p>
      <ul class="figures">
        <li class="figure"><p class="figure__value">71</p><p class="figure__label">{k['fig1']}</p></li>
        <li class="figure"><p class="figure__value">&times;7</p><p class="figure__label">{k['fig2']}</p></li>
        <li class="figure"><p class="figure__value">17<span class="figure__unit">%</span></p><p class="figure__label">{k['fig3']}</p></li>
        <li class="figure"><p class="figure__value">7<span class="figure__unit">%</span></p><p class="figure__label">{k['fig4']}</p></li>
      </ul>
      <p class="source">{k['source']} <a href="{faq}" {NEW_TAB}>{k['source_link']}{new_tab_hint(lang)}</a></p>
    </div>
  </section>

  <section class="section" aria-labelledby="news-title">
    <div class="container">
      <h2 class="section__title" id="news-title">{k['news_title']}</h2>
      <p class="section__intro">{k['news_intro']}</p>
      <div class="cards">
        <article class="card card--highlight">
          <p class="card__tag card__tag--red">{k['n1_tag']}</p>
          <h3 class="card__title">{k['n1_title']}</h3>
          <p>{k['n1_body']}</p>
          <ul class="results">
            <li><span class="results__head">{k['n1_r1h']}</span><span class="results__detail">{k['n1_r1d']}</span></li>
            <li><span class="results__head">{k['n1_r2h']}</span><span class="results__detail">{k['n1_r2d']}</span></li>
          </ul>
          <p class="card__kicker">{k['n1_kicker']}</p>
        </article>
        <article class="card">
          <p class="card__tag">{k['n2_tag']}</p>
          <h3 class="card__title">{k['n2_title']}</h3>
          <p>{k['n2_body']}</p>
          <p class="card__link"><a class="link link--external" href="https://vafest.org/norfolk-nato-festival/model-nato-challenge/" rel="noopener">{k['n2_link']}</a></p>
        </article>
        <article class="card">
          <p class="card__tag">{k['n3_tag']}</p>
          <h3 class="card__title">{k['n3_title']}</h3>
          <p>{k['n3_body']}</p>
          <p class="card__link"><a class="link link--external" href="https://www.cheminsdememoire.gouv.fr/fr/operation-heritiers-de-memoire" rel="noopener">{k['n3_link']}</a></p>
        </article>
      </div>
    </div>
  </section>

  <section class="section section--grey" aria-labelledby="about-title">
    <div class="container">
      <div class="split">
        <div class="split__body">
          <p class="eyebrow">{k['ab_eyebrow']}</p>
          <h2 class="section__title" id="about-title">{k['ab_title']}</h2>
          <p class="lead">{k['ab_lead']}</p>
          <p>{k['ab_p']}</p>
          <p class="host-schools__label">{k['ab_hosts']}</p>
          <ul class="host-schools">
            <li>Crossroads Elementary and Middle School</li>
            <li>John B. Dey Elementary School</li>
            <li>Great Neck Middle School</li>
            <li>Frank W. Cox High School</li>
          </ul>
          <p><a class="link link--arrow" href="{h('school-life-ns3')}">{k['ab_link']}</a></p>
        </div>
        <figure class="split__figure">
          <img src="{A('assets/img/school-bus.jpg')}" alt="{k['ab_alt']}" width="480" height="480" loading="lazy">
          <figcaption>{k['ab_cap']}</figcaption>
        </figure>
      </div>
    </div>
  </section>

  <section class="section" aria-labelledby="quick-title">
    <div class="container">
      <h2 class="section__title" id="quick-title">{k['q_title']}</h2>
      <p class="section__intro">{k['q_intro']}</p>
      <ul class="tiles">
        <li class="tile"><h3 class="tile__title"><a href="{h('9-elementary-school-operating-mode-ns2')}">{k['q1']}</a></h3><p class="tile__text">{k['q1d']}</p></li>
        <li class="tile"><h3 class="tile__title"><a href="{h('13-middle-school-schedule-ns2')}">{k['q2']}</a></h3><p class="tile__text">{k['q2d']}</p></li>
        <li class="tile"><h3 class="tile__title"><a href="{h('19-high-school-baccalaureat-ns2')}">{k['q3']}</a></h3><p class="tile__text">{k['q3d']}</p></li>
        <li class="tile"><h3 class="tile__title"><a href="{h('24-school-district-and-transportation')}">{k['q4']}</a></h3><p class="tile__text">{k['q4d']}</p></li>
        <li class="tile"><h3 class="tile__title"><a href="{h('tuition-and-payment-terms')}">{k['q5']}</a></h3><p class="tile__text">{k['q5d']}</p></li>
        <li class="tile"><h3 class="tile__title"><a href="{h('testimonies')}">{k['q6']}</a></h3><p class="tile__text">{k['q6d']}</p></li>
        <li class="tile"><h3 class="tile__title"><a href="{h('volunteering-ns1-a')}">{k['q7']}</a></h3><p class="tile__text">{k['q7d']}</p></li>
        <li class="tile"><h3 class="tile__title"><a href="{faq}" {NEW_TAB}>{k['q8']} <span class="tile__meta">PDF</span>{new_tab_hint(lang)}</a></h3><p class="tile__text">{k['q8d']}</p></li>
      </ul>
    </div>
  </section>

  <section class="section section--grey" aria-labelledby="partners-title">
    <div class="container">
      <h2 class="section__title" id="partners-title">{k['p_title']}</h2>
      <p class="section__intro">{k['p_intro']}</p>
      <ul class="partners">
        <li class="partner"><img src="{A('assets/img/partners/ministere-education-nationale.png')}" alt="Ministère de l’Éducation nationale et de la Jeunesse" loading="lazy"></li>
        <li class="partner"><img src="{A('assets/img/partners/ministere-des-armees.png')}" alt="Ministère des Armées" loading="lazy"></li>
        <li class="partner"><img src="{A('assets/img/partners/mlfmonde.png')}" alt="Réseau mlfmonde — MLF, OSUI, MLCI, MLF America" loading="lazy"></li>
        <li class="partner"><img src="{A('assets/img/partners/norfolk-public-schools.png')}" alt="Norfolk Public Schools" loading="lazy"></li>
        <li class="partner"><img src="{A('assets/img/partners/virginia-beach-city-public-schools.png')}" alt="Virginia Beach City Public Schools" loading="lazy"></li>
        <li class="partner"><img src="{A('assets/img/partners/alliance-francaise-hampton-roads.png')}" alt="Alliance Française Hampton Roads" loading="lazy"></li>
      </ul>
    </div>
  </section>

{contact_strip(lang, p_depth, grey=False)}

  <section class="section section--tight" aria-labelledby="notice-title">
    <div class="container">
      <div class="notice">
        <h2 class="notice__title" id="notice-title">{k['notice_title']}</h2>
        <p>{k['notice_body']}</p>
      </div>
    </div>
  </section>

</main>
"""
    out = [
        head("Home" if lang == "en" else "Accueil", H.escape(t["home_meta"], quote=True),
             lang, a_depth, other, HOME_EXTRA.format(**k)),
        header(lang, a_depth, p_depth, other, None, None),
        main,
        HOME_JSONLD,
        footer(lang, a_depth, p_depth, other),
    ]
    d = os.path.join(ROOT, sub(lang))
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(out))


REDIRECT = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Page déplacée</title>
<meta name="robots" content="noindex">
<link rel="canonical" href="{to}">
<meta http-equiv="refresh" content="0; url={to}">
<script>location.replace("{to}" + location.hash);</script>
</head>
<body>
<p>Cette page a changé d’adresse : <a href="{to}">continuer</a>.</p>
</body>
</html>
"""


def write_redirect(d, to):
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8", newline="\n") as f:
        f.write(REDIRECT.format(to=to))


def build_redirects():
    """Anciennes adresses /fr/… → nouvelles adresses à la racine, et pages retirées."""
    n = 0
    if LEGACY_PREFIX == DEFAULT:
        for slug in [None] + list(PAGES):
            to = "../" if slug is None else f"../../{slug}/"
            write_redirect(os.path.join(ROOT, LEGACY_PREFIX, *([slug] if slug else [])), to)
            n += 1
    for old, new in REMOVED.items():
        for lang in LANGS:
            write_redirect(os.path.join(ROOT, sub(lang), old), f"../{new}/")
        if LEGACY_PREFIX == DEFAULT:
            write_redirect(os.path.join(ROOT, LEGACY_PREFIX, old), f"../../{new}/")
        n += 1
    return n


def main():
    for lang in LANGS:
        build_home(lang)
        for slug in PAGES:
            build_page(slug, lang)
        print(f"  {lang} : 1 + {len(PAGES)} pages")
    n = build_redirects()
    if n:
        print(f"  /{LEGACY_PREFIX}/ : {n} redirections vers la racine")

    urls = []
    for lang in LANGS:
        p = "/" + sub(lang)
        urls += [p] + [f"{p}{s}/" for s in PAGES]
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8", newline="\n") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for u in urls:
            f.write(f"  <url><loc>{u}</loc></url>\n")
        f.write("</urlset>\n")
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write("User-agent: *\nAllow: /\nSitemap: /sitemap.xml\n")

    print(f"-- {len(urls)} pages générées")
    if MISSING:
        uniq = sorted({m for _, m in MISSING})
        print(f"!! {len(uniq)} phrases sans traduction française "
              f"(ajoutez-les dans _source/i18n/fr.json) :")
        for m in uniq[:15]:
            print("   ", m[:100])


if __name__ == "__main__":
    main()
