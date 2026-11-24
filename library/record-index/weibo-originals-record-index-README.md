# Weibo Original-Post Record Index

## Source object

- Original export: `materials/weibo-1760432301-combined-originals-2026-11-24T06-35-03-529Z.txt`
- Platform/account: Weibo / 元吾氏
- Account UID: `1760432301`
- Source export label: “合并备份 · 原创微博”
- Export says: 765 original posts, 148 monthly groups, August 2010–November 2026.
- Export pagination: 160 pages.
- Time zone stated by export: Beijing Time (UTC+8).
- Git blob SHA of preserved source at indexing time: `50b5f3a20b5f2065fd6401816251356609afbed9`

## Index output

- `weibo-originals-record-index.csv` contains one row per detected post marker.
- The index preserves the extracted post text as exported, plus record number, timestamp, export page, source line range, character count, media note, and URLs visible in the text.
- Record numbers are the export's sequential labels (01–765), not asserted to be Weibo's native post IDs.
- Source line ranges refer to the unmodified TXT source file.
- Text is retained in Chinese and is not translated, normalized, or rewritten.

## Structural validation

- Detected post markers: 765
- Sequential numbering: 01–765, no gaps detected
- First timestamp: 2010-08-09 22:49:00
- Last timestamp: 2026-11-23 23:58:00
- Export pages detected: 0
- Records containing an explicit omitted-image note: 134
- URL strings found in extracted text: 114
- Records with empty extracted text: 0

## Live-account spot check (2026-11-24)

A connected-browser snapshot of the source account timeline exposed a top item titled “空间是什么”, with permalink `https://weibo.com/1760432301/RsLldnd80`. Its title matches export record 765, timestamped `2026-11-23 23:58:00` Beijing Time. This confirms that one item represented at the end of the export was also visible in the account timeline snapshot. The snapshot exposed only a limited recent-feed window; it does not validate the other 764 records, establish full account-history coverage, or preserve the associated video binary.

## Important limitations

This index is a navigation and search aid, not proof that the account's entire historical output has been captured. The export itself says it contains only locally saved original content. It does not establish completeness against the live account, deleted/private posts, reposts, or other Weibo content types.

The export is text-only. It explicitly notes omitted images in some records; video and image media are not preserved as binary attachments by this TXT file. Visible URLs are copied as found in the export and may be incomplete, line-wrapped, encoded, or malformed. No attempt has been made to repair them.

No topic labels have been assigned automatically. Topic classification should be a separate, reviewable derived layer linked to these stable export record numbers, so that interpretive tags do not alter the source text.

## Preservation rule

Keep the original TXT unchanged. Treat this CSV as a derived index. If a later export is made, preserve it as a separate version and compare it with this source; do not overwrite this archive or silently merge differing records.


## Follow-on discovery layers

- Provisional topic classification: `weibo-originals-topic-index.csv` (keyword-based, multi-label, review required).
- Media reference locator: `weibo-media-reference-index.csv` (not a media download; see the separate classification README).
- Method and limitations: `weibo-topic-classification-README.md`.

These derived files do not replace or modify the original export or the first structural index.

## Live media locator follow-up — 2026-11-24

The connected Weibo profile snapshot confirms that the latest visible post, `空间是什么`, matches export record 765. Its permalink is `https://weibo.com/1760432301/RsLldnd80`; the page exposes video locator `https://video.weibo.com/show?fid=1034:5368550857310263` and displays a duration of 01:55. A thumbnail filename is visible in the player snapshot: `68ee10adly1ijcio49qlnj21hc0u0ju7.jpg`.

The media-reference index now records the verified post and video URLs on record 765. This is locator verification only: neither the video nor thumbnail binary has been captured or checksummed. Do not count them as recovered media yet.

## Recent live-timeline reconciliation — 2026-11-24

A connected-browser snapshot of the account profile displayed six recent timeline entries, dated 2026-11-06 through 2026-11-23. Each entry was matched to a corresponding local export record by date and visible post label/text:

- Records 760–765 match the six visible timeline entries in the same date sequence.
- Verified post permalinks and the two visible video locators are recorded in `weibo-recent-timeline-live-match.csv`.
- Record 760 also exposes the linked article for “破权威幻”.
- Records 762 and 765 expose video players with displayed durations of 04:04 and 01:55 respectively.

This is a six-record recent-timeline spot check, not a complete account-history reconciliation. It does not establish that all 936 profile items are original posts or that the 765 locally saved export records cover the entire account history. The videos, thumbnail files and other omitted media remain unrecovered.
