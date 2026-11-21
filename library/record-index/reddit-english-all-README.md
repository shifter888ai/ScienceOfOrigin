# Reddit English All — Post and YWS Author-Marker Indexes

**Source:** `materials/reddit-english-all.txt`  
**Source Git blob SHA:** `0452d11a39654864572c0d563667765b5c96da3c`  
**Observed size:** 1,651,691 characters  
**Observed line count:** 29,553 lines  
**Status:** Structural indexes only; not a content analysis or case extraction.

## Files

- [`reddit-english-all-post-index.csv`](reddit-english-all-post-index.csv) — one row for each of the 617 post/thread blocks.
- [`reddit-english-all-yws-author-marker-index.csv`](reddit-english-all-yws-author-marker-index.csv) — one row for each exact `Lower-Lingonberry-40:` author marker found in the source.

## Structural findings

- 617 post/thread blocks, delimited by lines of at least 20 equals signs.
- 617 date headers, one in each post block.
- Date range in the date headers: 2023-10-29 through 2026-11-18.
- 772 `--- comments ---` section markers.
- 772 `Source:` permalink lines.
- 904 exact `Lower-Lingonberry-40:` author markers.

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
