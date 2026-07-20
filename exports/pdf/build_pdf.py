#!/usr/bin/env python3
"""Build KDP-compliant manuscript PDF from chapter files.
Order: front matter -> ch1..ch22 -> epilogue -> back matter
Letter size 8.5x11, 11pt Liberation Serif, 14pt leading, page numbers in footer after front matter.
"""
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pathlib import Path

PROJECT = Path('/home/ubuntu/.openclaw-author/coffee-rings-and-bad-decisions')
DRAFTS = PROJECT / 'drafts'
EXPORTS = PROJECT / 'exports' / 'pdf'
OUT = EXPORTS / 'coffee-rings-and-bad-decisions.pdf'
FRONT = PROJECT / 'exports' / 'front-matter.md'
ACK = PROJECT / 'exports' / 'acknowledgments.md'
BIO = PROJECT / 'exports' / 'author-bio.md'

FONT_DIR = Path('/usr/share/fonts/truetype/liberation')
pdfmetrics.registerFont(TTFont('LiberationSerif-Regular', str(FONT_DIR / 'LiberationSerif-Regular.ttf')))
pdfmetrics.registerFont(TTFont('LiberationSerif-Bold',    str(FONT_DIR / 'LiberationSerif-Bold.ttf')))
pdfmetrics.registerFont(TTFont('LiberationSerif-Italic',  str(FONT_DIR / 'LiberationSerif-Italic.ttf')))

PAGE_W, PAGE_H = letter
MARGIN = 1*inch

TITLE_STYLE = ParagraphStyle('Title', fontName='LiberationSerif-Bold', fontSize=28, leading=34, alignment=TA_CENTER, spaceAfter=18)
SUBTITLE_STYLE = ParagraphStyle('SubTitle', fontName='LiberationSerif-Italic', fontSize=18, leading=22, alignment=TA_CENTER, spaceAfter=12)
CHAPTER_HEAD_STYLE = ParagraphStyle('ChapterHead', fontName='LiberationSerif-Bold', fontSize=18, leading=22, alignment=TA_CENTER, spaceBefore=32, spaceAfter=20, textColor=(0x1a, 0x17, 0x13))
BODY_STYLE = ParagraphStyle('Body', fontName='LiberationSerif-Regular', fontSize=11, leading=14, alignment=TA_LEFT, spaceAfter=10, firstLineIndent=24)
ITALIC_STYLE = ParagraphStyle('Italic', fontName='LiberationSerif-Italic', fontSize=12, leading=16, alignment=TA_CENTER, spaceAfter=14)
TAGLINE_STYLE = ParagraphStyle('Tagline', fontName='LiberationSerif-Italic', fontSize=11, leading=14, alignment=TA_CENTER, spaceBefore=24, spaceAfter=24)

def read_md(path: Path):
    lines = path.read_text().splitlines()
    out = []
    for line in lines:
        if line.startswith('# '):
            continue
        if line.strip() == '':
            out.append('<br/>')
        else:
            out.append(line)
    return '<br/>'.join(out)

def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFont('LiberationSerif-Regular', 9)
    if doc.page > 2:
        canvas.drawCentredString(PAGE_W/2, 0.6*inch, str(doc.page - 2))
    canvas.restoreState()

def build():
    doc = SimpleDocTemplate(str(OUT), pagesize=letter,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=MARGIN, bottomMargin=MARGIN)
    story = []

    # Front matter (pages 1–2)
    story.append(Spacer(1, 120))
    story.append(Paragraph('Coffee Rings and Bad Decisions', TITLE_STYLE))
    story.append(Paragraph('by Alex Rogers', SUBTITLE_STYLE))
    story.append(PageBreak())
    story.append(Paragraph(read_md(FRONT), ITALIC_STYLE))
    story.append(Spacer(1, 40))
    story.append(Paragraph('A NOVEL', TAGLINE_STYLE))

    # Chapters 1–22
    for i in range(1, 23):
        ch = DRAFTS / f'chapter-{i}.md'
        title_line = ch.read_text().splitlines()[0].strip().replace('# ', '')
        story.append(PageBreak())
        story.append(Paragraph(title_line, CHAPTER_HEAD_STYLE))
        story.append(Paragraph(read_md(ch), BODY_STYLE))

    # Epilogue
    story.append(PageBreak())
    story.append(Paragraph('Epilogue', CHAPTER_HEAD_STYLE))
    story.append(Paragraph(read_md(DRAFTS / 'epilogue.md'), BODY_STYLE))

    # Back matter
    story.append(PageBreak())
    story.append(Paragraph('Acknowledgments', CHAPTER_HEAD_STYLE))
    story.append(Paragraph(read_md(ACK), ITALIC_STYLE))
    story.append(PageBreak())
    story.append(Paragraph('About the Author', CHAPTER_HEAD_STYLE))
    story.append(Paragraph(read_md(BIO), ITALIC_STYLE))

    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)

    import re
    try:
        import PyPDF2
        with open(OUT, 'rb') as f:
            pages = len(PyPDF2.PdfReader(f).pages)
        print(f'Built: {OUT.name} ({pages} pages)')
        return pages
    except Exception:
        print(f'Built: {OUT.name}')
        return None

if __name__ == '__main__':
    build()
