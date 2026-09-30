"""Visits, about, contact, videos, portfolio pages."""
from chrome import ARROW, page_hero, video, contact_section, contact_form

# ---------------------------------------------------------------- about / contact
NEWSLETTER = """<section class="sec news-band" id="newsletter"><div class="wrap">
      <div class="sec-head rv"><h2>Newsletter</h2></div>
      <div class="news-card rv"><iframe src="https://thepennycarnival.substack.com/embed" title="Subscribe to The Penny Carnival on Substack" loading="lazy" scrolling="no"></iframe></div>
    </div></section>"""


def about():
    text = """<p>When I was five, my career ambition was to be a cake decorator. Making paintings you could eat, what could be better? As it turns out, I became a storyteller. I hope my five-year-old self is okay with this change in course.</p>
<p>I read a lot when I was a kid. I also performed at the Minneapolis <a href="https://www.childrenstheatre.org/" target="_blank" rel="noopener">Children’s Theatre Company</a>. I was in Alice in Wonderland, Madeline’s Rescue, Babar, Pippi Longstocking, Pinocchio, The 500 Hats of Bartholomew Cubbins, A Wrinkle in Time and other plays. To balance out these enriching educational experiences, I also watched a lot of TV. For a while, my favorite show was called Small Wonder, about a little girl robot named Vicki who could lift a car over her head.</p>
<p>Spending so much time immersed in stories as a kid did something to me, like in Batman, when that guy falls in a vat of chemical green goo and becomes the Joker. But instead of becoming a supervillain with diabolical plans, I became a storyteller determined to write and draw. Me and the Joker both like to laugh, though.</p>
<p>I’ve written three middle-grade novels: <a href="pencilvania.html">Pencilvania</a>, <a href="elvis-olive.html">Elvis &amp; Olive</a> and <a href="elvis-olive-super-detectives.html">Elvis &amp; Olive: Super Detectives</a>. I also wrote the picture books <a href="best-friends-in-the-universe.html">Best Friends in the Universe</a>, <a href="behold-a-baby.html">Behold! A Baby</a> and <a href="the-wee-hours.html">The Wee Hours</a>. And in 2028, my author-illustrator debut comes out. It’s called YES, A DRESS!</p>
<p>A proud product of the Minneapolis Public Schools (Clara Barton Open, South High), I also attended Sarah Lawrence College in New York. I’ve been lucky to receive grants from the Minnesota State Arts Board and the Jerome Foundation. Currently, I live in Minneapolis, MN.</p>
<p>In addition to writing stories, I also teach <a href="teaching.html">writing workshops</a> for children and adults.</p>"""
    return f"""{page_hero("About me")}
  <section class="wrap sec pt0">
    <div class="book-layout about-layout">
      <div class="rv">
        <div class="prose">{text}</div>
        <div class="btn-row"><a class="btn btn-fill" href="index.html#books">Books {ARROW}</a><a class="btn btn-line" href="teaching.html">Teaching &amp; Speaking</a></div>
      </div>
      <div class="book-aside rv"><div class="photo-wrap"><img src="img/about_portrait_2026.jpg" width="1200" height="1600" alt="Stephanie Watson" style="aspect-ratio:4/5;object-position:center 30%" fetchpriority="high"></div></div>
    </div>
  </section>
  {NEWSLETTER}
  {contact_section()}"""


def contact():
    return f"""{page_hero("Contact Stephanie", "Interested in a workshop or presentation? Have general questions or comments? I’d love to hear from you.")}
  <section class="wrap sec pt0">
    <div class="contact-page">
      <div class="form-card rv">{contact_form()}</div>
      <aside class="side-col">
        <div class="side-photos rv">
          <img src="img/contact_sketchbook.jpg" width="1200" height="1600" alt="Stephanie Watson sketching on the beach">
          <img src="img/contact_age-3-drawing.jpg" width="1045" height="1045" alt="Stephanie Watson at age three, beside her chalkboard drawing">
        </div>
      </aside>
    </div>
  </section>"""


# ---------------------------------------------------------------- videos
def videos():
    top = f"""<div class="feature">
      <div class="rv"><h2 class="h2-sm">Behind the Book</h2><p class="muted">Ever wonder how a book gets made? How long does it take? Is it easy or is it hard? Find out in this video series about my writing process for my latest book, Pencilvania.</p></div>
      {video("giqAr8Obbyo", "Behind the Book: Pencilvania")}
    </div>
    <div class="feature">
      {video("UsMOICEpiGA", "Writing Process")}
      <div class="rv"><h2 class="h2-sm">Writing Process</h2><p class="muted">When I sit down at my writing desk in the morning, part of me is desperate to do anything BUT write. Another part of me is deeply committed to my daily writing practice (M-F). These two parts are forever at war.</p></div>
    </div>"""
    pair = f"""<div class="video-grid">
      {video("iDNj3Q03UO0", "Watch Best Friends in the Universe", heading="Watch Best Friends in the Universe")}
      {video("h0BLlROmNwU", "Hear the first few chapters of Pencilvania", heading="Hear the first few chapters of Pencilvania")}
    </div>"""
    ws = f"""<div class="video-grid">
      {video("1aX3aAMaBiE", "Word Slingers Episode 1: Begin Again", heading="Episode 1: Begin Again")}
      {video("aehyiFlzYNE", "Word Slingers Episode 2: The Buddy System", heading="Episode 2: The Buddy System")}
      {video("IapqP6t0cXA", "Overcoming Creative Heartbreak: Interview w/ Jacquelyn Fletcher", heading="Overcoming Creative Heartbreak: Interview w/ Jacquelyn Fletcher")}
      {video("xjzb0X_uC_k", "Becoming Your Own Publisher: Interview w/ Jacquelyn Fletcher", heading="Becoming Your Own Publisher: Interview w/ Jacquelyn Fletcher")}
    </div>"""
    return f"""{page_hero("Videos")}
  <section class="wrap sec pt0">{top}</section>
  <section class="wrap sec-sm pt0">{pair}</section>
  <section class="sec portfolio" id="word-slingers">
    <div class="wrap">
      <div class="ws-head rv">
        <a class="ws-logo" href="https://www.youtube.com/channel/UCqbDfqwIyCJDUw5iUK9CePA" target="_blank" rel="noopener" aria-label="Word Slingers on YouTube"><img src="img/WordSlingersLogo_1.jpg" width="500" height="500" alt="Word Slingers" loading="lazy"></a>
        <div><span class="eyebrow">Creative process talks and interviews</span><h2>Word Slingers: Video Series</h2>
        <p class="muted">In the Word Slingers video series, we shine a light on the creative writing process, and share ideas and inspiration to help move your writing practice forward. Created in partnership with John Schaidler, a fellow writer and interdisciplinary artist.</p></div>
      </div>
      {ws}
    </div>
  </section>
  {contact_section("Have an idea for a future episode of Word Slingers? We’d love to hear from you!")}"""


# ---------------------------------------------------------------- portfolio
PIECES = [
    # file, w, h, tags, lightbox title, visible caption, visible tag chips, alt
    ("BugTeaParty_2026.jpg", 1000, 755, "childrens character", "Mixed media", "Mixed media", ["Children’s illustration", "Character design"], "Insects in fancy dress having a tea party"),
    ("KnittingRaccoonMother_Child.jpg", 1500, 1018, "childrens character", "Oil pastel", "Oil pastel", ["Children’s illustration", "Character design"], "Illustration of a raccoon mother and child knitting, drawing in oil pastels"),
    ("RollerskatingOwl.jpg", 795, 1050, "childrens character", "Mixed media", "Mixed media", ["Children’s illustration", "Character design"], "Rollerskating owl created with mixed media"),
    ("Frogs1_2026.jpg", 1600, 1253, "childrens character editorial", "Mixed media", "Mixed media", ["Children’s illustration", "Character design", "Editorial"], "Three green frogs"),
    ("ChameleonsKnitting.jpg", 1050, 755, "character childrens", "Oil pastel, acrylic gouache and colored pencil", "Oil pastel, acrylic gouache and colored pencil", ["Children’s illustration", "Character design"], "Oil pastel, acrylic gouache and colored pencil"),
    ("BlueWhale.jpg", 1200, 908, "editorial", "Oil pastel, acrylic gouache and colored pencil", "Oil pastel, acrylic gouache and colored pencil", ["Editorial"], "A blue whale"),
    ("RaccoonKnittingSocks.jpg", 765, 1050, "character childrens", "Oil pastel, acrylic gouache and colored pencil", "Oil pastel, acrylic gouache and colored pencil", ["Character design", "Children’s illustration"], "Raccoon knitting socks"),
    ("Minneapolis_oilcrayons.jpg", 1050, 790, "editorial", "Downtown Minneapolis in oil pastel", "Downtown Minneapolis in oil pastel", ["Editorial"], "Downtown Minneapolis in oil pastel"),
    ("Moths_oilpastel.jpg", 1050, 793, "editorial sketchbook", "Spotted lanternflies", "Spotted lanternflies in oil pastel", ["Editorial", "Sketchbook"], "Spotted lanternflies in oil pastel"),
    ("MCADFigureDrawing1.jpg", 1050, 761, "figure sketchbook", "Figure drawing", "Figure in oil pastel", ["Sketchbook", "Figure Drawing"], "Figure in oil pastel"),
    ("KnittingCrab_oilpastel.jpg", 1400, 1075, "character childrens editorial", "Oil pastel", "Oil pastels and acrylic gouache", ["Character design", "Children’s illustration", "Editorial"], "Knitting crab in oil pastel"),
    ("BabyDeer_oilpastel.jpg", 750, 1060, "childrens", "Mixed media", "Mixed media", ["Children’s Illustration"], "Baby deer in oil pastel"),
    ("MCADFigureDrawing2.jpg", 1050, 771, "figure", "Oil pastel", "Oil pastel", ["Figure drawing"], "Figure drawing in oil pastel"),
    ("KoiatComo.jpg", 1019, 848, "sketchbook", "Koi fish", "Oil pastel in sketchbook", ["Sketchbook"], "Sketchbook page of koi fish in oil pastel"),
    ("Hollyhock3.jpg", 1253, 1600, "sketchbook editorial", "Gouache and soft pastel", "Gouache and soft pastel", ["Sketchbook", "Editorial"], "Pink hollyhocks"),
    ("PeggyFleming.jpg", 1208, 1600, "sketchbook editorial", "Mixed media", "Mixed media", ["Sketchbook", "Editorial"], "Figure skater Peggy Fleming"),
]


def portfolio():
    filters = [("all", "All Work"), ("childrens", "Children’s illustration"), ("editorial", "Editorial"),
               ("character", "Character design"), ("sketchbook", "Sketchbook"), ("figure", "Figure drawing")]
    fb = "".join(f'<button type="button" data-filter="{k}" aria-pressed="{str(k == "all").lower()}">{l}</button>' for k, l in filters)
    items = []
    for f, w, h, tags, title, cap, chips, alt in PIECES:
        chip_html = "".join(f"<span>{c}</span>" for c in chips)
        items.append(f"""<figure class="piece" data-tags="{tags}" data-title="{title}">
        <button type="button" aria-label="View larger: {cap}"><img src="img/{f}" width="{w}" height="{h}" alt="{alt}" loading="lazy"></button>
        <figcaption><p>{cap}</p><div class="tags">{chip_html}</div></figcaption></figure>""")
    return f"""{page_hero("Portfolio", "Illustrations &amp; artwork handmade by Stephanie Watson. Use the filters to explore by category.", center=True)}
  <section class="wrap sec pt0">
    <div class="filters rv" role="group" aria-label="Filter portfolio by category">{fb}</div>
    <div class="gallery">{"".join(items)}</div>
  </section>"""
