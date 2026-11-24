# Reddit profile comments feed assessment — 2026-11-24

## Source and capture

- Account: u/Lower-Lingonberry-40
- Profile comments page: https://www.reddit.com/user/Lower-Lingonberry-40/comments/
- Capture date: 2026-11-24
- Surface: signed-in Reddit browser tab, extracted visible page text
- Visible profile setting: “Showing all comments”
- Sort selected: New

## Observed coverage

- Distinct comment IDs in the captured page: **36**
- Comment bodies rendered in the text snapshot: **36/36**
- Subreddit distribution: NoStupidQuestions 27; EscapingPrisonPlanet 7; alieninterview 2
- Relationship types: comment 33; reply 3
- Displayed relative ages: 2 yr. ago 35; 3 yr. ago 1
- First/newest visible item: lk5n97v (2 yr. ago)
- Last/oldest visible item: l1rncim (3 yr. ago)

All 36 native comment IDs match the earlier 2026-11-24 live-feed capture; this inspection did not reveal additional IDs beyond that prior capture.

## Recovery of previously unreadable comment

The oldest visible comment, `l1rncim`, now has its body rendered in the profile feed as **“👍”**. The earlier individual-thread text snapshot did not render the body. The profile-feed capture therefore resolves the body-text gap for this record.

## Native-ID and source-text crosswalk

A direct comparison of all 36 captured profile-feed records against the primary Reddit TXT (blob SHA 0452d11a39654864572c0d563667765b5c96da3c) gives the following breakdown:

| Cross-source result | Count | Interpretation |
|---|---:|---|
| Exact profile comment IDs present in the primary TXT | 24 | Exact native comment-ID matches |
| Comment IDs absent, but matching body text appears in the corresponding parent-thread block | 5 | Four comments under post 1eydeks and one under post 1eyufcg; body-level matches, not native-ID matches |
| Parent post and comment IDs absent; thread title displayed as “[deleted by user]” in the profile feed | 6 | No corresponding parent block or exact body text found in the primary TXT |
| Parent post and comment ID absent, with body recovered from profile feed | 1 | l1rncim in post 1cf7vdu; captured body is “👍” |

### Five body-level matches without native comment IDs

- Post 1eydeks, source block lines 86–175: profile comment IDs ljyxctg, ljyx4ax, ljywvqu and ljywl5t. Their exact body texts appear within this same parent-thread block, but those four profile comment IDs are not present in the TXT.
  - TXT Source locator: https://www.reddit.com/r/EscapingPrisonPlanet/comments/1eydeks/bad_news_it_seems_like_youll_get_sent_back_to/ljckzao/?context=3
- Post 1eyufcg, source block lines 177–197: profile comment ID ljyvgxb. Its exact body text appears within this same parent-thread block, but the profile comment ID is not present in the TXT.
  - TXT Source locator: https://www.reddit.com/r/EscapingPrisonPlanet/comments/1eyufcg/woman_stuck_in_dream_for_40_years/ljfyhgj/?context=3

These are strong body-and-parent-block correspondences, but the TXT does not preserve the same native comment IDs for those five records. Keep them labelled as body-level matches rather than exact ID matches.

### Six deleted-title records absent from the primary TXT

The following profile-feed records have the displayed thread title “[deleted by user]”; neither their parent post IDs nor comment IDs occur in the primary TXT, and their captured body texts were not found there:

- lk5k3r4 — post 1f2dllc
- lk5jk51 — post 1f20zhh
- lk5j7wo — post 1f1x4ul
- lk5j3zo — post 1f2d2de
- lk5hu19 — post 1f29szz
- ljzvb4w — post 1f1ibgz

The available evidence does not establish why these six records are absent from the TXT. Do not infer a filtering or deletion cause.

### One recovered body with no matching parent block

- l1rncim — post 1cf7vdu — body text “👍”.
- The body is preserved in the profile-feed JSONL capture.
- The parent post ID and comment ID are absent from the primary TXT.
- No explanation for the mismatch is inferred.

## Completeness assessment

The page visibly reports “Showing all comments” and the captured text contains no “Load more” or next-page control. However, it does not expose an explicit total-comment count, a terminal/end-of-history marker, or a verifiable pagination cursor. Therefore:

- The 36 records are a verified capture of all comment cards exposed in this browser snapshot.
- The displayed age range reaches back to “3 yr. ago”.
- This is **not yet sufficient evidence to certify that the 36 records are the account’s complete public comment history since account creation**.
- Do not infer missing-comment counts from the profile’s aggregate “Contributions” figure; it is not a verified comment total.

## Preservation

The per-comment text and native IDs are preserved in the adjacent JSONL capture. This is a browser text extraction, not a byte-for-byte export of Reddit’s underlying data. Relative ages are retained as displayed; exact timestamps have not been independently recovered.

## Next verification

A full-history claim still requires either an authoritative Reddit account export/API result with pagination exhausted, or a browser session capable of loading and verifying every page/scroll segment through the earliest available comment. Keep the source status as partial-capture until that check is completed.
