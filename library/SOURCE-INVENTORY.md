# Initial Source Inventory — Science of Origin

**Inventory version:** 0.1  
**Repository:** `shifter888ai/ScienceOfOrigin`  
**Branch reviewed:** `main`  
**Repository tree commit reviewed:** `75b01f903f0c88c66aed5d904fc291db45172262`  
**Inventory date:** 2026-11-21  
**Status:** Initial repository-level inventory; not yet a complete inventory of all materials ever recorded.

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
