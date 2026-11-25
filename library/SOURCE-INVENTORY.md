# Initial Source Inventory — Science of Origin

**Inventory version:** 0.2  
**Repository:** `shifter888ai/ScienceOfOrigin`  
**Branch reviewed:** `main`  
**Historical repository tree commit:** `75b01f903f0c88c66aed5d904fc291db45172262`  
**Inventory date:** 2026-11-25  
**Status:** Historical baseline retained; current state reconciled through main commit `61e9649dd29a3131c37e674ac61ceb5880eb4656`. See the current-state reconciliation section for verified counts and remaining gaps.

## 1. Scope and limits

This inventory records the contents visible in the Science of Origin GitHub repository at the commit above and identifies additional project reference files currently supplied to this workspace.

It does not establish that these are all materials ever created, recorded, or held elsewhere. External websites, accounts, historical forums, local disks, cloud drives, private conversations, media, notebooks, and other repositories have not yet been comprehensively inventoried.

The inventory distinguishes original source collections from research pages, working documents, website implementation files, and derived extraction reports.

## 2. Repository snapshot

The recursive Git tree contained **120 files** with a combined reported size of **54,579,959 bytes** (approximately 52.0 MiB).

| File type | Count | Reported size |
|---|---:|---:|
| HTML | 93 | 992,860 bytes |
| Markdown | 12 | 71,436 bytes |
| TXT | 4 | 4,846,102 bytes |
| PDF | 2 | 48,621,520 bytes |
| JavaScript | 3 | 13,831 bytes |
| CSS | 1 | 5,335 bytes |
| JSON | 2 | 13,364 bytes |
| MJS | 1 | 8,665 bytes |
| XML | 1 | 6,840 bytes |
| .gitignore | 1 | 6 bytes |
| **Total** | **120** | **54,579,959 bytes** |

These counts describe repository files, not the number of independent research records, cases, or concepts. A webpage may contain multiple research records; a source collection may contain many posts or messages; different files may overlap.

## 3. Existing source collections in `materials/`

The following files are present in the repository and must be preserved as separate source objects:

| Current path | Type | Reported size | Initial catalogue note |
|---|---|---:|---|
| `materials/reddit-english-all.txt` | TXT | 1,666,537 bytes | English Reddit collection; exact scope and internal structure require source-level inventory |
| `materials/reddit-english-qa.txt` | TXT | 360,078 bytes | English Q&A collection; possible overlap with the all-content collection must be examined, not assumed |
| `materials/元吾氏集录20210203-1.pdf` | PDF | 24,104,234 bytes | Chinese compilation, volume 1; inspect pages, embedded text, images, and structure |
| `materials/元吾氏集录20210203-2.pdf` | PDF | 24,517,286 bytes | Chinese compilation, volume 2; inspect pages, embedded text, images, and structure |
| `materials/元吾氏集录20210203.txt` | TXT | 2,819,410 bytes | Chinese text compilation; relationship to the PDF volumes and any conversion process requires verification |

The text and PDF versions must not be treated as interchangeable or duplicates until their contents, page boundaries, omissions, diagrams, tables, and conversion fidelity have been compared. Preserve every version.

The repository's `materials/README.md` describes the folder as public research materials and instructs preservation of original wording, dates, authorship, and source context. The repository is public; rights and permissions for each item still require review.

## 4. Existing research and architecture documents

The repository includes Markdown documents that should be catalogued as research/architecture sources rather than merged into the original source collections:

- `master.md` — locked Complete Research Library — Research Base Principle.
- `central-research-history-architecture.md` — Central Research History architecture and working principles.
- `recursive-discovery-architecture-update-001.md` — recursive discovery architecture update.
- `zero-origin-research-working-record.md` — Zero-Origin Research working record.
- `zero-origin-research-records-001-090.md` — numbered Zero-Origin research records 001–090.
- `research-dialogues-origin-and-loops.html` — research dialogue.
- `science-of-consciousness.html` — Science of Consciousness research page.
- `science-of-consciousness-progress-004.html` — Science of Consciousness progress record.
- `terminology.html` — evolving terminology reference.
- `research-history.html` — Central Research History published index.
- `research-map.html`, `research-directory.html`, and `research-framework.html` — navigation and framework views.

This list is illustrative, not exhaustive. All 93 HTML files and all 12 Markdown files are included in the repository-level file count and must be considered during full content inventory. The current site pages may contain source-derived text, current synthesis, editorial framing, or combinations of these; their internal content and provenance must be assessed individually.

## 5. Website and technical files

The repository also contains website implementation and navigation files, including:

- `assets/` — CSS and JavaScript assets.
- `functions/` — Cloudflare Pages function code.
- `scripts/` — site build script.
- `src/components/` — shared HTML components.
- `search-index.json`, `sitemap.xml`, `robots.txt`, `package.json`.
- Root-level site HTML pages.

These files are part of the repository inventory. Their primary role may be technical rather than source research, but they must not be silently discarded from the overall inventory. Their relevance can be reviewed later.

## 6. Additional project reference files supplied outside the repository

The following files are present in the current project workspace but were not identified as files in the repository tree reviewed above:

| Workspace filename | Approximate size | Initial role |
|---|---:|---|
| `Science-of-Consciousness.txt` | 5.8 KB | Project Description & Research Framework |
| `Science-of-Consciousness-—-Research-Architecture.txt` | 357 bytes | Research architecture outline |

These are additional project references. Before archival ingestion, register their original filenames, exact bytes, checksum, source/provenance, and access classification. Do not assume that a project upload is already preserved in the Git repository.

## 7. Existing derived extraction documents in the current workspace

Two prior working documents are also available in the current workspace:

- `Science-of-Origin-Full-Source-Extraction.md` — thematic extraction dossier.
- `Science-of-Origin-Passage-Level-Research-Index.md` — preliminary passage-level navigation index.

These are derived research aids, not original source archives. The passage-level index was produced with keyword-assisted classification and must remain labelled preliminary; it is not a complete or definitive case index. Both documents should be registered as derived artefacts with links to the sources and methods used to create them if they are later added to the repository.

## 8. Authorship and attribution notes requiring preservation

A previous project instruction states that answers in the identified user-supplied Chinese and English Q&A materials are authored by YWS, even when the source does not display a name or uses aliases/nicknames. This attribution instruction should be recorded as an explicit source-level attribution rule for those identified collections, while questioners and other original participants remain separately attributed.

This rule must not be generalized to unrelated sources without evidence. Preserve the source's displayed identity and the canonical attribution as distinct metadata where both are relevant.

## 9. Initial inventory findings and unresolved checks

1. The repository already contains both source collections and a large body of research pages and records.
2. The two English Reddit text files may overlap; compare record-level coverage before treating them as separate or duplicate content.
3. The Chinese TXT compilation and two PDF volumes require page-level comparison, including diagrams, tables, OCR, and text omissions.
4. The 93 HTML pages require content-level classification and source tracing; filenames and navigation labels are not sufficient.
5. Markdown files may contain original research notes, evolving frameworks, architecture, or derived summaries; classify by actual content and provenance.
6. Website technical files are inventoried but should not be treated as research claims.
7. The current inventory does not yet cover all external, private, offline, or historical source locations.
8. Access rights and privacy status need review before any broader republication or ingestion into a public-facing system.

## 10. Next inventory actions

- [ ] Generate a complete path-by-path catalogue of every repository file, retaining Git blob SHA, byte size, and file type.
- [ ] Calculate SHA-256 checksums for all source files after obtaining their exact bytes.
- [ ] Compare English source collections for overlap while preserving both originals.
- [ ] Compare Chinese PDF volumes against the TXT compilation, page by page.
- [ ] Review PDF page images for diagrams, tables, handwriting, and content not captured by text extraction.
- [ ] Inventory all HTML and Markdown contents, distinguishing source material, research records, current synthesis, and technical documentation.
- [ ] Register the two supplied Science of Consciousness files and prior extraction reports as separate project-workspace artefacts if approved for archival inclusion.
- [ ] Identify additional repositories, websites, accounts, local archives, media, and historical collections.
- [ ] Record privacy, permissions, copyright, and access restrictions before public copying.
- [ ] Update this inventory only with traceable findings and a dated revision history.

## 11. Governing reminder

This inventory is a starting snapshot, not a relevance filter and not a declaration of completeness.

**Preserve everything first. Discover and organize relationships through research.**


## Repository inventory refresh — 2026-11-25

A refreshed recursive Git tree inventory was captured from `main` at commit `48cf484a007ff651cceebfb2d7fe9fd2077f32d8` (tree `48cf484a007ff651cceebfb2d7fe9fd2077f32d8`). The current snapshot contains **215 repository files excluding this manifest itself**, totaling **60,831,716 bytes**. The refreshed manifest is [`FILE-MANIFEST.json`](FILE-MANIFEST.json), version 0.2. Existing inventory IDs were retained; newly discovered paths were appended with new IDs.

| Extension | Files |
|---|---:|
| `html` | 95 |
| `md` | 58 |
| `csv` | 38 |
| `txt` | 10 |
| `js` | 3 |
| `pdf` | 2 |
| `json` | 2 |
| `gitignore` | 1 |
| `css` | 1 |
| `jsonl` | 1 |
| `docx` | 1 |
| `rtf` | 1 |
| `mjs` | 1 |
| `xml` | 1 |
| **Total** | **215** |

This refresh includes the expanded research-library coverage and record-index files created since the initial snapshot. The count describes repository objects at this commit only; it does not establish completeness of the historical source archive.

### Newly registered entropy assessment source versions

| Repository path | Format | Size (bytes) | Git blob SHA | Content status |
|---|---|---:|---|---|
| `materials/熵值检测点RR部分.docx` | DOCX | 1,764,873 | `509d7dc53ba656bcc4b7f19631d162986b0a9119` | Initial inventory checkpoint only; superseded by the later DOCX/RTF comparison in the current-state section |
| `materials/熵值检测点RR部分.rtf` | RTF | 812,389 | `4554f3c8fbdf64a76f4fbbfc4a51dac10de05657` | Text successfully extracted and structurally reviewed; see the derived index |

At the initial inventory checkpoint, equivalence had not been established; the later current-state comparison records the normalized body-text result and remaining formatting gaps. Both formats remain separate source objects. Neither Git blob SHA is a SHA-256 checksum.


## Owner-confirmed source archives and repository snapshot — 2026-11-25

### Reddit

The project owner confirms that `materials/reddit-english-all.txt` and `materials/reddit-english-qa.txt` are complete, manually extracted and checked TXT archives for their intended Reddit collection scopes. Existing indexes are separate derived layers. Preserve the original TXT files unchanged and add one new manually checked version monthly.

### Weibo

The project owner confirms that `materials/weibo-1760432301-combined-originals-2026-11-24T06-35-03-529Z.txt` is the complete, manually extracted and checked TXT archive for its intended Weibo original-post scope. Existing 765-record and 160-page indexes are derived navigation layers. Preserve the source TXT unchanged and add one new manually checked version monthly. Optional media-binary recovery is a separate layer, not a completeness condition for this TXT archive.

### Awakenology

The upstream repository `https://github.com/shifter888ai/awakenology` is pinned at `05523aec14c286bce397678b8a213cca1fc29563` (648 file blobs, 823 recursive tree entries, 51,750,456 bytes). The current library stores this exact revision as ordinary tracked files under `materials/awakenology/`, with a complete path/mode/Git-blob-SHA/size manifest. This is a physical in-repository copy, not a Git submodule pointer. Update the copy and manifest monthly; preserve prior snapshots in Git history.



## Current-state reconciliation — 2026-11-25

The historical inventory sections above are retained as dated baselines. The latest repository-wide integrity audit covers main commit `61e9649dd29a3131c37e674ac61ceb5880eb4656` and the final Yuanwushi archive branch at `e9f8f7cadf6e9aa31063a781e1708f38d4c2c3ae`.

- Main: 897 tracked file blobs / 114,185,422 bytes.
- Yuanwushi archive branch: 1,870 tracked file blobs / 421,098,213 bytes.
- Aggregate: 1,534 unique Git blobs independently hashed, 402,538,820 unique-blob bytes, 2,767 path/ref records; zero Git blob SHA-1 mismatches; no Git LFS pointers.
- Awakenology: 648 physical tracked blobs / 51,750,456 bytes; subtree SHA exactly matches the pinned upstream commit's root tree SHA.
- Yuanwushi: 993 stored files / 993 unique paths / 307,557,680 bytes; independent SHA-256 audit passed. Its Wiki listing reconciles to 2,659 unique record IDs across 133 pages, with zero duplicates.
- Reddit and Weibo: owner-confirmed complete for their defined supplied TXT archive scopes; monthly updates are additive.
- Chinese compilation: 1,671 PDF pages match 1,671 TXT page markers; 1,455 exact normalized matches, 10 high-similarity, 206 image-only/no-extractable-text pages; OCR derivative stored separately.
- Entropy assessment: DOCX/RTF body text matches exactly after excluding the RTF-only TOC.
- Science of Consciousness: two uploaded TXT originals are archived separately and their repository SHA-256 values match the supplied originals.

The current `library/repository-integrity-manifest.json` and report are the active SHA-256 inventory. The older `library/FILE-MANIFEST.json` is a historical manifest and must not be treated as the current SHA-256 baseline.

## Historical automation branch review

The older Awakenology snapshot, physical-archive, bootstrap, workflow-fix, and Yuanwushi initial-crawl branches were compared with main by path and Git blob identity. They contain older workflow/register/site snapshots but no unique source-file paths absent from main; the early Awakenology bootstrap/physical-archive branch has an obsolete `.gitmodules` entry. The final Yuanwushi archive remains a separate source-bearing branch and is included in the integrity audit.

## Current completion boundary

The four priority source-acquisition milestones remain achieved within their defined scopes: Reddit TXT archive, Weibo TXT archive, Awakenology pinned repository snapshot, and Yuanwushi initial website crawl. The Chinese compilation TXT and Entropy RTF are owner-confirmed complete canonical sources for their defined research scopes. The two PDFs and DOCX remain preserved as supplemental originals; prior comparison and OCR outputs are optional derived aids, not completion gates.

Still open:
1. Identity/provenance checks for the seven Yuanwushi 404 recovery candidates; detail-page bodies, embedded media, deleted/private and unlinked historical resources are not all independently validated.
2. Awakenology live-site parity, .org/.space alias/redirect checks, linked external resources, and historical versions.
3. Discovery and rights/privacy review of external, private, offline, historical, and other-repository sources.
4. Monthly additive source updates and refresh of derived indexes/manifests.

Optional research-quality tasks, if later needed, include human verification of the Chinese OCR derivative and further PDF/DOCX visual or metadata review. These are not blockers to the owner-defined canonical source scopes.

The two Science of Consciousness uploads remain unchanged original TXT files; no merged or normalized replacement has been substituted.


## Owner clarification of canonical source scope — 2026-11-25

The project owner confirms that the Chinese compilation TXT (`materials/元吾氏集录20210203.txt`) alone is a complete source for the current research scope. The two PDFs contain additional images, but those images are not important at this stage; retain the PDFs as supplemental references, not as required completion inputs.

The project owner also confirms that the Entropy assessment RTF (`materials/熵值检测点RR部分.rtf`) alone is a complete source. The DOCX contains the same substantive content and no images; retain it as a supplementary duplicate-format copy. The RTF is the canonical source for current research use. These scope decisions supersede historical inventory statements that required PDF visual/OCR review or DOCX/RTF format reconciliation as completion gates. Preserve all original files unchanged.
