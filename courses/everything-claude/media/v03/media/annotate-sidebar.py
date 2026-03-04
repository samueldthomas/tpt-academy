from PIL import Image, ImageDraw
import os

input_path = "/Users/sammyt/Documents/Pinegrow/live/v03-outcome-obsessed/media/recordings-claude-l2-sidebar.png"
output_path = "/Users/sammyt/Documents/Pinegrow/live/v03-outcome-obsessed/media/recordings-claude-l2-sidebar-annotated.png"

img = Image.open(input_path)
width, height = img.size
print(f"Image dimensions: {width}x{height}")

overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
draw = ImageDraw.Draw(overlay)

# Sidebar bounding box: left edge to divider (~284px), full height
# Adding a small inset (4px) so the stroke sits just inside the sidebar edges
x1, y1, x2, y2 = 4, 4, 280, height - 4

# Draw rounded rectangle — orange, 3px stroke, no fill, 8px radius
orange = (255, 160, 26, 255)

# PIL's rounded_rectangle draws filled + outline; use outline only
draw.rounded_rectangle(
    [x1, y1, x2, y2],
    radius=8,
    outline=orange,
    width=3
)

# Composite and save
result = Image.alpha_composite(img.convert("RGBA"), overlay)
result = result.convert("RGB")
result.save(output_path, format="PNG")
print(f"Saved: {output_path}")
