# Awakenology — Non-Sitemap HTML Route Review

**Assessment date:** 2026-11-24  
**Repository:** https://github.com/shifter888ai/awakenology  
**Reviewed repository baseline:** recursive tree commit `05523aec14c286bce397678b8a213cca1fc29563`  
**Review scope:** the 12 HTML routes previously found outside the 136 sitemap URL paths.

## Result

The 12 routes are not a homogeneous set of omitted content. Source inspection classifies them into:

- 1 custom 404 page.
- 1 experimental ASK model lab page.
- 3 public utility routes: combined Search / Ask, dedicated Ask, and dedicated Search.
- 4 editor/authoring routes (including a GitHub-hosted editor pilot).
- 3 prototype asset fragments (two scripts and one stylesheet).

No route in this 12-item set currently appears to be an omitted public article page. This is a provisional repository-source classification, not a live HTTP or access-control test.

## Important nuance

- `/ai-search/` is a public Search / Ask utility route and has no explicit noindex directive in the inspected HTML. Its sitemap omission should be tracked as a utility-route decision, not silently treated as a missing article.
- `/ask/` and `/search/` are utility pages with explicit `noindex,follow` metadata.
- `/Internal/New-Article/` identifies itself as an experimental, non-production ASK Model Lab and explicitly sets `noindex,nofollow`.
- `/editor/` is disallowed in the repository's `robots.txt`; the two generator pages and `/github-editor/` include explicit `noindex,nofollow` metadata.
- The three `scripts/static_html_poc/assets/` files are script/style fragments used as prototype assets, not standalone articles.
- `/404.html` is a custom not-found page and should remain part of the repository's operational site infrastructure.

## Route-by-route evidence

See [awakenology-nonsitemap-route-review.csv](awakenology-nonsitemap-route-review.csv) for the route-level evidence and provisional classification.

## Limits and next verification

This review inspects repository source files and robots metadata. It does not prove live response status, redirect behavior, authentication enforcement, or the currently deployed content. Next, test the 136 sitemap URLs and these 12 routes against the live canonical domains, record HTTP status and redirect chains, and compare linked assets/documents. Do not change sitemap membership or delete routes based on this classification alone.
