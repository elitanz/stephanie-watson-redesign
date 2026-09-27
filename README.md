# Stephanie Watson — website redesign preview

**Live preview: https://elitanz.github.io/stephanie-watson-redesign/**

A redesign mockup of [stephanie-watson.com](https://www.stephanie-watson.com/), the site of Minneapolis children's book author and illustrator Stephanie Watson. It's a preview for her to look at, not the live site.

- All 20 pages from her current site, with her text, images, and buttons kept.
- Fixes the mobile layout: one clean header with a full-screen menu, book covers two across, a portfolio that fits the screen, and nothing that scrolls sideways.
- The contact forms are preview-only and don't send messages.
- Search engines are asked not to list this copy (`noindex`), so it never competes with her real site.

## Rebuild

```bash
python3 build/build.py
```

The pages are generated from `build/` (shared layout in `chrome.py`, page content in `books.py` and `other.py`). The build checks that every link, image and file resolves.
