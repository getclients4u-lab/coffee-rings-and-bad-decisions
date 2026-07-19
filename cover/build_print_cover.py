#!/usr/bin/env python3
"""Build print-ready KDP paperback cover for 5.5x8.5 trim size."""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

src = '/home/ubuntu/.openclaw-author/coffee-rings-and-bad-decisions/cover/clean-base.png'
out = '/home/ubuntu/.openclaw-author/coffee-rings-and-bad-decisions/cover/print-cover-alex-rogers.png'
FONT_DIR = '/usr/share/fonts/truetype/liberation'
BOLD = Path(FONT_DIR) / 'LiberationSerif-Bold.ttf'
REG  = Path(FONT_DIR) / 'LiberationSerif-Regular.ttf'
ITAL = Path(FONT_DIR) / 'LiberationSerif-Italic.ttf'

# KDP 5.5x8.5 paperback: assembled full cover with bleed
# Trim 5.5 + 5.5 = 11.0, spine ~0.85 for 230pp; add 0.125 bleed per side
SPINE_INCHES = 0.85
DPI = 300
FRONT_PX = int(5.625 * DPI)    # 1688
SPINE_PX = int((SPINE_INCHES + 0.25) * DPI)  # 330
BACK_PX  = int(5.625 * DPI)    # 1688
H_PX     = int(8.625 * DPI)    # 2588

TOTAL_W = FRONT_PX + SPINE_PX + BACK_PX  # 3706

# Open and crop source
img = Image.open(src).convert('RGB')
sw, sh = img.size
ratio = max(TOTAL_W / sw, H_PX / sh)
img = img.resize((int(sw*ratio), int(sh*ratio)), Image.LANCZOS)
x = (img.width - TOTAL_W) // 2
y = (img.height - H_PX) // 2
img = img.crop((x, y, x + TOTAL_W, y + H_PX))

def fpath(p, size):
    return ImageFont.truetype(str(p), size) if p.exists() else ImageFont.load_default()

canvas = Image.new('RGB', (TOTAL_W, H_PX), (28, 36, 50))
canvas.paste(img, (0, 0))
draw = ImageDraw.Draw(canvas, 'RGBA')

# Top/bottom gradients
for i in range(90):
    a = int(200 * (1 - i/90))
    draw.line([(0,i),(TOTAL_W,i)], fill=(0,0,0,a))
for i in range(H_PX-100, H_PX):
    a = int(220 * ((i-(H_PX-100))/100))
    draw.line([(0,i),(TOTAL_W,i)], fill=(0,0,0,a))

CX = TOTAL_W // 2
title_font  = fpath(BOLD, 114)
small_font  = fpath(ITAL, 38)
author_font = fpath(REG,  48)

draw.text((CX, 72),  'COFFEE',            font=title_font,  fill=(245, 240, 232), anchor='mm')
draw.text((CX, 124), 'RINGS',             font=title_font,  fill=(245, 240, 232), anchor='mm')
draw.text((CX, 182), 'and Bad Decisions', font=small_font,  fill=(201, 134,  42), anchor='mm')
draw.text((CX, H_PX - 160), 'Alex Rogers', font=author_font, fill=(245, 240, 232), anchor='mm')

# ISBN / Barcode placeholder on back
bx, by = TOTAL_W - 200, H_PX - 280
draw.rectangle([bx, by, bx+140, by+180], fill=(255,255,255))
draw.text((bx+70, by+90), 'ISBN', font=fpath(REG, 18), fill=(0,0,0), anchor='mm')

# Spine
sp_x = FRONT_PX
sp_y = 0
for y in range(H_PX):
    a = int(40 * abs(y - H_PX//2) / (H_PX//2))
    draw.line([(sp_x,y),(sp_x+SPINE_PX,y)], fill=(0,0,0,a))
for x in [sp_x, sp_x + SPINE_PX]:
    draw.line([(x,60),(x,H_PX-60)], fill=(201,134,42), width=4)

# Spine text (rotated)
spine_center_x = sp_x + SPINE_PX//2
spine_center_y = H_PX//2
spine_img = Image.new('RGBA', (H_PX, SPINE_PX), (0,0,0,0))
sd = ImageDraw.Draw(spine_img)
sd.text((H_PX//2, 40), 'COFFEE RINGS', font=fpath(BOLD, 36), fill=(245,240,232), anchor='mm')
sd.text((H_PX//2, 90), 'and Bad Decisions', font=fpath(ITAL, 22), fill=(201,134,42), anchor='mm')
sd.text((H_PX//2, SPINE_PX-80), 'Alex Rogers', font=fpath(REG, 26), fill=(200,200,200), anchor='mm')
spine_rot = spine_img.rotate(90, expand=True)
sw, sh = spine_rot.size
ox = spine_center_x - sh//2
oy = spine_center_y - sw//2
canvas.paste(spine_rot, (ox, oy), spine_rot)

# Spine border
draw.rectangle([sp_x, 0, sp_x+SPINE_PX, H_PX], outline=(201,134,42), width=4)

# Back cover text
pub_font = fpath(REG, 24)
pub_lines = [
    'Coffee Rings Press',
    'coffeeringsnovel.com',
    ' ',
    'Coffee Rings and Bad Decisions',
    'A Romantic Comedy Novel',
    'by Alex Rogers',
    ' ',
    'Available on Amazon KDP:',
    'eBook • Paperback • Kindle Unlimited',
]
for i, line in enumerate(pub_lines):
    draw.text((120, 120 + i*36), line, font=pub_font, fill=(220,225,230), anchor='lm')

bio_font = fpath(ITAL, 22)
bio = [
    'About the Author',
    ' ',
    'Alex Rogers writes romantic comedies about coffee,',
    'community, and the kind of love that sneaks up',
    "on you when you're too busy arguing about grind",
    'sizes to notice.',
    ' ',
    'Coffee Rings and Bad Decisions is her debut.',
]
for i, line in enumerate(bio):
    draw.text((120, 880 + i*30), line, font=bio_font, fill=(180,190,200), anchor='lm')

# Front bleed border markers (safe area)
# 0.25" bleed on all sides = 75px
bleed_px = int(0.125 * DPI)  # 37px
draw.rectangle([bleed_px, bleed_px, TOTAL_W-bleed_px, H_PX-bleed_px],
               outline=(255,255,0,120), width=2)

canvas.save(out, 'PNG')
print('Print cover saved:', out, 'size:', canvas.size)
