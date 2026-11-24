# Yuanwushi CX Club — All-Courses PDF Assessment

**Assessment date:** 2026-11-24 (Japan Standard Time)  
**Resource:** https://www.yuanwushi.org/cxclub/qa/all.pdf  
**Parent index:** https://www.yuanwushi.org/cxclub/  
**Assessment status:** Text-extraction review only; original PDF bytes and visual pages not preserved in this assessment.

## Observations

1. The live CX Club index links this resource with the label “下载全部课程PDF版” (download all course PDF version).
2. The PDF's extracted opening table of contents lists lessons 1–16.
3. Immediately after that table, the extracted text lists lessons 17, 18, and 19 as separate numbered entries.
4. The extracted document body begins with “催醒游戏俱乐部 第一课”, includes the second lesson later in the text, and reaches an explicit “催醒游戏俱乐部 第七课” heading at extracted line 8007.
5. The extracted document ends at line 8721 during lesson 7 content. The extraction contains no explicit lesson 8 heading in the body, and searches for “第二十课” and “第二十一课” return no match.
6. The opening contents do not list lessons 20 or 21.

## What this establishes — and what it does not

- The PDF's table of contents is not sufficient evidence that the corresponding lesson bodies are present.
- The available text extraction supports that the document body reaches lesson 7; it does not demonstrate that lesson bodies 8–19 are preserved in this PDF.
- Lessons 20 and 21 are present as individual HTML pages linked from the live CX Club index, but are not listed in the extracted PDF contents.
- This is not a binary integrity or visual-page audit. The PDF must still be downloaded/preserved, hashed, and visually checked page by page before a final completeness decision.

## Required next checks

1. Preserve the exact PDF bytes and calculate SHA-256.
2. Record PDF page count, metadata, file size, and any extraction errors.
3. Inspect every page visually and compare section boundaries against the extracted text.
4. Compare the PDF's actual lesson bodies against the 21 individual HTML lesson pages.
5. Record per-lesson PDF coverage as present, partial, absent, or uncertain; do not infer coverage from the table of contents alone.
6. Preserve the PDF as an original source object; keep this assessment as a separate derived record.

## Provenance

This assessment is based on the public PDF text extraction available through the web reading tool on 2026-11-24, including its opening contents (extracted lines 0–29), the explicit lesson 7 heading (line 8007), the final extracted lines (through 8721), and text searches for lesson 8, 20, and 21 markers. It is not a substitute for the original PDF file.

## Additional per-lesson PDF discovery (2026-11-24)

Search-indexed content for lesson 1 (`/cxclub/lesson1.html`) and lesson 8 (`/cxclub/lesson8.html`) visibly includes the label “下载本课PDF版” (download this lesson PDF). This establishes that at least these two lesson pages expose individual PDF download links in the indexed page text. The exact target `href` values and PDF bytes have not yet been captured. Other lesson pages have not been exhaustively checked for equivalent links; do not infer that only lessons 1 and 8 have separate PDFs.

A supplementary discovery list is maintained at `../record-index/yuanwushi-cxclub-attachment-discovery.csv`. The all-courses PDF assessment above remains separate; these per-lesson links do not resolve the all-courses PDF's incomplete extracted body or contents discrepancy.

## Follow-up: current reader extraction check (2026-11-24)

A recent reader extraction of the linked all-courses PDF exposes 8,721 text lines. Its visible directory lists lessons 1–16 and then separate entries for lessons 17, 18 and 19. Targeted text searches found no “第二十课” or “第二十一课” entries in the extracted text. The extracted text reaches its final lines at 8,721.

This strengthens the documented directory discrepancy against the live CX Club index, which lists lessons 1–21. It does **not** establish that the original PDF binary itself ends at lesson 19: the reader may have omitted or failed to extract pages/content. The original PDF bytes, metadata, page count, rendered pages and a page-by-page visual check remain outstanding.
