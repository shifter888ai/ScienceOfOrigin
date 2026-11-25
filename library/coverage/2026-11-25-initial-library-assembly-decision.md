# Science of Origin — Initial Library Assembly Decision

**Decision date:** 2026-11-25 (Japan Standard Time)  
**Repository:** `shifter888ai/ScienceOfOrigin`  
**Decision:** The initial identified-source library baseline is assembled and integrity-checked within the bounded scope below. Residual unavailable resources and separate discovery/maintenance work are explicitly recorded; they are not concealed or treated as recovered.

## 1. What this decision covers

The baseline includes the following source objects and owner-defined scopes:

| Collection | Canonical/current source | Baseline disposition |
|---|---|---|
| Reddit | `materials/reddit-english-all.txt` and `materials/reddit-english-qa.txt` | Complete for the two owner-confirmed supplied TXT scopes; originals preserved |
| Weibo | `materials/weibo-1760432301-combined-originals-2026-11-24T06-35-03-529Z.txt` | Complete for the owner-confirmed original-post TXT scope; original preserved |
| Awakenology repository | Upstream commit `05523aec14c286bce397678b8a213cca1fc29563` | Complete physical tracked-file snapshot: 648 blobs, 823 tree entries, 51,750,456 bytes; subtree tree identity matches the pinned upstream tree |
| Yuanwushi website | Snapshot `materials/yuanwushi/snapshots/2026-11-25/` on `automation/yuanwushi-crawl` | Verified-with-gaps: 993 stored files independently checksum-audited; 133 Wiki pages and 2,659 unique record IDs reconciled; seven linked resources returned HTTP 404 and remain unavailable/unverified |
| Chinese compilation | `materials/元吾氏集录20210203.txt` | Complete for the owner-confirmed current research scope; two PDF volumes retained as supplemental references |
| Entropy assessment points | `materials/熵值检测点RR部分.rtf` | Complete canonical source per owner confirmation; DOCX retained as a supplemental duplicate-format copy |
| Science of Consciousness | Two separate TXT files under `materials/science-of-consciousness/` | Both original project uploads preserved unchanged and registered separately with SHA-256 values |

The Reddit and Weibo completeness statements apply only to the supplied archives and scopes confirmed by the project owner. They do not claim that every item ever posted to either platform has been captured.

## 2. Integrity evidence

The latest repository integrity report and manifest are authoritative for the selected branch-tip audit. The recorded audit checked 881 tracked files on `main` and 1,870 tracked files on the Yuanwushi archive branch; 1,518 unique Git blobs were independently hashed, with zero Git blob SHA-1 mismatches. SHA-256 values were generated for all unique blobs in scope.

The Awakenology physical subtree contains 648 ordinary tracked file blobs and matches the pinned upstream commit's root tree identity. It is not a submodule pointer.

The Yuanwushi archive contains 993 stored files at 993 unique paths (307,557,680 bytes). All 993 files passed independent SHA-256 verification: zero missing files, invalid paths, duplicate paths, size mismatches, or hash mismatches. The Wiki listing reconciliation found 2,659 record links and 2,659 distinct IDs across 133 pages, with zero duplicates.

These checks prove integrity and reconciliation of the captured objects; they do not prove that every possible historical, deleted, private, unlinked, or off-site source has been discovered.

## 3. Seven Yuanwushi resources: final baseline disposition

Seven linked resources returned HTTP 404 during the 2026-11-25 crawl: six gallery images and one audio file. Each URL is listed in `library/SOURCE-REGISTER.md` and `materials/yuanwushi/recovery-candidates/recovery-candidate-register.csv`.

Six image candidates exist at matching relative paths in the Awakenology archive. The audio candidate comes from the MDN `interactive-examples` repository at pinned commit `13024db581b08fae11a0ca229497198b9b0534e7`, whose repository declares CC0 1.0 Universal. **None of the seven candidates is byte-verified against the unavailable Yuanwushi original.**

Final disposition for this baseline: retain all seven as unavailable/unverified gaps; preserve candidate files only in the separate candidate layer; do not copy them into the immutable Yuanwushi snapshot or label them recovered. Reopen only if authoritative original bytes, cache evidence, or provenance sufficient to establish identity becomes available, or if a specific research task makes one of the missing assets material.

## 4. Awakenology live website: separate verification track

The pinned Awakenology Git repository is physically archived and verified. Public search/page snapshots also expose current homepage and language-index content, plus selected pages such as What Is Awakenology, Coach, and Disclaimer. These are discovery observations, not byte-level captures.

A full same-session HTTP audit of `.org`, `.space`, `www` aliases, redirect chains, canonical headers, all 136 sitemap routes, 12 non-sitemap routes, linked live assets, and historical website revisions has **not** been completed. This is a separate live-publication verification track; it does not invalidate the completed pinned Git repository snapshot. Do not claim live-domain parity until that direct audit is done.

## 5. What is outside this baseline

This decision does not claim an exhaustive inventory of every material ever created or held elsewhere. The following are explicitly outside the current baseline unless they become relevant to a defined research question or are supplied/discovered later:

- private, deleted, login-restricted, or otherwise inaccessible platform content;
- offline files, local disks, private cloud drives, email attachments, notebooks, and other accounts not supplied or connected for this review;
- historical website and repository revisions beyond the pinned snapshots;
- external linked works and third-party media not captured in the preserved source sets;
- future posts, lessons, repository changes, and other newly published material.

Rights, privacy, access conditions, and redistribution permissions must be reviewed before copying or publishing third-party material. No access control should be bypassed.

## 6. Maintenance and reopening rules

1. Add new Reddit and Weibo monthly TXT exports as immutable versions; record capture date, provenance, and checksums; regenerate derived indexes against the exact version.
2. Update the Awakenology physical repository snapshot monthly; preserve prior revisions and regenerate the path/blob/size manifest.
3. Run additive Yuanwushi crawls monthly and capture new CX Club lessons and linked files promptly under the event-driven lesson protocol.
4. Refresh the repository-wide integrity audit after source changes.
5. Reopen a bounded gap only when new evidence or a research need justifies it. Do not turn optional OCR, duplicate-format comparisons, or speculative source hunting into universal completion gates.

## 7. Completion statement

**Initial Library Assembly: complete within the identified and owner-confirmed baseline scope, with the seven Yuanwushi 404s explicitly retained as unavailable/unverified and Awakenology live-site parity separately unverified.**

**Library Coverage and Maintenance: ongoing.** New discoveries and monthly updates are additive. This is a bounded completion decision, not a claim that no other source exists anywhere.
