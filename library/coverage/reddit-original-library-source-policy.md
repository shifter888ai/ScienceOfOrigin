# Reddit Human-Readable Original Library

**Decision date:** 2026-11-24  
**Source:** `materials/reddit-english-all.txt`  
**Account:** u/Lower-Lingonberry-40  
**Status:** Primary human-readable original-library source; account-wide completeness not yet certified

## Decision

The owner confirms that this file was produced by an engineer on the team using an automated extraction script and was intentionally designed for human readers. The owner approves using the resulting TXT directly as the primary original-library source for Reddit research.

The file should therefore be read and researched directly in its supplied human-readable form. It is not merely a temporary intermediate for conversion into a database, nor should a profile-page capture or normalized index replace it.

## Preservation model

1. Preserve `materials/reddit-english-all.txt` unchanged as the primary reader-facing source.
2. Never overwrite it with a new script run, normalization, translation, formatting pass, or merged export.
3. Preserve future extraction runs and official exports as separate, dated source objects.
4. Build machine-readable indexes, native-ID maps, permalink reconciliations, topic tags, translations, and analysis as separate derived layers.
5. Link derived records back to the original TXT record and source permalink wherever possible.
6. Record SHA-256 for each exact source version when technically possible.

## Current observed structure

The inspected file contains:
- 617 dated post/thread blocks.
- Date range: 2023-10-29 through 2026-11-18.
- 772 `Source:` permalink lines.
- 1,096 occurrences of the `Lower-Lingonberry-40:` author marker.

These are structural counts, not interchangeable measures. In particular, the 1,096 author-marker occurrences must not be described as 1,096 distinct comments without a record-level audit. The 617 blocks are post/thread records, not 617 comments authored by the account.

A separate Reddit Q&A dataset contains 651 records and remains a related but distinct research dataset; it does not replace the primary TXT.

## Supplementary verification sources

- **Individual Reddit permalinks:** verify original wording, context, native IDs, and current availability.
- **Account Comments feed:** discover and cross-check comments not represented in the current archive. The 2026-11-24 capture contains 36 visible comment cards with all 36 bodies rendered, but it is one browser snapshot and does not prove account-wide completeness.
- **Yuanwushi Reddit archive portal:** supplementary discovery and cross-checking source; its monthly counts must be reconciled by native record identity and counting unit.
- **Reddit official account-data export:** optional independent completeness benchmark. It is supplementary evidence, not the preferred reading library.

## Known reconciliation gaps as of 2026-11-24

The 36-comment profile-feed slice was reconciled against the source archive by native subreddit, post ID, and comment ID:
- 24 exact native post-and-comment ID matches.
- 5 comments belong to threads present in the TXT, but their comment IDs are absent from the source permalink set.
- 6 deleted-title threads are absent from the archive.
- 1 parent thread is unmatched in the archive; its comment body is rendered in the profile feed as `👍`.

The feed capture does not expose an explicit account-wide comment total or verifiable pagination end. These gaps must remain explicit; do not infer a total missing-comment count from this single slice.

## Extraction provenance to preserve going forward

For each future automated extraction, record:
- Capture date/time and timezone.
- Script name, version, commit, or checksum.
- Configuration and filters.
- Account identity and input sources.
- Included record types (posts, comments, replies, third-party replies, media, deleted/unavailable placeholders).
- Date range and pagination/exhaustion method.
- Output filename, byte size, record counts by clearly defined unit, and SHA-256.
- Any errors, rate limits, skipped pages, inaccessible records, or transformations.

Where available, preserve the script source and configuration or a stable version reference. Do not claim completeness until the script's input scope and collection boundaries have been tested against independent evidence.

## Research-use rule

Quote and analyze the human-readable TXT as the primary library source. Use structured indexes to locate, count, compare, and cross-reference records, not to silently replace the wording or structure of the original. Keep source-derived observations distinct from later interpretation.
