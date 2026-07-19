#!/bin/bash
# Compile full manuscript for KDP upload
# Requires pandoc: https://pandoc.org/installing.html
# Usage: cd ~/.openclaw-author/coffee-rings-and-bad-decisions/exports && bash compose-manuscript.sh

PROJECT=../../drafts
OUT=KindleExport/OEBPS/manuscript.xhtml

mkdir -p "$(dirname "$OUT")"

echo '<?xml version="1.0" encoding="UTF-8"?>' > "$OUT"
echo '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">' >> "$OUT"
echo '<html xmlns="http://www.w3.org/1999/xhtml">' >> "$OUT"
echo '<head><title>Coffee Rings and Bad Decisions</title><meta charset="UTF-8"/></head>' >> "$OUT"
echo '<body>' >> "$OUT"

for f in "$PROJECT"/front-matter.md "$PROJECT"/*.md "$PROJECT"/../front-matter.md "$PROJECT"/../acknowledgments.md "$PROJECT"/../author-bio.md; do
  [ -f "$f" ] || continue
  echo "<!-- === $f ===" >> "$OUT"
  if command -v pandoc &>/dev/null; then
    pandoc -f markdown -t html5 "$f" >> "$OUT" 2>/dev/null || cat "$f" >> "$OUT"
  else
    # basic markdown -> xhtml fallback
    sed 's/^# /<h1>/g; s/^## /<h2>/g; s/^\*/\<p\>/g; s/---/<hr\/>/g' "$f" >> "$OUT"
  fi
  echo " -->" >> "$OUT"
done

echo '</body></html>' >> "$OUT"
echo "Manuscript written to $OUT"
