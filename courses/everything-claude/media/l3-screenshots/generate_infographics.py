from PIL import Image, ImageDraw, ImageFont
import os

OUTPUT_DIR = "/tmp/scratchpad/everything-claude/tests/media"

# Colour palette
CREAM = (252, 248, 240)
TERRACOTTA = (193, 108, 72)
DEEP_BLUE = (32, 52, 82)
LIGHT_BLUE = (220, 232, 245)
WHITE = (255, 255, 255)
LIGHT_TERRA = (245, 225, 210)
WARM_GREY = (180, 170, 160)
SOFT_GREEN = (200, 225, 200)

def get_font(size):
    """Try to get a clean sans-serif font."""
    font_paths = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/SFNSText.ttf",
        "/Library/Fonts/Arial.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
    ]
    for path in font_paths:
        try:
            return ImageFont.truetype(path, size)
        except (OSError, IOError):
            continue
    return ImageFont.load_default()

def get_bold_font(size):
    """Try to get a bold font."""
    font_paths = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/Library/Fonts/Arial Bold.ttf",
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    ]
    for path in font_paths:
        try:
            return ImageFont.truetype(path, size, index=1)
        except (OSError, IOError):
            try:
                return ImageFont.truetype(path, size)
            except (OSError, IOError):
                continue
    return get_font(size)


def draw_rounded_rect(draw, xy, radius, fill, outline=None):
    """Draw a rounded rectangle."""
    x0, y0, x1, y1 = xy
    draw.rectangle([x0 + radius, y0, x1 - radius, y1], fill=fill)
    draw.rectangle([x0, y0 + radius, x1, y1 - radius], fill=fill)
    draw.pieslice([x0, y0, x0 + 2*radius, y0 + 2*radius], 180, 270, fill=fill)
    draw.pieslice([x1 - 2*radius, y0, x1, y0 + 2*radius], 270, 360, fill=fill)
    draw.pieslice([x0, y1 - 2*radius, x0 + 2*radius, y1], 90, 180, fill=fill)
    draw.pieslice([x1 - 2*radius, y1 - 2*radius, x1, y1], 0, 90, fill=fill)


def create_model_lineup():
    """PANEL 3: The Model Lineup Cards"""
    W, H = 1200, 675
    img = Image.new('RGB', (W, H), CREAM)
    draw = ImageDraw.Draw(img)

    # Title
    title_font = get_bold_font(36)
    draw.text((W//2, 40), "The Claude Model Lineup", fill=DEEP_BLUE, font=title_font, anchor="mt")

    # Three cards
    cards = [
        {"name": "Haiku 4.5", "subtitle": "Fast & Lightweight", "context": "200K tokens", "color": SOFT_GREEN, "icon": "lightning"},
        {"name": "Sonnet 4.5", "subtitle": "Balanced & Versatile", "context": "200K tokens", "color": LIGHT_BLUE, "icon": "scales"},
        {"name": "Opus 4.6", "subtitle": "Deepest Reasoning", "context": "1M tokens", "color": LIGHT_TERRA, "icon": "brain"},
    ]

    card_w = 320
    card_h = 380
    gap = 40
    total_w = 3 * card_w + 2 * gap
    start_x = (W - total_w) // 2
    start_y = 100

    name_font = get_bold_font(28)
    sub_font = get_font(20)
    ctx_font = get_font(18)
    note_font = get_font(16)
    icon_font = get_font(48)

    icons = {"lightning": "\u26A1", "scales": "\u2696", "brain": "\u2B55"}

    for i, card in enumerate(cards):
        x = start_x + i * (card_w + gap)
        y = start_y

        # Card background
        draw_rounded_rect(draw, (x, y, x + card_w, y + card_h), 16, fill=WHITE)

        # Colour accent bar at top
        draw_rounded_rect(draw, (x, y, x + card_w, y + 8), 4, fill=card["color"])

        # Icon circle
        cx = x + card_w // 2
        cy = y + 70
        draw.ellipse([cx-35, cy-35, cx+35, cy+35], fill=card["color"])

        # Icon text
        if card["icon"] == "lightning":
            draw.text((cx, cy), "\u26A1", fill=DEEP_BLUE, font=icon_font, anchor="mm")
        elif card["icon"] == "scales":
            draw.text((cx, cy), "\u2696", fill=DEEP_BLUE, font=icon_font, anchor="mm")
        else:
            draw.text((cx, cy), "\u25CE", fill=DEEP_BLUE, font=icon_font, anchor="mm")

        # Model name
        draw.text((cx, cy + 60), card["name"], fill=DEEP_BLUE, font=name_font, anchor="mt")

        # Subtitle
        draw.text((cx, cy + 100), card["subtitle"], fill=TERRACOTTA, font=sub_font, anchor="mt")

        # Separator line
        draw.line([(x + 40, cy + 140), (x + card_w - 40, cy + 140)], fill=WARM_GREY, width=1)

        # Context window
        draw.text((cx, cy + 160), "Context Window", fill=WARM_GREY, font=ctx_font, anchor="mt")
        draw.text((cx, cy + 190), card["context"], fill=DEEP_BLUE, font=name_font, anchor="mt")

    # Bottom note
    draw.text((W//2, H - 50), "Naming pattern:  Claude  [Tier]  [Version]", fill=WARM_GREY, font=note_font, anchor="mt")

    # Underline the pattern parts with terracotta
    draw.text((W//2, H - 25), "\u2500" * 50, fill=TERRACOTTA, font=note_font, anchor="mt")

    path = os.path.join(OUTPUT_DIR, "l3-model-lineup-cards.jpg")
    img.save(path, 'JPEG', quality=85)
    print(f"Created {path} ({os.path.getsize(path)/1024:.0f}KB)")
    return path


def create_speed_capability():
    """PANEL 4: Speed vs Capability Spectrum"""
    W, H = 1200, 675
    img = Image.new('RGB', (W, H), CREAM)
    draw = ImageDraw.Draw(img)

    title_font = get_bold_font(36)
    label_font = get_bold_font(24)
    sub_font = get_font(18)
    small_font = get_font(16)
    name_font = get_bold_font(20)

    # Title
    draw.text((W//2, 40), "Speed vs Capability", fill=DEEP_BLUE, font=title_font, anchor="mt")
    draw.text((W//2, 85), "Every model has its place in your workflow", fill=WARM_GREY, font=sub_font, anchor="mt")

    # Main spectrum bar
    bar_y = 240
    bar_h = 60
    bar_x0 = 120
    bar_x1 = W - 120
    bar_w = bar_x1 - bar_x0

    # Gradient effect — draw segments
    for x in range(bar_x0, bar_x1):
        ratio = (x - bar_x0) / bar_w
        r = int(SOFT_GREEN[0] * (1 - ratio) + LIGHT_TERRA[0] * ratio)
        g = int(SOFT_GREEN[1] * (1 - ratio) + LIGHT_TERRA[1] * ratio)
        b = int(SOFT_GREEN[2] * (1 - ratio) + LIGHT_TERRA[2] * ratio)
        draw.line([(x, bar_y), (x, bar_y + bar_h)], fill=(r, g, b))

    # Axis labels
    draw.text((bar_x0, bar_y - 30), "\u2190  Faster", fill=DEEP_BLUE, font=label_font, anchor="lt")
    draw.text((bar_x1, bar_y - 30), "More Capable  \u2192", fill=DEEP_BLUE, font=label_font, anchor="rt")

    # Model markers
    positions = [
        (bar_x0 + bar_w * 0.15, "Haiku 4.5", "Quick Tasks", SOFT_GREEN),
        (bar_x0 + bar_w * 0.50, "Sonnet 4.5", "Daily Driver", LIGHT_BLUE),
        (bar_x0 + bar_w * 0.85, "Opus 4.6", "Deep Work", LIGHT_TERRA),
    ]

    for px, name, desc, color in positions:
        px = int(px)
        # Marker circle on bar
        draw.ellipse([px-20, bar_y + bar_h//2 - 20, px+20, bar_y + bar_h//2 + 20], fill=WHITE, outline=DEEP_BLUE, width=3)

        # Connector line down
        draw.line([(px, bar_y + bar_h + 20), (px, bar_y + bar_h + 60)], fill=DEEP_BLUE, width=2)

        # Info card below
        card_w = 220
        card_h = 130
        cx = px - card_w // 2
        cy = bar_y + bar_h + 60

        draw_rounded_rect(draw, (cx, cy, cx + card_w, cy + card_h), 12, fill=WHITE)
        draw_rounded_rect(draw, (cx, cy, cx + card_w, cy + 6), 3, fill=color)

        draw.text((px, cy + 30), name, fill=DEEP_BLUE, font=name_font, anchor="mt")
        draw.text((px, cy + 60), desc, fill=TERRACOTTA, font=sub_font, anchor="mt")

        # Small detail
        if "Haiku" in name:
            draw.text((px, cy + 90), "Fast responses, simple tasks", fill=WARM_GREY, font=small_font, anchor="mt")
        elif "Sonnet" in name:
            draw.text((px, cy + 90), "Best balance of speed & depth", fill=WARM_GREY, font=small_font, anchor="mt")
        else:
            draw.text((px, cy + 90), "Complex reasoning, large docs", fill=WARM_GREY, font=small_font, anchor="mt")

    path = os.path.join(OUTPUT_DIR, "l3-speed-capability-spectrum.jpg")
    img.save(path, 'JPEG', quality=85)
    print(f"Created {path} ({os.path.getsize(path)/1024:.0f}KB)")
    return path


def create_decision_guide():
    """PANEL 9: Model Decision Guide"""
    W, H = 1200, 675
    img = Image.new('RGB', (W, H), CREAM)
    draw = ImageDraw.Draw(img)

    title_font = get_bold_font(36)
    name_font = get_bold_font(24)
    sub_font = get_font(20)
    task_font = get_font(18)
    arrow_font = get_bold_font(28)

    # Title
    draw.text((W//2, 40), "Choosing the Right Model", fill=DEEP_BLUE, font=title_font, anchor="mt")
    draw.text((W//2, 85), "Match your task to the right tool", fill=WARM_GREY, font=sub_font, anchor="mt")

    # Three rows
    rows = [
        {
            "task": "Quick question or simple task",
            "examples": "\"What's the capital of NZ?\"  \u2022  Format a date  \u2022  Short translation",
            "model": "Haiku 4.5",
            "color": SOFT_GREEN,
            "icon_text": "\u26A1",
        },
        {
            "task": "Writing, summarising, everyday work",
            "examples": "Draft an email  \u2022  Summarise a report  \u2022  Brainstorm ideas",
            "model": "Sonnet 4.5",
            "color": LIGHT_BLUE,
            "icon_text": "\u2696",
        },
        {
            "task": "Complex analysis or deep reasoning",
            "examples": "Analyse a contract  \u2022  Compare strategies  \u2022  Process large documents",
            "model": "Opus 4.6",
            "color": LIGHT_TERRA,
            "icon_text": "\u25CE",
        },
    ]

    row_h = 140
    row_w = 1000
    start_x = (W - row_w) // 2
    start_y = 140

    for i, row in enumerate(rows):
        y = start_y + i * (row_h + 25)

        # Left section: task description
        left_w = 600
        draw_rounded_rect(draw, (start_x, y, start_x + left_w, y + row_h), 12, fill=WHITE)

        draw.text((start_x + 25, y + 25), row["task"], fill=DEEP_BLUE, font=name_font, anchor="lt")
        draw.text((start_x + 25, y + 65), row["examples"], fill=WARM_GREY, font=task_font, anchor="lt")

        # Arrow
        arrow_x = start_x + left_w + 25
        draw.text((arrow_x + 20, y + row_h//2), "\u2192", fill=TERRACOTTA, font=arrow_font, anchor="mm")

        # Right section: model
        right_x = arrow_x + 70
        right_w = row_w - left_w - 95
        draw_rounded_rect(draw, (right_x, y, right_x + right_w, y + row_h), 12, fill=row["color"])

        draw.text((right_x + right_w//2, y + 35), row["icon_text"], fill=DEEP_BLUE, font=arrow_font, anchor="mt")
        draw.text((right_x + right_w//2, y + 80), row["model"], fill=DEEP_BLUE, font=name_font, anchor="mt")

    # Bottom tip
    tip_font = get_font(16)
    draw.text((W//2, H - 40), "Tip: You can switch models mid-conversation if your task changes.", fill=TERRACOTTA, font=tip_font, anchor="mt")

    path = os.path.join(OUTPUT_DIR, "l3-model-decision-guide.jpg")
    img.save(path, 'JPEG', quality=85)
    print(f"Created {path} ({os.path.getsize(path)/1024:.0f}KB)")
    return path


if __name__ == "__main__":
    create_model_lineup()
    create_speed_capability()
    create_decision_guide()
    print("All infographics generated.")
