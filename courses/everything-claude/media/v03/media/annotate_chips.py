from PIL import Image, ImageDraw

# Load screenshot
img = Image.open("/Users/sammyt/Documents/Pinegrow/live/v03-outcome-obsessed/media/recordings-claude-l2-main-chat.png")
print(f"Image size: {img.size}")

# Create transparent overlay
overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
draw = ImageDraw.Draw(overlay)

# Suggestion chips row coordinates (from visual inspection)
# Chips: Write, Learn, From Drive, From Calendar, From Gmail
# Row spans approximately x=383 to x=947, y=445 to y=483
# Adding 10px padding around the row
x1 = 373
y1 = 443
x2 = 957
y2 = 485

padding = 10
x1 -= padding
y1 -= padding
x2 += padding
y2 += padding

# Draw rounded rectangle - outline only, no fill
# PIL's rounded_rectangle requires Pillow 8.2+
draw.rounded_rectangle(
    [x1, y1, x2, y2],
    radius=12,
    outline=(255, 160, 26, 255),
    width=3
)

# Composite and save
result = Image.alpha_composite(img.convert("RGBA"), overlay)
result.save("/Users/sammyt/Documents/Pinegrow/live/v03-outcome-obsessed/media/recordings-claude-l2-suggestion-chips-annotated.png")
print("Saved annotated image.")
