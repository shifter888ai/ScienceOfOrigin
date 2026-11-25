# Original Source Collection Register

**Register version:** 0.2  
**Main commit audited:** `61e9649dd29a3131c37e674ac61ceb5880eb4656`  
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

### Chinese compilation — page comparison and OCR review

The original source set consists of two PDF volumes and one TXT compilation. Volume 1 contains 1,100 pages and volume 2 contains 571 pages (1,671 total), matching the TXT's 1,671 page markers.

The 2026-11-25 normalized page comparison found:
- 1,455 exact page matches.
- 10 high-similarity pages (0.9804–0.9955); differences are concentrated in spacing, line breaks, and emoji extraction.
- 206 pages with no extractable text in either the PDF text layer or TXT page segment.

All 18 contact sheets covering the 206 image-only pages were visually triaged. They contain a mixture of chat/message screenshots and other text-bearing images, diagrams/illustrations, and some apparently blank or near-blank pages. They must not be treated as 206 empty pages.

Tesseract OCR (chi_sim+eng, page segmentation mode 6) produced non-empty output on 192/206 pages; 143 pages contain at least 10 recognized Han characters. The 63,773 raw OCR characters are uncorrected machine output, not verified transcription. The page-level OCR TXT and CSV are preserved separately under `library/derived/`; see `library/derived/README.md`. The page comparison CSV and report are under `library/coverage/`.

Remaining work: review the 10 high-similarity pages; verify OCR against original page images; classify image-only pages page by page; resolve any page-number offsets, missing visual content, or transcription uncertainty. Preserve both PDF originals and the TXT original unchanged.

## Integrity and provenance

A repository-wide integrity baseline is now recorded in `library/repository-integrity-manifest.json` and `library/repository-integrity-report.md`. It covers the current main source tree and the final Yuanwushi archive branch, recomputes Git blob SHA-1 values from exact object bytes, and records SHA-256 for every unique blob. The 2026-11-25 run hashed 1,534 unique blobs across 2,767 path/ref records, with zero Git blob SHA-1 mismatches and no Git LFS pointers. The generated manifest/report paths are excluded to avoid self-reference. This is a branch-tip audit, not a scan of unreachable Git history, external LFS payloads, or resources outside the selected branches.

The two Science of Consciousness uploads have SHA-256 values matching the originals supplied in this project workspace. The Yuanwushi snapshot has its own independent SHA-256 audit of all 993 stored files. Source rights, private/offline material, external resources, and independent off-repository backups remain separate provenance and access-review work.

## Next actions

- Review and correct the 206-page OCR derivative against the original PDFs; prioritize pages with recognized Chinese text and the 10 high-similarity TXT/PDF comparisons.
- Complete visual/format comparison of the Entropy DOCX and RTF, including the RTF-only table of contents and any layout or metadata differences.
- Investigate the seven Yuanwushi 404 resources using the separate recovery-candidate register; do not treat same-path candidates as verified originals.
- Complete Awakenology live-site parity, alias/redirect, asset, and historical-version review.
- Inventory additional external, private, offline, historical, and other-repository sources; review rights and privacy before copying.
- Continue monthly additive source updates and regenerate derived indexes against exact immutable source versions.

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
| SRC-CAND-007 | `materials/熵值检测点RR部分.docx` | DOCX | 1,764,873 | `509d7dc53ba656bcc4b7f19631d162986b0a9119` | Inspected: 957 paragraphs; no tables, inline shapes, or embedded media; body matches RTF after excluding TOC |
| SRC-CAND-008 | `materials/熵值检测点RR部分.rtf` | RTF | 812,389 | `4554f3c8fbdf64a76f4fbbfc4a51dac10de05657` | Text extracted; includes a 3,266-character TOC absent from DOCX; body text matches DOCX after excluding TOC |

The formats are not text-identical: the RTF contains a 3,266-character table-of-contents block absent from the DOCX. After excluding that block, their normalized body text matches exactly. This does not establish identical formatting, layout, metadata, or provenance. Both originals remain preserved.

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
| SRC-AWK-REPO | `materials/awakenology/` (physical tracked-file archive) | Full Awakenology Git repository tree at `05523aec14c286bce397678b8a213cca1fc29563` | Complete physical copy: 648 blobs / 51,750,456 bytes; subtree SHA exactly matches upstream root tree SHA `6fd6ffabeb09b671f15b4b81e27a378b5f5a6bd1` | Update from upstream `main` monthly; preserve prior snapshots and manifests |

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

### Yuanwushi 404 recovery candidates — separate, unverified layer

The 2026-11-25 crawl recorded seven HTTP 404 resources. Six image files referenced by Yuanwushi article-13-6710 have same-relative-path/name candidates in the Awakenology physical archive. The T-Rex audio referenced by article-5-6634 has a candidate copy from `mdn/interactive-examples` at pinned commit `13024db581b08fae11a0ca229497198b9b0534e7`, whose repository declares CC0 1.0 Universal. The candidate files, sizes, SHA-256 values, and provenance are recorded under `materials/yuanwushi/recovery-candidates/`. None is byte-verified against the unavailable Yuanwushi original; they remain candidates and do not replace the original crawl.

### Science of Consciousness project uploads — originals registered

Two UTF-8 TXT source documents supplied in this project workspace on 2026-11-25 have been copied unchanged into `materials/science-of-consciousness/`:

| Source ID | Original filename | Repository path | SHA-256 |
|---|---|---|---|
| SRC-SOC-FRAMEWORK | `Science-of-Consciousness.txt` | `materials/science-of-consciousness/Science-of-Consciousness.txt` | `0955131bcdfadffcf59cafbeb5fd6f97cb4fd163137f40e1c950ee6a19c44a53` |
| SRC-SOC-ARCH | `Science-of-Consciousness-—-Research-Architecture.txt` | `materials/science-of-consciousness/Science-of-Consciousness-—-Research-Architecture.txt` | `cded63335372b921c7fda4922d046410cb96ffee020063e75b201c1f6ed2e4f0` |

These are source documents, not a merged or normalized replacement. Their contents are related but not identical in scope: the project-description document includes the research scope, four core fields, Spectrum/Spectra methodology, the Spectrum of Things = Spectrum of Consciousness research objective, five applications, principles, and vision; the architecture outline is a shorter hierarchy. Preserve both originals. No scientific claims in either file are independently validated by this registration.

### Chinese compilation and Entropy assessment — current comparison results

**Source ID:** `SRC-CHINESE-COMPILATION`. The two PDFs contain 1,671 pages total (1,100 + 571), matching the TXT's 1,671 page markers. The page-level comparison found 1,455 exact normalized matches, 10 high-similarity matches (0.9804–0.9955), and 206 pages with no extractable text in either source. All 18 contact sheets were visually triaged; the image-only pages contain screenshots/text-bearing images, diagrams/illustrations, and some apparently blank/near-blank pages. Tesseract OCR produced non-empty output on 192/206 pages; 143 pages contain at least 10 recognized Han characters. The 63,773 raw OCR characters are preserved as an uncorrected derivative under `library/derived/`. See `library/coverage/source-format-comparison-2026-11-25.md` and `library/coverage/chinese-compilation-pdf-text-comparison-2026-11-25.csv`. Human OCR verification and page-by-page visual classification remain open.

**Source ID:** `SRC-ENTROPY-RR`. The DOCX has 957 paragraphs, no tables, inline shapes, or embedded media. The RTF includes a 3,266-character table-of-contents block absent from the DOCX; after excluding this block, normalized body text matches exactly. The formats are not otherwise established as layout-identical. Review of page layout, metadata, and the TOC difference remains open.

### Repository-wide integrity and collection boundary

The active SHA-256 manifest and report are `library/repository-integrity-manifest.json` and `library/repository-integrity-report.md`. The 2026-11-25 audit run `45560330817` covered main commit `61e9649dd29a3131c37e674ac61ceb5880eb4656` and the final Yuanwushi archive branch `e9f8f7cadf6e9aa31063a781e1708f38d4c2c3ae`: 897 main blobs / 114,185,422 bytes; 1,870 Yuanwushi-branch blobs / 421,098,213 bytes; 1,534 unique Git blobs hashed; 402,538,820 unique-blob bytes; 2,767 path/ref records; zero Git blob SHA-1 mismatches; no Git LFS pointers. Generated manifest/report paths are excluded from the inventory. This is a tracked branch-tip audit, not an audit of unreachable Git history or external resources.

The Awakenology physical subtree (648 blobs / 51,750,456 bytes) has a tree SHA exactly matching the pinned upstream commit's root tree SHA. The two Science of Consciousness TXT uploads have SHA-256 values matching the originals supplied in this project workspace. The Yuanwushi snapshot has an independent SHA-256 audit of all 993 stored files. Historical automation branches were compared by path and blob identity; no unique source paths were found outside main, except an obsolete `.gitmodules` entry in an early Awakenology branch.

The four priority acquisition milestones are complete within their owner-defined scopes: Reddit supplied TXT, Weibo supplied TXT, Awakenology pinned repository snapshot, and Yuanwushi initial website crawl. This does not prove that all external, private, offline, historical, or other-account sources have been discovered. Rights/privacy review and live-source parity remain open.

**Preservation rule:** keep original source files immutable; store indexes, extraction outputs, comparisons, OCR, and interpretations as separately identified derived layers.


## Owner clarification: canonical source files — 2026-11-25

The project owner has clarified the intended source scope for two collections. This section supersedes any earlier statement that treats the supplemental formats as required for source completeness.

### Chinese compilation — TXT is the complete source

The owner confirms that `materials/元吾氏集录20210203.txt` alone is the complete source for the Chinese compilation at this stage. The two PDF volumes contain additional images, but those images are not important to the current research scope and are not a completion requirement. Preserve the PDFs as supplemental reference material; do not require OCR, page-image classification, or PDF/TXT visual equivalence before marking the TXT source complete. The prior page comparison and OCR outputs remain optional derived aids, not blockers to source completion.

### Entropy assessment points — RTF is the complete source

The owner confirms that `materials/熵值检测点RR部分.rtf` alone is the complete source for the Entropy assessment points. The DOCX contains the same substantive content and no images; the RTF is the canonical complete source for current use. Preserve the DOCX as a supplementary duplicate-format copy, but do not treat its comparison, layout, or the RTF table-of-contents difference as an outstanding source-completeness gate. The RTF-derived index remains a separate navigation aid.

These are owner-defined scope decisions. They do not delete, overwrite, or discard either PDF or the DOCX. All original files remain preserved unchanged.
