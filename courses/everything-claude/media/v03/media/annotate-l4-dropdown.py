from PIL import Image, ImageDraw
import os

input_path = "/Users/sammyt/Documents/Pinegrow/live/v03-outcome-obsessed/media/recordings-claude-l4-artifact-toolbar-dropdown-new.png"
output_path = "/Users/sammyt/Documents/Pinegrow/live/v03-outcome-obsessed/media/recordings-claude-l4-artifact-toolbar-dropdown-annotated.png"

# Load image and convert to RGBA
img = Image.open(input_path).convert("RGBA")
overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
draw = ImageDraw.Draw(overlay)

# TPT orange
ORANGE = (255, 160, 26, 255)
STROKE = 3
RADIUS = 8

def draw_rounded_rect(draw, x1, y1, x2, y2, radius, color, width):
    """Draw a rounded rectangle outline using pieslice + rectangle approach."""
    # Draw four corner arcs
    draw.arc([x1, y1, x1 + radius*2, y1 + radius*2], 180, 270, fill=color, width=width)
    draw.arc([x2 - radius*2, y1, x2, y1 + radius*2], 270, 360, fill=color, width=width)
    draw.arc([x1, y2 - radius*2, x1 + radius*2, y2], 90, 180, fill=color, width=width)
    draw.arc([x2 - radius*2, y2 - radius*2, x2, y2], 0, 90, fill=color, width=width)

    # Draw four straight edges
    draw.line([x1 + radius, y1, x2 - radius, y1], fill=color, width=width)  # top
    draw.line([x1 + radius, y2, x2 - radius, y2], fill=color, width=width)  # bottom
    draw.line([x1, y1 + radius, x1, y2 - radius], fill=color, width=width)  # left
    draw.line([x2, y1 + radius, x2, y2 - radius], fill=color, width=width)  # right

# --- Box 1: "Copy" button with chevron (top-right toolbar) ---
# The Copy button + chevron spans roughly x: 1050 to 1110, y: 11 to 38
draw_rounded_rect(draw, 1048, 10, 1112, 39, RADIUS, ORANGE, STROKE)

# --- Box 2: Dropdown menu area (three items) ---
# Dropdown: Download, Download as PDF, Publish artifact
# Roughly x: 960 to 1110, y: 50 to 150
draw_rounded_rect(draw, 958, 50, 1115, 152, RADIUS, ORANGE, STROKE)

# Composite overlay onto image
result = Image.alpha_composite(img, overlay)
result.save(output_path, format="PNG", compress_level=0)
print(f"Saved to: {output_path}")
print(f"Output size: {result.size}")
