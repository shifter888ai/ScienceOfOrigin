# Original Source Collection Register

**Register version:** 0.1  
**Repository snapshot:** `45de49cb111a378e5baf9eaba847911be9edf18e`  
**Status:** Initial registration candidates; provenance and integrity checks remain pending.

## Purpose

This register identifies the source collection files currently present in `materials/`. It does not decide that different formats are duplicates, and it does not claim that these files represent the entire historical archive.

The repository-wide file manifest is [`FILE-MANIFEST.json`](FILE-MANIFEST.json). It records every file path, byte size, Git blob identifier, and provisional classification at the reviewed commit.

## Candidate source objects

| Provisional source key | Original filename | Format | Size (bytes) | Registration status |
|---|---|---:|---:|---|
| SRC-CAND-001 | `reddit-english-all.txt` | TXT | 1,666,537 | Candidate identified; detailed provenance pending |
| SRC-CAND-002 | `reddit-english-qa.txt` | TXT | 360,078 | Candidate identified; overlap review pending |
| SRC-CAND-003 | `元吾氏集录20210203-1.pdf` | PDF | 24,104,234 | Candidate identified; page and media review pending |
| SRC-CAND-004 | `元吾氏集录20210203-2.pdf` | PDF | 24,517,286 | Candidate identified; page and media review pending |
| SRC-CAND-005 | `元吾氏集录20210203.txt` | TXT | 2,819,410 | Candidate identified; relationship to PDF volumes pending |

These provisional keys are inventory references only. Permanent source IDs should be assigned when the source objects are formally registered under the schema.

## Attribution rule supplied by the project owner

For the identified English and Chinese Q&A collections above, the project owner has instructed that **all answers are authored by YWS**, even when a displayed name is absent or an alias/nickname is used.

Implementation requirements:

- Preserve the source's displayed author name or alias exactly as shown.
- Record canonical answer authorship as YWS for answers in the identified collections.
- Keep questioners and other participants separately attributed.
- Preserve author roles (questioner, answerer, commenter, poster) rather than treating every participant as an author of the answer.
- Do not extend this attribution rule to unrelated sources without evidence.
- If a source boundary or answer attribution is ambiguous, retain the original context and mark the attribution for review rather than guessing.

## Initial record-boundary work completed

The English Q&A collection `materials/reddit-english-qa.txt` has a first structural boundary index at [`record-index/reddit-english-qa-index.csv`](record-index/reddit-english-qa-index.csv).

The source was read as 357,871 characters across 3,682 lines. The boundary pass identified 651 Q&A records, each with one anchored `Q:` and one anchored `A:` marker. It records 1-based inclusive source line ranges, including multiline question and answer spans. This is a navigation/indexing result only; it does not constitute content review, case extraction, or evidence assessment.

The remaining English source checks—including comparison with `reddit-english-all.txt`, original post IDs, timestamps, export provenance, and collection completeness—remain open.

## Initial Chinese compilation page indexing completed

The Chinese text compilation `materials/元吾氏集录20210203.txt` has a page-level index at [`record-index/chinese-compilation-page-index.csv`](record-index/chinese-compilation-page-index.csv), with methodology and cautions in [`record-index/chinese-compilation-page-index-README.md`](record-index/chinese-compilation-page-index-README.md).

The inspected text contains 1,671 explicit page markers (Page 1–1671), across 46,783 source lines and 1,147,327 decoded characters. The index records inclusive source line ranges, extracted text size, first-line excerpt, and date strings found per page. 206 page markers have no extracted nonblank text; these are marked for visual review and are not assumed to represent physically blank PDF pages.

The compilation's opening editorial note says it combines blog, Tieba/forum, and online material. It warns that some online app exchanges may be ordinary Q&A, jokes, irony, context-specific replies, or deliberate bait, and notes that some reposted content was not included. These cautions are retained as source-provided provenance context; they are not independent verification of completeness.

PDF-to-text page comparison, visual inspection, within-page record boundaries, and platform-level provenance remain open.

## Initial Reddit archive structural indexing completed

The English Reddit archive `materials/reddit-english-all.txt` has two navigation indexes:
- [`record-index/reddit-english-all-post-index.csv`](record-index/reddit-english-all-post-index.csv) — 617 post/thread blocks with inclusive line ranges, displayed date, subreddit, original poster, comment-section count, and permalink count.
- [`record-index/reddit-english-all-yws-author-marker-index.csv`](record-index/reddit-english-all-yws-author-marker-index.csv) — 904 exact `Lower-Lingonberry-40:` author-marker locations linked to their containing post and comment section.
- [`record-index/reddit-english-all-README.md`](record-index/reddit-english-all-README.md) — boundary method, counts, and limitations.

The inspected source contains 617 separator-delimited post blocks, 617 date headers (2023-10-29 through 2026-11-18), 772 `--- comments ---` markers, 772 `Source:` permalink lines, and 904 exact YWS author markers. The 904 markers are not assumed to equal 904 complete comments; comment spans and reply relationships require separate analysis.

Both English collections are preserved separately. Their overlap and coverage relationship have not yet been determined.

## Initial English collection overlap comparison completed

A first exact-text comparison is documented in [`record-index/english-reddit-overlap-analysis.md`](record-index/english-reddit-overlap-analysis.md), with a 651-row cross-reference at [`record-index/reddit-english-qa-to-all-overlap.csv`](record-index/reddit-english-qa-to-all-overlap.csv).

After limited normalization of case, whitespace, Markdown emphasis/code markers, and common curly quote/apostrophe variants, 487 of the 651 Q&A answer spans matched one or more indexed `Lower-Lingonberry-40:` author-marker bodies in the all-post archive. Of those, 473 had one exact-text match and 14 had multiple matching locations. 164 had no exact match located by this method.

This establishes substantial textual overlap, not equivalence or completeness. No-match results do not prove absence from the all-post archive; text may be edited, split, truncated, or formatted differently. Both original collections remain separately preserved. Do not deduplicate or delete either source based on this pass.

## Source-level checks still required

### English Reddit collections

- Determine exact platform, account/community, collection period, retrieval method, and export date if documented.
- Identify internal record boundaries and stable post/comment IDs.
- Compare `reddit-english-all.txt` and `reddit-english-qa.txt` for overlap and omissions.
- Preserve both files even if one is later found to be a subset or derivative of the other.
- Confirm whether timestamps are original platform timestamps, export timestamps, or normalized dates.

### Chinese compilation

- Inspect both PDFs page by page, including images, diagrams, tables, footnotes, and page numbering.
- Compare the TXT compilation against both PDF volumes.
- Identify whether the TXT is a full transcription, OCR output, edited compilation, or a different edition; do not assume.
- Record page-to-text mapping, missing pages, duplicated passages, and conversion uncertainty.
- Preserve original Chinese wording and source context.

## Integrity and provenance

The repository manifest records Git blob SHA values, which identify Git objects. They are **not SHA-256 file checksums**.

SHA-256 checksums, exact file bytes, original source URLs, acquisition dates, publication dates, rights status, and independent backup status have not yet been verified in this register. These fields must be added only after the corresponding checks are completed.

## Next actions

- [ ] Register each source using the full schema in [`SCHEMA.md`](SCHEMA.md).
- [ ] Obtain and record SHA-256 checksums for exact source bytes.
- [ ] Preserve an independent archival copy with access and rights controls.
- [ ] Inspect source structure and define reliable record boundaries.
- [ ] Compare English collection overlap without deleting either source.
- [ ] Compare Chinese PDF pages with the TXT version, including visual content.
- [ ] Create source-linked record entries only after locators and context rules are verified.
- [ ] Extend the inventory to other repositories, project uploads, external archives, local collections, and media.

**Preserve every original version. Establish what each file is before extracting what it contains.**


## Weibo original-post export — initial structural index

The file `materials/weibo-1760432301-combined-originals-2026-11-24T06-35-03-529Z.txt` has been preserved as the original Xiaowei Memory text export. Its embedded header identifies Weibo UID `1760432301` (元吾氏), 765 original-post entries, 148 monthly groups, and a stated date span of August 2010–November 2026. The export contains 160 pages and states that it includes only original content saved locally on the user's device.

A structural record index is available at [`record-index/weibo-originals-record-index.csv`](record-index/weibo-originals-record-index.csv), with methodology and limitations in [`record-index/weibo-originals-record-index-README.md`](record-index/weibo-originals-record-index-README.md). The indexing pass detected all 765 sequential export markers (01–765), with no numbering gaps. It records export timestamps (Beijing Time), source line ranges, extracted text, visible URLs, and explicit omitted-image notes.

This is a navigation/indexing result only. It does not establish completeness against the live Weibo account. The export is text-only and notes omitted images; binary images/videos, reposts, comments, deleted/private content, and unsaved historical posts are not established as captured. Topic classification is intentionally deferred to a separate reviewable layer. The original export remains unchanged.
