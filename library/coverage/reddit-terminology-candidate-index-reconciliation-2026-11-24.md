# Reddit terminology candidate-index reconciliation — 2026-11-24

**Status:** Source-count correction recorded; candidate-term index regeneration remains outstanding  
**Primary source:** materials/reddit-english-all.txt  
**Primary source Git blob SHA:** 0452d11a39654864572c0d563667765b5c96da3c  
**Review basis:** Current author-marker index, merged Terminology Inventory pass 2, and its Reddit YWS terminology candidate index

## Verified source counts

| Measure | Current result |
|---|---:|
| Dated post/thread blocks | 617 |
| Comment-section markers | 772 |
| Source permalink lines | 772 |
| Exact Lower-Lingonberry-40 author-marker occurrences | 1,096 |
| Current author-marker index data rows | 1,096 |

The 1,096 figure counts exact author-marker occurrences. It is not a verified count of distinct complete comments. The primary TXT remains unchanged.

## Status of the pass-2 candidate index

The merged library/record-index/reddit-all-yws-terminology-candidate-index.csv contains 120 curated term records. Its source-marker references were generated against the earlier 904-marker locator set.

A structural read of the CSV confirms:
- 120 data records and 120 unique candidate terms.
- 474 distinct author-marker IDs referenced across those terms.
- Highest referenced marker ID: 902.

The current author-marker index now has 1,096 rows. The candidate-term index has not been regenerated against the newly reconciled marker set. The 120-term list remains a useful earlier discovery layer, but its counts, parent-post coverage and line locators must not be treated as complete for the current 1,096-marker source.

The earlier inventory statements reporting 904 markers have been corrected to 1,096 marker occurrences, and the inventory now carries this coverage limitation beside the candidate index description.

## Relationship to the repository-wide occurrence index

The separate library/record-index/public-page-terminology-occurrence-index.csv is being extended across source classes such as public pages, project documents, terminology artifacts and research-library records. That occurrence index is a separate lexical navigation layer. It does not regenerate or validate the Reddit YWS speaker-span candidate index.

## Required next pass

1. Preserve the 120-term candidate list and the current CSV as the earlier pass; do not overwrite the source TXT.
2. Re-run whole-word/phrase matching against all 1,096 author-marker occurrences.
3. Apply the documented speaker-span boundaries: next detected speaker label, Source line, comment-section boundary, post separator, or next author marker.
4. Record the extraction script/version and exact boundary rules used. The earlier method is rule-based and still requires manual review in nested Reddit threads.
5. Produce a new dated candidate-index version, or explicitly version the replacement, so the earlier 904-marker-based results remain traceable.
6. Reconcile term counts, marker IDs, parent post IDs and source line ranges against the current author-marker index.
7. Keep the results labelled as lexical discovery aids, not semantic counts, validated definitions or proof of author endorsement.

## Interpretation boundary

The 1,096 marker occurrences establish the current count of exact author-marker labels in the primary TXT. They do not establish account-wide completeness, a count of distinct comments, a complete reply tree, or one-to-one mapping between markers and source permalinks. The candidate-term index likewise does not establish semantic use or endorsement.
