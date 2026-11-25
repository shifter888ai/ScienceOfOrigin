# Yuanwushi recovery candidates

This directory is a separate, additive candidate-recovery layer. It does not modify or replace the original 2026-11-25 Yuanwushi crawl.

## Candidate findings

- Six image files referenced by Yuanwushi article-13-6710 returned HTTP 404 in the crawl. Files with the same relative paths and names exist in the physically archived Awakenology repository. Their current sizes and SHA-256 values are recorded in recovery-candidate-register.csv. The original Yuanwushi bytes were unavailable, so **same filename/path is not proof of byte identity**.
- The audio file /media/cc0-audio/t-rex-roar.mp3 returned HTTP 404 from Yuanwushi article-5-6634. The same relative path and filename exist in mdn/interactive-examples at pinned commit 13024db581b08fae11a0ca229497198b9b0534e7. That repository declares CC0 1.0 Universal. A candidate copy is stored here with SHA-256 recorded in the CSV. This is a strong source candidate, but byte identity to the unavailable Yuanwushi file is still unverified.

## Preservation rule

Do not move these candidate files into the original Yuanwushi snapshot or mark the seven resources recovered until identity or provenance is confirmed. Keep candidate source, commit, license, byte size, and SHA-256 recorded.
