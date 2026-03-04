from PIL import Image, ImageDraw

# Load screenshot
img = Image.open("/Users/sammyt/Documents/Pinegrow/live/v03-outcome-obsessed/media/recordings-claude-l5-search-process-panel.png")
width, height = img.size
print(f"Image dimensions: {width}x{height}")

# Create overlay
overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
draw = ImageDraw.Draw(overlay)

# Image is 1280x761.
# The search process panel (the grey expanded area) spans:
# - Top: ~185px (just above "Aggregated recent Anthropic news headlines for synthesis")
# - Bottom: ~535px (just below "Done")
# - Left: ~305px (left edge of the grey panel content)
# - Right: ~1060px (right edge of the panel)

x1 = 305
y1 = 185
x2 = 1060
y2 = 535

orange = (255, 160, 26, 255)  # #ffa01a

# Draw 3px rounded rectangle (simulate by drawing 3 concentric with 1px each)
for i in range(3):
    draw.rounded_rectangle(
        [x1 - i, y1 - i, x2 + i, y2 + i],
        radius=8,
        outline=orange,
        width=1
    )

# Composite and save
result = Image.alpha_composite(img.convert("RGBA"), overlay)
result = result.convert("RGB")
result.save("/Users/sammyt/Documents/Pinegrow/live/v03-outcome-obsessed/media/recordings-claude-l5-search-process-panel-annotated.png")
print("Saved annotated screenshot.")
