# Source Format Comparison — 2026-11-25

## Chinese compilation: two PDFs vs TXT

- TXT page markers: 1,671 (Page 1–1671)
- PDF page count: 1,671
- PDF volumes: materials/元吾氏集录20210203-1.pdf (1100 pages), materials/元吾氏集录20210203-2.pdf (571 pages)
- TXT pages without extracted nonblank text: 206
- PDF pages without extractable text: 206
- Contact sheets created for visual inspection: 18
- OCR method: tesseract chi_sim+eng --psm 6
- Image-only PDF pages with non-empty OCR output: 192 / 206
- Pages with at least 10 recognized Han characters: 143 / 206
- Raw OCR characters recovered (unreviewed): 63,773
- Page-comparison rows: 1,671

### Page comparison status counts

- both-no-extracted-text: 206
- exact-normalized-match: 1,455
- high-similarity: 10 (normalized similarity 0.9804–0.9955)

Similarity is computed after Unicode NFKC normalization and whitespace removal. It is a triage measure, not proof of transcription fidelity. Page-number alignment assumes TXT Page N corresponds to combined PDF page N; volume offsets and inserted cover pages must be checked before interpreting low similarity as omission.
Contact sheets are review aids only. OCR is a machine-generated derivative and has not been manually corrected; a blank OCR result does not prove a page is blank. The 10-Han-character threshold is only a screening measure, not a quality guarantee.
Manual overview review of all 18 contact sheets found mixed image-only content: chat/message screenshots and other text-bearing images, illustrations/diagrams, and some apparently blank or near-blank pages. Page-by-page classification and OCR correction remain open.

## Entropy assessment: DOCX vs RTF

- DOCX extracted characters: 25,432
- RTF extracted characters: 29,292
- Normalized text similarity: 0.9377
- Exact normalized text equality: no
- Body comparison: The only normalized text difference is an RTF-only table-of-contents block of 3,266 characters inserted after the opening 99 characters. After excluding that block, the DOCX and RTF body text matches exactly.
- DOCX structure: 957 paragraphs, 0 tables, 0 inline shapes, 0 embedded media files, 1 section

DOCX extraction preserves paragraph and table-cell text in document-body order. RTF text was extracted with striprtf. Similarity does not assess layout, images, formulas, footnotes, comments, or semantic equivalence. Inspect differences and embedded objects before deciding whether one format faithfully represents the other.

The page-level OCR text and CSV are preserved as separate derived files under library/derived/. Detailed extracted PDF text and contact sheets remain in the workflow artifact source-format-review. Original files remain unchanged.
