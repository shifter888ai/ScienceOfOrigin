# Source Completion Program — Coverage Baseline

**Baseline date:** 2026-11-24 (Japan Standard Time)  
**Current disposition (2026-11-25):** Initial Library Assembly is complete within the identified and owner-confirmed source baseline, with the seven Yuanwushi 404 resources explicitly bounded as unavailable/unverified. Library Coverage and Maintenance remains ongoing. The current [Completion Dashboard](../COMPLETION-DASHBOARD.md), [Initial Library Assembly Decision](2026-11-25-initial-library-assembly-decision.md), and [source coverage status](source-coverage-status.csv) supersede older checkpoint language below.  
**Governing principle:** Preserve everything first. Discover and organize relationships through research.

## Purpose

This directory tracks completion of the four priority source collections:

1. Yuanwushi website and its priority resources.
2. Awakenology website and its source repository.
3. Reddit account comments, using the Yuanwushi Reddit archive as the primary archive portal.
4. Weibo account original posts and recoverable media.

A source is not complete merely because a portal page, sitemap, export, or repository is available. Completion requires a defined scope, source-by-source coverage reconciliation, preservation of original objects and attachments where available, integrity checks, provenance, rights/privacy review, and an explicit gap report.

## Current baseline

See [source-coverage-status.csv](source-coverage-status.csv) for machine-readable status and [capture-log.csv](capture-log.csv) for the observations recorded in this baseline.

### Yuanwushi website

- Priority entry points: `https://www.yuanwushi.org/`, `/wiki.html`, `/article-1.html`, `/cxclub/`, and `/reddit/`.
- Search-indexed `article-1.html` currently reports 106 articles in the collection index. The Wiki Q&A index reports 2,659 total Q&A records and has paginated views (for example, `wiki.html?p=3` and `p=4`). These are discovery counts, not proof that all underlying article/Q&A records or attachments have been preserved.
- The live CX Club index exposes 21 individual lesson links (July–November 2026), with lesson 22 described as upcoming. A second index route, `/cxclub/index.html`, is also indexed and appears to mirror the root index; alias/canonical behavior has not been verified. The 21 URLs and index titles/dates are recorded in [yuanwushi-cxclub-lesson-index.csv](yuanwushi-cxclub-lesson-index.csv). Search-index excerpts are now recorded for all 21 lessons, including lesson 21; these excerpts remain discovery evidence, not original page captures.
- The index links a “download all courses PDF” resource at `https://www.yuanwushi.org/cxclub/qa/all.pdf`. Separate lesson-page PDF links are also visible in search-indexed content for lessons 1 and 8; their exact target URLs have not yet been captured. These are recorded in [yuanwushi-cxclub-attachment-discovery.csv](../record-index/yuanwushi-cxclub-attachment-discovery.csv). Its extracted table of contents lists lessons 1–16 and then separate entries for lessons 17–19, but the available extracted body ends during lesson 7; it has no lesson 20 or 21 entry. This mismatch is documented in [yuanwushi-cxclub-pdf-assessment.md](yuanwushi-cxclub-pdf-assessment.md). The original PDF bytes and visual pages still require preservation and page-by-page verification.
- The index URL inventory is now established, but lesson-page originals, the linked PDF bytes, embedded images/attachments, a full-site crawl, and Wiki capture have not yet been preserved.
- Search-engine discovery is not equivalent to a source capture or full crawl.

### Awakenology repository

- Upstream repository: `https://github.com/shifter888ai/awakenology`.
- The 2026-11-25 snapshot is pinned to commit `05523aec14c286bce397678b8a213cca1fc29563`: 648 file blobs, 823 recursive tree entries, 51,750,456 bytes.
- The library records a pinned Git submodule reference and a complete path/mode/Git-blob-SHA/size manifest in [awakenology-repository-snapshot-2026-11-25.md](awakenology-repository-snapshot-2026-11-25.md) and [awakenology-repository-snapshot-2026-11-25.csv](awakenology-repository-snapshot-2026-11-25.csv).
- This is a reproducible repository-tree snapshot reference, not an independent physical duplication of all blobs. Live website route parity, domain aliases, historical versions, and external linked resources remain separate from the repository snapshot.

### Reddit account archive

- The project owner confirms that `materials/reddit-english-all.txt` and `materials/reddit-english-qa.txt` are complete TXT archives for their intended Reddit collection scopes. Both were manually extracted and checked for completion.
- Treat the supplied files as complete source archives. The 617 post/thread blocks, 772 comment-section/permalink locators, 1,096 exact author-marker occurrences, and 651 Q&A records are existing structural index results, not reasons to reopen archive completeness.
- Preserve both TXT files unchanged. Each month, add one new manually checked version as a separate source object and regenerate the derived indexes against that exact version.
- Earlier portal/profile comparisons remain supplementary observations only; they are not completion gates for the owner-confirmed TXT archives.

### Weibo account archive

- The project owner confirms that the supplied TXT export is complete for its intended Weibo original-post scope and was manually extracted and checked for completion.
- Treat the supplied TXT as a complete source archive. Do not use the aggregate profile counter or limited live timeline snapshots to reopen its completeness status.
- Existing derived layers include a 765-record structural index, 160-page coverage index, topic index, and media-reference locators. The TXT remains unchanged.
- Image/video binaries represented by omission notes or media locators are a separate media-preservation layer; their absence does not make the owner-confirmed TXT archive incomplete.
- Each month, add the new manually checked TXT export as a separate immutable version, compare it with the previous version, and regenerate indexes against the exact new source.

## Completion criteria

For each source, record:

1. Scope and identity (account/site/domain, owner, canonical URLs, aliases).
2. Discovery set (sitemaps, navigation, archive indexes, exports, API data, linked resources).
3. Expected item count and actual captured item count, with counting unit clearly defined.
4. Original bytes/files or exact content captures, plus SHA-256 where available.
5. Attachments and embedded media, each linked to its parent record.
6. Date range and gaps; inaccessible, deleted, private, or missing items distinguished.
7. Duplicate/mirror/version relationships without deleting originals.
8. Provenance, capture method/time, language, attribution, licence, privacy and republication status.
9. Verification report and explicit residual gaps.
10. A dated completion decision with scope limitations.

## Work sequence

1. Yuanwushi site: map all routes and attachments; prioritize Wiki, CX Club, linked files, and media capture.
2. Awakenology: update the pinned Git repository snapshot monthly; live-domain crawling and route checks are separate optional work.
3. Reddit: add the new manually checked monthly TXT versions, preserve prior versions, and regenerate source-linked indexes.
4. Weibo: add the new manually checked monthly TXT version, preserve prior versions, and regenerate source-linked indexes. Track optional media recovery separately.
5. Awakenology: update the pinned Git repository commit and full file-tree manifest monthly.
5. Cross-source deduplication and relationship indexing only after original capture and identity checks.

## Rights and privacy

The user's statement of ownership over their original authored material is recorded in project context. It must not be generalized to third-party comments, participant submissions, platform content, or embedded works. Preserve attribution and source context; review rights, privacy, and access conditions before public redistribution. Do not bypass authentication or access controls.

## Status vocabulary

- `not-started`: no source-specific inventory yet.
- `discovery`: source map or expected item set is being built.
- `partial-capture`: some originals captured; coverage not reconciled.
- `reconciliation`: compare expected and captured objects.
- `verified-with-gaps`: scope checked; remaining gaps explicitly listed.
- `complete-within-defined-scope`: all defined items accounted for and validated; scope and exclusions published.

A status applies only to the stated scope and date. Never use “complete” without a defined scope.


## Monthly maintenance

All four source collections now follow the [Monthly Source Maintenance Protocol](monthly-maintenance-protocol.md). The [monthly update register](monthly-update-register.csv) records the November 2026 checkpoint and will hold one row per source per monthly cycle.

Monthly reconciliation is the standard for Yuanwushi, Awakenology, Reddit, and Weibo. New material should be captured as soon as practical rather than waiting for month-end. CX Club has an additional event-driven rule: capture each new Wednesday lesson and its linked files promptly, then reconcile the month's lesson sequence, dates, PDFs, and media during the monthly review. The owner reports approximately 1,200 students; this is owner-supplied context, not a verified website metric.

The November 2026 register is the dated baseline checkpoint. Current completion status is governed by the Completion Dashboard and Initial Library Assembly Decision. New material is handled additively; the seven Yuanwushi 404s remain unavailable/unverified, not recovered.


## Awakenology repository manifests

The 2026-11-24 repository snapshot manifests are `awakenology-repository-tree-manifest-2026-11-24.csv`, `awakenology-sitemap-route-to-blob-manifest-2026-11-24.csv`, and `awakenology-repository-tree-assessment-2026-11-24.md`. They map the 136 sitemap routes to repository blob objects and extend the non-sitemap route review with blob provenance. See the assessment for scope and live-domain limitations.


## Yuanwushi article index

The live homepage's six article categories are indexed in `yuanwushi-article-collection-index-2026-11-24.csv` (106 unique article URLs). The scope and link-only capture limitation are documented in `yuanwushi-article-collection-index-2026-11-24.md`.


## Current baseline decision — 2026-11-25

The initial identified-source baseline has been assembled and integrity-checked. This decision is bounded to the sources listed in [Initial Library Assembly Decision](2026-11-25-initial-library-assembly-decision.md). It includes the owner-confirmed Reddit and Weibo TXT scopes, the physical Awakenology repository snapshot, the checksum-verified Yuanwushi crawl with seven explicitly unavailable/unverified 404s, the owner-confirmed Chinese TXT and Entropy RTF scopes, and the two separate Science of Consciousness TXT uploads.

Important corrections to historical checkpoint text in this README:

- Awakenology is physically copied as ordinary tracked files under `materials/awakenology/`; it is not a submodule pointer.
- Yuanwushi's 993 stored files and 2,659 Wiki IDs have passed the independent checks described in the dashboard. Older discovery-stage statements that say no crawl or Wiki capture exists are historical checkpoints, not current status.
- The seven 404 candidate files are not recovered originals. Their identity remains unverified.
- The Chinese TXT and Entropy RTF owner-defined scopes are complete; the PDFs and DOCX are supplemental.
- Live Awakenology domain parity, private/offline/historical material discovery, and monthly updates are separate ongoing coverage/maintenance tasks, not proof that the identified baseline was never assembled.

Do not infer from this baseline that all possible material has been discovered. Apply the defined-scope completion rule and preserve future discoveries additively.
