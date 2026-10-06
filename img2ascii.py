#!/usr/bin/env python3
"""Turn a photo into ASCII art for your README.

    pip install pillow
    python tools/img2ascii.py me.jpg --width 60 > portrait.txt

Paste the output inside a ``` code block in README.md.
Tip: use a high-contrast photo with a plain background.
Add --invert if it looks like a negative on your theme.
"""
import argparse
from PIL import Image, ImageOps

p = argparse.ArgumentParser()
p.add_argument("image")
p.add_argument("--width", type=int, default=60)
p.add_argument("--invert", action="store_true")
a = p.parse_args()

# dark theme: bright pixel -> dense character
ramp = " .:-=+*#%@"
if a.invert:
    ramp = ramp[::-1]

im = ImageOps.autocontrast(Image.open(a.image).convert("L"))
w, h = im.size
im = im.resize((a.width, max(1, int(h / w * a.width * 0.5))))  # chars are ~2x taller than wide
px = im.load()
for y in range(im.height):
    print("".join(ramp[px[x, y] * (len(ramp) - 1) // 255] for x in range(im.width)).rstrip())
