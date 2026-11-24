# Yuanwushi Wiki Pagination Discovery — 2026-11-24

## Observed scope

The public Wiki index reports **2,659 Q&A records** under the heading “所有答疑”. Search-index results expose pagination URLs for `p=1`, `p=2`, `p=3`, `p=4`, and `p=133`.

The sampled indexed excerpts show progressively older content:
- `p=1`: visible records from 2024
- `p=2`: visible records from March 2022
- `p=3`: visible records from October 2021
- `p=4`: visible records from January 2021
- `p=133`: visible records from May 2008

The page number 133 demonstrates that at least that pagination parameter is indexed. It is **not yet verified as the final page**, and the number of records per page has not been established. Do not calculate a page count or assume a complete 133-page range until the live pagination controls and page boundaries are captured.

## Evidence and limitations

- The total 2,659 is the number displayed by the Wiki index/search snapshots.
- Five page parameters are represented in `yuanwushi-wiki-pagination-discovery.csv`.
- Direct web-reader opens of the sampled pages returned cache misses during this review.
- Search-index excerpts are discovery evidence, not original page captures.
- No complete Q&A record bodies, page HTML, attachments, images, or pagination navigation has been preserved in this update.

## Next capture work

1. Capture the live Wiki index and its pagination controls directly.
2. Determine the true first and last page parameters and page size.
3. Capture each page as an immutable original, then extract every Q&A record with source-page and source-record locators.
4. Reconcile the resulting records against the displayed 2,659 total.
5. Capture attachments and linked media, retaining parent Q&A IDs and provenance.
