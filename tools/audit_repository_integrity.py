#!/usr/bin/env python3
"""Build a SHA-1/SHA-256 integrity inventory for selected Git branch snapshots."""
from __future__ import annotations
import argparse
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

def git(*args: str) -> bytes:
    return subprocess.check_output(["git", *args])

def tracked_entries(ref: str) -> list[dict]:
    raw = git("ls-tree", "-r", "-l", "-z", ref)
    entries = []
    for item in raw.split(b"\\0"):
        if not item:
            continue
        metadata, raw_path = item.split(b"\\t", 1)
        mode, kind, oid, size_text = metadata.decode("ascii").split(" ", 3)
        path = raw_path.decode("utf-8")
        if kind == "blob":
            entries.append({"ref": ref, "path": path, "mode": mode, "git_blob_sha1": oid, "bytes": int(size_text), "object_type": "blob"})
        else:
            entries.append({"ref": ref, "path": path, "mode": mode, "git_object": oid, "object_type": kind})
    return entries

def hash_blob(oid: str, expected_size: int) -> dict:
    process = subprocess.Popen(["git", "cat-file", "blob", oid], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    sha256 = hashlib.sha256()
    sha1 = hashlib.sha1()
    sha1.update(f"blob {expected_size}\\0".encode("ascii"))
    size = 0
    assert process.stdout is not None
    while True:
        chunk = process.stdout.read(1024 * 1024)
        if not chunk:
            break
        size += len(chunk)
        sha256.update(chunk)
        sha1.update(chunk)
    stderr = process.stderr.read() if process.stderr else b""
    status = process.wait()
    if status:
        raise RuntimeError(f"git cat-file failed for {oid}: {stderr.decode('utf-8', 'replace')}")
    if size != expected_size:
        raise RuntimeError(f"size mismatch for {oid}: tree={expected_size}, read={size}")
    actual_git_sha1 = sha1.hexdigest()
    if actual_git_sha1 != oid:
        raise RuntimeError(f"Git blob hash mismatch for {oid}: computed {actual_git_sha1}")
    probe = subprocess.check_output(["git", "cat-file", "blob", oid])[:80]
    return {"bytes": size, "git_blob_sha1_verified": actual_git_sha1, "sha256": sha256.hexdigest(),
            "git_lfs_pointer": probe.startswith(b"version https://git-lfs.github.com/spec/v1")}

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--refs", nargs="+", required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()
    commit_ids = {ref: git("rev-parse", ref).decode().strip() for ref in args.refs}
    entries = []
    for ref in args.refs:
        entries.extend(tracked_entries(ref))
    sizes: dict[str, int] = {}
    for entry in entries:
        if entry["object_type"] == "blob":
            oid, size = entry["git_blob_sha1"], entry["bytes"]
            if oid in sizes and sizes[oid] != size:
                raise RuntimeError(f"inconsistent sizes for Git blob {oid}")
            sizes[oid] = size
    blob_hashes = {oid: hash_blob(oid, size) for oid, size in sorted(sizes.items())}
    for entry in entries:
        if entry["object_type"] == "blob":
            entry.update(blob_hashes[entry["git_blob_sha1"]])
    branch_summary = []
    for ref in args.refs:
        rows = [e for e in entries if e["ref"] == ref]
        blobs = [e for e in rows if e["object_type"] == "blob"]
        branch_summary.append({
            "ref": ref, "commit": commit_ids[ref], "tracked_blobs": len(blobs),
            "tracked_blob_bytes": sum(e["bytes"] for e in blobs),
            "non_blob_entries": len(rows) - len(blobs),
            "lfs_pointer_blobs": sum(1 for e in blobs if e.get("git_lfs_pointer")),
        })
    manifest = {
        "schema_version": 1,
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Tracked tree entries at selected branch tips; not unreachable Git history or external LFS payloads.",
        "refs": branch_summary,
        "unique_git_blobs_hashed": len(blob_hashes),
        "unique_git_blob_bytes": sum(sizes.values()),
        "files": sorted(entries, key=lambda e: (e["ref"], e["path"])),
    }
    args.manifest.parent.mkdir(parents=True, exist_ok=True)
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.manifest.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\\n", encoding="utf-8")
    lines = [
        "# Repository Integrity Audit", "",
        f"**Generated (UTC):** {manifest['generated_utc']}", "",
        "## Scope", "", manifest["scope"], "",
        "Git blob SHA-1 values were independently recomputed from exact blob bytes and compared with their tree object IDs. SHA-256 was also computed for every unique blob. Git LFS pointer blobs are identified; their external payloads are not included.", "",
        "## Branch snapshots", "",
        "| Ref | Commit | Tracked blobs | Bytes | Non-blob entries | LFS pointers |",
        "|---|---|---:|---:|---:|---:|",
    ]
    for row in branch_summary:
        lines.append(f"| {row['ref']} | {row['commit']} | {row['tracked_blobs']:,} | {row['tracked_blob_bytes']:,} | {row['non_blob_entries']:,} | {row['lfs_pointer_blobs']:,} |")
    lines += ["", "## Aggregate", "",
        f"- Unique Git blobs independently hashed: **{len(blob_hashes):,}**",
        f"- Unique blob bytes read: **{sum(sizes.values()):,}**",
        f"- Path/ref records: **{len(entries):,}**",
        "- Git blob SHA-1 mismatches: **0** (the script stops on any mismatch)",
        f"- SHA-256 values recorded: **{len(blob_hashes):,}**", "",
        "The full path-by-path manifest is repository-integrity-manifest.json. It is generated separately from the source tree so the manifest does not hash itself.", ""]
    args.report.write_text("\\n".join(lines), encoding="utf-8")
    print(json.dumps({"refs": branch_summary, "unique_git_blobs_hashed": len(blob_hashes),
        "unique_git_blob_bytes": sum(sizes.values()), "path_ref_records": len(entries),
        "manifest": str(args.manifest), "report": str(args.report)}, ensure_ascii=False, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
