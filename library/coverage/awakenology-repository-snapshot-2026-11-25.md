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

The CSV enumerates every file blob in the source commit, including its repository-relative path, Git mode, object type, Git blob SHA, and byte size. The library's `materials/awakenology` entry is a Git submodule pointer pinned to this exact commit, with `.gitmodules` pointing to the upstream repository.

This captures the entire repository tree at the pinned revision as a reproducible, auditable reference. It includes site pages, images and other assets, scripts, documentation, workflows, internal tools, and other tracked files.

## Important implementation distinction

The library uses a **pinned Git submodule reference plus a complete tree manifest**. It does not physically duplicate every source blob into the ScienceOfOrigin repository. The source content remains hosted in the Awakenology repository and is retrieved when the submodule is initialized. The manifest records the exact object identities and sizes, so the referenced revision can be checked against the original tree.

## Monthly update procedure

1. Fetch the upstream `main` commit and recursive Git tree.
2. Compare it with the prior pinned commit and manifest.
3. Record added, modified, renamed, and deleted paths.
4. Update the submodule pointer and create a dated full manifest.
5. Preserve prior snapshot manifests and commits in repository history.
6. Verify the pinned submodule commit and every manifest path, mode, Git blob SHA, and size.

## Scope boundary

This is a complete snapshot of the tracked Git repository tree at the stated commit. It is not a live-site crawl, a complete history of every past repository revision, or a capture of external resources linked from the site. Live-domain aliases, redirects, route responses, and historical website versions remain separate research tasks.

Git blob SHA values are Git object identifiers, not SHA-256 file checksums.
