# Reddit Comment-to-Source Permalink Reconciliation — 2026-11-24

## Method

Compared all 36 comment permalinks in the frozen signed-in Reddit Comments feed capture against every `Source:` permalink in the preserved 617-thread original TXT archive (`materials/reddit-english-all.txt`, Git blob `0452d11a39654864572c0d563667765b5c96da3c`).

Reddit uses different URL path shapes in the profile feed and archive export. Identity was matched on the native tuple **subreddit + post ID + comment ID**, not on display title or literal URL string. Parent-thread-only matches are kept separate from exact comment matches.

## Results

- **24** of 36 captured comments have an exact native subreddit + post ID + comment ID match in the source archive.
- **5** comments belong to threads present in the source archive, but their individual comment IDs are not present in the archive's Source-permalink set.
  - Four are additional comments on the existing “Bad News! it seems like you’ll get sent back to earth even if you say ‘no’, during an NDE” thread.
  - One is an additional comment on “Woman stuck in dream for 40 years”; the source archive contains a different comment by the account in that thread.
- **6** comments belong to threads whose displayed title is `[deleted by user]` and whose native post IDs are not present in the local archive.
- **1** comment belongs to a thread not found in the local archive under its native post ID.

These categories sum to all 36 captured feed records. The CSV contains per-record IDs, source record and line ranges where a parent thread is present, and match status.

## Interpretation

The 24 exact matches confirm that the local TXT archive contains those specific comment records. The five thread-present records are comment-level gaps in the local archive, not missing parent threads. The six deleted-thread records are unavailable/deleted-source cases in this snapshot, not evidence that the account never commented there. The one absent thread is a source-archive coverage gap for this captured slice.

This is a comparison of one rendered 36-card feed slice against the local archive. It does not establish the account-wide comment total, complete pagination, or complete coverage of all historic comments.

## Files

- `reddit-comments-live-capture-2026-11-24.csv` — live comment-feed capture.
- `reddit-comments-to-source-permalink-reconciliation-2026-11-24.csv` — exact native-ID comparison.
- `reddit-comments-to-post-index-candidates-2026-11-24.csv` — earlier title/subreddit candidate layer; retain it as an explicitly weaker derived layer.
- `reddit-english-all-post-index.csv` — 617 source thread boundary records.
