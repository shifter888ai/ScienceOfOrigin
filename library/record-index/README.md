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

## Repository terminology occurrence index

- [repository-terminology-occurrence-index.csv](repository-terminology-occurrence-index.csv) — first-pass exact lexical occurrence index for 70 selected English and Chinese terminology strings across the repository's 145 HTML/Markdown text files at the time of extraction. The current index contains 1,329 term/file rows across 126 files with at least one match.

### Fields

- `term`: exact search string from the fixed candidate list.
- `source_class`: broad file class (`public-page`, `shared-component`, `project-document`, `terminology-artifact`, `research-library`, or `source-materials-readme`).
- `path`: repository-relative source path.
- `occurrence_count`: number of lexical matches in that file.
- `line_numbers`: 1-based source line numbers containing at least one match; multiple matches on the same line are counted in `occurrence_count` but the line number appears once.

### Matching method and limitations

English strings are matched case-insensitively with ASCII-alphanumeric word boundaries. Chinese strings are matched as literal substrings. The index records raw source-file text, including HTML markup and project/research documents; it is not a rendered-page index. It is a navigation aid, not a semantic classification or a claim that every hit uses the term in the same sense.

The candidate list is deliberately finite and reflects the current terminology review. It does not discover every possible synonym, spelling, translation, inflection, or related expression. The index does not distinguish quotations, negations, historical usage, proposed terms, or source-attributed claims from current framework definitions. Each hit must be checked in context before it is used to support a definition or conceptual relationship. Re-run the index when repository text changes or the candidate vocabulary expands.
