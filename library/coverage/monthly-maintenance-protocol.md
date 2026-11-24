# Monthly Source Maintenance Protocol

**Adopted:** 2026-11-24  
**Applies to:** Yuanwushi, Awakenology, Reddit, and Weibo source collections  
**Governing principle:** Preserve everything first. Discover and organize relationships through research.

## 1. Cadence

Run one consolidated maintenance cycle every calendar month. Reddit and Weibo receive new manually checked TXT archives; Awakenology receives a Git repository snapshot update; Yuanwushi receives a separate web-crawling review. Complete the cycle within the first five calendar days of the following month where source availability permits. Record actual capture date/time; never backdate a capture.

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

### Awakenology Git repository

- Treat `https://github.com/shifter888ai/awakenology` as the primary maintained source repository.
- At each monthly cycle, record the exact upstream `main` commit, recursive tree, file count, total bytes, and path/mode/Git-blob-SHA manifest.
- Compare the new tree with the previous pinned commit; record added, modified, renamed, and deleted paths.
- Update the pinned library snapshot reference and manifest. Preserve prior monthly commit references and manifests in Git history; never overwrite historical snapshot records.
- The 2026-11-25 baseline is commit `05523aec14c286bce397678b8a213cca1fc29563` (648 file blobs; 823 tree entries; 51,750,456 bytes).
- Live-site route/redirect/canonical checks are a separate web-crawling task, not a condition for completing the repository snapshot.

### Reddit

- The project owner confirms that `materials/reddit-english-all.txt` and `materials/reddit-english-qa.txt` are complete TXT archives for their intended Reddit collection scopes. They were manually extracted and checked for completion.
- Treat these supplied files as complete source archives. Do not reopen their completeness based on portal counts, profile-feed slices, or external account views.
- Preserve each source TXT unchanged. Each month, add the new manually checked TXT version as a separate immutable source object; never overwrite the previous version.
- Keep post/thread indexes, comment-section locators, author-marker indexes, Q&A indexes, native IDs, topic tags, translations, and analysis as separate derived layers linked to the exact source version.
- At each monthly update, record capture date/time, filename, Git blob SHA, SHA-256 where available, and the extraction/check status supplied by the owner. Compare the new version with the previous one and regenerate indexes against the exact new source object.
- The 1,096 author-marker occurrences in the current all-post archive are not asserted to be 1,096 distinct complete comments; this is a counting-unit limitation of the derived index, not a completeness gap in the supplied TXT archive.
- Preserve privacy, attribution, and rights context.

### Weibo

- The project owner confirms that the supplied Weibo TXT export is complete for its intended original-post scope and was manually extracted and checked for completion.
- Treat the supplied TXT as a complete source archive. Do not use aggregate profile counters or limited live-timeline snapshots to reopen its completeness status.
- Each month, add the new manually checked TXT export as a separate immutable source version; preserve all previous versions and record capture date/time, filename, Git blob SHA, and SHA-256 where available.
- Compare new records with the prior export and regenerate structural indexes, page indexes, and topic/media locator layers against the exact new source version.
- Image/video binaries represented by omission notes or media locators are a separate media-preservation layer; their absence does not make the owner-confirmed TXT archive incomplete.

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
