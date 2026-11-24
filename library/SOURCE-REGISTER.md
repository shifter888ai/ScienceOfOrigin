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


## Weibo derived discovery layers

The original Weibo export remains preserved unchanged. Additional discovery files are maintained under `library/record-index/`:

- `weibo-originals-topic-index.csv` — provisional multi-label keyword classification with matched-keyword evidence; not a verified interpretation.
- `weibo-media-reference-index.csv` — locator inventory for posts containing URLs or media-related notes/markers; not proof that binary media has been downloaded.
- `weibo-topic-classification-README.md` — tag definitions, counts, method, and limitations.

These are derived research aids and must remain distinct from the source record. Topic tags require review before being used for quantitative conclusions. Media retrieval must be tracked separately with per-item provenance and outcome.


## Entropy assessment points — RR source versions

Two versions of the source titled **熵值检测点RR部分** are present in `materials/` and are registered separately:

| Provisional source key | Repository path | Format | Size (bytes) | Git blob SHA | Status |
|---|---|---|---:|---|---|
| SRC-CAND-007 | `materials/熵值检测点RR部分.docx` | DOCX | 1,764,873 | `509d7dc53ba656bcc4b7f19631d162986b0a9119` | Identified; binary content not inspected |
| SRC-CAND-008 | `materials/熵值检测点RR部分.rtf` | RTF | 812,389 | `4554f3c8fbdf64a76f4fbbfc4a51dac10de05657` | Text extracted; structural index prepared |

Do not assume that the DOCX and RTF are byte-identical, text-identical, or equally complete. The RTF is the currently readable version used for the content index. Both originals remain preserved.

### Source-derived metadata from the readable RTF

- Title: `熵值检测点` (Entropy Measurement Points).
- Version shown: v1.1; the document also retains v1.0 notes.
- Update note: v1.1 says one sample dataset was deleted and a second batch was received on 2026-06-08, concerning several subdivisions in the first area.
- Download period stated in the document: 2025-09-03 to 2025-09-30; it says this covered nine `互催` documents.
- Information source field: `南山`.
- The document's first overview section attributes the measurement-point system's production source to `超级灵联盟`; this is recorded as a statement in the source, not independently verified authorship or provenance.
- The source describes nine main areas and one auxiliary area. Its overview states approximately 1,800 main measurement points, with further totals described as tens of thousands and subdivisions as over one hundred thousand. These are source-stated figures, not independently audited counts.
- The source says scoring is not uniformly percentage-based and can exceed conventional percentage ranges at higher stages. Preserve this as the source's scoring description; do not normalize it into a standard scale.

A navigable outline and extraction notes are in [`record-index/entropy-rr-assessment-points-index.md`](record-index/entropy-rr-assessment-points-index.md). The index is derived from the RTF text and its table of contents; it is not a replacement for the original document or a complete point-by-point transcription.

### Interpretation boundary

The document contains assessment descriptions and comparative entries labelled `RR`, `88`, and `JJ`. Those labels and values are preserved as source content. They must not be silently reinterpreted as standardized measurements, validated scores, or independently comparable scales. Any later analysis should cite the exact source section and distinguish source statements, participant assessments, and our own research interpretations.


## Owner-confirmed archive registrations — 2026-11-25

The following source scopes are formally registered under the owner's completeness instructions. These determinations apply to the supplied archive objects and their stated scopes; they do not silently extend to unrelated platform content.

| Source ID | Source object | Format / scope | Status | Monthly maintenance |
|---|---|---|---|---|
| SRC-RED-COMMENTS | `materials/reddit-english-all.txt` and `materials/reddit-english-qa.txt` | TXT; complete Reddit archives for their intended collection scopes | Complete per owner; manually extracted and checked | Add one new checked version monthly; preserve prior versions |
| SRC-WEIBO-POSTS | `materials/weibo-1760432301-combined-originals-2026-11-24T06-35-03-529Z.txt` | TXT; complete Weibo original-post archive for its intended scope | Complete per owner; manually extracted and checked | Add one new checked version monthly; preserve prior versions |
| SRC-AWK-REPO | `materials/awakenology` (pinned Git submodule reference) | Full Awakenology Git repository tree at `05523aec14c286bce397678b8a213cca1fc29563` | Complete pinned repository snapshot reference; see limitation below | Update from upstream `main` monthly and preserve prior commit references |

**Awakenology snapshot implementation note:** the library stores a Git submodule pointer pinned to the exact upstream commit plus a complete path/mode/Git-blob-SHA/size manifest. This makes the repository snapshot reproducible and traceable, but it is not an independent physical duplication of every upstream blob. The source repository remains the content host for the submodule checkout.
