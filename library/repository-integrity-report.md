# Repository Integrity Audit

**Generated (UTC):** 2026-11-25T05:59:11.589108+00:00

## Scope

Tracked tree entries at selected branch tips; not unreachable Git history or external LFS payloads.

Git blob SHA-1 values were independently recomputed from exact blob bytes and compared with their tree object IDs. SHA-256 was also computed for every unique blob. Git LFS pointer blobs are identified; their external payloads are not included.

## Branch snapshots

| Ref | Commit | Tracked blobs | Bytes | Non-blob entries | LFS pointers |
|---|---|---:|---:|---:|---:|
| main | 92a2502af507b9274ff072945a0860737fe54751 | 881 | 113,081,391 | 0 | 0 |
| refs/remotes/origin/automation/yuanwushi-crawl | e9f8f7cadf6e9aa31063a781e1708f38d4c2c3ae | 1,870 | 421,098,213 | 0 | 0 |

## Aggregate

- Unique Git blobs independently hashed: **1,518**
- Unique blob bytes read: **401,434,789**
- Path/ref records: **2,751**
- Git blob SHA-1 mismatches: **0** (the script stops on any mismatch)
- SHA-256 values recorded: **1,518**

The full path-by-path manifest is repository-integrity-manifest.json. It is generated separately from the source tree so the manifest does not hash itself.
