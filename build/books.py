"""Children's books section: overview + one page per book + Elvis & Olive extras."""
import html as H
import json
import re
from chrome import (ARROW, STAR, EXT, ext, crumb, page_hero, video, contact_section)

BOOKS_CRUMB = crumb("Children’s Books", "index.html#books")


def btn(label, href, kind="btn-fill", extra=""):
    return f'<a class="btn {kind} {extra}" href="{href}"{ext(href)}>{label}</a>'


def book_page(*, title, cover, cover_w, cover_h, cover_alt="", cover_href=None, zoom=None,
              desc, facts=(), awards=(), pull="", reviews=(), reviews_heading="",
              buy=(), buy_label="Buy the book", after="", crumb_html=BOOKS_CRUMB):
    if zoom:
        cover_open, cover_close = f'<a class="book-cover" href="{zoom}" data-zoom aria-label="Enlarge cover">', "</a>"
    elif cover_href:
        cover_open, cover_close = f'<a class="book-cover" href="{cover_href}"{ext(cover_href)}>', "</a>"
    else:
        cover_open, cover_close = '<div class="book-cover">', "</div>"
    buy_html = ""
    if buy:
        buttons = "".join(btn(l, h) for l, h in buy)
        buy_html = f'<div class="buy"><span class="lbl">{buy_label}</span>{buttons}</div>'
    facts_html = ("<ul class=\"facts\">" + "".join(f"<li>{f}</li>" for f in facts) + "</ul>") if facts else ""
    awards_html = ("<div class=\"awards\">" + "".join(f'<span class="award">{STAR}<span>{a}</span></span>' for a in awards) + "</div>") if awards else ""
    pull_html = f'<blockquote class="pull">{pull}</blockquote>' if pull else ""
    rev_html = ""
    if reviews:
        cards = "".join(f'<blockquote class="review"><p>{q}</p><cite>{s}</cite></blockquote>' for q, s in reviews)
        rh = f'<h2 class="h2-sm">{reviews_heading}</h2>' if reviews_heading else ""
        rev_html = f'<div class="rv" style="margin-top:40px">{rh}<div class="reviews">{cards}</div></div>'
    paras = "".join(f"<p>{p}</p>" for p in desc)
    return f"""{page_hero(title, crumb_html=crumb_html)}
  <section class="wrap sec pt0">
    <div class="book-layout">
      <aside class="book-aside rv">
        {cover_open}<img src="{cover}" width="{cover_w}" height="{cover_h}" alt="{cover_alt}" fetchpriority="high">{cover_close}
        {buy_html}
        {facts_html}
      </aside>
      <div class="rv">
        {awards_html}{pull_html}
        <div class="prose">{paras}</div>
        {rev_html}
      </div>
    </div>
  </section>
  {after}"""


def videos_band(items, one=False):
    cls = "video-grid one" if one else "video-grid"
    return f'<section class="sec-sm"><div class="wrap"><div class="{cls}">{"".join(items)}</div></div></section>'


# ---------------------------------------------------------------- overview
# ---------------------------------------------------------------- book pages
def pencilvania():
    after = videos_band([
        video("jyQ6gkE2xyk", "Pencilvania book trailer", heading="Watch the book trailer"),
        video("h0BLlROmNwU", "Pencilvania: the first few chapters", heading="Hear the first few chapters"),
    ]) + f"""<section class="wrap sec-sm pt0"><a class="guide-link rv" href="files/Pencilvania-DiscussionGuide_2021.pdf" target="_blank" rel="noopener">
      <span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h6"/></svg></span>
      <span>Use the discussion guide in your classroom or book club</span></a></section>
    {contact_section("Have a question or comment? I’d love to hear from you.")}"""
    return book_page(
        title="Pencilvania", cover="img/Pencilvania-350x509.jpg", cover_w=350, cover_h=509,
        cover_alt="Pencilvania Stephanie Watson", zoom="img/Pencilvania.jpg",
        desc=[
            "Ever since she first learned to hold a crayon, twelve-year-old Zora Webb has been unstoppable. She draws rainbows and balloons and trees and skyscrapers. She draws hamsters wearing pajamas, and hundreds of horses (at the request of her horse-obsessed little sister Frankie). Zora’s drawings fill sketchbooks and cover the walls of the happy home she shares with Frankie and their mom in Duluth, Minnesota. Her drive to create—which Zora and Mom call “Voom”—is powerful and constant.",
            "But when Zora’s mom is diagnosed with leukemia, everything changes. After months of illness, her mom dies, and with her goes Zora’s drive to create. Desperate to escape the pain, Zora scribbles out her artwork and vows to never draw again. Her dark, furious scribbles lift off the page and yank Zora and Frankie into Pencilvania, a magical world that’s home to everything Zora has ever drawn. And one drawing—a scribbled-out horse named Viscardi—is determined to finish the destruction that Zora started.",
            "Viscardi kidnaps Frankie, promising to scribble her and all of Pencilvania out at sunrise. Zora sets out to rescue her sister, venturing deep into Pencilvania—a place crawling with memories, dangers, and new friends. If she is to save Frankie, Zora will have to face the darkness that both surrounds her and is inside of her.",
        ],
        pull="“A vibrant celebration of art’s power to console and heal.” –Kirkus",
        awards=['Named one of the best books of 2021 by the <a href="https://www.nypl.org/books-more/recommendations/best-books/kids?facets_query=&amp;f%5B0%5D=terms%3AMiddle%20Grade" target="_blank" rel="noopener">New York Public Library</a>'],
        facts=["Sourcebooks, October 2021", "Ages 8 and up",
               'Illustrations by <a href="https://www.sofiamooreart.com/" target="_blank" rel="noopener">Sofia Moore</a>'],
        buy=[("Hardcover: $16.99", "https://moonpalacebooks.com/item/yxefp03frD5-_dkxso2VDA"),
             ("Paperback: $7.99", "https://moonpalacebooks.com/item/yxefp03frD5IZHoFT17w5g")],
        buy_label="Buy the book:", after=after)


def best_friends():
    amazon = "http://www.amazon.com/Best-Friends-Universe-Stephanie-Watson/dp/0545659884"
    after = videos_band([video("iDNj3Q03UO0", "Best Friends in the Universe")], one=True) + \
        contact_section("Have a question or comment? Write to me! I love hearing from readers.")
    return book_page(
        title="Best Friends in the Universe", cover="img/Jacket_BFITU_Small.jpg", cover_w=1167, cover_h=1400,
        cover_alt="Best Friends in the Universe book cover", cover_href=amazon,
        desc=[
            "Best friends Hector and Louie do everything together. They have dance parties, invent new foods, tell knock-knock jokes, share secrets, and write books together.",
            "Their friendship is totally perfect and nothing could ever wreck it, except if they told each other’s secrets. Then the friendship would be cancelled and they’d have to rip the book they are writing to shreds. But that will never happen.",
            "Never ever.",
        ],
        facts=["by Stephanie Watson", "Illustrations by LeUyen Pham", "Scholastic/Orchard Books", "For all ages"],
        reviews_heading="Reviews",
        reviews=[
            ("An entertaining look at two besties who get in a fight and find their way to forgiveness.", "—School Library Journal, starred review"),
            ("A high-energy rollercoaster ride.", "—Booklist, starred review"),
            ("Watson captures the intensity and vulnerability of childhood friendships with lively, free-flowing dialogue. A vivacious tribute to both friendship and the artistic imagination.", "—Horn Book"),
            ("A tried-and-true friendship story executed with creativity and verve.", "—Kirkus"),
            ("Bubbles with a fun, noisy energy—this is not a book to read aloud with your inside voice.", "—Publishers Weekly"),
        ],
        buy=[("Buy the book", "http://www.amazon.com/Best-Friends-Universe-Stephanie-Watson/dp/0545659884/ref=sr_1_1?ie=UTF8&amp;qid=1535985714&amp;sr=8-1&amp;keywords=best+friends+in+the+universe")],
        buy_label="Get a copy", after=after)


def behold():
    return book_page(
        title="Behold! A Baby", cover="img/BeholdABabyCover.jpg", cover_w=743, cover_h=837,
        cover_alt="Behold! A Baby book cover", zoom="img/BeholdABabyCover.jpg",
        desc=[
            "Step right up, step right up! Come see one of the most amazing, astounding, stunning and stupendous wonders of the world. Behold: a baby!",
            "Prepare to be filled with wonder as the incredible baby performs feats such as smiling, eating a banana and babbling. There’s just one person in the audience who is unimpressed: The baby’s big brother.",
        ],
        facts=["by Stephanie Watson", 'Illustrations by <a href="http://joyang.ca/artwork/" target="_blank" rel="noopener">Joy Ang</a>', "Bloomsbury", "For all ages"],
        awards=["2016 Minnesota Book Award finalist"],
        reviews=[
            ("Stephanie Watson brings a jolt of theatrical energy to the much-visited subject of a new baby’s arrival. A brash and endearing picture book for soon-to-be-older siblings.", "—The Wall Street Journal"),
            ("Warm and affirming. . . Could lead to discussions about how to be a big brother/sister helper.", "—School Library Journal"),
        ],
        buy=[("Buy the book", "http://www.amazon.com/Behold-Baby-Stephanie-Watson/dp/161963452X/ref=sr_1_1?ie=UTF8&amp;qid=1490287642&amp;sr=8-1&amp;keywords=behold+a+baby")],
        buy_label="Get a copy",
        after=contact_section("Have a question or comment? Write to me! I love hearing from readers."))


def wee_hours():
    after = videos_band([video("bxkrdOpphyo", "The Wee Hours book trailer", heading="Watch the book trailer:")], one=True) + \
        contact_section("Have a question or comment? Drop me a line! I’d love to hear from you.")
    return book_page(
        title="The Wee Hours", cover="img/Wee_hours_Jkt2P_CoverOnly-1.jpg", cover_w=1223, cover_h=1400,
        cover_alt="The Wee Hours book cover", zoom="img/Wee_hours_Jkt2P_CoverOnly-1.jpg",
        desc=["As you sleep and dream, the playful Wee Hours appear when the clock strikes one, two, three and four. These mischievous creatures pull books from your shelves, build towers from your shoes, put on plays behind your curtains and do backflips off your bedposts. As morning draws near, the older hours emerge to tidy up the mess the Wee Hours have made, and carry them off to bed."],
        facts=["Written by Stephanie Watson, illustrated by Mary GrandPré", "Disney-Hyperion", "For all ages"],
        reviews=[
            ("For children who wonder what goes on while they’re asleep, Watson suggests one possibility: Little elfin creatures arrive, one at a time, on the hour, and wreak mischievous mayhem in children’s bedrooms, emptying bureau drawers, pulling down curtains and interfering with dreams. As dawn approaches, older, more responsible Hours arrive to tidy up and tuck the Wee Hours into their own beds. GrandPré, who illustrated the American editions of the “Harry Potter” series, here uses rich purples and velvety reds to evoke a moonlit room full of mysterious shadows. Though there’s not a wand in sight, there’s plenty of magic in play.", "–The New York Times"),
            ("Children will be tickled to see the wee hours of the morning come to life as irresistible, toddlerlike imps in this whimsical tale.", "–Kirkus"),
            ("The Wee Hours–whose apparent ages correspond to their respective hours–release birds, horses, and dinosaurs from the girl’s dreams and make a mess of her room with mischief worthy of The Cat in the Hat’s Thing One and Thing Two. GrandPré’s (Flight of the Last Dragon) luminous pastels convey the rabble-rousers’ infectious enthusiasm and create playful chaos.", "–Publishers Weekly"),
        ],
        buy=[("Buy the book", "http://www.amazon.com/Wee-Hours-Stephanie-Elaine-Watson/dp/1423140389/ref=sr_1_2?ie=UTF8&amp;qid=1490291783&amp;sr=8-2&amp;keywords=the+wee+hours")],
        buy_label="Get a copy", after=after)


def elvis_olive():
    tiles = [
        ("Read Chapter One", "The first day of summer vacation stretched in front of Natalie Wallis like a long road with no street signs…", "Keep reading", "elvis-olive-chapter-one.html"),
        ("Elvis &amp; Olive Discussion Guide", "After reading the book, consider these questions classroom or book club. There are no right or wrong answers!", "See Discussion Guide", "elvis-olive-discussion-guide.html"),
        ("Like this book? Read the sequel!", "In <em>Elvis &amp; Olive: Super Detectives</em>, Natalie and Annie help their neighbors solve mysteries both small and large.", "see the sequel", "elvis-olive-super-detectives.html"),
    ]
    tiles_html = "".join(f'<div class="tile rv"><h3 class="h3">{t}</h3><p>{p}</p><a class="btn btn-line btn-sm" href="{h}">{b} {ARROW}</a></div>' for t, p, b, h in tiles)
    after = f'<section class="wrap sec-sm pt0"><div class="read-more">{tiles_html}</div></section>' + \
        contact_section("Have a question or comment? Write to me! I’d love to hear from you.")
    return book_page(
        title="Elvis &amp; Olive", cover="img/EO-1-FNL-CVR_smaller-350x509.jpeg", cover_w=350, cover_h=509,
        cover_alt="Elvis and Olive Stephanie Watson", zoom="img/EO-1-FNL-CVR_smaller.jpeg",
        desc=[
            "Ten-year-old Natalie Wallis is a shy bookish perfectionist. Annie Beckett (age 9) is a wild tomboy liar. Why do these two very different girls become friends? Because they’ve got some serious spying to do.",
            "“Even the most dull-looking people do all kinds of weird, interesting things when they think no one’s watching,” Annie says. With this in mind, the girls form a secret spying club and start snooping on their neighbors under the code names Elvis &amp; Olive.",
            "By the end of their summer together, Elvis &amp; Olive have uncovered a number of strange secrets about their neighbors. Eaten far too many freeze pops. And formed a friendship like no other.",
        ],
        facts=["Scholastic Press, 2008", "Ages 7 – 12, 230 p.p."],
        awards=["Washington Post Book of the Week", "2008 Junior Library Guild Selection"],
        reviews=[
            ("…a satisfying friendship story with drama and humor in fine balance.", "–Kirkus Reviews"),
            ("…an accomplished first novel.", "–Publishers Weekly"),
            ("Young readers won’t want to put this book down until they find out how Elvis and Olive emerge from the mess they created.", "–Palo Alto Weekly"),
        ],
        after=after)


def super_detectives():
    after = videos_band([
        video("4k-SF8DVZLQ", "Chapter one of Elvis & Olive: Super Detectives", heading="Listen to chapter one of Elvis &amp; Olive: Super Detectives:"),
        video("p8wjJpJhudg", "Interview conducted by a disinterested dog", heading="Watch an interview conducted by a disinterested dog:"),
    ])
    return book_page(
        title="Elvis &amp; Olive: Super Detectives", cover="img/ElvisOlive_SuperDetectives_HighRes-1.jpg", cover_w=600, cover_h=814,
        cover_alt="Elvis & Olive: Super Detectives book cover", zoom="img/ElvisOlive_SuperDetectives_HighRes-1.jpg",
        desc=[
            'In the sequel to <a href="elvis-olive.html">Elvis &amp; Olive,</a> Natalie and Annie open the E &amp; O Detective Agency to solve neighborhood mysteries. They find no shortage of people who could use their help. Albert Castle needs a hand with song lyrics, and Ms. Hatch is looking for a lost flip-flop. Mrs. Warsaw is desperate to find the mysterious Zadie Zeolite, and a lost dog needs help finding his way home.',
            "What’s more, Natalie is searching for a way to win the Student Council election while Annie is on a quest to find her missing mom. Will the biggest cases they have to solve be their own?",
        ],
        facts=["288 p.p.", "Ages 7 to 12", "Scholastic Press, 2010"],
        reviews=[
            ("Watson’s lightly poetic prose contributes to an overall sense of goodwill and abundant imagination. Fresh and affecting.", "–Kirkus"),
            ("Stephanie Watson brings new resonance to familiar kid-lit motifs — secret clubs, young sleuths — by charting the tender as well as the funny moments of this unlikely friendship. Subplots involving a stray dog, banned comic books and Annie’s condemned home resolve in unpredictable ways, and descriptive phrases surprise and delight.", "–The Washington Post"),
        ],
        after=after)


# ---------------------------------------------------------------- Elvis & Olive extras
def _chapter_paragraphs(pages_json):
    """Pull the Chapter One excerpt verbatim from her WordPress export."""
    raw = next(p for p in json.load(open(pages_json)) if p["slug"] == "chapter-one-elvis-olive")["content"]["rendered"]
    raw = re.sub(r"\[/?vc_[^\]]*\]", "", raw)
    paras = re.findall(r"<p>(.*?)</p>", raw, re.S)
    out, credit = [], ""
    for p in paras:
        p = re.sub(r"<h1[^>]*>.*?</h1>", "", p, flags=re.S)
        p = re.sub(r"<(?!/?em\b)[^>]+>", "", p).strip()
        if not p:
            continue
        if p.startswith("<em>Excerpted"):
            credit = re.sub(r"</?em>", "", p).split("All rights reserved.")[0] + "All rights reserved."
            break
        out.append(p)
    assert len(out) > 40 and credit.endswith("reserved."), (len(out), credit)
    return out, credit


def chapter_one(pages_json):
    paras, credit = _chapter_paragraphs(pages_json)
    body = "".join(f"<p>{p}</p>" for p in paras)
    bn = "http://www.barnesandnoble.com/w/elvis-olive-stephanie-watson/1100178136"
    return f"""{page_hero("Chapter One: Elvis &amp; Olive", crumb_html=crumb("Elvis &amp; Olive", "elvis-olive.html"), center=True)}
  <section class="wrap sec pt0">
    <article class="reading">{body}<p class="credit">{credit}</p>
      <p style="text-align:center;margin-top:1.4em">{btn("Buy the book", bn)}</p>
    </article>
    <div class="end-card rv">
      <img src="img/EO-1-FNL-CVR_7x11-1.jpg" width="962" height="1400" alt="Elvis &amp; Olive book cover" loading="lazy">
      <div class="stack">{btn("Buy the book", bn)}{btn("Discussion guide", "elvis-olive-discussion-guide.html", "btn-line")}</div>
    </div>
  </section>"""


def discussion_guide():
    qs = [
        "What does Natalie gain from being Annie’s friend?",
        "What does Annie gain from being Natalie’s friend?",
        "Why does Annie lie? Why does Natalie want to believe her?",
        "Have you ever had a fight with a best friend? Can fights ever be a good thing for a friendship?",
        "How Natalie and Annie’s spying help the neighbors? How does it hurt them?",
        "When is it a good idea to tell secrets, and when is it best to keep them?",
        "What are some of the different ways this story could have ended?",
    ]
    q_html = "".join(f"<li>{q}</li>" for q in qs)
    lede = 'After reading <a class="link" href="elvis-olive.html">Elvis &amp; Olive</a>, use these questions to start a discussion in your classroom or book club. There are no right or wrong answers!'
    return f"""{page_hero("Elvis &amp; Olive Discussion Guide", lede, crumb_html=crumb("Elvis &amp; Olive", "elvis-olive.html"))}
  <section class="wrap sec pt0">
    <div class="feature" style="align-items:start">
      <div class="rv">
        <ol class="questions">{q_html}</ol>
        <div class="prose">
          <p>Read the <a href="http://www.scholastic.com/teachers/article/booktalk-elvis-and-olive" target="_blank" rel="noopener"><em>Elvis &amp; Olive</em> Book Talk by Scholastic</a></p>
          <p>Are you a teacher or librarian? Learn about my <a href="for-kids.html">school presentations</a></p>
        </div>
      </div>
      <div class="feature-img rv" style="position:sticky;top:110px"><img src="img/37179_443947918379_4141309_n.jpg" width="720" height="540" alt="Author Stephanie Watson reading from one of her books." loading="lazy"></div>
    </div>
  </section>"""
