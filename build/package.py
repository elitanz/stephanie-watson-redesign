#!/usr/bin/env python3
"""Make the LIVE upload for her web host (IONOS) in dist/swatson-v3/ (+ a zip of it).

Run `python3 build/build.py` first. IONOS's Webspace Explorer uploads files, not folders, so the
layout is flat: the .html pages, .htaccess and robots.txt at the top, plus img/, assets/ and files/
with no folders inside them. Only images a page actually uses are included.

Unlike the GitHub preview (which stays hidden from search engines so it never competes with her
real site), this copy is search-visible: the noindex tag is removed from every page and robots.txt
allows everything. Files are copied byte-for-byte; images are never recompressed.
"""
import datetime
import glob
import os
import re
import shutil
import zipfile

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FOLDER = "swatson-v3"  # her launch notes: a NEW folder, not swatson-v2 (WordPress lives there)
OUT = os.path.join(SITE, "dist", FOLDER)
NOINDEX = '<meta name="robots" content="noindex, nofollow">\n'
ROBOTS = "User-agent: *\nDisallow:\n"  # empty Disallow = allow everything
STORED = {".jpg", ".jpeg", ".png", ".pdf", ".webp", ".gif"}  # already compressed


def pages():
    return sorted(os.path.basename(p) for p in glob.glob(os.path.join(SITE, "*.html")))


def used_files(page_names):
    """Every img/, assets/ and files/ path a page or the stylesheet points at."""
    text = "".join(open(os.path.join(SITE, n), encoding="utf-8").read() for n in page_names)
    text += open(os.path.join(SITE, "assets", "site.css"), encoding="utf-8").read()
    found = set(re.findall(r'((?:img|assets|files)/[^"\'\s?#),]+)', text))
    missing = [f for f in found if not os.path.isfile(os.path.join(SITE, f))]
    nested = [f for f in found if f.count("/") > 1]
    if missing or nested:
        raise SystemExit(f"missing: {missing}  nested folders: {nested}")
    return sorted(found)


def live_page(name):
    html = open(os.path.join(SITE, name), encoding="utf-8").read()
    if html.count(NOINDEX) != 1:
        raise SystemExit(f"{name}: expected exactly one noindex tag")
    return html.replace(NOINDEX, "")


def write_checklist(names, files):
    """dist/UPLOAD-CHECKLIST.txt: exactly which folders to create in IONOS and what goes in each."""
    lines = [f"Upload checklist for {FOLDER} (IONOS Webspace Explorer uploads files, not folders)", "",
             f"1. Create the folder {FOLDER}. Upload these {len(names) + 2} files into it:",
             "   .htaccess   (hidden on a Mac: press Cmd+Shift+. in Finder to see it)", "   robots.txt"]
    lines += [f"   {n}" for n in names]
    for i, sub in enumerate(("img", "assets", "files"), start=2):
        inside = [f.split("/", 1)[1] for f in files if f.startswith(sub + "/")]
        lines += ["", f"{i}. Inside {FOLDER}, create the folder {sub}. Upload these {len(inside)} files into it:"]
        lines += [f"   {n}" for n in inside]
    lines += ["", "No other folders. Nothing goes inside img, assets or files except the files listed."]
    with open(os.path.join(SITE, "dist", "UPLOAD-CHECKLIST.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def main():
    names = pages()
    if "index.html" not in names or not os.path.exists(os.path.join(SITE, ".htaccess")):
        raise SystemExit("run python3 build/build.py first")
    shutil.rmtree(OUT, ignore_errors=True)
    for sub in ("img", "assets", "files"):
        os.makedirs(os.path.join(OUT, sub))
    for name in names:
        with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
            f.write(live_page(name))
    with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(ROBOTS)
    shutil.copyfile(os.path.join(SITE, ".htaccess"), os.path.join(OUT, ".htaccess"))
    files = used_files(names)
    for rel in files:
        shutil.copyfile(os.path.join(SITE, rel), os.path.join(OUT, rel))

    zpath = os.path.join(SITE, "dist", f"{FOLDER}-{datetime.date.today().isoformat()}.zip")
    with zipfile.ZipFile(zpath + ".tmp", "w") as z:
        for root, _, fnames in os.walk(OUT):
            for fn in sorted(fnames):
                path = os.path.join(root, fn)
                rel = os.path.relpath(path, OUT)
                kind = zipfile.ZIP_STORED if os.path.splitext(fn)[1].lower() in STORED else zipfile.ZIP_DEFLATED
                z.write(path, f"{FOLDER}/{rel}", compress_type=kind)
    os.replace(zpath + ".tmp", zpath)
    write_checklist(names, files)
    print(f"{len(names)} pages + .htaccess + robots.txt + {len(files)} files -> {OUT}")
    print(f"zip: {zpath} ({os.path.getsize(zpath) / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()
