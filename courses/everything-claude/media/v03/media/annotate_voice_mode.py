from PIL import Image, ImageDraw
import os

# Load screenshot
img = Image.open("/Users/sammyt/Documents/Pinegrow/live/v03-outcome-obsessed/media/recordings-claude-l2-main-chat.png")
print(f"Image size: {img.size}")

# The voice mode icon (waveform bars) is at approx x=963-983, y=390-410
# Add padding around the icon
padding = 8
x1 = 955 - padding
y1 = 388 - padding
x2 = 985 + padding
y2 = 412 + padding

# Create overlay for the rounded rectangle
overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
draw = ImageDraw.Draw(overlay)

# Draw rounded rectangle - outline only, no fill
orange = (255, 160, 26, 255)
corner_radius = 8
stroke_width = 3

# Draw rounded rectangle stroke
draw.rounded_rectangle(
    [x1, y1, x2, y2],
    radius=corner_radius,
    outline=orange,
    width=stroke_width
)

# Composite and save
result = Image.alpha_composite(img.convert("RGBA"), overlay)
result.save("/Users/sammyt/Documents/Pinegrow/live/v03-outcome-obsessed/media/recordings-claude-l2-voice-mode-annotated.png")
print(f"Saved annotated image. Box coords: ({x1},{y1}) -> ({x2},{y2})")
