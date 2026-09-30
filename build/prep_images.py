"""Copy Stephanie's new photos and art into img/ at web size.

Run once after downloading her Dropbox folder:  python3 build/prep_images.py
Source: the "Stephanie-Watson.com assets" folder she shared (Sept 29, 2026), unzipped in ~/Downloads.
Uses macOS `sips` (no Pillow needed). Photos -> JPG, longest side PHOTO_PX. Partner logos are done by prep_logos.py.
"""
import os
import struct
import subprocess
import sys

SRC = os.path.expanduser("~/Downloads/Stephanie-Watson.com assets")
SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(SITE, "img")
PHOTO_PX = 1600
QUALITY = "78"

# source (relative to SRC) -> new name in img/
PHOTOS = {
    "2026 Photos/Bancroft photos/SchoolPresentation_SWatson_2-scaled.jpg": "home_teaching_school-presentation.jpg",
    "2026 Photos/ComicsWorkshop_StephanieWatsonIllustrator.jpg": "teaching_intro_comics-workshop.jpg",
    "2026 Photos/AuthorVisit_LibraryVisit_Minnesota.jpg": "teaching_kids-card_library-visit.jpg",
    "2026 Photos/Confab_2023_DrawingGames_StephanieWatson.jpg": "teaching_adults-card_confab-drawing-games.jpg",
    "2026 Photos/DSCF5549 copy.JPG": "adults_intro_drawing-workshop.jpg",
    "2026 Photos/StephanieWatson_IllustratorAuthor2026.JPG": "about_portrait_2026.jpg",
    "All website photos/2026/08/IMG_6832-scaled.jpg": "about_photo_studio.jpg",
    "2026 Photos/StephanieWatsonSketchbook.JPG": "contact_sketchbook.jpg",
    "2026 Photos/StephanieAge3Drawing copy.jpeg": "contact_age-3-drawing.jpg",
    # For Adults "Recent classes and events" — her picks (content map, For Adults photo table)
    "2026 Photos/Stephanie Watson Speaker.JPG": "adults_grid_confab-speaker.jpg",
    "2026 Photos/IMG_4809 copy.JPG": "grid_confab-drawings-held-up.jpg",
    "2026 Photos/MusicantWorkshop_Aug2022 copy.jpeg": "adults_grid_musicant-workshop.jpg",
    "2026 Photos/StephanieWatsonDrawingWorkshop copy.jpeg": "adults_grid_drawing-workshop.jpg",
    "2026 Photos/StephanieWatsonAuthorMinnesota_BFITU-launch-scaled.jpeg": "adults_grid_keynote.jpg",
    "2026 Photos/StephanieWatsonAuthorTwinCities copy.jpeg": "adults_grid_moon-palace-launch.jpg",
    # For Kids "Past Events" — her picks (content map, For Kids photo table)
    "2026 Photos/Mall of America Reading1.jpeg": "kids_past_mall-of-america-reading.jpg",
    "2026 Photos/Screen Shot 2020-08-22 at 7.58.45 AM copy.png": "kids_past_saints-game.jpg",
    "2026 Photos/SchoolPresentation_SWatson_2 copy.jpeg": "kids_past_school-assembly.jpg",
    "2026 Photos/IMG_6576.JPG": "kids_past_edina-outdoor-storytime.jpg",
    "2026 Photos/BattleoftheBooks_Brainerd_2023_2 copy.jpg": "kids_past_brainerd-book-club.jpg",
    "2026 Photos/Bancroft photos/IMG_5969.jpg": "kids_past_comics-lab-shareout.jpg",  # Sept 30: replaces the Confab photo
    # new book tiles + portfolio art
    "2026 Photos/EO_Cover_Square-500x500.jpg": "EO_Cover_Square-500x500.jpg",
    "2026 Photos/ElvisOlive_SuperDetectives_Square-500x500.jpeg": "ElvisOlive_SuperDetectives_Square-500x500.jpg",
    "2026 Photos/BugTeaParty_2026.jpg": "BugTeaParty_2026.jpg",
    "2026 Photos/Frogs1_2026.png": "Frogs1_2026.jpg",
    "2026 Photos/Hollyhock3.png": "Hollyhock3.jpg",
    "2026 Photos/PeggyFleming.png": "PeggyFleming.jpg",
}



def sips(args):
    return subprocess.run(["sips", *args], check=True, capture_output=True, text=True).stdout


def size(path):
    out = sips(["-g", "pixelWidth", "-g", "pixelHeight", path])
    vals = [int(line.split()[-1]) for line in out.splitlines() if "pixel" in line]
    return vals[0], vals[1]


ROTATE_FOR = {3: 180, 6: 90, 8: 270}  # EXIF orientation -> clockwise degrees


def _orientation_slot(data):
    """Byte offset + endianness of the EXIF orientation value in a JPEG, or None."""
    i = 2
    while i < len(data) - 4 and data[i] == 0xFF:
        marker, length = data[i + 1], struct.unpack(">H", data[i + 2:i + 4])[0]
        if marker == 0xE1 and data[i + 4:i + 10] == b"Exif\0\0":
            base = i + 10
            e = "<" if data[base:base + 2] == b"II" else ">"
            ifd = base + struct.unpack(e + "I", data[base + 4:base + 8])[0]
            for k in range(struct.unpack(e + "H", data[ifd:ifd + 2])[0]):
                p = ifd + 2 + 12 * k
                if struct.unpack(e + "H", data[p:p + 2])[0] == 0x0112:
                    return p + 8, e
            return None
        if marker == 0xDA:
            return None
        i += 2 + length
    return None


def bake_orientation(path):
    """Phone photos are often stored sideways with a 'rotate me' tag. Rotate the pixels for real
    and reset the tag, so width/height in the HTML match what people see."""
    slot = _orientation_slot(open(path, "rb").read())
    if not slot:
        return
    pos, e = slot
    value = struct.unpack(e + "H", open(path, "rb").read()[pos:pos + 2])[0]
    if value not in ROTATE_FOR:
        return
    sips(["-r", str(ROTATE_FOR[value]), path])
    data = bytearray(open(path, "rb").read())
    pos, e = _orientation_slot(data)
    data[pos:pos + 2] = struct.pack(e + "H", 1)
    with open(path + ".tmp", "wb") as f:
        f.write(data)
    os.replace(path + ".tmp", path)


def main():
    missing = [p for p in PHOTOS if not os.path.exists(os.path.join(SRC, p))]
    if missing:
        sys.exit("missing source files:\n" + "\n".join(missing))
    for src, name in PHOTOS.items():
        path = os.path.join(SRC, src)
        shrink = ["-Z", str(PHOTO_PX)] if max(size(path)) > PHOTO_PX else []  # never upscale
        out = os.path.join(IMG, name)
        sips(["-s", "format", "jpeg", "-s", "formatOptions", QUALITY, *shrink, path, "--out", out])
        bake_orientation(out)
    print(f"wrote {len(PHOTOS)} photos (logos: see prep_logos.py)")


if __name__ == "__main__":
    main()
