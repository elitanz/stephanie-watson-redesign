"""Visits, about, contact, videos, portfolio pages."""
from chrome import (ARROW, EXT, ext, crumb, page_hero, video, contact_section, contact_form)

VISITS_CRUMB = crumb("Author &amp; Illustrator Visits", "author-visits.html")


def quotes(items, cls="quote-grid"):
    cards = "".join(f'<blockquote class="quote rv"><p>{q}</p><cite>{c}</cite></blockquote>' for q, c in items)
    return f'<div class="{cls}">{cards}</div>'


def feature(img, w, h, body, flip=False, alt=""):
    f = " flip" if flip else ""
    return f"""<div class="feature{f}">
      <div class="feature-img rv"><img src="{img}" width="{w}" height="{h}" alt="{alt}" loading="lazy"></div>
      <div class="rv">{body}</div>
    </div>"""


# ---------------------------------------------------------------- visits
def author_visits():
    opts = [
        ("School Visits", "img/writing-workshop-minneapolis-minnesota.jpeg", 500, 333,
         "Choose a ready-made talk or workshop, designed for both large and small groups. You can also request a custom presentation.", "school-visits.html"),
        ("Library Visits", "img/Stephanie-Watson-library-storytime-1.jpg", 600, 400,
         "My fun, fast-paced library storytime presentation keeps little ones engaged as they learn. I also offer programs for older kids and adults.", "library-storytimes.html"),
        ("Other Presentations", "img/StephanieWatsonAuthorTwinCities-scaled.jpeg", 1400, 933,
         "Need a keynote speaker for your special event? Or a writing workshop for adults? I’d love to work with you.", "other-presentations.html"),
    ]
    cards = "".join(f"""<article class="option rv"><img src="{src}" width="{w}" height="{h}" alt="" loading="lazy">
      <div class="body"><h3 class="h3">{t}</h3><p>{p}</p><a class="btn btn-fill btn-sm" href="{href}">Learn More {ARROW}</a></div></article>"""
                    for t, src, w, h, p, href in opts)
    return f"""{page_hero("Author &amp; Illustrator Visits", "Looking for a children’s book creator to visit your classroom, library or at a special event? Whether your group is small or large, comprised of children or adults, I can create a presentation or workshop that’s just the right fit.")}
  <section class="wrap sec pt0">
    <h2 class="h2-sm rv">Explore options by presentation type:</h2>
    <div class="options">{cards}</div>
  </section>
  {contact_section("Want to inquire about my rates, or are you ready to schedule a virtual or in-person visit? Please get in touch.")}"""


def _program(name, text, grades, size, length):
    return f"""<article class="program rv"><h3>{name}</h3><p>{text}</p>
      <ul class="specs"><li>Grade levels: {grades}</li><li>Group size: {size}</li><li>Length: {length}</li></ul></article>"""


def school_visits():
    pres = _program("10 Things", "All writers rely on tools and tricks to help them create good stories. In this dynamic presentation, you’ll learn the 10 things that have helped me most as a writer. If you’re interested in becoming a writer, these things can help you, too!",
                    "2 – 8", "30 – 1,000 students", "45 – 60 min") + \
        _program("The Picture Book Process", 'In this highly visual presentation, I share each step of the process, including my rough drafts, editing the text, as well as the illustrator’s initial sketches and final artwork. Choose either <a href="best-friends-in-the-universe.html">Best Friends in the Universe</a> or <a href="behold-a-baby.html">Behold! A Baby</a>. Followed by a Q&amp;A.',
                 "K – 8", "30 – 1,000 students", "45 – 60 min")
    work = _program("Raise the Stakes", "To grab readers’ attention and keep them hooked till the last page, your story needs high stakes. In this workshop, we’ll do fun group activities and writing exercises to practice upping the ante.",
                    "2 – 8", "30 – 60 students", "45 – 60 min") + \
        _program("Story Jars", "Do you ever sit down to start a story and find yourself staring at the blank page? Writing prompts, also known as story starters, can be a great way to get the ball rolling. As a group, we’ll create Story Jars–writing prompt tools that can remain in the classroom for future use.",
                 "2 – 8", "30 – 60 students", "45 – 60 min")
    q = quotes([
        ("We loved hearing the process of making a book and listening to Stephanie's stories.", "- Erin Geary, 2nd grade teacher at Lakeview Public School, Cottonwood, MN"),
        ("Stephanie spent two days with the pre-k to fifth grade kids during the Blake LitFest. She had fun, age-appropriate interactive presentations, and her stories kept the kids engaged and asking questions. We loved working with Stephanie!", "- Jacquelyn Fletcher-Johnson, The Blake School LitFest Co-Chair"),
        ("I appreciated that Stephanie spoke at the students' level. She had great ideas for writing that were just right for my students.", "- Mary Roe, 4th grade teacher at Lakeview Public School, Cottonwood, MN"),
    ])
    lede = "Want to turbo-charge a writing unit? Looking for a fun way to kick off a read-a-thon or book fair? Considering hiring me for a school presentation or workshop! Browse my ready-made workshops and presentations below, or request a custom presentation. To ask about fees and availability, please get in touch."
    return f"""{page_hero("School Visits: Author &amp; Illustrator", lede, crumb_html=VISITS_CRUMB)}
  <section class="wrap sec pt0">
    <div class="group">
      <div class="group-head">
        <div class="rv"><span class="kicker">for 30 or more people</span><h2>Presentations</h2></div>
        <img class="rv" src="img/minneapolis-author-school-visit-e1496944139765.jpeg" width="350" height="341" alt="" loading="lazy" style="aspect-ratio:16/10">
      </div>
      <div class="programs">{pres}</div>
    </div>
    <div class="group">
      <div class="group-head">
        <div class="rv"><span class="kicker">for 10 – 60 people</span><h2>Workshops</h2></div>
        <img class="rv" src="img/writing-workshop-minneapolis-minnesota.jpeg" width="500" height="333" alt="" loading="lazy" style="aspect-ratio:16/10">
      </div>
      <div class="programs">{work}</div>
    </div>
  </section>
  <section class="sec testis">
    <div class="wrap">
      {q}
      <div class="center rv"><a class="btn btn-fill" href="testimonials.html">Read all testimonials {ARROW}</a></div>
    </div>
  </section>
  {contact_section("Want to schedule a visit or workshop, or to inquire about fees? I’d love to hear from you.")}"""


def library_storytimes():
    body = feature("img/Stephanie-Watson-library-storytime-1.jpg", 600, 400,
                   '<h2 class="h2-sm">Family Storytime</h2><p>My standard 30-minute presentation is designed for ages 0 – 5 (and their adults). Features <a class="link" href="behold-a-baby.html">Behold! A Baby</a> and <a class="link" href="the-wee-hours.html">The Wee Hours</a>, and includes interactive games, songs and puppets! Aligns with early literacy learning objectives, with elements that foster vocabulary, letter knowledge, phonological awareness, print motivation and numeracy.</p>') + \
        feature("img/IMG_2944_v2.jpg", 1080, 656,
                '<h2 class="h2-sm">Presentation for grades K – 8</h2><p>In this highly visual talk for older kids, we explore the writing and publishing process. I share images of my early drafts, my desk and illustrator sketches. I talk about how I create a book, from initial idea to finished product, and invite kids to consider creating their own stories. This type of presentation typically lasts 30 – 60 minutes.</p>', flip=True) + \
        feature("img/Writing-Hand.jpeg", 428, 222,
                '<h2 class="h2-sm">Adult Writing Workshops</h2><p>I’d love to offer a writing workshop for adults in your community. These are typically one- to two-hour standalone sessions, but we can also do a series. You choose the focus: idea generation, character development, revision, or another writing topic. Each participant will leave the class with the beginnings of a brand new story!</p>')
    lede = "Looking for a special program for your library, either virtual or in-person? Explore the options below. If you don’t see what you need, please contact me. I’m always glad to work with you to customize a storytime presentation or writing workshop."
    return f"""{page_hero("Library Storytimes &amp; Workshops", lede, crumb_html=VISITS_CRUMB)}
  <section class="wrap sec pt0">{body}</section>
  {contact_section("To inquire about fees and availability, please write to me. I look forward to hearing from you!")}"""


def other_presentations():
    body = feature("img/12743652_960442657380772_3228764945647219935_n-1.jpg", 960, 736,
                   '<h2 class="h2-sm">Keynote Speeches</h2><p>I love sharing the story of my creative journey, and hope that audience members leave feeling inspired to exercise their creativity, too. To create a keynote address, I start by learning more about your organization and your goals for the day. I then craft my talk to suit your audience and preferred length (usually 30 – 60 minutes).</p>', flip=True) + \
        feature("img/alphabet-forest-minnesota-state-fair-big-but-short.jpeg", 450, 371,
                """<h2 class="h2-sm">Festivals &amp; Fairs</h2><p>I’d be delighted to present at your upcoming book festival or fair. I’ve been a featured author at:</p>
                <ul><li>The Festival of Children’s Literature at the Anderson Center in Redwing, MN</li><li>The Twin Cities Book Festival</li><li>The Alphabet Forest at the Minnesota State Fair</li><li>LitFest at the Blake School in Minneapolis, MN</li><li>St. Paul Saints games</li><li>Rhythm &amp; Words Festival in Burnsville, MN</li></ul>
                <p>I’d love to come celebrate with you, too!</p>""")
    q = quotes([
        ("Stephanie made her presentation interesting for everyone in the multi-generational audience. across generations of people, and she made the desire to write an aspiration for the young people who were listening to her.", "- Zylpha Gregorson, Emcee of Mother-Daughter-Sister-Friend Breakfast, Central Lutheran Church, Minneapolis"),
        ("Thanks for all the effort you put into the presentation--it was very fun!", "- Nicole Brinkman, Children's Librarian at Ramsey County Library - Roseville, MN"),
        ("I liked the combination of Stephanie's visual presentation with her expressive voice.", "- Ann Oyen, Organizer for Mother-Daughter-Sister-Friend Breakfast, Central Lutheran Church, Minneapolis"),
    ])
    lede = "Looking for a virtual or in-person speaker for an upcoming event? I enjoy sharing my ideas about writing and creativity with people of all ages. I’ve delivered author keynote speeches and presentations at conferences, book festivals, luncheons, museums, baseball games–even on an old-time trolley car. If you don’t see what you’re looking for in the list below, I’m happy to customize a presentation for your event. Please contact me for more info!"
    return f"""{page_hero("Other Presentations", lede, crumb_html=VISITS_CRUMB)}
  <section class="wrap sec pt0">{body}</section>
  <section class="sec testis"><div class="wrap"><div class="sec-head rv"><h2>Testimonials</h2></div>{q}</div></section>
  {contact_section("To inquire about fees and availability, please write to me. I look forward to hearing from you.")}"""


def testimonials():
    def card(q, name, role):
        return f'<blockquote class="quote rv"><p>{q}</p><cite>{name}<br><span style="color:var(--ink-2);font-weight:500">{role}</span></cite></blockquote>'
    items = [
        card("Stephanie spent two days with the pre-k to fifth grade kids during the Blake LitFest. She had fun, age-appropriate interactive presentations, and her stories kept the kids engaged and asking questions. We loved working with Stephanie!", "Jacquelyn Fletcher-Johnson, LitFest Co-Chair", "The Blake School, Hopkins, MN"),
        '<img class="rv" src="img/37179_443947918379_4141309_n.jpg" width="720" height="540" alt="" loading="lazy">',
        card("We loved hearing the process of making a book and listening to Stephanie’s stories.", "Erin Geary, 2nd grade teacher", "Lakeview Public School, Cottonwood, MN"),
        card("My class was thrilled to have Stephanie come for an author visit to lead a character workshop. She helped the students create interesting characters by asking probing questions, which led to mapping out exciting individual stories. At the end of the workshop we had time for a Q&amp;A session and autographs!", "Rayna Lechelt, 3rd grade teacher", "Prairie View Elementary, Eden Prairie, MN"),
        '<img class="rv" src="img/12743652_960442657380772_3228764945647219935_n.jpg" width="960" height="736" alt="" loading="lazy">',
        card("I appreciated that Stephanie spoke at the students’ level. She had great ideas for writing that were just right for my students. I also liked that she allowed time for questions.", "Mary Roe, 4th grade teacher", "Lakeview Public School, Cottonwood, MN"),
    ]
    return f"""{page_hero("Testimonials", crumb_html=VISITS_CRUMB)}
  <section class="wrap sec pt0"><div class="masonry">{"".join(items)}</div></section>
  {contact_section()}"""


# ---------------------------------------------------------------- about / contact / how-to
NEWSLETTER = """<section class="sec news-band" id="newsletter"><div class="wrap">
      <div class="sec-head rv"><h2>Newsletter</h2></div>
      <div class="news-card rv"><iframe src="https://thepennycarnival.substack.com/embed" title="Subscribe to The Penny Carnival on Substack" loading="lazy" scrolling="no"></iframe></div>
    </div></section>"""


def about():
    text = """<p>When I was five, my career ambition was to be a cake decorator. Making paintings you could eat, what could be better? As it turns out, I became a storyteller. I hope my five-year-old self is okay with this change in course.</p>
<p>I read a lot when I was a kid. I also performed at the Minneapolis <a href="https://www.childrenstheatre.org/" target="_blank" rel="noopener">Children’s Theatre Company</a>. I was in Alice in Wonderland, Madeline’s Rescue, Babar, Pippi Longstocking, Pinocchio, The 500 Hats of Bartholomew Cubbins, A Wrinkle in Time and other plays. To balance out these enriching educational experiences, I also watched a lot of TV. For a while, my favorite show was called Small Wonder, about a little girl robot named Vicki who could lift a car over her head.</p>
<p>Spending so much time immersed in stories as a kid did something to me, like in Batman, when that guy falls in a vat of chemical green goo and becomes the Joker. But instead of becoming a supervillain with diabolical plans, I became a storyteller determined to write and draw. Me and the Joker both like to laugh, though.</p>
<p>I’ve written three middle-grade novels: <a href="pencilvania.html">Pencilvania</a>, <a href="elvis-olive.html">Elvis &amp; Olive</a> and <a href="elvis-olive-super-detectives.html">Elvis &amp; Olive: Super Detectives</a>. I also wrote the picture books <a href="best-friends-in-the-universe.html">Best Friends in the Universe</a>, <a href="behold-a-baby.html">Behold! A Baby</a> and <a href="the-wee-hours.html">The Wee Hours</a>.</p>
<p>A proud product of the Minneapolis Public Schools (Clara Barton Open, South High), I also attended Sarah Lawrence College in New York. I’ve been lucky to receive grants from the Minnesota State Arts Board and the Jerome Foundation. Currently, I live in Minneapolis, MN.</p>
<p>In addition to writing stories, I also teach <a href="author-visits.html">writing workshops</a> for children and adults.</p>"""
    return f"""{page_hero("About me")}
  <section class="wrap sec pt0">
    <div class="book-layout about-layout">
      <div class="rv">
        <div class="prose">{text}</div>
        <div class="btn-row"><a class="btn btn-fill" href="books.html">See Stephanie’s books {ARROW}</a><a class="btn btn-line" href="school-visits.html">About school visits</a></div>
      </div>
      <div class="book-aside rv"><div class="photo-wrap"><img src="img/StephanieWatsonAuthorMinnesota_BFITU-launch-scaled.jpeg" width="1400" height="933" alt="" style="aspect-ratio:4/5"></div></div>
    </div>
  </section>
  {NEWSLETTER}
  {contact_section()}"""


def contact():
    return f"""{page_hero("Contact Stephanie", "Ready to schedule a school or library visit, or want to inquire about fees? Have general questions or comments? I’d love to hear from you.")}
  <section class="wrap sec pt0">
    <div class="contact-page">
      <div class="form-card rv">{contact_form()}</div>
      <aside class="side-card rv">
        <img src="img/055_Watson_web_cropped.jpg" width="382" height="455" alt="" loading="lazy" style="object-position:center 25%">
        <div class="body"><strong>Want to write children’s books?</strong>
          <p>If you’re interested in becoming an author but aren’t sure where to start, these resources can help.</p>
          <a class="btn btn-fill btn-sm" href="how-to-become-an-author.html">Go {ARROW}</a></div>
      </aside>
    </div>
  </section>"""


def how_to_author():
    res = [
        ("The Loft Literary Center", "https://www.loft.org/", "This Twin Cities-based writing center was where I took classes after college graduation. Loft classes helped me further my writing technique and plug into the kid lit community. The in-person classes are great, but if you’re out of town, you’re in luck: the Loft offers online classes."),
        ("Children’s Writer’s &amp; Illustrator’s Market", "", "This book, updated annually, is a vital resource for both new and experienced writers. The front section is chock full of answers to your questions about how to get an agent, how to craft a query letter, and more. The second half of the book is a directory of agents and publishers. Buy this book! It’s a lot of great info for $30. Not including a link to buy, since there’s a new version every year. Just Google it up and you’ll find the latest edition."),
        ("SCBWI", "http://www.scbwi.org/", "If you’re serious about creating children’s books, consider joining the Society of Children’s Book Writers &amp; Illustrators. They host tons of events and workshops that can help you get your footing in the world of kid lit."),
        ("QueryTracker", "https://querytracker.net/index.php", "If you’ve put your manuscript through the rigors of peer critique and revision and you think you’re ready to start querying agents, check out this scrappy little website. Once you create a free account, you can browse a directory of agents, read about what each is looking for, find contact info, and connect with other brave querying souls like yourself."),
    ]
    cards = "".join(
        f'<div class="resource rv"><h3>' + (f'<a href="{h}" target="_blank" rel="noopener">{t} {EXT}</a>' if h else t) + f'</h3><p>{p}</p></div>'
        for t, h, p in res)
    lede = "Are you interested in writing children’s books? Awesome! I was once right where you are, excited about the idea of writing a book but not sure where to begin. Below are a few resources to get you started."
    return f"""{page_hero("How to Become an Author", lede, crumb_html=crumb("About", "about.html"))}
  <section class="wrap sec pt0">
    <div class="feature" style="align-items:start">
      <div><div class="resources">{cards}</div><p class="rv" style="font:600 30px/1 var(--hand);color:var(--rust);margin:26px 0 0">Good luck!</p></div>
      <div class="feature-img rv" style="position:sticky;top:110px"><img src="img/12967392_10153457014323344_1870109107206466787_o-1.jpg" width="1400" height="1400" alt="" loading="lazy" style="aspect-ratio:1"></div>
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
    ("KnittingRaccoonMother_Child.jpg", 1500, 1018, "childrens character", "Oil pastels and graphite", "Children’s Illustration 1", ["Children’s illustration", "Character design"], "Illustration of a raccoon mother and child knitting, drawing in oil pastels"),
    ("RollerskatingOwl.jpg", 795, 1050, "childrens character", "Mixed media", "Mixed media", ["Children’s illustration", "Character design"], "Rollerskating owl created with mixed media"),
    ("ChameleonsKnitting.jpg", 1050, 755, "character childrens", "Oil pastel, acrylic gouache and colored pencil", "Oil pastel, acrylic gouache and colored pencil", ["Children’s illustration", "Character design"], "Oil pastel, acrylic gouache and colored pencil"),
    ("BlueWhale.jpg", 1200, 908, "editorial", "Oil pastel, acrylic gouache and colored pencil", "Oil pastel, acrylic gouache and colored pencil", ["Editorial"], "A blue whale"),
    ("RaccoonKnittingSocks.jpg", 765, 1050, "character childrens", "Oil pastel, acrylic gouache and colored pencil", "Oil pastel, acrylic gouache and colored pencil", ["Character design", "Children’s illustration"], "Raccoon knitting socks"),
    ("Minneapolis_oilcrayons.jpg", 1050, 790, "editorial", "Downtown Minneapolis in oil pastel", "Downtown Minneapolis in oil pastel", ["Editorial"], "Downtown Minneapolis in oil pastel"),
    ("Moths_oilpastel.jpg", 1050, 793, "editorial sketchbook", "Spotted lanternflies", "Spotted lanternflies in oil pastel", ["Editorial", "Sketchbook"], "Spotted lanternflies in oil pastel"),
    ("MCADFigureDrawing1.jpg", 1050, 761, "figure sketchbook", "Figure drawing", "Figure in oil pastel", ["Sketchbook", "Figure Drawing"], "Figure in oil pastel"),
    ("KnittingCrab_oilpastel.jpg", 1400, 1075, "character childrens editorial", "Oil pastel", "Oil pastels and acrylic gouache", ["Character design", "Children’s illustration", "Editorial"], "Knitting crab in oil pastel"),
    ("BabyDeer_oilpastel.jpg", 750, 1060, "childrens", "Title of piece", "Title of piece", ["Children’s Illustration"], "Baby deer in oil pastel"),
    ("MCADFigureDrawing2.jpg", 1050, 771, "figure", "Oil pastel", "Oil pastel", ["Figure drawing"], "Figure drawing in oil pastel"),
    ("KoiatComo.jpg", 1019, 848, "sketchbook", "Koi fish", "Oil pastel in sketchbook", ["Sketchbook"], "Sketchbook page of koi fish in oil pastel"),
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
