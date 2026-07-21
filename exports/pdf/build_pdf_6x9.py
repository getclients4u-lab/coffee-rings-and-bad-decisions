#!/usr/bin/env python3
"""Build KDP-compliant 6x9 manuscript PDF matching print cover trim."""
from reportlab.lib.pagesizes import *
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from pathlib import Path

PROJECT = Path('/home/ubuntu/.openclaw-author/coffee-rings-and-bad-decisions')
DRAFTS = PROJECT / 'drafts'
EXPORTS = PROJECT / 'exports' / 'pdf'
OUT = EXPORTS / 'coffee-rings-and-bad-decisions-6x9.pdf'
FRONT = PROJECT / 'exports' / 'front-matter.md'
ACK = PROJECT / 'exports' / 'acknowledgments.md'
BIO = PROJECT / 'exports' / 'author-bio.md'

FONT_DIR = Path('/usr/share/fonts/truetype/liberation')
pdfmetrics.registerFont(TTFont('LiberationSerif-Regular', str(FONT_DIR / 'LiberationSerif-Regular.ttf')))
pdfmetrics.registerFont(TTFont('LiberationSerif-Bold',    str(FONT_DIR / 'LiberationSerif-Bold.ttf')))
pdfmetrics.registerFont(TTFont('LiberationSerif-Italic',  str(FONT_DIR / 'LiberationSerif-Italic.ttf')))

# 6x9 trim with 0.5 inch margins (safe for KDP)
TRIM_W = 6 * inch
TRIM_H = 9 * inch
MARGIN = 0.5 * inch

PAGE_W = TRIM_W + 2 * MARGIN
PAGE_H = TRIM_H + 2 * MARGIN

TITLE_STYLE = ParagraphStyle('Title', fontName='LiberationSerif-Bold', fontSize=26, leading=32, alignment=TA_CENTER, spaceAfter=14, textColor=HexColor('#1a1713'))
SUBTITLE_STYLE = ParagraphStyle('SubTitle', fontName='LiberationSerif-Italic', fontSize=16, leading=20, alignment=TA_CENTER, spaceAfter=10, textColor=HexColor('#332e28'))
CHAPTER_HEAD_STYLE = ParagraphStyle('ChapterHead', fontName='LiberationSerif-Bold', fontSize=16, leading=20, alignment=TA_CENTER, spaceBefore=24, spaceAfter=16, textColor=HexColor('#1a1713'))
BODY_STYLE = ParagraphStyle('Body', fontName='LiberationSerif-Regular', fontSize=10.5, leading=13.5, alignment=TA_JUSTIFY, spaceAfter=8, firstLineIndent=20)
ITALIC_STYLE = ParagraphStyle('Italic', fontName='LiberationSerif-Italic', fontSize=11, leading=15, alignment=TA_CENTER, spaceAfter=12)

def read_md(path: Path):
    text = path.read_text()
    lines = text.splitlines()
    out = []
    for line in lines:
        if line.startswith('# '):
            continue
        if line.strip() == '':
            out.append('<br/>')
        else:
            out.append(line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))
    return '<br/>'.join(out)

def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFont('LiberationSerif-Regular', 8)
    if doc.page > 2:
        canvas.drawCentredString(PAGE_W/2, 0.35*inch, str(doc.page - 2))
    canvas.restoreState()

def build():
    doc = SimpleDocTemplate(str(OUT), pagesize=(PAGE_W, PAGE_H),
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=MARGIN, bottomMargin=MARGIN)
    story = []
    story.append(Spacer(1, 100))
    story.append(Paragraph('Coffee Rings and Bad Decisions', TITLE_STYLE))
    story.append(Paragraph('by Alex Rogers', SUBTITLE_STYLE))
    story.append(PageBreak())
    story.append(Paragraph(read_md(FRONT), ITALIC_STYLE))
    story.append(Spacer(1, 30))
    story.append(Paragraph('A NOVEL', ITALIC_STYLE))

    for i in range(1, 23):
        ch = DRAFTS / f'chapter-{i}.md'
        title_line = ch.read_text().splitlines()[0].strip().replace('# ', '')
        story.append(PageBreak())
        story.append(Paragraph(title_line, CHAPTER_HEAD_STYLE))
        story.append(Paragraph(read_md(ch), BODY_STYLE))

    story.append(PageBreak())
    story.append(Paragraph('Epilogue', CHAPTER_HEAD_STYLE))
    story.append(Paragraph(read_md(DRAFTS / 'epilogue.md'), BODY_STYLE))

    story.append(PageBreak())
    story.append(Paragraph('Acknowledgments', CHAPTER_HEAD_STYLE))
    story.append(Paragraph(read_md(ACK), ITALIC_STYLE))

    story.append(PageBreak())
    story.append(Paragraph('About the Author', CHAPTER_HEAD_STYLE))
    story.append(Paragraph(read_md(BIO), ITALIC_STYLE))

    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
    print(f'Built: {OUT.name}')

build()
