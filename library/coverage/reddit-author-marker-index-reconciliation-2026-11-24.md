# Reddit author-marker index reconciliation — 2026-11-24

## Source and method

- Primary source: `materials/reddit-english-all.txt`
- Source Git blob SHA: `0452d11a39654864572c0d563667765b5c96da3c`
- Direct source retrieval: Git blob content
- Counting rule: count every exact occurrence of the literal string `Lower-Lingonberry-40:` in the source, then record its containing line.
- Parent post assignment: use the ordinal of the preceding 20-or-more-equals separator; this corresponds to the 617 post blocks indexed in the existing post index.
- Comment-section assignment: count preceding `--- comments ---` markers within that post block.
- Source line numbers are 1-based.

## Recount result

| Measure | Result |
|---|---:|
| Source characters | 1,651,691 |
| Source lines | 29,553 |
| Post/date blocks | 617 |
| Comment-section markers | 772 |
| Source permalink lines | 772 |
| Exact author-marker occurrences | 1,096 |
| Prior author-marker index data rows | 904 |
| Prior index shortfall | 192 |

The direct recount reproduces 1,096 occurrences. The earlier index contained only 904 data rows and was incomplete by 192 marker occurrences. The README's previous 904-marker statement was therefore stale/incorrect for the current source blob.

## Corrective action

- Regenerated `reddit-english-all-yws-author-marker-index.csv` with 1,096 rows against the same source blob.
- Recorded the source blob SHA on each index row.
- Preserved exact source line numbers, parent post record IDs, comment-section ordinal, indentation, and the existing limitation that a marker does not define a complete comment span.
- Updated `reddit-english-all-README.md` to report 1,096 markers and document the reconciliation.
- Did not modify `materials/reddit-english-all.txt`.

## Interpretation boundary

The 1,096 count is a count of exact author-marker occurrences, not a verified count of distinct complete comments. A marker may introduce a comment or reply; full spans, reply relationships, and exact one-to-one permalink associations still require separate structural analysis.

## Extraction script provenance

A recursive repository-tree inspection at commit `434b8b6ebb44080a17cfec2a8c0b27b5cdea53cc` found no tracked file clearly identifiable as the Reddit extraction script or its configuration. The script may be maintained outside this repository. The team should provide a stable script version/source, configuration and input-scope description; absence from this tree is not evidence that no script exists.
