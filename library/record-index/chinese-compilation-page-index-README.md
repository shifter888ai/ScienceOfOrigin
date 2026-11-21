# Chinese Compilation — Page-Level Source Index

**Source:** `materials/元吾氏集录20210203.txt`  
**Source Git blob SHA:** `051b2a12490cacf3dc96e24cb99858ececa6bff0`  
**Observed size:** 1,147,327 characters  
**Observed line count:** 46,783  
**Page markers:** 1,671 (Page 1 through Page 1671)  
**Status:** Structural page index; page content has not been fully reviewed.

## Files

- [`chinese-compilation-page-index.csv`](chinese-compilation-page-index.csv) — one row per source page marker, with inclusive line locators, extracted text length, first-line excerpt, and date strings detected on that page.

## Boundary method and checks

Page boundaries are defined by explicit source markers in the text file: `--- Page N ---`. The index records the source line containing each page marker through the line before the next marker. Source line numbers are 1-based and inclusive.

The full text was inspected through the repository's Git blob content. The observed structure contains:

- 1,671 page markers, numbered consecutively from 1 through 1671.
- 1,465 pages with extracted nonblank text.
- 206 page markers with no extracted nonblank text.
- 763 pages containing at least one date-like string under the index's date pattern.

**Important:** A page marker with no extracted text is not evidence that the corresponding PDF page is physically blank. It may contain an image, diagram, screenshot, scanned text, or other material omitted from the text extraction. Such pages are marked `no-extracted-text-visual-review-required`, not discarded or treated as empty originals.

## Source structure and editorial cautions recorded in the compilation

The opening page describes the compilation as combining material from blog, Tieba/forum, and online sources. It explains that blog material was organized using the blog's own categories and that forum material includes posts and replies. It also warns that online app conversations may be ordinary Q&A, jokes, ironic replies, context-specific exchanges, or deliberate bait, and asks readers to judge the context. It notes that some reposted material on WeChat, Weibo, and blogs was not included in this compilation.

These are statements made by the compilation itself. They are important provenance and interpretation cautions, not independent verification of the underlying platforms or the completeness of the collection.

## Date handling

The CSV preserves date strings as they appear in the text and does not normalize ambiguous formats or infer a date for an undated page. A page may contain multiple dates from different posts or replies; the dates are not necessarily the page's publication date or a single record's date.

## What remains open

- Compare the text file page-by-page with both original PDF volumes.
- Inspect all pages marked as having no extracted text, plus pages where diagrams, screenshots, tables, or layout may have been lost.
- Determine the exact PDF-to-text page mapping and whether page numbering aligns in both volumes.
- Identify source boundaries within pages; a page may contain multiple posts or fragments, and one post may continue across pages.
- Preserve platform, author, date, and conversational context at record level where the source supports them.
- Do not treat this page index as a case index or topic classification.

**The page index makes the text navigable. It does not replace the PDFs or establish that all visual and contextual information has been captured.**
