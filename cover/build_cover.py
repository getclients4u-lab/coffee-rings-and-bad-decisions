#!/usr/bin/env python3
"""Generate clean English book cover from coffee shop photo."""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

src = '/home/ubuntu/.openclaw-author/coffee-rings-and-bad-decisions/cover/clean-base.png'
out = '/home/ubuntu/.openclaw-author/coffee-rings-and-bad-decisions/cover/authors/alex-rogers-cover-kdp.png'

img = Image.open(src).convert('RGB')
src_w, src_h = img.size
target_w, target_h = 2560, 1600
target_ratio = target_w / target_h
src_ratio = src_w / src_h

if src_ratio > target_ratio:
    # source wider than target — fit height, crop width
    new_h = target_h
    new_w = int(src_w * (target_h / src_h))
else:
    # source taller than target — fit width, crop height
    new_w = target_w
    new_h = int(src_h * (target_w / src_w))

img = img.resize((new_w, new_h), Image.LANCZOS)

# center crop
left = (new_w - target_w) // 2
top = (new_h - target_h) // 2
img = img.crop((left, top, left + target_w, top + target_h))

draw = ImageDraw.Draw(img, 'RGBA')

# LAYOUT: 2560x1600
band_h = 100
for y in range(band_h):
    alpha = int(220 * (1 - y / band_h))
    draw.line([(0, y), (2560, y)], fill=(0, 0, 0, alpha))

for y in range(1600 - 110, 1600):
    alpha = int(255 * ((y - (1600 - 110)) / 110))
    draw.line([(0, y), (2560, y)], fill=(0, 0, 0, alpha))

FONT_DIR = '/usr/share/fonts/truetype/liberation'
BOLD = Path(FONT_DIR) / 'LiberationSerif-Bold.ttf'
REG  = Path(FONT_DIR) / 'LiberationSerif-Regular.ttf'
ITAL = Path(FONT_DIR) / 'LiberationSerif-Italic.ttf'

def fpath(p, size):
    return ImageFont.truetype(str(p), size) if p.exists() else ImageFont.load_default()

title_font  = fpath(BOLD, 130)
small_font  = fpath(ITAL, 46)
author_font = fpath(REG,  56)

CX = 1280
draw.text((CX, 72),  'COFFEE',            font=title_font,  fill=(245, 240, 232), anchor='mm')
draw.text((CX, 122), 'RINGS',             font=title_font,  fill=(245, 240, 232), anchor='mm')
draw.text((CX, 182), 'and Bad Decisions', font=small_font,  fill=(201, 134,  42), anchor='mm')
draw.text((CX, 1535), 'Alex Rogers',      font=author_font, fill=(245, 240, 232), anchor='mm')

img.save(out, 'PNG')
print('Cover saved:', out, 'size:', img.size)
