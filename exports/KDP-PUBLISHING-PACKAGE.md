# Coffee Rings and Bad Decisions — Amazon KDP Publishing Package

**Status:** Ready for KDP upload

**Files in this package:**
```
~/.openclaw-author/coffee-rings-and-bad-decisions/
├── config.yaml
├── outline.md
├── drafts/
│   ├── front-matter.md
│   ├── chapter-1.md … chapter-22.md
│   ├── epilogue.md
│   └── acknowledgments.md | author-bio.md
├── cover/
│   ├── ebook-cover-kdp.png   (2560x1600)
│   └── ebook-cover.png       (1024x576 original)
└── exports/
    ├── kdp-metadata.md       ← Upload this first
    ├── front-matter.md
    ├── acknowledgments.md
    ├── author-bio.md
    └── compose-manuscript.sh
```

**Word count:** 22,874
**Estimated pages:** ~22,874 / 250 = ~230 pages
**Price recommendation:** $3.99 eBook, $12.99 paperback

---

## KDP Upload Checklist

### 1. eBook
- **Title:** Coffee Rings and Bad Decisions
- **Subtitle:** A Novel
- **Author name:** [Your name here]
- **Description:** Copy from `exports/kdp-metadata.md`
- **Keywords:** Copy 7 keywords from metadata doc
- **Categories:** 
  - Romance > Contemporary
  - Fiction > Romance
  - Romance > New Adult
- **Cover:** Upload `cover/ebook-cover-kdp.png`
- **Manuscript:** Run `exports/compose-manuscript.sh`, then create EPUB via Kindle Create or Calibre

### 2. Paperback
- **Trim size:** 5.5" x 8.5" (standard trade paperback)
- **Cover:** Use `cover/ebook-cover.png` as base; extend to 1600x2400 with spine
- **Interior:** Same manuscript, page ordering via Kindle Create
- **Price:** $12.99

### 3. Kindle Unlimited
- Enroll in KDP Select
- Upload eBook
- Set KU enrollment to 90 days minimum

---

## Book Cover Details

**eBook cover:** `cover/ebook-cover-kdp.png`
- Dimensions: 2560x1600
- Format: PNG
- Style: Warm coffee shop scene, two people, amber + navy, golden hour
- Title: "Coffee Rings and Bad Decisions" in serif
- Subtitle: "A Novel"
- Author name: [Placeholder — swap before upload]

**To swap author name:** Regenerate with image_generate including your name in the prompt, or edit post-generation.

---

## Keywords

1. coffee shop romance
2. small business love story
3. Portland romantic comedy
4. enemies to lovers romance
5. indie coffee shop novel
6. workplace romance
7. banter-filled romcom

---

## Categories

**Primary:** Romance > Contemporary
**Secondary:** Fiction > Romance > General
**Tertiary:** Romance > New Adult

---

## Author Placeholder

**Bio:** Writer of coffee shop romances. Swapped in `exports/author-bio.md`.

**Website:** Set up at your domain or via KDP Author Central
**Social:** Instagram/Twitter handles
**Newsletter:** Optional — use MailerLite or ConvertKit

---

## Next Steps

1. Replace "Author Placeholder" everywhere in cover/author-bio
2. Regenerate cover with real author name
3. Run `compose-manuscript.sh` and convert via:
   - **Kindle Create** (recommended, KDP's free tool)
   - **Calibre** (open source alternative)
   - **Pandoc** (if installed): `pandoc manuscript.xhtml -o book.epub`
4. Upload eBook + cover to KDP
5. Upload paperback interior + cover (separate file)
6. Set price, KU enrollment, categories
7. Hit Publish

---

Generated: 2026-07-19
