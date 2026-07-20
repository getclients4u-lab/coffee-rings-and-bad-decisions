#!/usr/bin/env python3
"""Build KDP full-wrap print cover PDF.
Estimates 178 pages -> spine ~0.40 inches for standard white paper.
Trim 6x9, bleed 0.125, safe margin 0.25.
"""
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageTemplate, Frame
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pathlib import Path

PROJECT = Path('/home/ubuntu/.openclaw-author/coffee-rings-and-bad-decisions')
COVER_IMG = PROJECT / 'cover' / 'authors' / 'alex-rogers-cover-kdp.png'
OUT = PROJECT / 'cover' / 'print-cover-alex-rogers.pdf'

FONT_DIR = Path('/usr/share/fonts/truetype/liberation')
pdfmetrics.registerFont(TTFont('LiberationSerif-Bold',    str(FONT_DIR / 'LiberationSerif-Bold.ttf')))
pdfmetrics.registerFont(TTFont('LiberationSerif-Regular', str(FONT_DIR / 'LiberationSerif-Regular.ttf')))
pdfmetrics.registerFont(TTFont('LiberationSerif-Italic',  str(FONT_DIR / 'LiberationSerif-Italic.ttf')))

# Trim / bleed
TEXT_W = 6 * inch
TEXT_H = 9 * inch
BLEED = 0.125 * inch
SPINE = 0.40 * inch  # 178 pages standard white

WRAP_W = TEXT_W * 2 + SPINE
WRAP_H = TEXT_H + 2 * BLEED
SAFE = 0.25 * inch

TITLE = 'Coffee Rings and Bad Decisions'
AUTHOR = 'Alex Rogers'
BLURB = ("Maya Chen built her Portland coffee shop on bad decisions and burnt beans. "
         "When a rogue 500-pound order collapses her savings, the only way out is the Mystery Bean lottery—and the one man who might actually understand what she's fighting for.")

def build_back_page(c, x_start, y_start, w, h):
    c.saveState()
    # cream background
    c.setFillColor(HexColor('#F5F0E8'))
    c.rect(x_start, y_start, w, h, fill=1, stroke=0)

    # decorative top bar
    c.setFillColor(HexColor('#C9862A'))
    c.rect(x_start, y_start + h - SAFE*1.8, w, SAFE*1.8, fill=1, stroke=0)

    c.setFillColor(HexColor('#0D1B2A'))
    c.setFont('LiberationSerif-Bold', 20)
    c.drawCentredString(x_start + w/2, y_start + h - SAFE*2.8 - 20, TITLE)

    c.setFont('LiberationSerif-Italic', 24)
    c.drawCentredString(x_start + w/2, y_start + h - SAFE*2.8 - 52, AUTHOR)

    # Blurb text with margins
    c.setFillColor(HexColor('#1f1b16'))
    c.setFont('LiberationSerif-Regular', 11)
    y = y_start + h - SAFE*2.8 - 110
    max_w = w - 2*SAFE
    line_h = 15
    words = BLURB.split()
    line = []
    for word in words:
        test = ' '.join(line + [word])
        if c.stringWidth(test, 'LiberationSerif-Regular', 11) <= max_w:
            line.append(word)
        else:
            c.drawCentredString(x_start + w/2, y, ' '.join(line))
            y -= line_h
            line = [word]
    if line:
        c.drawCentredString(x_start + w/2, y, ' '.join(line))

    # bottom band
    c.setFillColor(HexColor('#2D6A9F'))
    bottom_y = y_start + SAFE*0.8
    c.rect(x_start, bottom_y, w, 18, fill=1, stroke=0)
    c.setFont('LiberationSerif-Bold', 9)
    c.setFillColor(HexColor('#F5F0E8'))
    c.drawCentredString(x_start + w/2, bottom_y + 6, 'www.coffeerings.com')
    c.restoreState()

def build_front_page(c, x_start, y_start, w, h):
    c.saveState()
    # place cover image inside safe margin on front
    cover_path = PROJECT / 'cover' / 'authors' / 'alex-rogers-cover-kdp.png'
    c.drawImage(str(cover_path), x_start + SAFE, y_start + BLEED, TEXT_W, TEXT_H, preserveAspectRatio=True, anchor='c')
    c.restoreState()

def build_spine(c, x_start, y_start, w, h):
    c.saveState()
    c.setFillColor(HexColor('#0D1B2A'))
    c.rect(x_start, y_start, w, h, fill=1, stroke=0)
    c.setFillColor(HexColor('#C9862A'))
    c.rect(x_start, y_start + h - 6, w, 6, fill=1, stroke=0)
    c.rotate(90)
    c.setFillColor(HexColor('#F5F0E8'))
    c.setFont('LiberationSerif-Bold', 9)
    c.drawCentredString(y_start + h/2, - (x_start + w + 16), TITLE)
    c.setFont('LiberationSerif-Bold', 7)
    c.drawCentredString(y_start + h/2, - (x_start + w + 30), AUTHOR)
    c.restoreState()

def build_back_cover(c, x_start, y_start, w, h):
    build_back_page(c, x_start, y_start, w, h)

def on_page(c, doc):
    build_front_page(c, BLEED, BLEED, TEXT_W, TEXT_H)
    build_spine(c, BLEED + TEXT_W, BLEED, SPINE, TEXT_H)
    build_back_page(c, BLEED + TEXT_W + SPINE, BLEED, TEXT_W, TEXT_H)

doc = SimpleDocTemplate(str(OUT), pagesize=(WRAP_W, WRAP_H),
                        leftMargin=0, rightMargin=0,
                        topMargin=0, bottomMargin=0)
doc.build([Spacer(1,1)], onFirstPage=on_page, onLaterPages=on_page)
print('Print cover saved:', OUT, 'Size:', (WRAP_W, WRAP_H))
