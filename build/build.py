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
    "books": "books.html",
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
    # the old "Author & Illustrator Visits" pages now live inside Teaching
    "author-visits": "teaching.html",
    "author-visits/school-visits": "for-kids.html",
    "school-visits": "for-kids.html",
    "author-visits/library-storytimes": "for-kids.html#library",
    "author-visits/other-presentations": "for-adults.html",
    "author-visits/testimonials": "for-kids.html#testimonials",
    "school-visits/testimonials": "for-kids.html#testimonials",
    "about": "about.html",
    "contact": "contact.html",
    "contact/how-to-become-an-author": "how-to-become-an-author.html",
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


# filename -> (title or None for home, description, section, body-builder)
def page_table():
    pj = PAGES_JSON
    return {
        "index.html": (None, SITE_DESC, "home", home),
        "books.html": ("Children’s Books", "Children’s books by Minneapolis author Stephanie Watson: Pencilvania, Best Friends in the Universe, Behold! A Baby, The Wee Hours and the Elvis & Olive novels.", "books", books.books_overview),
        "pencilvania.html": ("Pencilvania", "Pencilvania, a middle-grade novel by Stephanie Watson, illustrated by Sofia Moore (Sourcebooks, 2021).", "books", books.pencilvania),
        "best-friends-in-the-universe.html": ("Best Friends in the Universe", "Best Friends in the Universe by Stephanie Watson, illustrated by LeUyen Pham (Scholastic/Orchard Books).", "books", books.best_friends),
        "behold-a-baby.html": ("Behold! A Baby", "Behold! A Baby by Stephanie Watson, illustrated by Joy Ang (Bloomsbury). 2016 Minnesota Book Award finalist.", "books", books.behold),
        "the-wee-hours.html": ("The Wee Hours", "The Wee Hours by Stephanie Watson, illustrated by Mary GrandPré (Disney-Hyperion).", "books", books.wee_hours),
        "elvis-olive.html": ("Elvis & Olive", "Elvis & Olive, a novel by Stephanie Watson (Scholastic Press, 2008).", "books", books.elvis_olive),
        "elvis-olive-super-detectives.html": ("Elvis & Olive: Super Detectives", "Elvis & Olive: Super Detectives, the sequel to Elvis & Olive by Stephanie Watson (Scholastic Press, 2010).", "books", books.super_detectives),
        "elvis-olive-chapter-one.html": ("Chapter One: Elvis & Olive", "Read the first chapter of Elvis & Olive by Stephanie Watson.", "books", lambda: books.chapter_one(pj)),
        "elvis-olive-discussion-guide.html": ("Elvis & Olive Discussion Guide", "Discussion questions for Elvis & Olive by Stephanie Watson, for classrooms and book clubs.", "books", books.discussion_guide),
        "teaching.html": ("Teaching", "Book children’s author and illustrator Stephanie Watson for school visits, library storytimes, adult writing workshops, keynotes and special events.", "teaching", teaching.teaching),
        "for-kids.html": ("For Kids", "School presentations, writing workshops and library storytimes with children’s author and illustrator Stephanie Watson.", "teaching", teaching.for_kids),
        "for-adults.html": ("For Adults", "Writing workshops, keynote speeches and festival presentations for adults with author and illustrator Stephanie Watson.", "teaching", teaching.for_adults),
        "about.html": ("About", "About Stephanie Watson, children’s book author and illustrator in Minneapolis, Minnesota.", "about", other.about),
        "how-to-become-an-author.html": ("How to Become an Author", "Resources from Stephanie Watson for anyone who wants to write children’s books.", "about", other.how_to_author),
        "videos.html": ("Videos", "Videos from Stephanie Watson: behind the book, her writing process, readings and the Word Slingers series.", "videos", other.videos),
        "contact.html": ("Contact", "Contact Stephanie Watson about school and library visits, fees, or general questions.", "contact", other.contact),
        "portfolio.html": ("Portfolio", "Illustrations and artwork handmade by Stephanie Watson.", "home", other.portfolio),
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
            target = ref.split("#")[0]
            if target and not os.path.exists(os.path.join(SITE, target)):
                problems.append(f"{fn}: missing {ref}")
        for m in re.findall(r"srcset=\"([^\"]+)\"", s):
            for part in m.split(","):
                p = part.strip().split(" ")[0]
                if not p.startswith("http") and not os.path.exists(os.path.join(SITE, p)):
                    problems.append(f"{fn}: missing srcset {p}")
    return problems


def main():
    ig = ig_icon()
    written = []
    for fn, (title, desc, section, body) in page_table().items():
        html = head(title, desc, OG) + header(section) + '<main id="main">\n' + body() + "\n</main>\n" + footer(ig)
        write_safely(os.path.join(SITE, fn), html)
        written.append(fn)
    problems = verify(written)
    print(f"built {len(written)} pages")
    if problems:
        print("\n".join(problems))
        raise SystemExit(1)
    print("all local links, images and files resolve; nothing points at the live site")


if __name__ == "__main__":
    main()
