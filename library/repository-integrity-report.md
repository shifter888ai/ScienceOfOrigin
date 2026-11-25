# Repository Integrity Audit

**Generated (UTC):** 2026-11-25T06:24:39.145547+00:00

## Scope

Tracked tree entries at selected branch tips; generated integrity report/manifest paths are excluded to avoid self-reference; not unreachable Git history or external LFS payloads.

Git blob SHA-1 values were independently recomputed from exact blob bytes and compared with their tree object IDs. SHA-256 was also computed for every unique blob. The generated integrity manifest and report are excluded from the inventory to avoid self-reference. Git LFS pointer blobs are identified; their external payloads are not included.

## Branch snapshots

| Ref | Commit | Tracked blobs | Bytes | Non-blob entries | LFS pointers |
|---|---|---:|---:|---:|---:|
| main | 61e9649dd29a3131c37e674ac61ceb5880eb4656 | 897 | 114,185,422 | 0 | 0 |
| refs/remotes/origin/automation/yuanwushi-crawl | e9f8f7cadf6e9aa31063a781e1708f38d4c2c3ae | 1,870 | 421,098,213 | 0 | 0 |

## Aggregate

- Unique Git blobs independently hashed: **1,534**
- Unique blob bytes read: **402,538,820**
- Path/ref records: **2,767**
- Git blob SHA-1 mismatches: **0** (the script stops on any mismatch)
- SHA-256 values recorded: **1,534**

The full path-by-path manifest is repository-integrity-manifest.json. It is generated separately from the source tree so the manifest does not hash itself.
