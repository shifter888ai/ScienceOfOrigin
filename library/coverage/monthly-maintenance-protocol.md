# Monthly Source Maintenance Protocol

**Adopted:** 2026-11-24  
**Applies to:** Yuanwushi, Awakenology, Reddit, and Weibo source collections  
**Governing principle:** Preserve everything first. Discover and organize relationships through research.

## 1. Cadence

Run one consolidated review for all four sources every calendar month. Complete the review within the first five calendar days of the following month where access and source availability permit. Record the actual capture date and time; never backdate a capture.

Monthly review is the reconciliation cycle, not a reason to wait before preserving new material. Capture newly published or newly accessible original material as soon as practical, then include it in the next monthly reconciliation.

### CX Club event-driven capture

CX Club is an active weekly teaching source. The owner reports that the weekly Wednesday lessons serve approximately 1,200 students; this audience figure is owner-supplied context, not an independently verified website metric.

- Wednesday is the teaching schedule, not a guaranteed online publication deadline. The owner reports that the team may publish weekly materials several days late; this is normal.
- Check the CX Club index on/after Wednesday and recheck during a rolling seven-day publication window.
- Do not classify a lesson as missing or overdue immediately after Wednesday. Only flag it as not yet published after the seven-day grace window, and retain that as a time-stamped observation rather than assuming permanent absence.
- Once a lesson appears, capture its original page and all linked downloadable files/media promptly; preserve each lesson as its own immutable source object.
- At month-end, reconcile lesson numbering, actual publication dates, lesson dates, monthly counts, index links, PDFs, embedded images, and revisions.
- Record cancellations, skipped weeks, delayed publication, unpublished lessons, or inaccessible material distinctly.

The public Yuanwushi homepage currently advertises a weekly Wednesday 20:00 Beijing-time public lesson. Actual publication and lesson date should be taken from the lesson record itself, not inferred from the schedule.

## 2. Monthly work by source

### Yuanwushi website

- Recheck the homepage, article collection, Wiki/Q&A pagination, CX Club index and lesson pages, Reddit archive portal, RSS/sitemaps if available, and all linked files.
- Capture new and changed original pages and attachments; preserve previous versions.
- Reconcile article/Q&A/lesson counts using clearly defined counting units.
- Prioritize the 21-lesson CX Club sequence and the all-courses PDF discrepancy, then complete Wiki and full-site route discovery.
- Maintain attribution, source language, timestamps, and rights/privacy notes.

### Awakenology website

- Check awakenology.org, awakenology.space, www aliases, language indexes, robots.txt, sitemap.xml, and repository changes.
- Reconcile the live route set against the repository's 136 sitemap entries and 148 HTML-file snapshot; investigate new, removed, redirected, or changed routes.
- Capture page originals and linked images, PDFs, videos, and other assets; record source revision and checksums.
- Preserve domain/redirect/canonical differences as observations until directly verified.

### Reddit

- Treat `materials/reddit-english-all.txt` as the primary human-readable original-library source. It was produced by the team's automated extraction script specifically for human reading and is intended to be read and researched directly, not replaced by a normalized database or profile-page scrape.
- Preserve the primary TXT unchanged. Do not silently normalize, rewrite, translate, split, or regenerate it in place. New script runs or source exports must be saved as additive, dated source versions.
- Keep post/comment indexes, native IDs, permalink reconciliations, topic tags, translations, and analytical interpretations as separate derived layers that point back to the original TXT and exact source locations where available.
- Record extraction provenance for each future run: capture date/time, script name and version or commit, configuration, input scope/date range, account identity, output filename, and SHA-256. Preserve the script/configuration or a stable version reference when the team can provide it.
- Recheck the source account's comments view, the Yuanwushi Reddit archive portal, and available monthly pages/downloads as supplementary discovery and verification sources. A profile view is not a replacement for the primary reader-facing archive.
- Reconcile additions and discrepancies using native Reddit post IDs and comment IDs/permalinks wherever available. Do not rely on title or text similarity alone to establish identity.
- The official Reddit account-data export may be obtained as an independent completeness benchmark. It is supplementary verification, not a replacement for the human-readable original library.
- Track original author comments, third-party replies, deleted/unavailable records, edits, and media as distinct record types. Do not infer account-wide completeness from a single profile-feed slice or from a displayed “Showing all comments” label without an explicit total or exhausted pagination evidence.
- Preserve privacy and attribution; public visibility does not automatically grant republication rights.

### Weibo

- Recheck account history and profile counters, and obtain a new original-post export when available.
- Compare new export records with the prior immutable export; preserve each export separately.
- The owner explains that Xiaowei Memory automatically filters out forwarded/reposted items. Therefore, the local original-post export is expected to be smaller than the profile's aggregate 936-post counter; do not treat the difference as a missing-record count.
- Reconcile the export against the original-post category/history, not the aggregate profile counter. Keep reposts, comments, deleted/private posts, and other account activity as separate categories.
- Recover image/video binaries and thumbnails item by item; record parent post number, native permalink, media URL, type, capture method/time, checksum, and recovery status.
- Record the Xiaowei Memory filtering behavior as owner-supplied workflow context until independently verified from the tool's own documentation or output.

## 3. Preservation and versioning rules

1. Never overwrite an original export, page capture, attachment, or prior monthly snapshot.
2. Store each capture as a new object/version with a stable identifier and source URL.
3. Calculate SHA-256 for every preserved binary or exact text capture where technically possible.
4. Keep raw originals separate from normalized text, indexes, translations, topic tags, and analysis.
5. Link every attachment/media object to its parent page or post.
6. Record source timezone and distinguish source-published time from capture time.
7. Record inaccessible, deleted, private, changed, and not-yet-checked items separately.
8. Do not infer equivalence from similar counts; reconcile record identities.
9. Respect authentication, access controls, licensing, attribution, participant privacy, and platform terms.

## 4. Monthly register and status

Use monthly-update-register.csv to record one row per source per monthly cycle. Link detailed inventories, capture logs, reconciliation reports, and unresolved gaps. Use the status vocabulary in README.md; a monthly review can remain partial or blocked.

A monthly cycle is not complete merely because all four rows have been updated. Mark a source verified-with-gaps only after the defined monthly delta has been checked and remaining gaps are explicit. The overall source collection may be certified complete-within-defined-scope only when its full scope and completion gates are satisfied.

## 5. Monthly checklist

- [ ] Record review window, capture date/time, and source identity.
- [ ] Discover new records and changed routes.
- [ ] Preserve new originals and attachments as immutable objects.
- [ ] Calculate checksums and record provenance.
- [ ] Reconcile counts and individual identities using explicit counting units.
- [ ] Update source-specific indexes and coverage status.
- [ ] Record rights, privacy, access, and attribution constraints.
- [ ] Publish a concise monthly delta report and list unresolved gaps.

## 6. Source-owner workflow clarifications (2026-11-24)

- **CX Club publication lag:** the owner reports several days of delay between the Wednesday lesson and publication of its weekly materials is normal. Use a seven-day rolling grace window; do not label a lesson missing merely because it is absent on Wednesday or Thursday.
- **Weibo export filter:** the owner reports Xiaowei Memory automatically filters forwarded posts. The 765 locally exported original posts therefore should not be compared directly with the 936 aggregate profile count. The 171-count arithmetic difference is not a missing-original estimate. Verify export coverage against the original-post category/history.

## 7. Reddit original-library decision (2026-11-24)

The owner confirms that `materials/reddit-english-all.txt` was extracted by an engineer on the team using an automated script and was purposely designed for human readers. The owner approves using this file directly as the primary original-library source for the Reddit collection.

This is a source-architecture decision, not a declaration that the file is a complete account-wide export. The current 617 post/thread blocks, permalink lines, author markers, and one 36-comment profile-feed slice are observations with distinct counting units. Completeness remains open until the extraction's input scope and provenance are documented and the source is reconciled against independent evidence.

The primary TXT is preserved as the reader-facing source. Indexes, structured records, topic classifications, translations, cross-source matches, and research interpretations remain separate derived materials. Preserve all future versions additively; never overwrite the primary file or prior captures.
