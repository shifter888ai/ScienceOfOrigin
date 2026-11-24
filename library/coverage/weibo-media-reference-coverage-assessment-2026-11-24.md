# Weibo Media-Reference Coverage and Omitted-Image Recovery Index — 2026-11-24

## Verified coverage

- The original TXT has **134** records with an explicit omitted-image note.
- The media-reference index contains **234** unique parent-post rows.
- All **134/134** omitted-image parent records are represented in the media-reference index.
- The source export contains **114 URL occurrences** across **67 unique URL values**.
- The media-reference index contains **121 URL occurrences** across **74 unique URL values**; the seven additional unique locators were added from live-profile spot checks. One URL differs only by trailing source punctuation.
- The media-reference index therefore provides a parent-record locator for every omitted-image note, but this does not mean the images themselves have been recovered.

## Binary recovery status

The export is text-only and explicitly omits the image binaries. No image binary has been archived or checksummed in this recovery index. Every one of the 134 records is marked `not-captured` / `not-recovered` until the actual image file is obtained and its SHA-256 recorded.

## Recovery index

`weibo-omitted-image-recovery-index.csv` contains one row per omitted-image post, including:
- original record number, timestamp, export page and source line range;
- original omission note;
- whether a media-reference index row exists;
- media-reference type and visible URL references;
- binary capture and recovery status.

## Important distinction

The 134/134 result is **index coverage**, not media recovery. Some posts may expose only a note that an image was omitted, without a direct image URL. Do not infer a recoverable asset URL from a filename or generic Weibo page locator. Recover each binary from a verified source and retain its parent record number and checksum.
