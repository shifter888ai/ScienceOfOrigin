# Awakenology — Cross-Domain Discovery Notes

**Assessment date:** 2026-11-24  
**Scope:** Search-index and page-snapshot observations for `awakenology.org` and `awakenology.space`.  
**Status:** Discovery only; no live HTTP parity or redirect audit completed.

## Confirmed discovery observations

1. Search indexes both `https://awakenology.space/` and `https://www.awakenology.org/` with the same home-page title, “Awakenology - How To Free Your Soul”.
2. The `.org` home page was readable as a page snapshot. It exposes English, Japanese, and Chinese navigation and a footer.
3. The `.org/English/` page snapshot exposes the English contents menu.
4. A recent search-index result for `.space/English/` exposes additional menu entries, including “Latest Videos”, a “Memories” section, and two more “The Ultimate Source” topics.

## Apparent menu divergence — do not over-interpret

The available `.space` English contents result was crawled last week. The opened `.org` English page snapshot was crawled about four months earlier. The newer `.space` result includes items not visible in that older `.org` snapshot.

This is evidence of different indexed snapshots, not proof that the current live domains serve different content. It may reflect different crawl times, cached versions, redirects, or actual content drift. Only a same-time direct capture of both domains can resolve this.

## Access limitations in this pass

- Direct open of the `.space` home and English contents pages returned cache misses.
- Direct reads of both domains' `robots.txt` and `sitemap.xml` were unavailable through the web reader.
- The repository `sitemap.xml` and `robots.txt` remain available as repository artifacts, but they do not establish current live responses.
- No HTTP status, redirect chain, canonical tag, response body hash, or live route equivalence has been verified.

## Next verification protocol

1. Capture `.org`, `.space`, `www.org`, and `www.space` responses in one session.
2. Record status code, redirect chain, final URL, canonical tag, response headers, retrieval timestamp, and SHA-256 of each response body.
3. Compare the home page and language indexes first, then test every one of the 136 sitemap routes on both hostnames.
4. Compare all 12 classified non-sitemap HTML routes, respecting robots and access controls.
5. Compare linked images, documents, videos, and other assets by URL and checksum; keep changed versions as separate source objects.
6. Only after these tests, classify routes as identical mirrors, redirects, domain-specific versions, unavailable, or uncertain.

## Provenance

See `awakenology-domain-discovery.csv` and capture-log records CAP-20261124-048 through CAP-20261124-053. Search/page references are preserved there for traceability. This report contains no original page HTML or media binaries.
