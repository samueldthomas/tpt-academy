from PIL import Image, ImageDraw

img = Image.open("/Users/sammyt/Documents/Pinegrow/live/v03-outcome-obsessed/media/recordings-claude-l2-settings-overview.png")
overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
draw = ImageDraw.Draw(overlay)

# Bounding box around the settings nav list:
# General, Account, Privacy, Billing, Usage, Capabilities, Connectors, Claude Code
x1, y1, x2, y2 = 308, 128, 540, 443
radius = 8
color = (255, 160, 26, 255)  # #ffa01a, fully opaque
stroke = 3

# Draw rounded rectangle (no fill)
draw.rounded_rectangle([x1, y1, x2, y2], radius=radius, outline=color, width=stroke)

result = Image.alpha_composite(img.convert("RGBA"), overlay)
result = result.convert("RGB")
result.save("/Users/sammyt/Documents/Pinegrow/live/v03-outcome-obsessed/media/recordings-claude-l2-settings-overview-annotated.png")
print("Done.")
