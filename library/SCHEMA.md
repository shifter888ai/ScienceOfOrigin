# Research Library Schema

**Version:** 0.1 — Initial working schema  
**Status:** Foundation for review; fields may evolve without altering preserved originals.

## 1. Design principles

The schema implements the Complete Research Library principle in `master.md`.

- Preserve complete source objects before extracting individual records.
- Keep source objects, extracted records, cases, terms, concepts, claims, measurements, and interpretations as distinct but connected entities.
- Store each original source once and link it to multiple records and research views.
- Make every derived item traceable to exact source locations.
- Support multilingual and mixed-format sources.
- Allow unknown and uncertain values.
- Preserve historical changes rather than rewriting the past.
- Treat automated classification and relationship suggestions as provisional until reviewed.

## 2. Entity types

| Entity | Purpose |
|---|---|
| Source | An original file, publication, conversation, media object, or other source container |
| Record | A traceable unit within a source: post, question, answer, message, passage, note, observation, or other identifiable unit |
| Case | An identifiable reported event, experience, observation, example, or measurement context |
| Term | A word, phrase, expression, symbol, or named terminology item in a particular language and usage |
| Concept | An idea or conceptual construct that may be expressed by multiple terms |
| Claim | A proposition asserted in a source or derived analysis |
| Measurement | A recorded measurement, data point, instrument reading, or quantitative result |
| Experiment | A documented procedure or investigation with conditions, methods, and outcomes |
| Relationship | A traceable link between any two library entities |
| Research view | A derived index, topic collection, glossary view, case collection, analysis, or report |

These entities must not be collapsed into one another. For example, a term is not automatically a concept; a claim is not automatically a finding; a case is not automatically proof of its proposed explanation.

## 3. Identifiers

Each entity receives a stable, unique identifier that does not encode an assumed date, topic, rank, or evidential status.

Suggested prefixes:

- `SRC-` source
- `REC-` record
- `CASE-` case
- `TERM-` term
- `CON-` concept
- `CLM-` claim
- `MEA-` measurement
- `EXP-` experiment
- `REL-` relationship
- `VIEW-` research view

Identifiers are permanent once assigned. A corrected title, changed topic classification, revised interpretation, or new relationship does not create a new identity for the same entity. A genuinely distinct source or record receives a new identifier.

Identifiers must not be assigned to individual extracted passages until their source boundaries and locator conventions are understood.

## 4. Source metadata

A source entry should contain the following fields when available:

| Field | Description |
|---|---|
| `source_id` | Stable source identifier |
| `title_original` | Original title or filename |
| `title_display` | Optional readable catalogue title |
| `source_type` | Book, PDF, webpage, forum thread, social post, chat, email, audio, video, image, dataset, notes, or other |
| `original_uri` | Original URL or source location, if available |
| `repository_path` | Preserved path within the archive |
| `original_filename` | Original filename, including extension |
| `language` | Original language or languages; use multiple values where needed |
| `creator_author` | Original author, creator, or publisher as supported |
| `participants` | Questioners, answerers, speakers, or other roles where known and appropriate |
| `created_at` | Original creation date/time, if known |
| `date_basis` | Exact, source-stated, approximate, inferred, range, or unknown |
| `published_at` | Original publication date, if known |
| `acquired_at` | Date the archive obtained the source |
| `ingested_at` | Date the source was registered in the library |
| `version` | Source version or edition, if known |
| `file_size_bytes` | Preserved file size |
| `checksum_sha256` | Integrity checksum of the preserved file |
| `completeness` | Complete, partial, excerpt, damaged, uncertain, or unknown |
| `provenance` | How and from where the source was obtained |
| `rights_status` | Known rights, licence, permission, or unresolved status |
| `access_level` | Public, project, restricted, private, or review-required |
| `preservation_status` | Identified, acquired, checksum-verified, backed-up, or needs review |
| `notes` | Additional factual notes; interpretations must be labelled |

Missing values remain null or explicitly unknown. Do not infer dates, authorship, source completeness, or rights from filenames alone.

## 5. Record metadata and source locators

A record represents a traceable unit inside a source. Depending on the source, it may be a complete thread, post, question, answer, message, page, numbered passage, paragraph, table, image, or other source unit.

Recommended fields:

- `record_id`
- `source_id`
- `record_type`
- `record_title` (if present in source)
- `source_locator` (page, page range, line range, post ID, URL fragment, timestamp, message ID, section, or other stable locator)
- `parent_record_id` (for nested records, if applicable)
- `sequence_in_source` (only when supported by source order)
- `original_language`
- `original_text` or a pointer to the preserved source span
- `context_before` and `context_after`, or an explicit context window
- `author_role` and `author_identity`, where supported
- `date_value` and `date_basis`
- `transcription_status` (verbatim, normalized, OCR, translated, excerpted, reconstructed, or unknown)
- `completeness`
- `review_status`
- `derived_from` and `supersedes`, where applicable

The original source remains authoritative for exact wording. Normalized text, OCR corrections, translations, summaries, and annotations must be separately labelled and linked to the original.

## 6. Case metadata

A case may be extracted from one or multiple records. A case can connect to multiple research fields and must not be restricted to one topic.

Recommended fields:

- `case_id`
- `case_title`
- `case_type` (experience, observation, event, example, measurement, experiment, or other)
- `case_narrative` (clearly labelled summary, not a substitute for source text)
- `involved_roles` (experiencer, observer, questioner, respondent, witness, researcher)
- `time_and_place` (only as supported and appropriate)
- `conditions_and_context`
- `observations`
- `reported_outcomes`
- `measurements`
- `source_record_ids`
- `source_locators`
- `related_term_ids`
- `related_concept_ids`
- `topic_links`
- `evidence_status`
- `limitations`
- `unresolved_questions`
- `extraction_status`
- `reviewer_notes`

A reported case is preserved as a report. It does not by itself establish the truth of every interpretation or mechanism associated with it.

## 7. Evidence and claim distinctions

Keep source form and evidential status separate. A source may contain more than one kind of content.

### Source/content type

- Original statement or source claim
- First-person experience or personal report
- Third-party observation
- Question or request
- Example, analogy, or illustration
- Interpretation or proposed explanation
- Measurement claim
- Experimental claim
- Later editorial or analytical statement

### Review/evidence status

- Not yet assessed
- Source located; content not independently checked
- Transcription or extraction checked against source
- Internally consistent across identified records
- Supported by specified measurements or experimental records
- Independently replicated or verified (details required)
- Disputed or contradicted
- Inconclusive
- Withdrawn or superseded

Do not use a stronger status without recording the supporting basis, method, reviewer, and date. Preserve source assertions even when disputed or unsupported; add review status rather than deleting the source content.

## 8. Term and glossary metadata

A term entry should support historical and multilingual usage:

- `term_id`
- `preferred_label`
- `original_forms`
- `language`
- `transliteration`, if useful
- `definition_current`
- `definition_source` and exact locator
- `historical_meanings`
- `aliases`
- `translation_equivalents`
- `broader_terms`
- `narrower_terms`
- `related_terms`
- `contrasting_terms`
- `concept_ids`
- `usage_record_ids`
- `validity_period` or date of usage where known
- `term_status` (current, evolving, proposed, historical, deprecated, disputed, or unresolved)
- `translation_notes`
- `review_status`

Do not automatically merge similar expressions, translations, spellings, or historical uses into one concept. Preserve distinctions and uncertainty.

## 9. Relationship metadata

Every meaningful relationship should be represented as a first-class entity:

- `relationship_id`
- `from_entity_type` and `from_entity_id`
- `relationship_type`
- `to_entity_type` and `to_entity_id`
- `directionality`
- `relationship_description`
- `source_record_ids` supporting the relationship
- `status` (proposed, under examination, supported, revised, not supported, or set aside)
- `confidence` (optional, with an explicit rating method)
- `created_at`, `reviewed_at`
- `created_by`, `reviewed_by`
- `revision_history`

A link alone does not establish equivalence, causation, dependency, or proof. Relationships may be many-to-many and revisable.

## 10. Measurement and experiment metadata

For quantitative or experimental records, capture as much as the source supports:

- subject or object measured
- measured property and operational definition
- unit and scale
- instrument, software, and version
- calibration and validation information
- protocol and procedure
- environmental and participant conditions
- sampling method and sample size
- raw data location
- processing and calculation methods
- uncertainty, error, and limitations
- result and date
- operator / researcher, where appropriate
- replication information
- linked claims, cases, records, and sources

Never invent missing instrument details, units, procedures, calibration, or sample information. Distinguish raw data from calculated values and later interpretations.

## 11. Versioning and corrections

- Original source files are immutable preservation objects.
- New source editions or corrected files are registered as new versions, linked to the earlier version.
- A checksum is calculated for each preserved file to detect accidental changes.
- Corrections to transcription or metadata are recorded in a change history.
- Derived summaries and translations carry their own version and source links.
- Later understanding may annotate an earlier record but must not silently rewrite what was recorded at the time.

## 12. Access, privacy, and rights

Every source and derived record must carry an access and rights review appropriate to its content.

Public availability does not automatically mean unrestricted republication is permitted. Private communications, personal information, student identities, sensitive experiences, and third-party content require appropriate privacy, permission, and rights review before wider access or publication.

The public website repository must not be treated as a secure store for private or restricted originals.

## 13. Minimum viable registration

A source must be registrable even when little is known. The minimum entry is:

- stable source ID
- original filename or source title
- source type
- source location
- language, if identifiable
- acquisition/registration date
- completeness status
- provenance status
- access/rights status
- checksum when a file is available

Unknown fields must be marked unknown rather than blocking preservation.

## 14. Open design questions

The following implementation choices remain open and should be resolved after the inventory and sample-source review:

- Canonical storage format for catalogue data (JSON, YAML, SQLite, or another format).
- Whether full text is stored in source files, extracted text companions, or a searchable index.
- How binary media and very large sources are stored and backed up.
- How private, project-only, and public collections are separated.
- How OCR and multilingual full-text search are implemented.
- How automated case and terminology suggestions are reviewed.
- How source versions and duplicate/overlapping collections are compared without deleting either original.
