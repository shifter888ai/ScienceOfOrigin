# Source Completion Program — Coverage Baseline

**Baseline date:** 2026-11-24 (Japan Standard Time)  
**Status:** Initial evidence-based baseline; none of the four sources is certified complete.  
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
- The live CX Club index exposes 21 individual lesson links (July–November 2026), with lesson 22 described as upcoming. The 21 URLs and index titles/dates are recorded in [yuanwushi-cxclub-lesson-index.csv](yuanwushi-cxclub-lesson-index.csv).
- The index links a single “download all courses PDF” resource at `https://www.yuanwushi.org/cxclub/qa/all.pdf`. Its extracted table of contents lists lessons 1–16 and then separate entries for lessons 17–19, but the available extracted body ends during lesson 7; it has no lesson 20 or 21 entry. This mismatch is documented in [yuanwushi-cxclub-pdf-assessment.md](yuanwushi-cxclub-pdf-assessment.md). The original PDF bytes and visual pages still require preservation and page-by-page verification.
- The index URL inventory is now established, but lesson-page originals, the linked PDF bytes, embedded images/attachments, a full-site crawl, and Wiki capture have not yet been preserved.
- Search-engine discovery is not equivalent to a source capture or full crawl.

### Awakenology website

- Repository: `https://github.com/shifter888ai/awakenology`.
- Recursive Git tree at commit `05523aec14c286bce397678b8a213cca1fc29563` contained 823 entries, including 148 HTML files and page assets, scripts, tests, documentation, and internal tools.
- Repository `sitemap.xml` contains 136 URLs, all now recorded in [awakenology-sitemap-url-inventory.csv](awakenology-sitemap-url-inventory.csv). A path-level comparison matched all 136 sitemap URLs to HTML routes in the reviewed repository tree snapshot.
- Twelve HTML routes were not in the sitemap. Source review now classifies them in [awakenology-nonsitemap-route-review.csv](awakenology-nonsitemap-route-review.csv) and [awakenology-nonsitemap-route-review.md](awakenology-nonsitemap-route-review.md): 1 custom 404, 1 experimental ASK model lab, 3 public utility routes (AI Search, Ask, Search), 4 editor/authoring tools, and 3 prototype asset fragments. No item in this set currently appears to be an omitted public article. This is a repository-source classification, not live HTTP/access-control verification.
- Repository `robots.txt` points to `https://awakenology.space/sitemap.xml` and disallows editor/auth/API routes. The sitemap is a discovery list, not proof that all historical or live resources are captured.
- Next checks: compare `.org`, `.space`, and `www` aliases and redirects; verify live status for all 136 sitemap URLs plus the 12 classified routes; inventory every linked asset/document/video; compare Git history and live routes; preserve exact source files and relevant rendered captures.
- The repository tree is not itself a complete live-site crawl or a historical archive.

### Reddit account archive

- Primary portal: `https://yuanwushi.org/reddit/`; the Reddit profile page is provenance/reference only and must not be separately re-collected as a duplicate.
- The portal currently displays monthly groups from 2023-10 through 2026-08. The visible monthly counts sum to 607 entries.
- Existing repository text collections are separate source objects: `materials/reddit-english-all.txt` (617 post/thread blocks) and `materials/reddit-english-qa.txt` (651 Q&A records).
- The portal's visible 607 monthly entries, 617 post/thread blocks, and 651 Q&A records are different counting units or coverage snapshots until reconciled. Do not infer that one count proves completeness.
- Existing indexes and overlap analysis remain useful, but account-wide comment completeness, replies, deleted/unavailable records, media, date boundaries, and export freshness have not been fully verified.

### Weibo account archive

- Preserved text export: `materials/weibo-1760432301-combined-originals-2026-11-24T06-35-03-529Z.txt`.
- Export contains 765 sequential original-post records (001–765), dated 2010-08-09 through 2026-11-23, with no numbering gaps in the export.
- A connected-browser snapshot of the account timeline showed a top post titled “空间是什么”, matching the title of export record 765; the visible permalink was `https://weibo.com/1760432301/RsLldnd80`. The same profile snapshot displayed `全部微博（936）`; this is not directly comparable with the export's 765 locally saved originals, but it is an account-level reconciliation lead.
- The live post exposed a video permalink, `https://video.weibo.com/show?fid=1034:5368550857310263`, a visible thumbnail filename, and a player duration of 01:55. These are locators/observations only; the video binary has not been preserved. See [weibo-live-media-followup.csv](../record-index/weibo-live-media-followup.csv).
- These observations do not establish a complete account-history reconciliation.
- The export states it includes only original posts saved locally. This does not establish complete account-history coverage.
- The derived structural index, provisional topic index, and media-reference locator index are navigation layers, not additional originals.
- Media omissions are noted in the export; binary image/video recovery, deleted or unsaved posts, comments, reposts, and account-history reconciliation remain outstanding.

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

1. Yuanwushi site: map all routes and attachments; prioritize Wiki, CX Club and Reddit archive; resolve the 16-PDF-lessons versus 21-indexed-lessons discrepancy.
2. Awakenology: reconcile all domains, 136 sitemap URLs, 148 HTML routes, assets, linked resources, and historical Git versions.
3. Reddit: reconcile the portal's monthly listing with both existing TXT datasets and source-account history; do not duplicate the profile collection.
4. Weibo: reconcile export against the source account and recover media item by item.
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
