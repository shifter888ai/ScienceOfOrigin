# Reddit Comments-to-Post Index Candidate Reconciliation — 2026-11-24

## Result

Compared the 36 visible account-comment records in `reddit-comments-live-capture-2026-11-24.csv` against the 617-row local post/thread index `reddit-english-all-post-index.csv`.

- 29 records have exactly one local post-index candidate with matching normalized thread title and subreddit.
- 7 records have no exact title/subreddit match; six show the thread title as `[deleted by user]`, and one is a thread not found under the current exact-title/subreddit rule.
- No multiple-candidate collision was found under this matching rule.

## Important limitation

These are **candidate matches, not confirmed record identity**. The local post index does not expose the native Reddit thread ID/permalink in its columns, so title + subreddit cannot prove that two records refer to the same thread. The comment feed's thread URL does expose the native post ID. A definitive match requires comparing that ID/permalink against the original TXT block or a richer source archive.

The 36-card feed snapshot is a single rendered slice; it is not the full account comment history. Relative ages are retained as displayed (approximately 2–3 years in this slice) and are not used as exact timestamps.

## Files

- `reddit-comments-live-capture-2026-11-24.csv` — captured account-comment permalink index.
- `reddit-comments-to-post-index-candidates-2026-11-24.csv` — one row per captured comment, with zero or one candidate local post record under the normalized title/subreddit rule.
- `reddit-english-all-post-index.csv` — 617 source post/thread boundary records.

## Next

1. Retrieve original TXT blocks by their indexed line ranges and inspect whether the native Reddit thread ID/permalink is present.
2. If the permalink is absent, preserve the title/subreddit candidate relationship as unconfirmed.
3. Match comment-level source blocks and portal records by native IDs where available.
4. Keep deleted thread titles and deleted/unavailable comments as separate states; do not discard their surviving comment permalinks.
