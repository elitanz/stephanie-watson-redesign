"""Build every page of the Stephanie Watson redesign mockup.

Run:  python3 build/build.py
Writes the .html files into the site folder, then checks that every local link,
image and file actually exists and that no link points back to the live site.
"""
import os
import re
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import books  # noqa: E402
import other  # noqa: E402
import teaching  # noqa: E402
from chrome import head, header, footer, contact_form, SITE_DESC  # noqa: E402

PAGES_JSON = os.path.join(SITE, "_crawl", "pages.json")
HOME_MAIN = os.path.join(SITE, "_crawl", "home_main.html")
OG = "https://www.stephanie-watson.com/wp-content/uploads/2020/09/Pencilvania_LowRes_Square.jpeg"

# Old live-site paths -> new local pages
ROUTES = {
    "": "index.html",
    "books": "index.html#books",  # the Books landing page was retired (Sept 29); the home page lists them
    "books/pencilvania": "pencilvania.html",
    "books/best-friends-in-the-universe": "best-friends-in-the-universe.html",
    "books/behold-a-baby": "behold-a-baby.html",
    "books/the-wee-hours": "the-wee-hours.html",
    "books/elvis-olive": "elvis-olive.html",
    "books/elvis-olive-super-detectives": "elvis-olive-super-detectives.html",
    "books/elvis-olive/chapter-one-elvis-olive": "elvis-olive-chapter-one.html",
    "books/elvis-olive/elvis-olive-discussion-guide": "elvis-olive-discussion-guide.html",
    "teaching": "teaching.html",
    "for-kids": "for-kids.html",
    "for-adults": "for-adults.html",
    "teaching/kids": "for-kids.html",
    "teaching/adults": "for-adults.html",
    # the old "Author & Illustrator Visits" pages now live inside Teaching
    "author-visits": "teaching.html",
    "author-visits/school-visits": "for-kids.html",
    "school-visits": "for-kids.html",
    "author-visits/library-storytimes": "for-kids.html",
    "author-visits/other-presentations": "for-adults.html",
    "author-visits/testimonials": "teaching.html",
    "school-visits/testimonials": "teaching.html",
    "about": "about.html",
    "contact": "contact.html",
    "contact/how-to-become-an-author": "contact.html",  # page deleted Sept 30; she wants it to land on Contact
    "videos": "videos.html",
    "portfolio": "portfolio.html",
}


def local_href(m):
    url = m.group(2)
    mm = re.match(r"(?:https?:)?//(?:www\.)?stephanie-watson\.com(?:/home)?/?([^#?\"]*)(#[^\"]*)?$", url) \
        or re.match(r"/()?(portfolio/?)(#[^\"]*)?$", url)
    if not mm:
        return m.group(0)
    if url.startswith("/portfolio"):
        path, frag = "portfolio", (mm.group(3) or "")
    else:
        path, frag = mm.group(1).strip("/"), (mm.group(2) or "")
    if path.startswith("wp-content/uploads/"):
        return f'{m.group(1)}img/{os.path.basename(path)}"'
    if path not in ROUTES:
        raise SystemExit(f"Unmapped internal link: {url}")
    target = ROUTES[path]
    return f'{m.group(1)}{target if "#" in target else target + frag}"'


def rewrite_links(html):
    return re.sub(r'(href=")([^"]+)"', local_href, html)


def home():
    main = open(HOME_MAIN, encoding="utf-8").read()
    main = rewrite_links(main)
    # the homepage's own contact form is swapped for the shared, working one
    main, n = re.subn(r'<form class="rv" id="contact-form".*?</form>', lambda _: f'<div class="rv">{contact_form()}</div>', main, flags=re.S)
    assert n == 1, "homepage contact form not found"
    return main


def ig_icon():
    svg = urllib.request.urlopen("https://cdn.jsdelivr.net/npm/simple-icons@latest/icons/instagram.svg", timeout=20).read().decode()
    svg = re.sub(r"<title>.*?</title>", "", svg).replace('role="img" ', 'aria-hidden="true" ')
    assert svg.startswith("<svg") and "<path" in svg
    return svg


# Retired pages that were plain .html files in this preview -> where they forward now
OLD_FILES = {
    "how-to-become-an-author.html": "contact.html",  # deleted Sept 30
}

SW = " | Stephanie Watson"


# filename -> (full <title>, description, section, body-builder)
# Titles and descriptions are Stephanie's, from her Sept 30 table. Use them exactly; don't reword.
def page_table():
    pj = PAGES_JSON
    return {
        "index.html": ("Stephanie Watson | Children's Book Author and Illustrator | Teaching and Speaking", SITE_DESC, "home", home),
        "pencilvania.html": ("Pencilvania" + SW, "Pencilvania, a middle-grade novel by Stephanie Watson, illustrated by Sofia Moore (Sourcebooks).", "books", books.pencilvania),
        "best-friends-in-the-universe.html": ("Best Friends in the Universe" + SW, "Best Friends in the Universe by Stephanie Watson, illustrated by LeUyen Pham (Scholastic/Orchard Books).", "books", books.best_friends),
        "behold-a-baby.html": ("Behold! A Baby" + SW, "Behold! A Baby by Stephanie Watson, illustrated by Joy Ang (Bloomsbury). 2016 Minnesota Book Award finalist.", "books", books.behold),
        "the-wee-hours.html": ("The Wee Hours" + SW, "The Wee Hours by Stephanie Watson, illustrated by Mary GrandPré (Disney-Hyperion).", "books", books.wee_hours),
        "elvis-olive.html": ("Elvis & Olive" + SW, "Elvis & Olive, a novel by Stephanie Watson (Scholastic Press).", "books", books.elvis_olive),
        "elvis-olive-super-detectives.html": ("Elvis & Olive: Super Detectives" + SW, "Elvis & Olive: Super Detectives, the sequel to Elvis & Olive by Stephanie Watson (Scholastic Press).", "books", books.super_detectives),
        "elvis-olive-chapter-one.html": ("Chapter One: Elvis & Olive" + SW, "Read the first chapter of Elvis & Olive by Stephanie Watson.", "books", lambda: books.chapter_one(pj)),
        "elvis-olive-discussion-guide.html": ("Elvis & Olive Discussion Guide" + SW, "Discussion questions for Elvis & Olive by Stephanie Watson, for classrooms and book clubs.", "books", books.discussion_guide),
        "teaching.html": ("Author & Illustrator Visits | Twin Cities | Minnesota", "Hire children’s author and illustrator Stephanie Watson for school and library visits, residencies, adult drawing and writing workshops, and talks.", "teaching", teaching.teaching),
        "for-kids.html": ("Author & Illustrator Visits | School and Library Presentations | MN", "School and library presentations, writing workshops and residencies for kids with children’s author and illustrator Stephanie Watson.", "teaching", teaching.for_kids),
        "for-adults.html": ("Writing and Drawing Workshops for Adults" + SW, "Drawing and writing workshops, multi-session classes, talks and keynotes for adults with author and illustrator Stephanie Watson.", "teaching", teaching.for_adults),
        "about.html": ("About" + SW, "About Stephanie Watson, children’s book author and illustrator in Minneapolis, Minnesota.", "about", other.about),
        "videos.html": ("Videos" + SW, "Behind-the-scenes and craft videos from children’s book author Stephanie Watson.", "about", other.videos),
        "contact.html": ("Contact" + SW, "Contact Stephanie Watson about workshops, presentations, school visits, or with general questions.", "about", other.contact),
        "portfolio.html": ("Portfolio" + SW, "Illustrations and artwork handmade by Stephanie Watson.", "portfolio", other.portfolio),
    }


def write_safely(path, text):
    assert len(text) > 3000, f"{path} suspiciously short ({len(text)})"
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(text)
    os.replace(tmp, path)


def verify(files):
    problems = []
    for fn in files:
        s = open(os.path.join(SITE, fn), encoding="utf-8").read()
        for ref in re.findall(r'(?:href|src)="([^"]+)"', s):
            if ref.startswith(("http", "mailto:", "tel:", "#", "data:")):
                if "stephanie-watson.com" in ref:
                    problems.append(f"{fn}: still points at live site -> {ref}")
                continue
            target = ref.split("#")[0].split("?")[0]
            if target and not os.path.exists(os.path.join(SITE, target)):
                problems.append(f"{fn}: missing {ref}")
        for m in re.findall(r"srcset=\"([^\"]+)\"", s):
            for part in m.split(","):
                p = part.strip().split(" ")[0]
                if not p.startswith("http") and not os.path.exists(os.path.join(SITE, p)):
                    problems.append(f"{fn}: missing srcset {p}")
    return problems


REDIRECT = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>This page has moved | Stephanie Watson</title>
<meta name="robots" content="noindex, nofollow">
<link rel="canonical" href="{to}">
<meta http-equiv="refresh" content="0; url={to}">
<script>location.replace("{to}" + ("{to}".indexOf("#") < 0 ? location.hash : ""))</script>
</head><body><p>This page has moved. <a href="{to}">Continue to the new page</a>.</p></body></html>
"""


def write_redirects():
    """Her old WordPress addresses (e.g. /author-visits/school-visits/) still get traffic, so each one
    gets a tiny page at that same path that forwards to its new home. GitHub Pages can't do
    server-side redirects; this is the static-site equivalent."""
    made = []
    for old, new in ROUTES.items():
        if not old:
            continue
        folder = os.path.join(SITE, *old.split("/"))
        os.makedirs(folder, exist_ok=True)
        to = "../" * len(old.split("/")) + new
        with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f:
            f.write(REDIRECT.format(to=to))
        if not os.path.exists(os.path.join(SITE, new.split("#")[0])):
            raise SystemExit(f"redirect /{old}/ points at missing page {new}")
        made.append(old)
    for old, new in OLD_FILES.items():
        with open(os.path.join(SITE, old), "w", encoding="utf-8") as f:
            f.write(REDIRECT.format(to=new))
        made.append(old)
    return made


def main():
    ig = ig_icon()
    written = []
    for fn, (title, desc, section, body) in page_table().items():
        html = head(title, desc, OG) + header(section) + '<main id="main">\n' + body() + "\n</main>\n" + footer(ig)
        write_safely(os.path.join(SITE, fn), html)
        written.append(fn)
    problems = verify(written)
    redirects = write_redirects()
    print(f"built {len(written)} pages + {len(redirects)} redirects from her old addresses")
    if problems:
        print("\n".join(problems))
        raise SystemExit(1)
    print("all local links, images and files resolve; nothing points at the live site")


if __name__ == "__main__":
    main()
