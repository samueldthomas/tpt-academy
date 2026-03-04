from PIL import Image, ImageDraw
import os

input_path = "/Users/sammyt/Documents/Pinegrow/live/v03-outcome-obsessed/media/recordings-claude-l2-settings-profile.png"
output_path = "/Users/sammyt/Documents/Pinegrow/live/v03-outcome-obsessed/media/recordings-claude-l2-settings-profile-annotated.png"

img = Image.open(input_path).convert("RGBA")
overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
draw = ImageDraw.Draw(overlay)

ORANGE = (255, 160, 26, 255)
STROKE = 3
RADIUS = 6

def draw_rounded_rect(draw, x1, y1, x2, y2, radius, color, width):
    # Draw four arcs at corners and three rectangles for the sides
    # Top-left arc
    draw.arc([x1, y1, x1 + 2*radius, y1 + 2*radius], 180, 270, fill=color, width=width)
    # Top-right arc
    draw.arc([x2 - 2*radius, y1, x2, y1 + 2*radius], 270, 360, fill=color, width=width)
    # Bottom-left arc
    draw.arc([x1, y2 - 2*radius, x1 + 2*radius, y2], 90, 180, fill=color, width=width)
    # Bottom-right arc
    draw.arc([x2 - 2*radius, y2 - 2*radius, x2, y2], 0, 90, fill=color, width=width)
    # Top line
    draw.line([x1 + radius, y1, x2 - radius, y1], fill=color, width=width)
    # Bottom line
    draw.line([x1 + radius, y2, x2 - radius, y2], fill=color, width=width)
    # Left line
    draw.line([x1, y1 + radius, x1, y2 - radius], fill=color, width=width)
    # Right line
    draw.line([x2, y1 + radius, x2, y2 - radius], fill=color, width=width)

# 1. Full name field (including avatar and input together — the whole row up to the midpoint)
draw_rounded_rect(draw, 571, 196, 978, 242, RADIUS, ORANGE, STROKE)

# 2. "What should Claude call you?" field
draw_rounded_rect(draw, 990, 196, 1240, 242, RADIUS, ORANGE, STROKE)

# 3. "What best describes your work?" dropdown
draw_rounded_rect(draw, 571, 289, 1240, 334, RADIUS, ORANGE, STROKE)

result = Image.alpha_composite(img, overlay)
result.save(output_path)
print(f"Saved: {output_path}")
