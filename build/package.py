#!/usr/bin/env python3
"""Zip the finished site for upload to her web host (IONOS).

Run `python3 build/build.py` first. Produces dist/swatson-v3-<date>.zip containing one folder,
swatson-v3/, with ONLY what the web server needs: pages, redirect pages, .htaccess, robots.txt,
assets/, img/, files/. Images are stored, not recompressed, so they are byte-identical to the
preview. Build tools, the crawl of her old site, and git history are left out.
"""
import datetime
import os
import zipfile

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FOLDER = "swatson-v3"  # the folder name her launch notes suggest (not swatson-v2: WordPress lives there)
SKIP_DIRS = {".git", "build", "_crawl", "dist", "__pycache__"}
SKIP_FILES = {".gitignore", "README.md", ".DS_Store"}
STORED = {".jpg", ".jpeg", ".png", ".pdf", ".webp", ".gif"}  # already compressed; zip them as-is


def site_files():
    for root, dirs, files in os.walk(SITE):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
        for name in sorted(files):
            if name in SKIP_FILES or name.endswith(".tmp"):
                continue
            path = os.path.join(root, name)
            yield path, os.path.relpath(path, SITE)


def main():
    for must in ("index.html", ".htaccess", "robots.txt", "assets/site.css"):
        if not os.path.exists(os.path.join(SITE, must)):
            raise SystemExit(f"missing {must}: run python3 build/build.py first")
    os.makedirs(os.path.join(SITE, "dist"), exist_ok=True)
    out = os.path.join(SITE, "dist", f"{FOLDER}-{datetime.date.today().isoformat()}.zip")
    count = 0
    with zipfile.ZipFile(out + ".tmp", "w") as z:
        for path, rel in site_files():
            kind = zipfile.ZIP_STORED if os.path.splitext(rel)[1].lower() in STORED else zipfile.ZIP_DEFLATED
            z.write(path, f"{FOLDER}/{rel}", compress_type=kind)
            count += 1
    os.replace(out + ".tmp", out)
    print(f"{count} files -> {out} ({os.path.getsize(out) / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()
