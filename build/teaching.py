"""Teaching section: the Teaching landing page and its two pages, For Kids and For Adults.

This replaces the old "Author & Illustrator Visits" group (School Visits, Library Storytimes,
Other Presentations, Testimonials). Stephanie is writing the new copy for this section herself,
so every sentence here is her published text moved over verbatim from those old pages.
`bucket()` marks a section she still has to write — never fill one with invented copy.
"""
from chrome import ARROW, crumb, page_hero, contact_section
from other import NEWSLETTER

TEACHING_CRUMB = crumb("Teaching", "teaching.html")


def quotes(items, cls="quote-grid"):
    cards = "".join(f'<blockquote class="quote rv"><p>{q}</p><cite>{c}</cite></blockquote>' for q, c in items)
    return f'<div class="{cls}">{cards}</div>'


def feature(img, w, h, body, flip=False, alt=""):
    f = " flip" if flip else ""
    return f"""<div class="feature{f}">
      <div class="feature-img rv"><img src="{img}" width="{w}" height="{h}" alt="{alt}" loading="lazy"></div>
      <div class="rv">{body}</div>
    </div>"""


def bucket(title, what):
    """A clearly marked empty section for Stephanie to write (a note to her, not site copy)."""
    return f"""<div class="bucket rv">
      <span class="bucket-tag">For Stephanie to write</span>
      <h3 class="h3">{title}</h3>
      <p>{what}</p>
    </div>"""


def sec_head(kicker, title, lede=""):
    kicker_html = f'<span class="eyebrow">{kicker}</span>' if kicker else ""
    lede_html = f'<p class="muted sec-lede">{lede}</p>' if lede else ""
    return f'<div class="sec-head left rv">{kicker_html}<h2>{title}</h2>{lede_html}</div>'


# ---------------------------------------------------------------- landing
def teaching():
    paths = [
        ("For Kids", "School visits · Library storytimes", "img/Stephanie-Watson-library-storytime-1.jpg", 600, 400,
         "Choose a ready-made talk or workshop, designed for both large and small groups. You can also request a custom presentation.",
         "for-kids.html"),
        ("For Adults", "Workshops · Keynotes · Festivals", "img/StephanieWatsonAuthorTwinCities-scaled.jpeg", 1400, 933,
         "Need a keynote speaker for your special event? Or a writing workshop for adults? I’d love to work with you.",
         "for-adults.html"),
    ]
    cards = "".join(f"""<article class="option rv"><a class="option-img" href="{href}" tabindex="-1" aria-hidden="true"><img src="{src}" width="{w}" height="{h}" alt="" loading="lazy"></a>
      <div class="body"><span class="eyebrow">{sub}</span><h2 class="h2-sm">{t}</h2><p>{p}</p><a class="btn btn-fill" href="{href}">{t} {ARROW}</a></div></article>"""
                    for t, sub, src, w, h, p, href in paths)
    lede = ("Looking for a children’s book creator to visit your classroom, library or at a special event? Whether your group is "
            "small or large, comprised of children or adults, I can create a presentation or workshop that’s just the right fit.")
    return f"""{page_hero("Teaching", lede)}
  <section class="wrap sec pt0">
    <div class="options two">{cards}</div>
  </section>
  {contact_section("Want to inquire about my rates, or are you ready to schedule a virtual or in-person visit? Please get in touch.")}"""


# ---------------------------------------------------------------- for kids
def _program(name, text, grades, size, length):
    return f"""<article class="program rv"><h3>{name}</h3><p>{text}</p>
      <ul class="specs"><li>Grade levels: {grades}</li><li>Group size: {size}</li><li>Length: {length}</li></ul></article>"""


def _school_groups():
    pres = _program("10 Things", "All writers rely on tools and tricks to help them create good stories. In this dynamic presentation, you’ll learn the 10 things that have helped me most as a writer. If you’re interested in becoming a writer, these things can help you, too!",
                    "2 – 8", "30 – 1,000 students", "45 – 60 min") + \
        _program("The Picture Book Process", 'In this highly visual presentation, I share each step of the process, including my rough drafts, editing the text, as well as the illustrator’s initial sketches and final artwork. Choose either <a href="best-friends-in-the-universe.html">Best Friends in the Universe</a> or <a href="behold-a-baby.html">Behold! A Baby</a>. Followed by a Q&amp;A.',
                 "K – 8", "30 – 1,000 students", "45 – 60 min")
    work = _program("Raise the Stakes", "To grab readers’ attention and keep them hooked till the last page, your story needs high stakes. In this workshop, we’ll do fun group activities and writing exercises to practice upping the ante.",
                    "2 – 8", "30 – 60 students", "45 – 60 min") + \
        _program("Story Jars", "Do you ever sit down to start a story and find yourself staring at the blank page? Writing prompts, also known as story starters, can be a great way to get the ball rolling. As a group, we’ll create Story Jars–writing prompt tools that can remain in the classroom for future use.",
                 "2 – 8", "30 – 60 students", "45 – 60 min")
    return f"""<div class="group">
      <div class="group-head">
        <div class="rv"><span class="kicker">for 30 or more people</span><h3 class="h2-sm">Presentations</h3></div>
        <img class="rv" src="img/minneapolis-author-school-visit-e1496944139765.jpeg" width="350" height="341" alt="" loading="lazy" style="aspect-ratio:16/10">
      </div>
      <div class="programs">{pres}</div>
    </div>
    <div class="group">
      <div class="group-head">
        <div class="rv"><span class="kicker">for 10 – 60 people</span><h3 class="h2-sm">Workshops</h3></div>
        <img class="rv" src="img/writing-workshop-minneapolis-minnesota.jpeg" width="500" height="333" alt="" loading="lazy" style="aspect-ratio:16/10">
      </div>
      <div class="programs">{work}</div>
    </div>"""


def for_kids():
    lede = "Want to turbo-charge a writing unit? Looking for a fun way to kick off a read-a-thon or book fair? Considering hiring me for a school presentation or workshop! Browse my ready-made workshops and presentations below, or request a custom presentation. To ask about fees and availability, please get in touch."
    library_lede = "Looking for a special program for your library, either virtual or in-person? Explore the options below. If you don’t see what you need, please contact me. I’m always glad to work with you to customize a storytime presentation or writing workshop."
    library = feature("img/Stephanie-Watson-library-storytime-1.jpg", 600, 400,
                      '<h3 class="h2-sm">Family Storytime</h3><p>My standard 30-minute presentation is designed for ages 0 – 5 (and their adults). Features <a class="link" href="behold-a-baby.html">Behold! A Baby</a> and <a class="link" href="the-wee-hours.html">The Wee Hours</a>, and includes interactive games, songs and puppets! Aligns with early literacy learning objectives, with elements that foster vocabulary, letter knowledge, phonological awareness, print motivation and numeracy.</p>') + \
        feature("img/IMG_2944_v2.jpg", 1080, 656,
                '<h3 class="h2-sm">Presentation for grades K – 8</h3><p>In this highly visual talk for older kids, we explore the writing and publishing process. I share images of my early drafts, my desk and illustrator sketches. I talk about how I create a book, from initial idea to finished product, and invite kids to consider creating their own stories. This type of presentation typically lasts 30 – 60 minutes.</p>', flip=True)
    q = quotes([
        ("Stephanie spent two days with the pre-k to fifth grade kids during the Blake LitFest. She had fun, age-appropriate interactive presentations, and her stories kept the kids engaged and asking questions. We loved working with Stephanie!", "- Jacquelyn Fletcher-Johnson, The Blake School LitFest Co-Chair"),
        ("My class was thrilled to have Stephanie come for an author visit to lead a character workshop. She helped the students create interesting characters by asking probing questions, which led to mapping out exciting individual stories. At the end of the workshop we had time for a Q&amp;A session and autographs!", "- Rayna Lechelt, 3rd grade teacher, Prairie View Elementary, Eden Prairie, MN"),
        ("We loved hearing the process of making a book and listening to Stephanie’s stories.", "- Erin Geary, 2nd grade teacher, Lakeview Public School, Cottonwood, MN"),
        ("I appreciated that Stephanie spoke at the students’ level. She had great ideas for writing that were just right for my students. I also liked that she allowed time for questions.", "- Mary Roe, 4th grade teacher, Lakeview Public School, Cottonwood, MN"),
    ], cls="quote-grid two")
    return f"""{page_hero("For Kids", lede, crumb_html=TEACHING_CRUMB, kicker="School &amp; library visits")}
  <section class="wrap sec pt0" id="school">
    {sec_head("", "School Visits")}
    {_school_groups()}
  </section>
  <section class="wrap sec pt0" id="library">
    {sec_head("", "Library Storytimes &amp; Workshops", library_lede)}
    {library}
  </section>
  <section class="sec testis" id="testimonials"><div class="wrap"><div class="sec-head rv"><h2>Testimonials</h2></div>{q}</div></section>
  {NEWSLETTER}
  {contact_section("Want to schedule a visit or workshop, or to inquire about fees? I’d love to hear from you.")}"""


# ---------------------------------------------------------------- for adults
def for_adults():
    lede = "Looking for a virtual or in-person speaker for an upcoming event? I enjoy sharing my ideas about writing and creativity with people of all ages. I’ve delivered author keynote speeches and presentations at conferences, book festivals, luncheons, museums, baseball games–even on an old-time trolley car. If you don’t see what you’re looking for in the list below, I’m happy to customize a presentation for your event. Please contact me for more info!"
    classes = feature("img/Writing-Hand.jpeg", 428, 222,
                      '<h3 class="h2-sm">Adult Writing Workshops</h3><p>I’d love to offer a writing workshop for adults in your community. These are typically one- to two-hour standalone sessions, but we can also do a series. You choose the focus: idea generation, character development, revision, or another writing topic. Each participant will leave the class with the beginnings of a brand new story!</p>') + \
        feature("img/12743652_960442657380772_3228764945647219935_n-1.jpg", 960, 736,
                '<h3 class="h2-sm">Keynote Speeches</h3><p>I love sharing the story of my creative journey, and hope that audience members leave feeling inspired to exercise their creativity, too. To create a keynote address, I start by learning more about your organization and your goals for the day. I then craft my talk to suit your audience and preferred length (usually 30 – 60 minutes).</p>', flip=True) + \
        feature("img/alphabet-forest-minnesota-state-fair-big-but-short.jpeg", 450, 371,
                """<h3 class="h2-sm">Festivals &amp; Fairs</h3><p>I’d be delighted to present at your upcoming book festival or fair. I’ve been a featured author at:</p>
                <ul><li>The Festival of Children’s Literature at the Anderson Center in Redwing, MN</li><li>The Twin Cities Book Festival</li><li>The Alphabet Forest at the Minnesota State Fair</li><li>LitFest at the Blake School in Minneapolis, MN</li><li>St. Paul Saints games</li><li>Rhythm &amp; Words Festival in Burnsville, MN</li></ul>
                <p>I’d love to come celebrate with you, too!</p>""")
    q = quotes([
        ("Stephanie made her presentation interesting for everyone in the multi-generational audience. across generations of people, and she made the desire to write an aspiration for the young people who were listening to her.", "- Zylpha Gregorson, Emcee of Mother-Daughter-Sister-Friend Breakfast, Central Lutheran Church, Minneapolis"),
        ("Thanks for all the effort you put into the presentation--it was very fun!", "- Nicole Brinkman, Children's Librarian at Ramsey County Library - Roseville, MN"),
        ("I liked the combination of Stephanie's visual presentation with her expressive voice.", "- Ann Oyen, Organizer for Mother-Daughter-Sister-Friend Breakfast, Central Lutheran Church, Minneapolis"),
    ])
    return f"""{page_hero("For Adults", lede, crumb_html=TEACHING_CRUMB, kicker="Workshops &amp; presentations")}
  <section class="wrap sec pt0" id="classes">
    {sec_head("Classes", "Workshops &amp; Presentations")}
    {classes}
    <div class="bucket-row">{bucket("More classes", "The other kinds of classes Stephanie teaches for adults: a short description of each, who it’s for, and how long it runs.")}</div>
  </section>
  <section class="wrap sec pt0" id="partnerships">
    {sec_head("Ongoing collaborations", "Partnerships")}
    {bucket("Partnerships", "The organizations Stephanie teaches with, and the classes she offers through each one.")}
  </section>
  <section class="wrap sec pt0" id="past-classes">
    {sec_head("Past classes", "In the Studio")}
    {bucket("Photos &amp; highlights from past classes", "Stephanie’s newer photos from classes she has taught, with a line about each one. Send the photos over and they’ll become a gallery here.")}
  </section>
  <section class="sec testis" id="testimonials"><div class="wrap"><div class="sec-head rv"><h2>Testimonials</h2></div>{q}</div></section>
  {NEWSLETTER}
  {contact_section("To inquire about fees and availability, please write to me. I look forward to hearing from you.")}"""
