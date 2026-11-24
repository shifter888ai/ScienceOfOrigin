# Reddit English All — Post and YWS Author-Marker Indexes

**Source:** `materials/reddit-english-all.txt`  
**Source Git blob SHA:** `0452d11a39654864572c0d563667765b5c96da3c`  
**Observed size:** 1,651,691 characters  
**Observed line count:** 29,553 lines  
**Status:** Structural indexes only; not a content analysis or case extraction.

## Files

- [`reddit-english-all-post-index.csv`](reddit-english-all-post-index.csv) — one row for each of the 617 post/thread blocks.
- [`reddit-english-all-yws-author-marker-index.csv`](reddit-english-all-yws-author-marker-index.csv) — one row for each exact `Lower-Lingonberry-40:` author marker found in the source (1,096 rows, reconciled 2026-11-24).
- [`reddit-english-all-comment-section-index.csv`](reddit-english-all-comment-section-index.csv) — one row per `--- comments ---` section, linking its source line range and Source permalink to the author-marker IDs it contains.

## Structural findings

- 617 post/thread blocks, delimited by lines of at least 20 equals signs.
- 617 date headers, one in each post block.
- Date range in the date headers: 2023-10-29 through 2026-11-18.
- 772 `--- comments ---` section markers.
- 772 `Source:` permalink lines.
- 1,096 exact `Lower-Lingonberry-40:` author markers.

The source title identifies the archive as a Reddit Q&A archive for `u/Lower-Lingonberry-40`. The project owner has instructed that answers in this identified collection are authored by YWS, even when aliases or nicknames appear. The index preserves the displayed author marker separately from the canonical attribution rule.

## Boundary and locator method

Post boundaries are the separator lines. Each post row records the inclusive source line range from the first line after one separator through the line before the next separator. The first header/title is taken from the first nonblank line in that block. The date, subreddit, and original poster are parsed from the date header and preserved as displayed.

The author-marker index records exact source lines matching `Lower-Lingonberry-40:`, including indentation. It links each marker to its containing post block and its ordinal `--- comments ---` section within that post.

**The author-marker index does not claim that each marker equals one complete comment.** A marker may begin a comment or reply within a nested thread. Full comment spans, reply relationships, and exact permalink association require a separate structural pass. Do not count markers as independently verified comment records.

## Source context and limitations

- The archive includes original posts by other Reddit users and comments by multiple participants. Preserve these roles separately.
- A post block may contain multiple comment sections and source permalinks.
- Source permalink lines are preserved in the original file; this index does not yet map every comment marker to an exact permalink.
- Images and links are represented by text placeholders/URLs in the export; external media should be inventoried separately if available.
- The post index is a navigation layer only. It does not classify topics, identify cases, validate claims, or determine evidential status.
- Line numbers are 1-based and inclusive. If the original file changes, regenerate the indexes against the new blob and retain prior versions.

**Preserve the full thread context before extracting individual cases or conclusions.**


## Portal monthly count reconciliation

A separate comparison of the 617 indexed post/thread blocks with the older Yuanwushi Reddit portal search snapshot is documented in `../coverage/reddit-monthly-count-reconciliation.md` and `reddit-monthly-count-reconciliation.csv`. It records monthly counts and discrepancies without asserting that portal entries and post/thread blocks are equivalent units. No source records were changed.

## 2026-11-24 author-marker index reconciliation

A direct recount of the unchanged source blob `0452d11a39654864572c0d563667765b5c96da3c` found **1096** exact `Lower-Lingonberry-40:` occurrences on 1096 source lines. The previous marker index contained 904 data rows and was incomplete by 192 markers. The index has been regenerated against the same source blob with source line numbers and parent post/comment-section associations. The primary TXT was not modified. Marker occurrences still do not equal verified complete comment records; comment spans and reply relationships remain unsegmented.

## Comment-section locator structure (2026-11-24)

The source contains 772 comment sections. Each section has exactly one `Source:` permalink line and at least one `Lower-Lingonberry-40:` marker. Of the 772 sections, 596 contain one author marker and 176 contain multiple author markers. The new section locator index preserves each section's line range, parent post ID, source permalink, and all marker IDs in that section. In multi-marker sections, it deliberately does not assert which individual marker the permalink identifies.
