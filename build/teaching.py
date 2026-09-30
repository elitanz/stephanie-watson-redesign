"""Teaching & Speaking section: the landing page and its two pages, For Kids and For Adults.

Every word of copy here is Stephanie's, taken verbatim from her content map
(stephanie-watson-website-content-map-v4.docx, Sept 29, 2026). Don't reword it.
Where she left something blank (e.g. photo captions), leave it out; never invent copy.
"""
from chrome import ARROW, crumb, contact_section

TEACHING_CRUMB = crumb("Teaching &amp; Speaking", "teaching.html")
CONNECT = "Let’s connect"

# Partner logos (img/logos/). Which logos go where is Eli's pick; Stephanie hasn't set an order yet.
LOGOS = {
    "asi": ("asi.png", 522, 240, "American Swedish Institute"),
    "mps": ("mps.png", 800, 122, "Minneapolis Public Schools"),
    "hennepin": ("hennepin-county-library.png", 239, 240, "Hennepin County Library"),
    "ramsey": ("ramsey-county-library.png", 227, 240, "Ramsey County Library"),
    "mia": ("mia.png", 476, 240, "Minneapolis Institute of Art"),
    "loft": ("loft.png", 349, 176, "The Loft Literary Center"),
    "fair": ("mn-state-fair.png", 416, 240, "Minnesota State Fair"),
    "saints": ("st-paul-saints.png", 184, 240, "St. Paul Saints"),
    "bestbuy": ("best-buy.png", 410, 240, "Best Buy"),
    "faceit": ("face-it.png", 153, 179, "Face It Foundation"),
    "hamline": ("hamline.png", 268, 240, "Hamline University"),
    "stthomas": ("st-thomas.png", 700, 140, "University of St. Thomas"),
    "seward": ("seward-montessori.png", 225, 240, "Seward Montessori"),
    "musicant": ("musicant-group.png", 677, 240, "The Musicant Group"),
    "moa": ("mall-of-america.png", 426, 240, "Mall of America"),
}
TEACHING_LOGOS = ["asi", "mps", "hennepin", "ramsey", "mia", "loft", "fair", "saints", "bestbuy", "faceit", "hamline", "stthomas"]
KIDS_LOGOS = ["mps", "asi", "hennepin", "seward", "fair"]
ADULT_LOGOS = ["mia", "loft", "bestbuy", "faceit", "musicant", "hamline"]

# Shared testimonials (her wording; she uses some on more than one page)
RAMGREN = ("It is a joy to work with Stephanie Watson and the residency she does with my 1st graders. She brings a level of enthusiasm and engagement that is amazing! She purposefully seeks input in her lessons from all of my students and makes connections with them in a very short time. Students feel seen by her and then are more invested in their work with her. She is so creative and draws out creativity from my students too.",
           "—Rebecca Ramgren, first-grade teacher at Bancroft Elementary in Minneapolis")


def quotes(items, cls="quote-grid"):
    cards = "".join(f'<blockquote class="quote rv"><p>{q}</p><cite>{c}</cite></blockquote>' for q, c in items)
    return f'<div class="{cls}">{cards}</div>'


def testimonials(items, cls="quote-grid"):
    return f"""<section class="sec testis" id="testimonials"><div class="wrap">
    <div class="sec-head rv"><h2>Testimonials</h2></div>
    {quotes(items, cls)}</div></section>"""


def sec_head(kicker, title, lede="", center=False):
    kicker_html = f'<span class="eyebrow">{kicker}</span>' if kicker else ""
    lede_html = f'<p class="muted sec-lede">{lede}</p>' if lede else ""
    align = "" if center else " left"
    return f'<div class="sec-head{align} rv">{kicker_html}<h2>{title}</h2>{lede_html}</div>'


LOGO_AREA = 9000      # every logo gets about the same visual area (px²), so wide and tall ones balance
LOGO_MAX_W, LOGO_MAX_H = 200, 84


def logo_width(w, h):
    aspect = w / h
    return round(min((LOGO_AREA * aspect) ** 0.5, LOGO_MAX_W, LOGO_MAX_H * aspect))


def logo_row(keys, cls):
    items = "".join(f'<li><img src="img/logos/{f}" width="{w}" height="{h}" alt="{alt}" loading="lazy" style="--w:{logo_width(w, h)}px"></li>'
                    for f, w, h, alt in (LOGOS[k] for k in keys))
    return f'<ul class="logos {cls} rv">{items}</ul>'


def partners(keys, title, cls):
    return f"""<section class="wrap sec-sm partners">
    {sec_head("Partners", title, center=True)}
    {logo_row(keys, cls)}
  </section>"""


def hero_split(kicker, h1, lede, img, w, h, alt="", crumb_html=""):
    kicker_html = f'<span class="eyebrow">{kicker}</span>' if kicker else ""
    return f"""<section class="page-hero wrap hero-split">
    <div class="rv">{crumb_html}{kicker_html}<h1>{h1}</h1><p class="lede">{lede}</p></div>
    <div class="hero-photo rv"><img src="{img}" width="{w}" height="{h}" alt="{alt}" fetchpriority="high"></div>
  </section>"""


def photo_grid(photos):
    """Photos that open larger on click. `photos` = (file, w, h). She hasn't written captions yet."""
    items = "".join(f'<li><a href="img/{f}" data-group><img src="img/{f}" width="{w}" height="{h}" alt="" loading="lazy"></a></li>'
                    for f, w, h in photos)
    return f'<ul class="photo-grid rv">{items}</ul>'


# ---------------------------------------------------------------- landing
def teaching():
    intro = ("One of the best parts of my job is sharing what I’ve learned as an author and illustrator, and inspiring people to make "
             "their own stories and art. I teach writing and drawing to kids and adults, in schools, libraries, museums and other "
             "community spaces. Through presentations and keynote speeches, I offer a window into the artistic process. Explore the "
             "ready-made options below, and if you have something else in mind, I'm game to customize a workshop or presentation for your group.")
    paths = [
        ("School &amp; Library Visits", "For Kids", "img/teaching_kids-card_library-visit.jpg", 1600, 1066,
         "Supercharge a writing unit or kick off a literacy event with an author/illustrator visit or workshop. My teaching is built "
         "around the belief that every kid is a natural artist and storyteller.",
         "See options for kids", "for-kids.html"),
        ("Workshops &amp; Presentations", "For Adults", "img/teaching_adults-card_confab-drawing-games.jpg", 1600, 1200,
         "I love leading drawing and writing workshops for adults at libraries, conferences, and creative organizations. Whether you've "
         "been making art for years or haven't picked up a pencil since third grade, my teaching aims to empower and inspire.",
         "See options for adults", "for-adults.html"),
    ]
    cards = "".join(f"""<article class="option rv"><a class="option-img" href="{href}" tabindex="-1" aria-hidden="true"><img src="{src}" width="{w}" height="{h}" alt="" loading="lazy"></a>
      <div class="body"><span class="eyebrow">{kick}</span><h2 class="h2-sm">{t}</h2><p>{p}</p><a class="btn btn-fill" href="{href}">{btn} {ARROW}</a></div></article>"""
                    for kick, t, src, w, h, p, btn, href in paths)
    q = [
        RAMGREN,
        ("I appreciated that Stephanie spoke at the students' level. She had great ideas for writing that were just right for my students.",
         "—Mary Roe, 4th grade teacher at Lakeview Public School, Cottonwood, MN"),
        ("Stephanie's teaching sparkles, reflecting not only her creativity and professionalism, but also her flexibility, her receptivity to feedback, and her skills of observation. Her varied approaches to creativity in her workshops are rigorous--and playful and supportive.",
         "—Susan Marie Swanson, Caldecott-winning author and arts educator"),
        ("Stephanie does a marvelous job of giving each student the opportunity to take the lead in developing their own ideas. She meets kids where they are, celebrates their ideas, and emphasizes that storytelling should be fun while helping students build confidence and strengthen their storytelling skills.",
         "—Lindsey Tscherne, Youth &amp; Family Programs Manager, American Swedish Institute"),
    ]
    return f"""{hero_split("", "Teaching &amp; Speaking", intro, "img/teaching_intro_comics-workshop.jpg", 1200, 1019)}
  <section class="wrap sec pt0">
    <div class="options two">{cards}</div>
  </section>
  {partners(TEACHING_LOGOS, "Organizations I’ve worked with", "grid")}
  {testimonials(q, "quote-grid two")}
  {contact_section("Interested in a workshop or school visit? I’d love to hear what you have in mind and chat about options.", CONNECT)}"""


# ---------------------------------------------------------------- for kids
def _program(name, text, grades, size, length):
    return f"""<article class="program rv"><h3>{name}</h3><p>{text}</p>
      <ul class="specs"><li>Grade levels: {grades}</li><li>Group size: {size}</li><li>Length: {length}</li></ul></article>"""


def _one_time_programs():
    presentations = _program("10 Things", "All writers rely on tools and tricks to help them create good stories. In this dynamic presentation, you’ll learn the 10 things that have helped me most as a writer. If you’re interested in becoming a writer, these things can help you, too!",
                             "2–8", "30–1,000 students", "45–60 min") + \
        _program("The Picture Book Process", 'In this highly visual presentation, I share each step of the process, including my rough drafts, editing the text, as well as the illustrator’s initial sketches and final artwork. Choose either <a href="best-friends-in-the-universe.html">Best Friends in the Universe</a> or <a href="behold-a-baby.html">Behold! A Baby</a>. Followed by a Q&amp;A.',
                 "K–8", "30–1,000 students", "45–60 min")
    workshops = _program("Raise the Stakes", "To grab readers’ attention and keep them hooked till the last page, your story needs high stakes. In this workshop, we’ll do fun group activities and writing exercises to practice upping the ante.",
                         "2–8", "30–60 students", "45–60 min") + \
        _program("Story Jars", "Do you ever sit down to start a story and find yourself staring at the blank page? Writing prompts, also known as story starters, can be a great way to get the ball rolling. As a group, we’ll create Story Jars–writing prompt tools that can remain in the classroom for future use.",
                 "2–8", "30–60 students", "45–60 min")
    return f"""<div class="program-cols">
      <div class="program-col"><div class="col-head rv"><h3 class="h2-sm">Presentations</h3><span class="kicker">(for 30–1,000 people)</span></div>{presentations}</div>
      <div class="program-col"><div class="col-head rv"><h3 class="h2-sm">Workshops</h3><span class="kicker">(for 10–60 people)</span></div>{workshops}</div>
    </div>"""


def _residencies():
    examples = [
        ("One week, Monday–Friday",
         "I lead an annual five-day writing and drawing workshop with first graders at Bancroft Elementary. Through this partnership with Minneapolis Public Schools and the American Swedish Institute, we develop original comic strip characters, settings, and storylines. At the end of the residency, each child has created an original comic strip, which we celebrate at a publishing party with caregivers and teachers."),
        ("Twice a week for six weeks",
         "During summer school at Highland Park Elementary, I led a 6-week Comics Lab with 4th and 5th graders. Twice a week, we experimented with different drawing techniques, developed original characters and used them to create comic strips, and collaborated on a class character. We practiced drawing expressive faces and bodies in motion. At the end of the residency, student work was publicly exhibited in the Picture Book Parade at the Minneapolis Farmers Market."),
    ]
    cards = "".join(f'<article class="residency rv"><span class="kicker">{when}</span><p>{text}</p></article>' for when, text in examples)
    return f"""<section class="sec residencies" id="residencies"><div class="wrap">
    {sec_head("Go deeper", "Residencies", "A multi-session residency gives your group a chance to explore ideas, build skills, and create finished work. No two residencies are the same, but here are two recent examples:")}
    <div class="residency-grid">{cards}</div>
    <div class="residency-end rv"><p>Every residency is customized around your group and your goals. Tell me what you have in mind, and we'll figure out the shape that fits!</p>
      <a class="btn btn-fill" href="#contact">Chat about a residency {ARROW}</a></div>
  </div></section>"""


KIDS_PAST_EVENTS = [
    ("kids_past_storytime-red-tent.jpg", 1200, 1600),
    ("kids_past_mall-of-america-reading.jpg", 1440, 1440),
    ("kids_past_comics-lab.jpg", 1600, 1287),
    ("kids_past_saints-game.jpg", 1600, 898),
    ("kids_past_toddler-storytime-moa.jpg", 1440, 1440),
    ("kids_past_alphabet-forest.jpg", 1200, 1600),
]


def for_kids():
    intro = ("In my school and library visits for kids, I offer a peek into my messy, colorful creative process and share how books are made. "
             "We can also take a deeper dive in a workshop, to give participants a chance to develop their own characters and stories. "
             "Choose from the options below, or reach out to discuss a customized visit.")
    q = [
        ("My class was thrilled to have Stephanie come for an author visit to lead a character workshop. She helped the students create interesting characters by asking probing questions, which led to mapping out exciting individual stories. At the end of the workshop we had time for a Q&amp;A session and autographs!",
         "—Rayna Lechelt, 3rd grade teacher at Prairie View Elementary, Eden Prairie, MN"),
        RAMGREN,
        ("Stephanie Watson spent two days with the pre-K to fifth grade kids during the Blake LitFest. She had fun, age-appropriate interactive presentations, and her stories kept the kids engaged and asking questions. We loved working with Stephanie!",
         "—Jacquelyn Fletcher-Johnson, The Blake School LitFest Co-Chair"),
    ]
    return f"""<section class="page-hero wrap"><div class="rv">{TEACHING_CRUMB}<span class="eyebrow">School &amp; Library Visits</span><h1>For Kids</h1><p class="lede">{intro}</p></div></section>
  <section class="wrap sec pt0" id="programs">
    {sec_head("", "One-time programs")}
    {_one_time_programs()}
  </section>
  {_residencies()}
  {partners(KIDS_LOGOS, "A few places I’ve taught and presented", "strip")}
  {testimonials(q)}
  <section class="wrap sec" id="past-events">
    {sec_head("", "Past Events")}
    {photo_grid(KIDS_PAST_EVENTS)}
  </section>
  {contact_section("Interested in a visit, workshop, or residency? Let me know what you have in mind!", CONNECT)}"""


# ---------------------------------------------------------------- for adults
def _offer(title, body, examples, fmt, label="", button=""):
    lbl = f'<p class="ex-label">{label}</p>' if label else ""
    ex = "".join(f"<li>{e}</li>" for e in examples)
    btn = f'<a class="btn btn-line btn-sm" href="#contact">{button} {ARROW}</a>' if button else ""
    return f"""<article class="offer rv"><h3>{title}</h3><p>{body}</p>{lbl}<ul class="examples">{ex}</ul>
      <p class="format">{fmt}</p>{btn}</article>"""


ADULT_PHOTOS = [
    ("adults_grid_drawing-games-room.jpg", 1600, 1200),
    ("adults_grid_musicant-workshop.jpg", 1600, 1199),
    ("adults_grid_author-talk.jpg", 1600, 1066),
    ("adults_grid_creative-workshop.jpg", 1427, 1062),
    ("adults_grid_drawing-workshop.jpg", 1600, 1178),
    ("adults_grid_mcba-parts-of-a-whole.jpg", 960, 960),
]


def for_adults():
    intro = ("I teach drawing and writing to adults through one-time workshops and multi-week sessions. I also give talks about bookmaking "
             "and creativity at libraries, conferences, and arts organizations. I've spoken at book festivals, luncheons, museums and "
             "baseball games—even on an old-time trolley car. Whatever your group or event looks like, I can build something that fits.")
    offers = _offer("Standalone workshops",
                    "One-time, hands-on sessions for libraries, conferences and organizations. You choose the focus: drawing, idea generation, character development, revision or another topic. Everyone leaves having made something new.",
                    ["Drawing Games workshop at Best Buy", "Half-day picture book workshop at the Loft Literary Center"],
                    "Typical format: 1–3 hours. In person or virtual.") + \
        _offer("Multi-session workshops",
               "Courses that give adults time to build a real creative practice, one session at a time.",
               ["<strong>Sketching Fashion at Minneapolis Institute of Art.</strong> Five weeks, for adults 55 and up, using Mia’s Paris Couture exhibition as a starting point for observational drawing, in the galleries and in the studio.",
                "<strong>Picture Book Dash at The Loft Literary Center.</strong> Eight-week course in picture-book writing, featuring both story craft and interdisciplinary exercises, designed to strengthen and expand creativity.",
                "<strong>Creative Workshop with Face It Foundation.</strong> A five-week class that used writing, drawing, collage, and theater improvisation to help participants cultivate joy and resilience in the face of depression and anxiety."],
               "Typical format: Weekly sessions over 4–8 weeks. In person or virtual.", label="Past workshops:", button="Ask about a class") + \
        _offer("Talks and keynotes",
               "In a speech, I can share my journey as an author and illustrator, and/or turn the focus on the group to offer ideas to nurture a creative practice or career. To create a talk, I start by learning about your organization and your goals for the day, then shape my presentation to fit your audience.",
               ["Featured presenter at the Twin Cities Book Festival",
                "Featured presenter at the Festival of Children’s Literature at the Anderson Center in Red Wing",
                "Keynote speaker at the Mother-Daughter-Sister-Friend Brunch, Minneapolis Area Synod—Central Lutheran Church"],
               "Typical format: 45–60 minutes. In person or virtual.", button="Ask about a talk")
    q = [
        ("Stephanie’s classes are a delight. She’s both honest and reassuring about the challenges of creative work. Better yet, she lures you back into play and shows you how to set your muse free. My first published picture book was born in her class!",
         "—Charlotte Sullivan Wild, author of Love, Violet and The Amazing Idea of You"),
        ("The group improv activities were especially fun, and I felt a sense of belonging and acceptance. Any apprehension or fear I felt before the workshop quickly faded away after we got started.",
         "—Participant in Face It Foundation workshop"),
        ("Stephanie made her presentation interesting for everyone in the multi-generational audience.",
         "—Zylpha Gregorson, Emcee, Mother-Daughter-Sister-Friend Brunch, Minneapolis Area Synod—Central Lutheran Church"),
    ]
    return f"""{hero_split("Workshops &amp; Presentations", "For Adults", intro, "img/adults_intro_drawing-workshop.jpg", 1600, 1066,
                        alt="Stephanie Watson leading a drawing workshop for adults", crumb_html=TEACHING_CRUMB)}
  {partners(ADULT_LOGOS, "A few places I’ve taught and presented", "strip six")}
  <section class="wrap sec" id="offer">
    {sec_head("What I offer", "Workshops &amp; talks")}
    <div class="offers">{offers}</div>
  </section>
  <section class="wrap sec pt0" id="photos">
    {sec_head("Photos", "Recent classes and events")}
    {photo_grid(ADULT_PHOTOS)}
  </section>
  {testimonials(q)}
  {contact_section("Interested in a class, workshop or talk? Tell me about your group and what you have in mind!", CONNECT)}"""
