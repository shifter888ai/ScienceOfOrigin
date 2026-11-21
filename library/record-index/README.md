# Reddit English Q&A — Record Boundary Index

**Source:** `materials/reddit-english-qa.txt`  
**Source Git blob SHA:** `d4f61612a60496e3b7d70868a4f57120ff5cf39c`  
**Observed size:** 357,871 UTF-8-decoded characters  
**Observed line count:** 3,682 lines  
**Indexed records:** 651  
**Status:** Structural boundary index; not a content analysis or evidence assessment.

## Files

- [`reddit-english-qa-index.csv`](reddit-english-qa-index.csv) — one row per detected Q&A record, with inclusive 1-based line locators into the original source.

## Boundary method

The index identifies each record by a line beginning with `Q:`. The next line beginning with `Q:` starts the next record. Within each record, the first subsequent line beginning with `A:` separates the question material from the answer material. Continuation lines are retained in their respective source spans.

This method was checked against the full text available through the repository connector:

- 651 Q-start boundaries detected.
- 651 records have one A-start boundary.
- 0 records have no A-start boundary.
- 651 records have multiline question spans.
- 301 records have multiline answer spans.
- No record had multiple anchored A-start markers under this boundary rule.

The file contains 651 blank lines. Blank lines are retained within the source line spans and are not treated as independent records.

## Locator interpretation

All line numbers are 1-based and inclusive. The CSV includes:

- Whole-record start and end lines.
- Question start and end lines.
- Answer start and end lines.
- A short label excerpt taken from the first question line.

The label excerpt is only a navigation aid. The original source text remains authoritative. Use the source file and line ranges to retrieve full wording and context.

## Identity and authorship

The `REC-ENQA-####` identifiers are stable administrative record IDs in source order; they do not imply chronology or research priority.

The project owner's attribution instruction for this identified Q&A collection is that answers are authored by YWS. This does not change the displayed identities of questioners or other participants, which must remain separately represented when extracted into full record metadata.

## Limitations

- This index does not contain the full question or answer text; it points to the preserved source.
- It does not infer original Reddit post IDs, authorship of questions, timestamps, or thread context when those details are absent from this file.
- It does not classify topics, cases, claims, concepts, or evidence.
- The source's original export provenance, collection completeness, and relationship to the other English collection remain under review.
- If the source file changes, this index must be regenerated against the new source blob and the previous index retained as a historical derivative.
