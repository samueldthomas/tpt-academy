from PIL import Image, ImageDraw
import os

input_path = "/Users/sammyt/Documents/Pinegrow/live/v03-outcome-obsessed/media/recordings-claude-l2-model-selector.png"
output_path = "/Users/sammyt/Documents/Pinegrow/live/v03-outcome-obsessed/media/recordings-claude-l2-model-selector-annotated.png"

img = Image.open(input_path).convert("RGBA")
overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
draw = ImageDraw.Draw(overlay)

ORANGE = (255, 160, 26, 255)
STROKE = 3
RADIUS = 8

def draw_rounded_rect(draw, x1, y1, x2, y2, radius, color, width):
    """Draw a rounded rectangle outline."""
    draw.rounded_rectangle([x1, y1, x2, y2], radius=radius, outline=color, width=width)

# Opus 4.6 row — spans full dropdown width, from top of row to bottom
draw_rounded_rect(draw, 700, 430, 940, 480, RADIUS, ORANGE, STROKE)

# Sonnet 4.6 row
draw_rounded_rect(draw, 700, 482, 940, 532, RADIUS, ORANGE, STROKE)

# Haiku 4.5 row
draw_rounded_rect(draw, 700, 534, 940, 584, RADIUS, ORANGE, STROKE)

# Extended thinking row (including toggle)
draw_rounded_rect(draw, 700, 596, 940, 648, RADIUS, ORANGE, STROKE)

result = Image.alpha_composite(img, overlay)
result.save(output_path)
print(f"Saved to: {output_path}")
