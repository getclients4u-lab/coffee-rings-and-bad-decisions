#!/usr/bin/env python3
"""Build KDP-ready EPUB for Coffee Rings and Bad Decisions."""
import os, re
from datetime import date

BASE = '/home/ubuntu/.openclaw-author/coffee-rings-and-bad-decisions'
DRAFTS = os.path.join(BASE, 'drafts')
EXPORTS = os.path.join(BASE, 'exports')
COVER = os.path.join(BASE, 'cover', 'alex-rogers-cover-kdp.png')
OUT_DIR = os.path.join(EXPORTS, 'epub', 'build')
OCF = os.path.join(OUT_DIR, 'OEBPS')
METAINF = os.path.join(OUT_DIR, 'META-INF')
os.makedirs(OCF, exist_ok=True)
os.makedirs(METAINF, exist_ok=True)

TITLE='Coffee Rings and Bad Decisions'
AUTHOR='Alex Rogers'
TODAY=date.today().isoformat()

# 1) mimetype
with open(os.path.join(OUT_DIR, 'mimetype'), 'w') as f:
    f.write('application/epub+zip')

# 2) container.xml
with open(os.path.join(METAINF, 'container.xml'), 'w') as f:
    f.write('''<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>''')

# 3) stylesheet
CSS='''body{font-family: Georgia, serif; line-height:1.7; margin:1em; color:#111;}
h1{font-size:2em; text-align:center; margin:1.5em 0 0.5em;}
h2{font-size:1.6em; margin-top:2em; color:#333;}
h3{font-size:1.3em; margin-top:1.5em; color:#444;}
.top{text-align:center; margin: 3em 0 2em;}
.subtitle{font-style:italic; color:#555; margin-top:0.5em;}
.by{color:#777; margin-top:0.8em;}
.break{page-break-before:always;}
p{margin:0 0 1em;}
blockquote{border-left:3px solid #c9a227; padding-left:1em; font-style:italic; margin-left:1em;}
hr{border:none; border-top:1px solid #ccc; margin:2em 0;}
.center{text-align:center;}
'''
with open(os.path.join(OCF, 'stylesheet.css'), 'w') as f:
    f.write(CSS)

# 4) content helper
def md_to_xhtml(text):
    lines = text.replace('\r\n','\n').split('\n')
    out=[]
    inpara=False
    inblock=False
    for line in lines:
        line=line.rstrip()
        if line.startswith('# '):
            if inpara: out.append('</p>'); inpara=False
            if inblock: out.append('</div>'); inblock=False
            out.append('<h1>'+line[2:]+'</h1>')
        elif line.startswith('## '):
            if inpara: out.append('</p>'); inpara=False
            if inblock: out.append('</div>'); inblock=False
            out.append('<h2>'+line[3:]+'</h2>')
        elif line.startswith('### '):
            if inpara: out.append('</p>'); inpara=False
            if inblock: out.append('</div>'); inblock=False
            out.append('<h3>'+line[4:]+'</h3>')
        elif line.startswith('- '):
            if inpara: out.append('</p>'); inpara=False
            if not inblock: out.append('<div class="bullet">'); inblock=True
            out.append('<p>• '+line[2:]+'</p>')
        elif line.strip()=='---':
            if inpara: out.append('</p>'); inpara=False
            if inblock: out.append('</div>'); inblock=False
            out.append('<hr/>')
        elif line.strip()=='':
            if inpara: out.append('</p>'); inpara=False
            if inblock: out.append('</div>'); inblock=False
        else:
            if not inpara: out.append('<p>'); inpara=True
            out.append(line+' ')
    if inpara: out.append('</p>')
    if inblock: out.append('</div>')
    return '\n'.join(out)

# 5) assemble spine
spine_ids=[]
manifest_parts=[]

front_path=os.path.join(EXPORTS,'front-matter.md')
if os.path.exists(front_path):
    with open(front_path,'r') as f: txt=f.read()
    xhtml=md_to_xhtml(txt)
    with open(os.path.join(OCF,'front-matter.xhtml'),'w') as f:
        f.write(xhtml)
    spine_ids.append('front-matter')
    manifest_parts.append(('front-matter.xhtml', 'Front Matter'))

# Load chapter list robustly
chapters=sorted([f for f in os.listdir(DRAFTS) if re.match(r'chapter-\d+\.md$', f)])
for ch in chapters:
    with open(os.path.join(DRAFTS, ch), 'r') as fh: txt=fh.read()
    xhtml=md_to_xhtml(txt)
    base=ch.replace('.md','')
    with open(os.path.join(OCF, base+'.xhtml'), 'w') as fh:
        fh.write(xhtml)
    spine_ids.append(base)
    num=int(re.search(r'\d+', ch).group())
    title=f'Chapter {num}'
    manifest_parts.append((base+'.xhtml', title))

if os.path.exists(os.path.join(EXPORTS,'acknowledgments.md')):
    with open(os.path.join(EXPORTS,'acknowledgments.md'),'r') as f: txt=f.read()
    xhtml=md_to_xhtml(txt)
    with open(os.path.join(OCF,'acknowledgments.xhtml'),'w') as f: f.write(xhtml)
    spine_ids.append('acknowledgments')
    manifest_parts.append(('acknowledgments.xhtml', 'Acknowledgments'))

if os.path.exists(os.path.join(EXPORTS,'author-bio.md')):
    with open(os.path.join(EXPORTS,'author-bio.md'),'r') as f: txt=f.read()
    xhtml=md_to_xhtml(txt)
    with open(os.path.join(OCF,'author-bio.xhtml'),'w') as f: f.write(xhtml)
    spine_ids.append('author-bio')
    manifest_parts.append(('author-bio.xhtml', 'About the Author'))

# cover page always first
# 6) toc.ncx
toc_items=''.join([f'<navPoint id="{i+1}" playOrder="{i+1}"><navLabel><text>{t}</text></navLabel><content src="{f}"/></navPoint>' for i,(f,t) in enumerate(manifest_parts)])
toc_ncx=f'''<?xml version="1.0" encoding="UTF-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
  <head><meta name="dtb:uid" content="urn:uuid:coffeerings-epub"/><meta name="dtb:depth" content="1"/></head>
  <docTitle><text>{TITLE}</text></docTitle>
  <navMap>{toc_items}</navMap>
</ncx>'''
with open(os.path.join(OCF,'toc.ncx'),'w') as f: f.write(toc_ncx)

# 7) content.opf
manifest_items=''.join([f'<item id="{f}" href="{f}" media-type="application/xhtml+xml"/>\n' for f,_ in manifest_parts])
spine_items=''.join([f'<itemref idref="{i}"/>\n' for i in spine_ids])
cover_media='application/octet-stream' if os.path.exists(COVER) else None

opf=f'''<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="uid">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:title>{TITLE}</dc:title>
    <dc:creator>{AUTHOR}</dc:creator>
    <dc:language>en</dc:language>
    <dc:identifier id="uid">urn:uuid:coffeerings-epub</dc:identifier>
    <dc:date>{TODAY}</dc:date>
    <meta property="dcterms:modified">{TODAY}T00:00:00Z</meta>
  </metadata>
  <manifest>
    {manifest_items}
    <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
    <item id="css" href="stylesheet.css" media-type="text/css"/>
    <item id="nav" href="nav.xhtml" media-type="application/xhtml+xml"/>
  </manifest>
  <spine toc="ncx">
    {spine_items}
  </spine>
  <guide>
    <reference type="text" title="Start" href="front-matter.xhtml"/>
  </guide>
</package>'''
with open(os.path.join(OCF,'content.opf'),'w') as f: f.write(opf)

# 8) nav
nav=f'''<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
<head><title>{TITLE}</title></head>
<body><nav epub:type="toc">
  <ol>{''.join(['<li><a href="'+f+'">'+t+'</a></li>' for f,t in manifest_parts])}</ol>
</nav></body>
</html>'''
with open(os.path.join(OCF,'nav.xhtml'),'w') as f: f.write(nav)

print('EPUB build ready at', OUT_DIR)
