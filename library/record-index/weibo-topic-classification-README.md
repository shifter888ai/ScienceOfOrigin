# Weibo Topic Classification — Provisional

## Purpose

This is a discovery aid over the preserved Xiaowei Memory export, not an authoritative interpretation of the author's intent or a validated taxonomy. It adds searchable topic labels without modifying the original TXT or the structural index.

## Method

- Input: `library/record-index/weibo-originals-record-index.csv`.
- Unit: one export record per sequential record number (001–765).
- Method: transparent Chinese keyword rules; multiple tags may apply to one record.
- Each row includes `classification_method` and `keyword_evidence` so a researcher can see why a tag was assigned.
- `general-reflection` is a fallback when none of the current keyword groups match.
- No model-generated interpretation, translation, claim verification, or topic adjudication is implied.

## Provisional tag groups

| Tag | Keyword family represented |
|---|---|
| consciousness-awakening | 意识、觉醒、开悟、灵魂、意识强度、催醒 |
| hypnosis-reincarnation | 催眠、轮回、转世、前世、潜催 |
| origin-cosmos-time-space | 本源、起源、宇宙、星际、空间、时间、维度 |
| freewill-freedom-choice | 自由意志、自由、选择、自主、意愿 |
| memory-dream-perception | 记忆、梦境、回忆、感知、幻觉 |
| practice-experience | 修炼、修行、观察、体验、方法、实践 |
| measurement-science | 检测、测量、数据、频率、光谱、熵、实验、科学 |
| relationships-society-commentary | 社会、人类、人性、教育、权威、迷信、认知 |
| announcements-projects | 公告、官网、网站、公开课、俱乐部、通知 |
| health-body-biology | 身体、健康、DNA、基因、大脑、神经 |
| general-reflection | Fallback only; no listed keyword matched |

## Current tag counts

Counts below are tag assignments, not mutually exclusive post totals.

- `general-reflection`: 397
- `consciousness-awakening`: 228
- `origin-cosmos-time-space`: 127
- `hypnosis-reincarnation`: 124
- `practice-experience`: 119
- `freewill-freedom-choice`: 100
- `memory-dream-perception`: 61
- `relationships-society-commentary`: 36
- `measurement-science`: 25
- `announcements-projects`: 19
- `health-body-biology`: 9

## Outputs

- `weibo-originals-topic-index.csv`: one row per post, same source fields as the structural index plus provisional tags, method, and matched keyword evidence.
- `weibo-media-reference-index.csv`: posts with explicit media notes, URLs, or media/link markers. This is a locator list only; it does not contain downloaded binary media.
- `weibo-topic-classification-README.md`: this method note.

## Review cautions

Keyword matching is sensitive to context and polysemy. A keyword can occur in a quotation, denial, criticism, tag string, or unrelated context. A missing keyword does not mean a topic is absent. These labels should be reviewed before being used for statistical claims or research conclusions. Preserve them as provisional and versioned.

## Media recovery status

The source export is text-only and explicitly records omitted image content in 134 posts. The media locator index currently covers 234 posts and contains 67 distinct visible URL strings. These URLs may point to videos, articles, profile pages, or other resources; they are not all direct downloadable media links. No media binaries have been recovered in this pass. Use the original Weibo post permalink or the visible URL as a locator and record each retrieval outcome separately.
