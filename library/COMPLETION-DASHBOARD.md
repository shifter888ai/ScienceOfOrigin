# Science of Origin — Library Completion Dashboard

**Review date:** 2026-11-25 (Japan Standard Time)  
**Repository:** `shifter888ai/ScienceOfOrigin`  
**Decision record:** [Initial Library Assembly Decision](coverage/2026-11-25-initial-library-assembly-decision.md)  
**Integrity baseline:** [Repository integrity report](repository-integrity-report.md) and [path-level manifest](repository-integrity-manifest.json).

<badge>Baseline assembled</badge>

**Overall status:** Initial Library Assembly is complete within the identified and owner-confirmed source scope. Library Coverage and Maintenance remains ongoing. Seven Yuanwushi resources are explicitly unavailable/unverified; Awakenology live-site parity is a separate, unfinished verification track. Neither is represented as recovered or verified.

## 1. Included source collections

| Collection | Baseline status | Verified scope and disposition |
|---|---|---|
| Reddit supplied TXT archives | Complete per owner-confirmed scope | Both TXT archives manually extracted and checked by the owner; indexes are separate derived layers |
| Weibo supplied TXT archive | Complete per owner-confirmed scope | Owner-confirmed original-post TXT archive; 765 sequential records and 160 page markers indexed; optional media binaries are a separate layer |
| Awakenology Git repository | Complete physical snapshot | Pinned commit `05523aec14c286bce397678b8a213cca1fc29563`; 648 blobs, 823 tree entries, 51,750,456 bytes; physical subtree tree identity matches upstream |
| Yuanwushi website | Verified-with-gaps | 993 stored files independently checksummed; 133 Wiki pages and 2,659 unique IDs reconciled; seven HTTP 404 resources listed separately as unavailable/unverified candidates |
| Chinese compilation | Complete per owner-confirmed scope | TXT is canonical for current research; two PDFs retained as supplemental references; OCR/image review is optional |
| Entropy assessment points | Complete per owner-confirmed scope | RTF is canonical and complete; DOCX retained as supplemental duplicate-format copy |
| Science of Consciousness | Original sources registered | Two distinct UTF-8 TXT uploads preserved unchanged with SHA-256 values |

## 2. Integrity and reconciliation

- Repository-wide selected-branch audit: 881 tracked files on `main`, 1,870 on the Yuanwushi archive branch, and 1,518 unique blobs independently hashed; zero Git blob SHA-1 mismatches.
- Awakenology: 648 physical tracked blobs match the pinned upstream root tree identity.
- Yuanwushi: 993/993 stored files passed independent SHA-256 checks; zero missing files, invalid paths, duplicate paths, size mismatches, or hash mismatches.
- Yuanwushi Wiki: 133 pages, 2,659 record links, 2,659 unique IDs, zero duplicates.

The integrity audit covers the selected branch tips. It does not cover unreachable Git history, future changes, private or deleted platform content, or all external resources.

## 3. Explicit residual gaps

### Yuanwushi — seven unavailable resources

Six image URLs and one audio URL returned HTTP 404 on 2026-11-25. Candidate files are stored separately with provenance and checksums, but none is byte-verified against the unavailable Yuanwushi original. They remain **unavailable/unverified**, not recovered. See [candidate register](../materials/yuanwushi/recovery-candidates/recovery-candidate-register.csv).

### Awakenology live website

The pinned Git repository snapshot is complete and verified. Current public page/search snapshots provide discovery evidence for the homepage, language indexes, and selected pages. A full same-session HTTP/redirect/canonical/asset audit of .org, .space, www aliases, all 136 sitemap routes, 12 non-sitemap routes, and historical versions remains unverified. This is separate from the completed repository snapshot.

## 4. Maintenance queue

1. Add new Reddit and Weibo monthly TXT versions immutably; refresh their indexes.
2. Update the Awakenology physical repository snapshot and manifest monthly.
3. Run additive Yuanwushi crawls monthly; capture newly published CX Club lessons and linked files promptly.
4. Re-run the integrity audit after source changes.
5. Reopen the seven 404 gaps only if authoritative originals or sufficient identity evidence become available.
6. Perform direct Awakenology live-site parity checks when a suitable HTTP/browser capture session is available.
7. Add newly supplied or discovered external/private/offline sources as separate, provenance-labelled objects after rights and privacy review.

## 5. Scope boundary

This dashboard reports the identified and owner-confirmed source baseline. It does not claim that every item ever created, posted, stored privately, deleted, or linked externally has been discovered. Unknown external/private/offline material is an open-ended discovery domain, not a finite prerequisite for closing this initial baseline.

The Chinese OCR derivative and supplemental PDF/DOCX format checks are optional and are not completion blockers under the owner's scope decisions.

**Preserve originals. Keep captures, indexes, comparisons, OCR, and interpretations separate. Close only what the evidence and defined scope support.**
