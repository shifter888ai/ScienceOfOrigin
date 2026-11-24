# Reddit Live Comments-to-Q&A Answer Reconciliation — 2026-11-24

Compared the 36 captured comment bodies from the signed-in Reddit Comments feed snapshot with the answer text in the 651-record `reddit-english-qa.txt` collection.

## Result

- **9** live comment bodies have an exact normalized-text match to a Q&A answer record.
- **27** have no exact answer-text match in that dataset.
- No multiple exact-answer matches were found.

The matched Q&A records are:
- RDC-20261124-011 → Q&A record 0640
- RDC-20261124-012 → Q&A record 0641
- RDC-20261124-013 → Q&A record 0642
- RDC-20261124-020 → Q&A record 0643
- RDC-20261124-022 → Q&A record 0644
- RDC-20261124-024 → Q&A record 0645
- RDC-20261124-031 → Q&A record 0649
- RDC-20261124-032 → Q&A record 0650
- RDC-20261124-033 → Q&A record 0651

## Interpretation

This establishes that the matching comment text is preserved as answer text in the Q&A collection. It does not prove that the Q&A record and Reddit comment are the same source-record type, nor does it replace native permalink matching. Keep the exact-text relationship as a cross-collection link.

The 27 no-match records are not automatically missing: the Q&A collection has a different scope and structure from the live Comments feed.

## Files

- `reddit-comments-feed-2026-11-24.txt` — captured feed text.
- `reddit-comments-to-qa-answer-reconciliation-2026-11-24.csv` — per-comment comparison and Q&A answer line locators.
- `reddit-english-qa-index.csv` — Q&A source record boundaries.
