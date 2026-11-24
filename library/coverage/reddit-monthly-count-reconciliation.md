# Reddit Archive — Monthly Count Reconciliation

**Assessment date:** 2026-11-24  
**Portal:** https://yuanwushi.org/reddit/  
**Local source index:** `library/record-index/reddit-english-all-post-index.csv`  
**Portal evidence:** search-index snapshot `turn375601search0`, crawled about two months before this assessment  
**Status:** Preliminary month-level reconciliation; source event identity not yet matched.

## Summary

The portal snapshot displays 26 monthly groups with counts totalling **607**. The local `reddit-english-all.txt` post index contains **617 post/thread blocks** dated 2023-10-29 through 2026-11-18.

The month-by-month comparison is unusually close, but the counting units are not yet proven equivalent:

- For most months displayed in the portal snapshot, portal count and local post/thread-block count are identical.
- The 2024 month differences are: September portal 75 vs local 76; October portal 75 vs local 76; November portal 45 vs local 44. Net difference across those three months: +1 local.
- The local index contains 9 post/thread blocks in 2026-09 through 2026-11 (5, 1, and 3 respectively), while those months do not appear in the portal snapshot.
- Overall, local post/thread blocks exceed portal monthly entries by 10 (617 vs 607). The month-level arithmetic accounts for this difference: +1 across the 2024 discrepancies and +9 in the later months absent from the older portal snapshot.

## Month-by-month table

See [reddit-monthly-count-reconciliation.csv](../record-index/reddit-monthly-count-reconciliation.csv). Blank portal counts mean the month was not listed in the portal search snapshot; they do not mean the live portal currently lacks those months.

## Interpretation limits

1. The portal search result was crawled about two months before 2026-11-24 and could be stale. Its visible range ends at 2026-08.
2. The portal labels its items as monthly comment entries; the local file index counts post/thread blocks. Their apparent numerical alignment does not prove they are the same unit or that every portal entry maps one-to-one to a block.
3. The 2024 discrepancies require record-level matching, not adjustment by aggregate counts.
4. The 9 local blocks dated 2026-09 through 2026-11 may simply be newer than the portal snapshot. A current portal capture is required to test that.
5. This analysis does not reconcile the separate 651-record Q&A dataset, 904 YWS author markers, individual comments/replies, or media.
6. Do not infer that the 10-count difference means 10 missing Reddit comments.

## Next checks

1. Obtain a fresh capture of the portal page and all monthly pages/download links, preserving original files and checksums.
2. Compare individual portal entries to local post/thread blocks using source permalinks, dates, subreddit, title, and comment structure.
3. Investigate the September–November 2024 one-count offsets at record level.
4. Check whether the portal has added September–November 2026 since its last indexed snapshot.
5. Keep the 651 Q&A collection and 617 post/thread collection separate; expand the existing exact-text overlap work into context/permalink-aware reconciliation.
6. Track deleted, edited, unavailable, and media-bearing records separately.

## Provenance and method

- Portal month counts are transcribed from search result `turn375601search0`; its 26 listed monthly values sum to 607.
- Local counts are grouped by the `post_date_as_recorded` field in the 617-row post index. The index source is the preserved `materials/reddit-english-all.txt` (Git blob `0452d11a39654864572c0d563667765b5c96da3c`).
- The comparison is arithmetic only; no records were merged or modified.
