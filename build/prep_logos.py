"""Turn Stephanie's partner logos into matching one-color PNGs for the site (img/logo-*, flat: her host uploads files, not folders).

Each logo is trimmed to its edges, turned grayscale, stretched so its darkest ink is near-black,
and recolored to the site's ink color on a transparent background, so they all sit evenly on
the paper color. Needs Pillow (the system Python's copy is Intel-only), so run it from a venv:
    python3 -m venv /tmp/pil && /tmp/pil/bin/pip install pillow && /tmp/pil/bin/python build/prep_logos.py
"""
import os

from PIL import Image, ImageOps

SRC = os.path.expanduser("~/Downloads/Stephanie-Watson.com assets/Partner logos")
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "img")
INK = (42, 37, 33)       # --ink
PAPER_CUTOFF = 240       # lighter than this counts as background
MAX_H = 240              # 2x the largest display height

LOGOS = {
    "ASI logo.png": "asi.png", "BBY-logo-white-background.jpeg": "best-buy.png", "Face it logo_bw.webp": "face-it.png",
    "Hennepin County Library.png": "hennepin-county-library.png", "Loft logo_large.png": "loft.png",
    "MN_State_Fair_Logo.jpg": "mn-state-fair.png", "Mall of America Logo.jpg": "mall-of-america.png",
    "Seward Montessori logo.png": "seward-montessori.png", "The Musicant Group logo.webp": "musicant-group.png",
    "UST logo.png": "st-thomas.png",
    "ramsey county library.png": "ramsey-county-library.png", "mps logo.png": "mps.png",
    "st paul saints.png": "st-paul-saints.png",
}


def darkest(gray):
    """The value 2% of the way into the logo's ink, so one stray dark pixel doesn't set the scale."""
    hist = gray.histogram()
    total, acc = sum(hist[:PAPER_CUTOFF]), 0
    for v in range(PAPER_CUTOFF):
        acc += hist[v]
        if acc >= total * 0.02:
            return v
    return 0


def convert(src, dst):
    im = Image.open(src).convert("RGBA")
    flat = Image.new("RGBA", im.size, (255, 255, 255, 255))
    flat.alpha_composite(im)
    gray = ImageOps.grayscale(flat.convert("RGB"))
    gray = gray.crop(gray.point(lambda v: 255 if v < PAPER_CUTOFF - 5 else 0).getbbox())
    span = max(1, PAPER_CUTOFF - darkest(gray))
    alpha = gray.point(lambda v: 0 if v >= PAPER_CUTOFF else min(255, round((PAPER_CUTOFF - v) / span * 255)))
    out = Image.new("RGBA", gray.size, INK + (0,))
    out.putalpha(alpha)
    if out.height > MAX_H:
        out = out.resize((round(out.width * MAX_H / out.height), MAX_H), Image.LANCZOS)
    out.save(dst, optimize=True)
    return out.size


# She picked these two as SVG wordmarks. They're vector, so recolor them to ink rather than rasterize.
SVG_LOGOS = {
    "Mia_Isolated_Wordmark_100K.svg": ("mia.svg", lambda s: s.replace("<svg ", '<svg fill="#2a2521" ', 1)),  # unfilled = black
    "hamline university.svg": ("hamline.svg", lambda s: s.replace("#FFFFFF", "#2a2521")),               # was white-on-dark
}


def main():
    os.makedirs(OUT, exist_ok=True)  # files are written as logo-<name>
    for src, (name, recolor) in SVG_LOGOS.items():
        with open(os.path.join(SRC, src), encoding="utf-8") as f:
            svg = recolor(f.read())
        with open(os.path.join(OUT, "logo-" + name), "w", encoding="utf-8") as f:
            f.write(svg)
        print(f"{name:32s} (svg)")
    for src, name in LOGOS.items():
        w, h = convert(os.path.join(SRC, src), os.path.join(OUT, "logo-" + name))
        print(f"{name:32s} {w}x{h}")


if __name__ == "__main__":
    main()
