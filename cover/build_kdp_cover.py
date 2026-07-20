#!/usr/bin/env python3
"""Build KDP-compliant eBook cover: 2560x1600, clean readable English typography."""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

src = '/home/ubuntu/.openclaw-author/coffee-rings-and-bad-decisions/cover/clean-base-v2.png'
out = '/home/ubuntu/.openclaw-author/coffee-rings-and-bad-decisions/cover/authors/alex-rogers-cover-kdp.png'

FONT_DIR = '/usr/share/fonts/truetype/liberation'
BOLD = Path(FONT_DIR) / 'LiberationSerif-Bold.ttf'
REG  = Path(FONT_DIR) / 'LiberationSerif-Regular.ttf'
ITAL = Path(FONT_DIR) / 'LiberationSerif-Italic.ttf'

def fpath(p, size):
    return ImageFont.truetype(str(p), size) if p.exists() else ImageFont.load_default()

TARGET_W, TARGET_H = 2560, 1600

img = Image.open(src).convert('RGB')
sw, sh = img.size
ratio = max(TARGET_W / sw, TARGET_H / sh)
img = img.resize((int(sw*ratio), int(sh*ratio)), Image.LANCZOS)
x = (img.width - TARGET_W) // 2
y = (img.height - TARGET_H) // 2
img = img.crop((x, y, x + TARGET_W, y + TARGET_H))

draw = ImageDraw.Draw(img, 'RGBA')

# --- Top gradient band for title ---
band_h = 220
for i in range(band_h):
    alpha = int(230 * (1 - i / band_h))
    draw.line([(0, i), (TARGET_W, i)], fill=(0, 0, 0, alpha))

# --- Bottom gradient band for author ---
for i in range(TARGET_H - 140, TARGET_H):
    alpha = int(245 * ((i - (TARGET_H - 140)) / 140))
    draw.line([(0, i), (TARGET_W, i)], fill=(0, 0, 0, alpha))

# --- Typography settings ---
CX = TARGET_W // 2

# Title: stacked "COFFEE RINGS" + "and Bad Decisions"
title_font  = fpath(BOLD, 160)   # very large, bold
sub_font    = fpath(ITAL, 72)    # italic subtitle

# Title drop-shadow layers (multiple offsets for depth)
for dx, dy in [(3,3), (5,5), (7,7)]:
    draw.text((CX, 70),  'COFFEE',            font=title_font, fill=(0,0,0,180), anchor='mm')
    draw.text((CX, 70),  'COFFEE',            font=title_font, fill=(0,0,0,120), anchor='mm')
    draw.text((CX, 70),  'COFFEE',            font=title_font, fill=(0,0,0, 60), anchor='mm')
    draw.text((CX, 140), 'RINGS',             font=title_font, fill=(0,0,0,180), anchor='mm')
    draw.text((CX, 140), 'RINGS',             font=title_font, fill=(0,0,0,120), anchor='mm')
    draw.text((CX, 140), 'RINGS',             font=title_font, fill=(0,0,0, 60), anchor='mm')

# Subtitle in gold
for dx, dy in [(2,2), (3,3)]:
    draw.text((CX, 215), 'and Bad Decisions', font=sub_font, fill=(0,0,0,160), anchor='mm')
draw.text((CX, 215), 'and Bad Decisions', font=sub_font, fill=(201, 134,  42), anchor='mm')

# Bold title in white on top of shadows
draw.text((CX, 70),  'COFFEE',            font=title_font, fill=(255, 255, 255), anchor='mm')
draw.text((CX, 140), 'RINGS',             font=title_font, fill=(255, 255, 255), anchor='mm')

# Thin decorative rule below title
rule_y = 258
draw.line([(CX-220, rule_y), (CX+220, rule_y)], fill=(201, 134, 42), width=4)

# --- Author name ---
author_font = fpath(BOLD, 78)
for dx, dy in [(3,3), (5,5), (7,7)]:
    draw.text((CX, TARGET_H - 112), 'Alex Rogers', font=author_font, fill=(0,0,0,180), anchor='mm')
    draw.text((CX, TARGET_H - 112), 'Alex Rogers', font=author_font, fill=(0,0,0,120), anchor='mm')
    draw.text((CX, TARGET_H - 112), 'Alex Rogers', font=author_font, fill=(0,0,0,  60), anchor='mm')
draw.text((CX, TARGET_H - 112), 'Alex Rogers', font=author_font, fill=(255, 252, 245), anchor='mm')

# Small "A NOVEL" above author
tag_font = fpath(REG, 42)
draw.text((CX, TARGET_H - 170), 'A NOVEL', font=tag_font, fill=(200, 210, 220), anchor='mm')

img.save(out, 'PNG')
print('Cover:', out)
print('Size:', img.size)
