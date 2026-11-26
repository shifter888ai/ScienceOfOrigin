# 熵值检测点 v1.1 — RTF Layout Verification

**Primary source:** `materials/熵值检测点RR部分.rtf`  
**RTF Git blob SHA:** `4554f3c8fbdf64a76f4fbbfc4a51dac10de05657`  
**Verification date:** 2026-11-26

## 1. Text-run transcription check

The RTF was parsed at its nested text-run level, retaining visible text while skipping formatting/control groups, bookmark boundary metadata and field-instruction text. The appendix begins after the visible `附录：互催原文档` marker. All **2,151** non-empty lines in `entropy-assessment-body-transcription-v1.1.md` were found in the original RTF text-run sequence, in the same order. No transcription line was missing in this comparison.

This is a text-content/order check. It does not reconstruct fonts, colors, emphasis, page layout or rendered page breaks.

## 2. TOC page-locator check

- The source review's top-level TOC inventory contains **114** headings.
- **113** body headings match those top-level TOC titles after punctuation/spacing normalization.
- Their page locators were compared with the RTF's own TOC hyperlink-result entries: **113** matched entries have a page locator and no mismatch was found.
- The one unresolved title difference remains `实践中的复盘能力` in the TOC versus `实践中的实时复盘能力` in the body. Neither wording is substituted for the other.

## 3. Assessment-label recognition correction

The initial register used an overly strict label detector: it required the exact standalone label and a colon on the next line. Four source-format variations were therefore misreported as incomplete sets:

- `,RR` at L1357
- `88,` at L1789
- `,RR` at L1993
- `JJ` at L0924 followed by `：大概` at L0925, where the colon/value begin on the next text run

After recognizing these source forms without altering the transcription, the RTF contains **375** point/aggregate assessment blocks: **125 RR**, **125 88**, and **125 JJ**. All **123** point headings with individual assessment blocks have a complete RR/88/JJ set. There are no incomplete point-level sets in this pass.

The literal source forms remain visible in the transcription and are recorded in the corrected point-level register. A standalone `JJ` appearing later in a comment (L0928) is retained as comment text, not treated as another score label, because no colon follows it. The corrected parser starts a new score block only when a recognized label is followed by a colon on the same or next text run.

## 4. Contextual aggregate blocks

Six blocks previously labelled “unheaded” are now retained in two explicit contexts:

1. **Zone 1 opening overview** — RR/88/JJ at L0027–L0039, following the Zone 1 overview and preceding the five smaller points.
2. **Zone 1 Part 3 aggregate** — RR/88/JJ at L0444–L0452, following the explicit source note `可以测一下这部分总的数值`.

These six blocks are not individual point scores and are not attached to a point heading.

## 5. Remaining limitations

- The RTF text-run order and TOC page locators have been checked. The original visual page rendering has not been independently compared screenshot-by-screenshot.
- The DOCX counterpart `materials/熵值检测点RR部分.docx` has not been directly inspected in this pass. Its GitHub blob is binary and the available text-file reader did not return its contents. No DOCX equivalence claim is made.
- The 224 body-heading records and 375 assessment blocks are an extraction register, not a complete count of all source-reported 1,800 main points or 100,000+ subdivisions.
- No score meaning, shared unit, directionality, calibration method, validity or comparability is inferred.
