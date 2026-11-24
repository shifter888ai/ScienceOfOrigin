# Source Owner Clarifications and Reddit Live Capture — 2026-11-24

## CX Club publication timing

The owner clarifies that Wednesday is the weekly teaching schedule, not a guaranteed publication deadline. The team may publish the weekly materials several days later; this is normal. Maintenance now uses a rolling seven-day grace window after Wednesday before flagging a lesson as not yet published. Once visible, capture the page and attachments promptly. Month-end reconciliation uses actual publication dates and lesson dates separately.

## Weibo export semantics

The owner clarifies that Xiaowei Memory automatically filters forwarded posts. Thus the 765 locally exported original-post records are not expected to equal the 936 aggregate profile counter. The difference of 171 must not be treated as missing originals. The remaining task is to verify that the export fully covers the account's original-post category/history and to recover media.

This is owner-supplied workflow context, not independently verified Xiaowei Memory documentation.

## Reddit Comments feed capture

A signed-in connected-browser snapshot of `https://www.reddit.com/user/Lower-Lingonberry-40/comments/` in New sort rendered 50 visible comment cards on 2026-11-24. The capture includes top-level comments and replies, each indexed by its own comment permalink, subreddit, thread title, relative age as displayed and relationship type.

Files:
- `reddit-comments-live-capture-2026-11-24.csv` — 50 visible comment-card index rows.
- `reddit-comments-feed-2026-11-24.txt` — feed-only text snapshot, trimmed before unrelated profile sidebar/chat content.

This is not a complete account-history capture. It does not establish pagination/infinite-scroll coverage, older comment history, all account comments, third-party replies or media. The mismatch between the New sort control and the uniformly old relative-age labels may indicate a stale/partial rendering or a non-obvious feed ordering; the live feed should be revisited and compared with direct comment permalinks before drawing chronology conclusions. Relative ages are retained as displayed and not converted into guessed timestamps. Repeated text across different subreddits remains separate because each permalink identifies a distinct comment record.

## Next work

1. Continue through older Comments feed pages and reconcile individual permalinks against the Yuanwushi portal and the two local Reddit TXT datasets.
2. Continue CX Club capture with the seven-day grace window and investigate original PDF binaries and linked files.
3. Verify Weibo original-post export coverage against Xiaowei Memory's filtered output category, then recover and checksum linked media.
4. Continue direct Awakenology domain and route checks.
