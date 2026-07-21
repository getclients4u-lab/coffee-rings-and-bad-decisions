#!/usr/bin/env python3
"""Build KDP eBook cover matching user's rom-com reference samples."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path

out = '/home/ubuntu/.openclaw-author/coffee-rings-and-bad-decisions/cover/authors/alex-rogers-cover-kdp.png'
base_img = '/home/ubuntu/.openclaw-author/coffee-rings-and-bad-decisions/cover/clean-base-v6.png'

FONT_DIR = '/usr/share/fonts/truetype/liberation'
BOLD = Path(FONT_DIR) / 'LiberationSerif-Bold.ttf'
REG  = Path(FONT_DIR) / 'LiberationSerif-Regular.ttf'
ITAL = Path(FONT_DIR) / 'LiberationSerif-Italic.ttf'
LIGHT = Path(FONT_DIR) / 'LiberationSerif-Regular.ttf'

def fpath(p, size):
    return ImageFont.truetype(str(p), size) if p.exists() else ImageFont.load_default()

TARGET_W, TARGET_H = 2560, 1600
CX = TARGET_W // 2

# Load base image
img = Image.open(base_img).convert('RGB')
sw, sh = img.size
ratio = max(TARGET_W / sw, TARGET_H / sh)
img = img.resize((int(sw*ratio), int(sh*ratio)), Image.LANCZOS)
x = (img.width - TARGET_W) // 2
y = (img.height - TARGET_H) // 2
img = img.crop((x, y, x + TARGET_W, y + TARGET_H))
draw = ImageDraw.Draw(img, 'RGBA')

# Warm dark overlay patterns for text legibility
for i in range(180):
    alpha = int(160 * (1 - i/180))
    draw.line([(0, i), (TARGET_W, i)], fill=(0, 0, 0, alpha))
for i in range(140):
    alpha = int(160 * (i/140))
    draw.line([(0, TARGET_H - 140 + i), (TARGET_W, TARGET_H - 140 + i)], fill=(0, 0, 0, alpha))

# --- Top genre: small centered uppercase with heart ---
genre_font = fpath(REG, 52)
genre_text = 'A ROMANTIC COMEDY'
heart = '♥'
full_genre = f'{heart}  {genre_text}  {heart}'

for dx, dy in [(2,2), (4,4)]:
    draw.text((CX + dx, 70 + dy), full_genre, font=genre_font, fill=(0,0,0,160), anchor='mm')
draw.text((CX, 70), full_genre, font=genre_font, fill=(255, 200, 220), anchor='mm')

# --- Title: three-part layout matching rom-com style ---
title_font_cream = fpath(ITAL, 180)    # "Coffee Rings" in cream/white script-like
sub_and_font = fpath(ITAL, 72)          # "and" small connector
pink_font = fpath(ITAL, 140)           # "Bad Decisions" in vibrant pink

# Top title block: "Coffee Rings"
title_y1 = 220
for dx, dy in [(6,6), (10,10)]:
    draw.text((CX + dx, title_y1 + dy), 'Coffee Rings', font=title_font_cream, fill=(0,0,0,180), anchor='mm')
draw.text((CX, title_y1), 'Coffee Rings', font=title_font_cream, fill=(255, 248, 235), anchor='mm')

# "and" connector
and_y = title_y1 + 190
draw.text((CX, and_y), 'and', font=sub_and_font, fill=(255, 255, 255), anchor='mm')

# "Bad Decisions" in vibrant pink
pink_y = and_y + 120
for dx, dy in [(6,6), (10,10)]:
    draw.text((CX + dx, pink_y + dy), 'Bad Decisions', font=pink_font, fill=(0,0,0,180), anchor='mm')
draw.text((CX, pink_y), 'Bad Decisions', font=pink_font, fill=(255, 105, 180), anchor='mm')

# Gold rule/border under title
rule_y = pink_y + 150
draw.line([(CX - 300, rule_y), (CX + 300, rule_y)], fill=(201, 134, 42), width=4)

# Small decorative dots
for dot_x in [CX - 420, CX + 420]:
    draw.ellipse([(dot_x - 8, rule_y - 4), (dot_x + 8, rule_y + 4)], fill=(255, 105, 180))

# --- Bottom: Author name + series info ---
author_font = fpath(REG, 100)
author_text = 'ALEX  ROGERS'
author_y = TARGET_H - 160

for dx, dy in [(6,6), (10,10)]:
    draw.text((CX + dx, author_y + dy), author_text, font=author_font, fill=(0,0,0,180), anchor='mm')
draw.text((CX, author_y), author_text, font=author_font, fill=(255, 255, 255), anchor='mm')

series_font = fpath(REG, 44)
series_text = 'BOOK 1 OF THE COCOA CHRONICLES'
draw.text((CX, TARGET_H - 90), series_text, font=series_font, fill=(200, 180, 190), anchor='mm')

# Ensure solid bottom edge to prevent any ghost artifacts
for i in range(TARGET_H - 50, TARGET_H):
    draw.line([(0, i), (TARGET_W, i)], fill=(0, 0, 0, 255))

img.save(out, 'PNG')
print('Cover:', out)
print('Size:', img.size)
