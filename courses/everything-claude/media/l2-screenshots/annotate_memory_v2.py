from PIL import Image, ImageDraw, ImageFont
import os

# Load clean raw screenshot
img = Image.open('/Users/sammyt/Documents/GitHub/tpt-academy/courses/everything-claude/media/l2-screenshots/l2-settings-memory-skills.jpg')
img = img.convert('RGBA')

w, h = img.size
print(f"Image size: {w}x{h}")

# Create transparent overlay
overlay = Image.new('RGBA', img.size, (0, 0, 0, 0))
draw = ImageDraw.Draw(overlay)

# TPT Orange
ORANGE_RGBA = (255, 160, 26, 255)
ORANGE_FILL = (255, 160, 26, 20)  # very subtle fill
TEXT_COLOR = (51, 51, 51, 255)    # #333333
BOX_BORDER = 3

# Load font — 20px bold as per style guide
font_paths = [
    '/Users/sammyt/Library/Fonts/Inter-Bold.ttf',
    '/System/Library/Fonts/Helvetica.ttc',
    '/Library/Fonts/Arial Bold.ttf',
    '/System/Library/Fonts/SFNSText-Bold.otf',
]
font_label = None
for fp in font_paths:
    if os.path.exists(fp):
        try:
            font_label = ImageFont.truetype(fp, 20)
            print(f"Loaded font: {fp}")
            break
        except Exception:
            continue
if font_label is None:
    font_label = ImageFont.load_default()
    print("Using default font")

# ─────────────────────────────────────────────
# TOGGLE ROW COORDINATES
# Image: 900x561
#
# Row 1: "Search and reference chats"
# Row bounding box: x1=283, y1=383, x2=868, y2=440
#
# Row 2: "Generate memory from chat history"
# Row bounding box: x1=283, y1=453, x2=868, y2=528
# ─────────────────────────────────────────────

ROW1 = (283, 383, 868, 440)
ROW2 = (283, 453, 868, 528)

def draw_rounded_rect(draw_obj, bbox, radius=6, border_color=ORANGE_RGBA, fill_color=ORANGE_FILL, border_width=BOX_BORDER):
    """Draw a rounded rectangle on the overlay."""
    x1, y1, x2, y2 = bbox
    draw_obj.rounded_rectangle([x1, y1, x2, y2], radius=radius, fill=fill_color, outline=border_color, width=border_width)

def draw_label(draw_obj, text, anchor_x, anchor_y, font, position='above'):
    """
    Draw a pill label with white background and orange border.
    anchor_x, anchor_y: centre anchor point for label placement.
    position: 'above' or 'below'
    """
    padding_h = 14
    padding_v = 7

    # Measure text
    bbox_text = font.getbbox(text)
    text_w = bbox_text[2] - bbox_text[0]
    text_h = bbox_text[3] - bbox_text[1]

    pill_w = text_w + padding_h * 2
    pill_h = text_h + padding_v * 2

    # Position pill relative to anchor
    if position == 'above':
        pill_x1 = anchor_x - pill_w // 2
        pill_y1 = anchor_y - pill_h - 8
    else:  # below
        pill_x1 = anchor_x - pill_w // 2
        pill_y1 = anchor_y + 8

    pill_x2 = pill_x1 + pill_w
    pill_y2 = pill_y1 + pill_h

    # Clamp within image bounds
    if pill_x1 < 5:
        shift = 5 - pill_x1
        pill_x1 += shift
        pill_x2 += shift
    if pill_x2 > w - 5:
        shift = pill_x2 - (w - 5)
        pill_x1 -= shift
        pill_x2 -= shift
    if pill_y1 < 5:
        pill_y1 = 5
        pill_y2 = pill_y1 + pill_h
    if pill_y2 > h - 5:
        pill_y2 = h - 5
        pill_y1 = pill_y2 - pill_h

    print(f"  Label '{text[:30]}': pill=({pill_x1},{pill_y1},{pill_x2},{pill_y2}), width={pill_w}")

    # Drop shadow (subtle)
    shadow_offset = 2
    draw_obj.rounded_rectangle(
        [pill_x1 + shadow_offset, pill_y1 + shadow_offset,
         pill_x2 + shadow_offset, pill_y2 + shadow_offset],
        radius=12,
        fill=(0, 0, 0, 40)
    )

    # White pill background with orange border
    draw_obj.rounded_rectangle(
        [pill_x1, pill_y1, pill_x2, pill_y2],
        radius=12,
        fill=(255, 255, 255, 240),
        outline=ORANGE_RGBA,
        width=1
    )

    # Text
    text_x = pill_x1 + padding_h - bbox_text[0]
    text_y = pill_y1 + padding_v - bbox_text[1]
    draw_obj.text((text_x, text_y), text, fill=TEXT_COLOR, font=font)

# ─────────────────────────────────────────────
# Draw annotation boxes
# ─────────────────────────────────────────────

draw_rounded_rect(draw, ROW1)
draw_rounded_rect(draw, ROW2)

# ─────────────────────────────────────────────
# Draw labels
# Centre of content area (between left edge of box and right toggle edge)
# x centre = (283 + 868) / 2 = 575
# ─────────────────────────────────────────────

content_centre_x = (ROW1[0] + ROW1[2]) // 2  # 575

print("Drawing labels:")
# Label 1: above row 1
draw_label(draw, "Search and reference chats", content_centre_x, ROW1[1], font_label, position='above')

# Label 2: below row 2
draw_label(draw, "Generate memory from chat history", content_centre_x, ROW2[3], font_label, position='below')

# ─────────────────────────────────────────────
# Composite and save
# ─────────────────────────────────────────────
result = Image.alpha_composite(img, overlay)
result = result.convert('RGB')

out_path = '/Users/sammyt/Documents/GitHub/tpt-academy/courses/everything-claude/media/l2-screenshots/claude-l2-settings-memory-annotated-v2.png'
result.save(out_path, format='PNG')
print(f"Saved to: {out_path}")
