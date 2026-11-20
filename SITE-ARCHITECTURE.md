# Site Architecture: Shared Components and Static Build

## Status

Architecture approved. The shared-component build foundation is implemented on a review branch. The existing published site and production deployment settings remain unchanged.

## Decision

Use **shared source components with build-time generation of complete static HTML pages**.

The header and footer each have one authoritative wrapper source. Existing research pages remain in their current root-level locations as editable source files. A small build step combines each page's own brand, navigation and footer content with the shared wrappers and produces ordinary HTML files for publication.

The site does not depend on runtime HTML injection through `worker.js`.

## Why this fits the current site

The website is a lightweight static HTML site with approximately 90 root-level HTML pages. Moving every page into a new source directory would create unnecessary file churn and increase the risk of broken relative links. Keeping the existing page files in place is simpler and reversible.

The builder extracts each page's existing brand link, navigation element and footer content. This preserves page-specific navigation state, including `aria-current`, and retains each page's existing footer links. The shared footer adds About or Contact links only when a page does not already contain them.

## Structure

```text
<header and footer source wrappers>
src/
  components/
    header.html
    footer.html

scripts/
  build-site.mjs

*.html                  existing editable page sources
assets/                 public styles and assets
materials/              public downloadable materials
robots.txt
sitemap.xml
search-index.json

dist/                   generated complete static site
```

- `src/components/` contains the shared header and footer wrappers.
- Existing root-level HTML files remain the page sources; their content and public URLs are not moved.
- `scripts/build-site.mjs` assembles pages using Node.js built-in modules only.
- `dist/` contains complete publishable HTML pages and copied public resources. Generated files are not hand-edited.

## Build requirements

1. No third-party packages, framework, external service, or runtime component loader.
2. Build output must be deterministic: the same sources produce the same files.
3. Fail clearly if a page has missing or duplicate header/footer structures, brand links or navigation elements.
4. Preserve page-specific content, navigation state, metadata, scripts, styles and relative URLs.
5. Preserve the existing public URL structure.
6. Generate every root-level HTML page and copy all required public static resources.
7. Keep generated output separate from editable source files.

## Migration plan

### Phase 1 — Architecture agreement

Complete. The shared-component static build direction was approved.

### Phase 2 — Build foundation

Complete as a prototype. Shared component wrappers and a dependency-free Node.js build command are in place.

### Phase 3 — Site-wide build and validation

Process all existing root-level HTML pages without relocating or rewriting their content. Verify that all pages build, required static resources are copied, relative links resolve, and search and sitemap behavior remain intact.

### Phase 4 — Deployment integration

Confirm the existing Cloudflare Pages build and output-directory settings. Configure the existing deployment path to run the build and publish `dist/`, without adding runtime HTML rewriting. Verify the preview deployment before production.

## Explicit non-goals

- No redesign of the header, footer or individual pages.
- No change to research content or page URLs.
- No Cloudflare Worker HTML injection.
- No new paid service, third-party dependency or frontend framework.
- No production deployment before preview validation and explicit approval.

## Acceptance criteria

- One source of truth for the global header wrapper and one for the global footer wrapper.
- All public HTML pages are generated as complete, standalone static HTML.
- Individual page content and navigation behavior are preserved.
- About and Contact links are available through the footer on every page.
- The build and validation process can be run locally with documented commands.
- The existing deployment method is retained or minimally adapted only after it has been inspected and tested.
