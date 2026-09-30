"""Shared page chrome: <head>, header + menus, contact section, footer."""
import html
import re

# Contact forms post here (FormSubmit.co). The first message ever sent triggers a one-time
# "Activate Form" email to this inbox; nothing is delivered until she clicks it.
FORM_ENDPOINT = "https://formsubmit.co/ajax/stephanie@plumlines.net"

SITE_DESC = ("Stephanie Watson is an author and illustrator specializing in children's books. "
             "She offers author and artist visits to schools and libraries in the Twin Cities, "
             "greater Minnesota, and beyond.")

# (label, href, section-key, children)
NAV = [
    ("Home", "index.html", "home", []),
    ("Children’s Books", "books.html", "books", [
        ("Pencilvania", "pencilvania.html"),
        ("Best Friends in the Universe", "best-friends-in-the-universe.html"),
        ("Behold! A Baby", "behold-a-baby.html"),
        ("The Wee Hours", "the-wee-hours.html"),
        ("Elvis &amp; Olive", "elvis-olive.html"),
        ("Elvis &amp; Olive: Super Detectives", "elvis-olive-super-detectives.html"),
    ]),
    ("Teaching &amp; Speaking", "teaching.html", "teaching", [
        ("For Kids", "for-kids.html"),
        ("For Adults", "for-adults.html"),
    ]),
    ("About", "about.html", "about", [
        ("How to Become an Author", "how-to-become-an-author.html"),
    ]),
    ("Newsletter", "https://thepennycarnival.substack.com/subscribe", "newsletter", []),
    ("Videos", "videos.html", "videos", []),
    ("Contact", "contact.html", "contact", []),
]

CARET = ('<svg class="caret" viewBox="0 0 10 10" aria-hidden="true"><path d="M1 3l4 4 4-4" '
         'fill="none" stroke="currentColor" stroke-width="1.6"/></svg>')
ARROW = ('<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M2 8h11M9 4l4 4-4 4" fill="none" '
         'stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>')
BACK = ('<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M14 8H3M7 4L3 8l4 4" fill="none" '
        'stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>')
EXT = ('<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M9 3h4v4M13 3L7 9M11 10v3H3V5h3" fill="none" '
       'stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>')
STAR = ('<svg viewBox="0 0 20 20" aria-hidden="true"><path fill="currentColor" d="M10 1.8l2.5 5.2 5.7.8-4.1 '
        '4 1 5.7L10 14.8l-5.1 2.7 1-5.7-4.1-4 5.7-.8z"/></svg>')


def ext(href):
    """Attributes for a link: external ones open in a new tab."""
    return ' target="_blank" rel="noopener"' if href.startswith("http") else ""


def head(title, desc, og_image):
    full = "Stephanie Watson | Children's Book Author and Illustrator | Author Visits" if title is None \
        else f"{title} | Stephanie Watson"
    t, d = html.escape(full), html.escape(desc)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t}</title>
<meta name="description" content="{d}">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:image" content="{og_image}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#fbf7f0">
<meta name="robots" content="noindex, nofollow">
<link rel="icon" href="img/cropped-IMG_5515-scaled-1-32x32.jpg" sizes="32x32">
<link rel="apple-touch-icon" href="img/cropped-IMG_5515-scaled-1-180x180.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,400;0,700;0,900;1,400;1,700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
<script>document.documentElement.classList.add('js')</script>
<a class="skip" href="#main">Skip to content</a>
"""


def header(section):
    items = []
    for label, href, key, kids in NAV:
        cur = ' aria-current="page"' if key == section else ""
        if kids:
            sub = "".join(f'<li><a href="{h}">{l}</a></li>' for l, h in kids)
            items.append(f'<li><a href="{href}"{cur}>{label} {CARET}</a><ul class="sub">{sub}</ul></li>')
        else:
            items.append(f'<li><a href="{href}"{cur}{ext(href)}>{label}</a></li>')
    mitems = []
    for label, href, key, kids in NAV:
        sub = ("<ul class=\"msub\">" + "".join(f'<li><a href="{h}">{l}</a></li>' for l, h in kids) + "</ul>") if kids else ""
        mitems.append(f'<li><a href="{href}"{ext(href)}>{label}</a>{sub}</li>')
    return f"""<header class="site-header" id="top">
  <div class="wrap header-in">
    <a class="logo" href="index.html" aria-label="Stephanie Watson — home">
      <img src="img/Wordmark_page-header_Aug2026_500px.jpg" width="500" height="234" alt="STEPHANIE WATSON">
    </a>
    <nav class="nav" aria-label="Main"><ul>{"".join(items)}</ul></nav>
    <button class="burger" aria-label="Open menu" aria-expanded="false" aria-controls="mnav"><span></span><span></span><span></span></button>
  </div>
</header>
<div class="mnav" id="mnav" aria-label="Mobile menu"><ul>{"".join(mitems)}</ul></div>
"""


_form_n = [0]


def contact_form():
    _form_n[0] += 1
    n = _form_n[0]
    return f"""<form class="js-contact" action="{FORM_ENDPOINT}" method="post" novalidate>
        <input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
        <div class="field">
          <span class="lbl">Your name <span class="req">*</span></span>
          <div class="row">
            <div><input id="f{n}-first" name="first" autocomplete="given-name" required aria-label="First name"><small>First</small></div>
            <div><input id="f{n}-last" name="last" autocomplete="family-name" required aria-label="Last name"><small>Last</small></div>
          </div>
        </div>
        <div class="field">
          <label for="f{n}-email">Your email <span class="req">*</span></label>
          <input id="f{n}-email" name="email" type="email" autocomplete="email" required>
        </div>
        <div class="field">
          <label for="f{n}-msg">What's on your mind? <span class="req">*</span></label>
          <textarea id="f{n}-msg" name="message" required></textarea>
        </div>
        <button class="btn btn-fill" type="submit">Send</button>
        <p class="form-note" role="status" aria-live="polite"></p>
      </form>"""


def contact_section(lede="", heading="Contact Stephanie"):
    """The dark contact band that ends most pages. `lede` is that page's own intro line."""
    return f"""<section class="sec contact" id="contact">
    <div class="wrap contact-grid">
      <div class="rv">
        <h2>{heading}</h2>
        <p class="lede">{lede}</p>
      </div>
      <div class="rv">{contact_form()}</div>
    </div>
  </section>"""


def footer(ig_svg):
    return f"""<footer>
  <div class="wrap foot">
    <div class="foot-right">
      <span>© 2026 by Stephanie Watson</span>
      <a class="ig" href="https://www.instagram.com/thepennycarnival/" target="_blank" rel="noopener" aria-label="Instagram">{ig_svg}</a>
    </div>
  </div>
</footer>
<a class="to-top" href="#top" aria-label="Back to top"><svg viewBox="0 0 18 18"><path d="M9 15V3M4 8l5-5 5 5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
<div class="lightbox" role="dialog" aria-modal="true" aria-label="Image viewer">
  <button class="lb-btn lb-close" aria-label="Close"><svg viewBox="0 0 20 20"><path d="M4 4l12 12M16 4L4 16" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg></button>
  <button class="lb-btn lb-prev" aria-label="Previous"><svg viewBox="0 0 20 20"><path d="M12 4l-6 6 6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
  <figure><img alt=""><figcaption></figcaption></figure>
  <button class="lb-btn lb-next" aria-label="Next"><svg viewBox="0 0 20 20"><path d="M8 4l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
</div>
<script src="assets/site.js"></script>
</body>
</html>
"""


def crumb(label, href):
    return f'<a class="crumb" href="{href}">{BACK} {label}</a>'


def page_hero(h1, lede="", crumb_html="", center=False, kicker=""):
    lede_html = f'<p class="lede">{lede}</p>' if lede else ""
    kicker_html = f'<span class="eyebrow">{kicker}</span>' if kicker else ""
    cls = "page-hero wrap center" if center else "page-hero wrap"
    return f'<section class="{cls}"><div class="rv">{crumb_html}{kicker_html}<h1>{h1}</h1>{lede_html}</div></section>'


def video(yt_id, title, heading="", text=""):
    h = f"<h3>{heading}</h3>" if heading else ""
    p = f"<p>{text}</p>" if text else ""
    t = html.escape(re.sub(r"<[^>]+>", "", title), quote=True)
    return f"""<div class="video rv">{h}{p}<div class="frame">
      <iframe src="https://www.youtube-nocookie.com/embed/{yt_id}?rel=0&amp;playsinline=1" title="{t}" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    </div></div>"""
