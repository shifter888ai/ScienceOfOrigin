# Original Source Collection Register

**Register version:** 0.2  
**Latest repository commit reviewed:** `78ee76b1b349bb0ba2abc47aefc5ded9d2aac755`  
**Status:** Reconciled 2026-11-25. Reddit/Weibo supplied TXT scopes are owner-confirmed complete; Awakenology is physically archived; Yuanwushi's initial crawl passed independent checksums and its 2,659-record listing reconciles; Science of Consciousness uploads are registered. Other comparisons and live-source checks remain open.

## Purpose

This register identifies source collection files and their defined scopes. Provisional candidate rows are retained as historical inventory notes; the owner-confirmed registrations appended below supersede their earlier pending status for Reddit and Weibo supplied TXT archives. Completeness statements apply to the defined supplied-file scopes.

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
| SRC-AWK-REPO | `materials/awakenology/` (physical tracked-file archive) | Full Awakenology Git repository tree at `05523aec14c286bce397678b8a213cca1fc29563` | Complete physical copy of the pinned repository snapshot: 648 blobs / 51,750,456 bytes | Update from upstream `main` monthly; preserve prior snapshots and manifests |

**Awakenology snapshot implementation note:** the library contains an ordinary tracked-file copy under `materials/awakenology/`, with 648 Git blobs across 823 tree entries (51,750,456 bytes), matching the pinned upstream tree. This is a physical copy within the Science of Origin repository, not a submodule pointer. Live-site parity and future upstream changes remain separate checks.


## Authoritative source-status reconciliation — 2026-11-25

This section supersedes earlier status statements in this register wherever they conflict with the dated findings below. Earlier notes are retained as historical records of the state at the time they were written; they are not the current status.

### Reddit and Weibo supplied TXT archives

The project owner confirms that the two Reddit TXT files and the Weibo TXT export are complete, manually extracted and checked for their intended scopes. Their status is **complete for those owner-defined supplied-file scopes**. Existing structural indexes are derived navigation aids and do not redefine archive completeness. Monthly updates are additive; preserve each prior source version unchanged. Optional media recovery and platform-wide comparison are separate workstreams.

### Awakenology repository — physical archive verified

The current Science of Origin repository contains an ordinary tracked-file copy under `materials/awakenology/`, not a Git submodule pointer. The current repository tree contains 648 file blobs under that path, totaling 51,750,456 bytes, across 823 tree entries. The subtree tree SHA `6fd6ffabeb09b671f15b4b81e27a378b5f5a6bd1` exactly matches the root tree SHA of pinned upstream commit `05523aec14c286bce397678b8a213cca1fc29563`. The files are stored as regular Git blobs in this repository. The earlier submodule descriptions in this register and related records are obsolete and superseded.

Scope limitation: this verifies the pinned repository tree, not live Awakenology website parity, historical upstream revisions, external linked resources, or future changes. Monthly upstream comparison and additive snapshot history remain required.

### Yuanwushi website — initial crawl and independent checksum audit passed

**Source ID:** `SRC-YWS-WEB`. The 2026-11-25 snapshot is stored on branch `automation/yuanwushi-crawl` at commit `e9f8f7cadf6e9aa31063a781e1708f38d4c2c3ae`. Its capture manifest contains 1,001 records; 993 files are stored at 993 unique paths, totaling 307,557,680 bytes. The independent checksum audit verified all 993 stored files: zero missing files, invalid paths, duplicate path groups, size mismatches, or SHA-256 mismatches. The audit workflow run is [45554125468](https://github.com/shifter888ai/ScienceOfOrigin/actions/runs/45554125468).

The crawl captured 106 article pages, 133 Wiki/Q&A pagination pages, 21 CX Club lessons, 727 linked attachments/media items, and two PDFs. The independent pagination reconciliation confirms that all 133 page parameters (1–133) are present and that the captured listing contains 2,659 Q&A record links, 2,659 unique record IDs, and zero duplicate links, matching the source index's displayed total of 2,659. See the page-level counts in `library/coverage/yuanwushi-wiki-page-record-counts-2026-11-25.csv`.

Seven linked resources returned HTTP 404 during the 2026-11-25 capture (one audio file and six gallery images):
- `https://www.yuanwushi.org/media/cc0-audio/t-rex-roar.mp3`
- `https://www.yuanwushi.org/gallery/ad1.png?ts=1782918978`
- `https://www.yuanwushi.org/gallery_gen/b52fa1d35f2d1619a1f59346867b078e_fit.png?ts=1782918978`
- `https://www.yuanwushi.org/gallery_gen/2651c57393beec7145101a09f294103b_fit.png?ts=1782918978`
- `https://www.yuanwushi.org/gallery/ad3.png?ts=1782918978`
- `https://www.yuanwushi.org/gallery_gen/df80bfe5abe2c2024c726a1b44b6c4ca_fit.png?ts=1782918978`
- `https://www.yuanwushi.org/gallery_gen/1a31ccfafcc0abc14fa37c5d2236feed_898x490_fit.png?ts=1782918978`

The 993 stored files pass independent checksums, and the 2,659 listing IDs reconcile to the displayed total. These checks do not independently verify every linked Q&A detail-page body, embedded media, deleted/private records, or all historical/unlinked resources. The seven 404 resources remain individually recorded pending alternate-source recovery checks or explicit disposition.

### Science of Consciousness project uploads — originals registered

Two UTF-8 TXT source documents supplied in this project workspace on 2026-11-25 have been copied unchanged into `materials/science-of-consciousness/`:

| Source ID | Original filename | Repository path | SHA-256 |
|---|---|---|---|
| SRC-SOC-FRAMEWORK | `Science-of-Consciousness.txt` | `materials/science-of-consciousness/Science-of-Consciousness.txt` | `0955131bcdfadffcf59cafbeb5fd6f97cb4fd163137f40e1c950ee6a19c44a53` |
| SRC-SOC-ARCH | `Science-of-Consciousness-—-Research-Architecture.txt` | `materials/science-of-consciousness/Science-of-Consciousness-—-Research-Architecture.txt` | `cded63335372b921c7fda4922d046410cb96ffee020063e75b201c1f6ed2e4f0` |

These are source documents, not a merged or normalized replacement. Their contents are related but not identical in scope: the project-description document includes the research scope, four core fields, Spectrum/Spectra methodology, the Spectrum of Things = Spectrum of Consciousness research objective, five applications, principles, and vision; the architecture outline is a shorter hierarchy. Preserve both originals. No scientific claims in either file are independently validated by this registration.

### Chinese compilation and Entropy assessment sources — review still open

The Chinese compilation remains represented by two original PDF volumes and one TXT file. The TXT index has 1,671 page markers; 206 markers have no extracted nonblank text and require visual PDF review. PDF-to-TXT page equivalence, visual content, and provenance are not yet established.

The Entropy assessment DOCX and RTF remain separate original source objects. The RTF has a derived structural index; DOCX/RTF equivalence, completeness, tables, embedded media, and formatting fidelity remain unverified. Do not treat the RTF extraction as a substitute for inspecting the DOCX.

### Repository-wide integrity and collection boundary

The current `main` tree at commit `78ee76b1b349bb0ba2abc47aefc5ded9d2aac755` contains 876 tracked file blobs totaling 113,056,244 bytes. This is a tree inventory count, not a SHA-256 audit. The repository-wide manifest and checksums must be regenerated/verified against this current commit; the earlier manifest snapshot is stale. External, private, offline, historical, and other-account sources have not been comprehensively inventoried, so the entire library must not yet be declared complete.

**Preservation rule:** keep original source files immutable; store indexes, extraction outputs, comparisons, and interpretations as separately identified derived layers.
