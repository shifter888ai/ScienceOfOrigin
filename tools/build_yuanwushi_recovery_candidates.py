#!/usr/bin/env python3
"""Build a provenance register for alternate-source candidates for Yuanwushi 404 assets."""
from __future__ import annotations
import csv, hashlib
from pathlib import Path

ROOT=Path(".")
MANIFEST=ROOT/"library/awakenology-file-manifest.json"
MDN_FILE=ROOT/"mdn-interactive-examples/live-examples/media/cc0-audio/t-rex-roar.mp3"
OUT=ROOT/"materials/yuanwushi/recovery-candidates"
OUT.mkdir(parents=True,exist_ok=True)
target=OUT/"mdn-t-rex-roar.mp3"
target.write_bytes(MDN_FILE.read_bytes())
audio_bytes=target.stat().st_size
audio_sha=hashlib.sha256(target.read_bytes()).hexdigest()

import json
manifest=json.loads(MANIFEST.read_text(encoding="utf-8"))
assets={
 "gallery/ad1.png":("https://www.yuanwushi.org/gallery/ad1.png?ts=1782918978","https://www.yuanwushi.org/article-13-6710.html"),
 "gallery_gen/b52fa1d35f2d1619a1f59346867b078e_fit.png":("https://www.yuanwushi.org/gallery_gen/b52fa1d35f2d1619a1f59346867b078e_fit.png?ts=1782918978","https://www.yuanwushi.org/article-13-6710.html"),
 "gallery_gen/2651c57393beec7145101a09f294103b_fit.png":("https://www.yuanwushi.org/gallery_gen/2651c57393beec7145101a09f294103b_fit.png?ts=1782918978","https://www.yuanwushi.org/article-13-6710.html"),
 "gallery/ad3.png":("https://www.yuanwushi.org/gallery/ad3.png?ts=1782918978","https://www.yuanwushi.org/article-13-6710.html"),
 "gallery_gen/df80bfe5abe2c2024c726a1b44b6c4ca_fit.png":("https://www.yuanwushi.org/gallery_gen/df80bfe5abe2c2024c726a1b44b6c4ca_fit.png?ts=1782918978","https://www.yuanwushi.org/article-13-6710.html"),
 "gallery_gen/1a31ccfafcc0abc14fa37c5d2236feed_898x490_fit.png":("https://www.yuanwushi.org/gallery_gen/1a31ccfafcc0abc14fa37c5d2236feed_898x490_fit.png?ts=1782918978","https://www.yuanwushi.org/article-13-6710.html"),
}
rows=[]
for path,(url,parent) in assets.items():
    entry=next(x for x in manifest["files"] if x["path"]==path)
    rows.append({
      "original_yuanwushi_url":url,"parent_page":parent,"capture_status":"HTTP 404 on 2026-11-25",
      "candidate_repository_path":"materials/awakenology/"+path,
      "candidate_source":"Awakenology physical archive; pinned upstream commit 05523aec14c286bce397678b8a213cca1fc29563",
      "candidate_bytes":entry["bytes"],"candidate_sha256":entry["sha256"],
      "identity_verification":"UNVERIFIED — same relative path and filename only; original source bytes unavailable",
      "notes":"Existing candidate retained in Awakenology archive; do not copy into the Yuanwushi original snapshot or label as recovered without identity/provenance confirmation."
    })
rows.append({
 "original_yuanwushi_url":"https://www.yuanwushi.org/media/cc0-audio/t-rex-roar.mp3",
 "parent_page":"https://www.yuanwushi.org/article-5-6634.html",
 "capture_status":"HTTP 404 on 2026-11-25",
 "candidate_repository_path":"materials/yuanwushi/recovery-candidates/mdn-t-rex-roar.mp3",
 "candidate_source":"mdn/interactive-examples at commit 13024db581b08fae11a0ca229497198b9b0534e7; live-examples/media/cc0-audio/t-rex-roar.mp3; repository LICENSE: CC0 1.0 Universal",
 "candidate_bytes":audio_bytes,"candidate_sha256":audio_sha,
 "identity_verification":"PROBABLE SOURCE CANDIDATE — identical relative path/name; byte identity to unavailable Yuanwushi file cannot be tested",
 "notes":"Stored only in the separate recovery-candidates layer. It does not replace the missing original capture."
})
csv_path=OUT/"recovery-candidate-register.csv"
with csv_path.open("w",encoding="utf-8-sig",newline="") as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(rows)
readme=f"""# Yuanwushi recovery candidates

This directory is a separate, additive candidate-recovery layer. It does not modify or replace the original 2026-11-25 Yuanwushi crawl.

## Candidate findings

- Six image files referenced by Yuanwushi article-13-6710 returned HTTP 404 in the crawl. Files with the same relative paths and names exist in the physically archived Awakenology repository. Their current sizes and SHA-256 values are recorded in recovery-candidate-register.csv. The original Yuanwushi bytes were unavailable, so **same filename/path is not proof of byte identity**.
- The audio file /media/cc0-audio/t-rex-roar.mp3 returned HTTP 404 from Yuanwushi article-5-6634. The same relative path and filename exist in mdn/interactive-examples at pinned commit 13024db581b08fae11a0ca229497198b9b0534e7. That repository declares CC0 1.0 Universal. A candidate copy is stored here with SHA-256 recorded in the CSV. This is a strong source candidate, but byte identity to the unavailable Yuanwushi file is still unverified.

## Preservation rule

Do not move these candidate files into the original Yuanwushi snapshot or mark the seven resources recovered until identity or provenance is confirmed. Keep candidate source, commit, license, byte size, and SHA-256 recorded.
"""
(OUT/"README.md").write_text(readme,encoding="utf-8")
print(f"candidate audio bytes={audio_bytes} sha256={audio_sha}; candidate register rows={len(rows)}")
