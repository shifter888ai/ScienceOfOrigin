# English Reddit Collections — Initial Exact-Text Overlap Analysis

**Status:** Preliminary cross-source text comparison  
**Sources:**
- `materials/reddit-english-qa.txt` — Git blob `undefined`
- `materials/reddit-english-all.txt` — Git blob `undefined`

## Result

A normalized exact-text comparison of answer bodies in the Q&A collection against the indexed `Lower-Lingonberry-40:` author-marker bodies in the all-post archive produced:

| Result | Count |
|---|---:|
| Q&A records examined | 651 |
| Records with one exact normalized answer-text match | 473 |
| Records with multiple exact normalized answer-text matches | 14 |
| Records with at least one exact match | 487 |
| Records with no exact match located | 164 |

The 14 multi-match records have between two and four matching author-marker locations. Repeated text may occur in multiple posts or threads; these must remain separate source occurrences.

## Cross-reference file

[`reddit-english-qa-to-all-overlap.csv`](reddit-english-qa-to-all-overlap.csv) contains one row for each of the 651 Q&A records, with the Q&A source line range and any exact-text matching post IDs and YWS author-marker line locations.

## Matching method

- Extracted each Q&A record's answer span from its `A:` marker through the next `Q:` record boundary.
- Extracted text following each exact `Lower-Lingonberry-40:` author marker in the all-post archive until the next author marker, comment-section marker, source permalink, or post separator.
- Normalized case, repeated whitespace, Markdown emphasis/code markers, and common curly quotation/apostrophe variants.
- Compared the resulting complete normalized strings for exact equality.
- Did not remove punctuation or attempt semantic/fuzzy matching.

## Interpretation limits

An exact text match is evidence of textual overlap between the two files. It does not by itself establish that both entries are complete copies of the same original Reddit event, because context, reply nesting, timestamps, and permalink relationships may differ.

A record with no exact match is **not** necessarily absent from the all-post archive. It may have been edited, truncated, formatted differently, split across replies, or represented by a larger/smaller text span. No-match results require further investigation if coverage completeness matters.

The two source files remain separate and preserved. Do not delete, merge, or replace either file based on this comparison. The cross-reference is a derived navigation aid and can be regenerated if either source changes.

**Conclusion:** There is substantial confirmed textual overlap, but the collections are not proven equivalent and should remain independently preserved.
