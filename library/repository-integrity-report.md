# Repository Integrity Audit

**Generated (UTC):** 2026-11-25T06:59:09.896222+00:00

## Scope

Tracked tree entries at selected branch tips; generated integrity report/manifest paths are excluded to avoid self-reference; not unreachable Git history or external LFS payloads.

Git blob SHA-1 values were independently recomputed from exact blob bytes and compared with their tree object IDs. SHA-256 was also computed for every unique blob. The generated integrity manifest and report are excluded from the inventory to avoid self-reference. Git LFS pointer blobs are identified; their external payloads are not included.

## Branch snapshots

| Ref | Commit | Tracked blobs | Bytes | Non-blob entries | LFS pointers |
|---|---|---:|---:|---:|---:|
| main | 858cc97447121a5e551a60ad7235c61badf9ef30 | 898 | 114,208,635 | 0 | 0 |
| refs/remotes/origin/automation/yuanwushi-crawl | e9f8f7cadf6e9aa31063a781e1708f38d4c2c3ae | 1,870 | 421,098,213 | 0 | 0 |

## Aggregate

- Unique Git blobs independently hashed: **1,540**
- Unique blob bytes read: **402,622,775**
- Path/ref records: **2,768**
- Git blob SHA-1 mismatches: **0** (the script stops on any mismatch)
- SHA-256 values recorded: **1,540**

The full path-by-path manifest is repository-integrity-manifest.json. It is generated separately from the source tree so the manifest does not hash itself.
