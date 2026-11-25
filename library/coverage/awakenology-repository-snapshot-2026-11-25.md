# Awakenology Git Repository Snapshot — 2026-11-25

## Snapshot identity

- Source repository: https://github.com/shifter888ai/awakenology
- Source branch: `main`
- Pinned commit: `05523aec14c286bce397678b8a213cca1fc29563`
- Recursive tree entries: 823
- File blobs: 648
- Combined file size: 51,750,456 bytes
- Directories/tree entries: 175
- Snapshot manifest: [awakenology-repository-snapshot-2026-11-25.csv](awakenology-repository-snapshot-2026-11-25.csv)

## What is preserved

The CSV enumerates every file blob in the source commit, including its repository-relative path, Git mode, object type, Git blob SHA, and byte size. The complete source tree is physically copied into `materials/awakenology/` as ordinary tracked files in the ScienceOfOrigin repository.

This captures the entire repository tree at the pinned revision as a reproducible, auditable reference. It includes site pages, images and other assets, scripts, documentation, workflows, internal tools, and other tracked files.

## Important implementation distinction

The library contains a **physical copy of all tracked source blobs plus a complete tree manifest**. The files are ordinary Git blobs in the ScienceOfOrigin repository, not a submodule pointer. The subtree tree SHA matches the root tree SHA of the pinned upstream commit, establishing exact tree identity for this snapshot.

## Monthly update procedure

1. Fetch the upstream `main` commit and recursive Git tree.
2. Compare it with the prior pinned commit and manifest.
3. Record added, modified, renamed, and deleted paths.
4. Update the physical source subtree and create a dated full manifest.
5. Preserve prior snapshot manifests and commits in repository history.
6. Verify the pinned upstream commit and every physical manifest path, mode, Git blob SHA, and size.

## Scope boundary

This is a complete snapshot of the tracked Git repository tree at the stated commit. It is not a live-site crawl, a complete history of every past repository revision, or a capture of external resources linked from the site. Live-domain aliases, redirects, route responses, and historical website versions remain separate research tasks.

Git blob SHA values are Git object identifiers, not SHA-256 file checksums.


## Physical archive correction — 2026-11-25

An earlier draft of this report incorrectly described the library copy as a Git submodule. The current implementation is a **physical copy** under `materials/awakenology/`: 648 file blobs, 823 recursive tree entries, 51,750,456 bytes. Its subtree tree SHA matches the pinned upstream commit's root tree SHA. The correction supersedes the submodule wording above wherever it appears in older historical notes.
