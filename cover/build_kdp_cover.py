#!/usr/bin/env python3
"""Build final eBook cover: AI-generated rom-com base + clean typography."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path

out = '/home/ubuntu/.openclaw-author/coffee-rings-and-bad-decisions/cover/authors/alex-rogers-cover-kdp.png'
base_img = '/home/ubuntu/.openclaw-author/coffee-rings-and-bad-decisions/cover/ai-base-landscape.png'

FONT_DIR = '/usr/share/fonts/truetype/liberation'
BOLD = Path(FONT_DIR) / 'LiberationSerif-Bold.ttf'
REG  = Path(FONT_DIR) / 'LiberationSerif-Regular.ttf'
ITAL = Path(FONT_DIR) / 'LiberationSerif-Italic.ttf'

def fpath(p, size):
    return ImageFont.truetype(str(p), size) if p.exists() else ImageFont.load_default()

TARGET_W, TARGET_H = 2560, 1600
CX = TARGET_W // 2

img = Image.open(base_img).convert('RGB')
sw, sh = img.size
ratio = max(TARGET_W / sw, TARGET_H / sh)
img = img.resize((int(sw*ratio), int(sh*ratio)), Image.LANCZOS)
x = (img.width - TARGET_W) // 2
y = (img.height - TARGET_H) // 2
img = img.crop((x, y, x + TARGET_W, y + TARGET_H))
draw = ImageDraw.Draw(img, 'RGBA')

# Light overlays for top/bottom legibility
overlay = Image.new('RGBA', img.size, (0,0,0,0))
ov_draw = ImageDraw.Draw(overlay)
for i in range(160):
    alpha = int(110 * (1 - i/160))
    ov_draw.line([(0, i), (TARGET_W, i)], fill=(0, 0, 0, alpha))
for i in range(140):
    alpha = int(160 * (i/140))
    ov_draw.line([(0, TARGET_H - 140 + i), (TARGET_W, TARGET_H - 140 + i)], fill=(0, 0, 0, alpha))
img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')
draw = ImageDraw.Draw(img, 'RGBA')

def shadow_text(draw, pos, text, font, fill, offsets=[(6,6),(10,10)]):
    x, y = pos
    for dx, dy in offsets:
        draw.text((x+dx, y+dy), text, font=font, fill=(0,0,0,180), anchor='mm')
    draw.text((x, y), text, font=font, fill=fill, anchor='mm')

# --- Top: genre + hearts ---
genre_font = fpath(REG, 52)
genre_text = '♥  A ROMANTIC COMEDY  ♥'
shadow_text(draw, (CX, 75), genre_text, genre_font, fill=(255, 200, 220))

# --- Title block ---
title_font = fpath(ITAL, 190)
and_font = fpath(ITAL, 76)
pink_font = fpath(ITAL, 155)

title_y = 240
shadow_text(draw, (CX, title_y), 'Coffee Rings', title_font, fill=(255, 248, 235))
shadow_text(draw, (CX, title_y + 210), 'and', and_font, fill=(255, 255, 255), offsets=[(3,3),(5,5)])
shadow_text(draw, (CX, title_y + 340), 'Bad Decisions', pink_font, fill=(255, 105, 180))

# Rule
rule_y = title_y + 500
draw.line([(CX - 340, rule_y), (CX + 340, rule_y)], fill=(201, 134, 42), width=5)
for dot_x in [CX - 460, CX + 460]:
    draw.ellipse([(dot_x - 10, rule_y - 5), (dot_x + 10, rule_y + 5)], fill=(255, 105, 180))

# --- Bottom: author + series ---
author_font = fpath(REG, 108)
author_text = 'A L E X   R O G E R S'
shadow_text(draw, (CX, TARGET_H - 170), author_text, author_font, fill=(255, 255, 255), offsets=[(6,6),(10,10)])

series_font = fpath(REG, 46)
series_text = 'BOOK 1 OF THE OCCUPIED SERIES'
shadow_text(draw, (CX, TARGET_H - 95), series_text, series_font, fill=(210, 180, 195), offsets=[(3,3),(5,5)])

# Solid seal bottom
for i in range(TARGET_H - 45, TARGET_H):
    draw.line([(0, i), (TARGET_W, i)], fill=(0, 0, 0, 255))

img.save(out, 'PNG')
print('Cover:', out)
print('Size:', img.size)
