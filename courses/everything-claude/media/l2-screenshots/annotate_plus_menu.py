from PIL import Image, ImageDraw
import os

BASE = "/Users/sammyt/Documents/GitHub/tpt-academy/courses/everything-claude/media/l2-screenshots/l2-plus-menu-v2.jpg"
OUT_DIR = "/Users/sammyt/Documents/GitHub/tpt-academy/courses/everything-claude/media/l2-screenshots"

ORANGE = (255, 160, 26)
ORANGE_FILL = (255, 160, 26, 20)  # semi-transparent fill

# (x1, y1, x2, y2) bounding boxes for each menu item
# Menu panel spans roughly x=295 to x=525
# Items are rows inside the dropdown
ITEMS = {
    "files":       ("claude-l2-plus-menu-files.png",       (295, 428, 525, 460)),
    "screenshot":  ("claude-l2-plus-menu-screenshot.png",  (295, 461, 525, 492)),
    "gdrive":      ("claude-l2-plus-menu-gdrive.png",      (295, 526, 525, 556)),
    "websearch":   ("claude-l2-plus-menu-websearch.png",   (295, 634, 525, 665)),
    "connectors":  ("claude-l2-plus-menu-connectors.png",  (295, 698, 525, 730)),
}

def draw_rounded_rect(draw, box, radius=6, outline_color=ORANGE, fill_color=ORANGE_FILL, width=3):
    x1, y1, x2, y2 = box
    # Draw filled rounded rect on overlay
    draw.rounded_rectangle([x1, y1, x2, y2], radius=radius, fill=fill_color, outline=outline_color, width=width)

for key, (filename, box) in ITEMS.items():
    img = Image.open(BASE).convert("RGBA")
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    draw_rounded_rect(draw, box)
    result = Image.alpha_composite(img, overlay).convert("RGB")
    out_path = os.path.join(OUT_DIR, filename)
    result.save(out_path, format="PNG", optimize=False)
    print(f"Saved: {out_path}")

print("Done.")
