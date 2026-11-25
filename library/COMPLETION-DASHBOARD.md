# Science of Origin — Library Completion Dashboard

**Review date:** 2026-11-25  
**Repository:** `shifter888ai/ScienceOfOrigin`  
**Main commit audited:** `4bbb8a5712b54bc6e4339567bbeca6551ef1545f`  
**Overall status:** In progress — priority source acquisition and first-pass format comparisons are complete; human verification, live-source parity, and wider source discovery remain open.

## 1. Priority source collections

| Collection | Current status | Verified scope | Remaining work |
|---|---|---|---|
| Reddit supplied TXT archives | Complete per owner-confirmed scope | Both supplied TXT files manually extracted and checked by the owner; structural indexes retained separately | Monthly additive versions |
| Weibo supplied TXT archive | Complete per owner-confirmed scope | Supplied TXT manually extracted and checked by the owner; 765 sequential records / 160 page markers indexed | Monthly additive versions; optional media-binary preservation is separate |
| Awakenology repository | Physical snapshot archived and tree identity verified | 648 blobs, 823 tree entries, 51,750,456 bytes; subtree SHA matches pinned upstream root tree SHA | Monthly upstream comparison; live-site parity and historical versions separate |
| Yuanwushi website | Initial crawl, checksums, and listing reconciliation passed | 1,001 manifest records; 993 stored files / 993 unique paths / 307,557,680 bytes; 133 Wiki pages; 2,659 unique Q&A IDs, zero duplicates | Seven 404 candidates remain unverified; linked detail bodies/media and historical/unlinked resources not all checked |

## 2. Other source collections

| Collection | Current status | Remaining work |
|---|---|---|
| Chinese compilation (two PDFs + TXT) | 1,671 PDF pages match 1,671 TXT markers; 1,455 exact normalized matches, 10 high-similarity, 206 image-only/no-extractable-text pages. OCR derivative preserved. | Human-check OCR; classify the 206 pages; review the 10 high-similarity pages and confirm visual/page mapping |
| Entropy assessment points (DOCX + RTF) | Normalized body text matches exactly after excluding the RTF-only 3,266-character TOC; DOCX has 957 paragraphs and no tables or embedded media | Review TOC difference, formatting, layout, and metadata |
| Science of Consciousness uploads | Two original TXT files registered and archived; repository SHA-256 matches supplied originals | Preserve originals; create derived research materials separately |

## 3. Repository state and integrity

The latest audited main tree contains **897 tracked file blobs totaling 114,174,511 bytes**. The final Yuanwushi archive branch contains **1,870 blobs totaling 421,098,213 bytes**. Across both branch tips, **1,534 unique Git blobs** were independently hashed (402,527,909 unique-blob bytes; 2,767 path/ref records). There were zero Git blob SHA-1 mismatches and no Git LFS pointers.

The current SHA-256 manifest and report are `library/repository-integrity-manifest.json` and `library/repository-integrity-report.md`. The audit covers tracked contents at the selected branch tips, not unreachable Git history or resources outside those branches. Historical automation branches were compared by path; no unique source-file paths were found outside main, except an obsolete `.gitmodules` entry in an early branch.

## 4. Open work queue

1. Human verification/correction of the Chinese image-page OCR; page-by-page classification of all 206 image-only pages; review the 10 high-similarity pages.
2. Entropy DOCX/RTF visual layout, metadata, and TOC review.
3. Investigate and verify identity/provenance for the seven Yuanwushi 404 candidates; validate linked detail bodies/media where required.
4. Complete Awakenology live-site alias, redirect, route, asset, and historical-version review.
5. Inventory additional external, private, offline, historical, and other-repository sources; review rights and privacy before copying.
6. Continue monthly additive updates for Reddit, Weibo, Awakenology, and Yuanwushi; refresh derived indexes and integrity manifests.

## 5. Completion rule

A collection is complete only within a clearly stated scope and against a documented completion gate. A successful checksum audit proves integrity of files that were captured; it does not prove that every possible source was discovered. Owner-confirmed archive completeness applies only to the supplied archive scopes. Historical checkpoints remain preserved but are superseded by later dated findings where explicitly stated.

**Preserve originals. Keep extraction, indexes, comparisons, and interpretations separate. Do not declare the entire library complete while the open work queue remains unresolved.**
