# Science of Origin — Library Completion Dashboard

**Review date:** 2026-11-25  
**Repository:** `shifter888ai/ScienceOfOrigin`  
**Integrity baseline:** See [`repository-integrity-report.md`](repository-integrity-report.md) and [`repository-integrity-manifest.json`](repository-integrity-manifest.json) for the latest audited refs, counts, and SHA-256 values.  
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
| Chinese compilation | Complete per owner-confirmed scope: the TXT alone is the complete source for current research. Two PDFs remain supplemental; prior page comparison/OCR outputs are optional derivatives. | No source-completeness work outstanding. OCR/image review only if later research requires the supplemental PDF images |
| Entropy assessment points | Complete per owner-confirmed scope: the RTF is canonical and complete; DOCX remains a supplemental duplicate-format copy. Prior text comparison is documented. | No source-completeness work outstanding; optional format review only if later needed |
| Science of Consciousness uploads | Two original TXT files registered and archived; repository SHA-256 matches supplied originals | Preserve originals; create derived research materials separately |

## 3. Repository state and integrity

The active SHA-256 manifest and report are `library/repository-integrity-manifest.json` and `library/repository-integrity-report.md`. The report is the authoritative, automatically refreshed record of audited branch-tip commits, exact blob/byte counts, path/ref coverage, and verification results. The audit independently checks Git blob SHA-1 values and records SHA-256 for every unique blob in scope; generated report/manifest paths are excluded to avoid self-reference. It does not cover unreachable Git history, external LFS payloads, or resources outside the selected branches. Historical automation branches were compared by path; no unique source-file paths were found outside main, except an obsolete `.gitmodules` entry in an early branch.

## 4. Open work queue

1. Investigate and verify identity/provenance for the seven Yuanwushi 404 candidates, or explicitly retain them as unavailable/unverified; validate linked detail bodies/media where required.
2. Complete Awakenology live-site alias, redirect, route, asset, and historical-version review.
3. Inventory additional external, private, offline, historical, and other-repository sources; review rights and privacy before copying.
4. Continue monthly additive updates for Reddit, Weibo, Awakenology, and Yuanwushi; refresh derived indexes and integrity manifests.

Optional, non-blocking research tasks: verify/correct the Chinese OCR derivative or inspect supplemental PDF/DOCX formatting if those materials become relevant to a specific study.

## 5. Completion rule

A collection is complete only within a clearly stated scope and against a documented completion gate. A successful checksum audit proves integrity of files that were captured; it does not prove that every possible source was discovered. Owner-confirmed archive completeness applies only to the supplied archive scopes. Historical checkpoints remain preserved but are superseded by later dated findings where explicitly stated.

**Preserve originals. Keep extraction, indexes, comparisons, and interpretations separate. Do not declare the entire library complete while the open work queue remains unresolved.**
