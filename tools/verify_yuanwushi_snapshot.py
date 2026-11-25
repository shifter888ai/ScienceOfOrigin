#!/usr/bin/env python3
"""Independently verify every stored file in a Yuanwushi snapshot."""
from __future__ import annotations
import argparse, hashlib, json, sys
from collections import Counter
from pathlib import Path

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository-root", type=Path, required=True)
    parser.add_argument("--snapshot", required=True)
    args = parser.parse_args()
    repo_root = args.repository_root.resolve()
    snapshot = (repo_root / args.snapshot).resolve()
    if repo_root not in snapshot.parents:
        raise SystemExit("ERROR: snapshot path escapes repository root")
    manifest = snapshot / "capture-manifest.jsonl"
    if not manifest.is_file():
        raise SystemExit(f"ERROR: manifest not found: {manifest}")
    records = []
    with manifest.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise SystemExit(f"ERROR: invalid JSON at line {line_number}: {exc}")
    stored = [r for r in records if r.get("stored") and r.get("path")]
    paths = [r["path"] for r in stored]
    counts = Counter(paths)
    duplicate_paths = sorted(p for p, count in counts.items() if count > 1)
    missing, size_mismatches, hash_mismatches, invalid_paths = [], [], [], []
    checked_bytes = 0
    checked_files = 0
    for record in stored:
        relative = Path(record["path"])
        if relative.is_absolute() or ".." in relative.parts:
            invalid_paths.append(record["path"])
            continue
        file_path = (repo_root / relative).resolve()
        if repo_root not in file_path.parents:
            invalid_paths.append(record["path"])
            continue
        if not file_path.is_file():
            missing.append(record["path"])
            continue
        digest = hashlib.sha256()
        actual_size = 0
        with file_path.open("rb") as source:
            while True:
                chunk = source.read(1024 * 1024)
                if not chunk:
                    break
                actual_size += len(chunk)
                digest.update(chunk)
        checked_files += 1
        checked_bytes += actual_size
        if record.get("bytes") is not None and actual_size != record["bytes"]:
            size_mismatches.append({"path": record["path"], "expected": record["bytes"], "actual": actual_size})
        actual_hash = digest.hexdigest()
        expected_hash = record.get("sha256")
        if not expected_hash or actual_hash.lower() != str(expected_hash).lower():
            hash_mismatches.append({"path": record["path"], "expected": expected_hash, "actual": actual_hash})
    result = {
        "snapshot": args.snapshot,
        "manifest_records": len(records),
        "stored_records": len(stored),
        "unique_stored_paths": len(set(paths)),
        "duplicate_path_groups": len(duplicate_paths),
        "files_independently_hashed": checked_files,
        "bytes_independently_hashed": checked_bytes,
        "missing_files": missing,
        "invalid_paths": invalid_paths,
        "size_mismatch_count": len(size_mismatches),
        "size_mismatches": size_mismatches,
        "sha256_mismatch_count": len(hash_mismatches),
        "sha256_mismatches": hash_mismatches,
        "duplicate_paths": duplicate_paths,
        "passed": not (missing or invalid_paths or size_mismatches or hash_mismatches or duplicate_paths),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if not result["passed"]:
        print("AUDIT FAILED", file=sys.stderr)
        return 1
    print("AUDIT PASSED: every stored source file matches its manifest size and SHA-256.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
