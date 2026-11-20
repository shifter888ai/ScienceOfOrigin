# Site Architecture: Shared Components and Static Build

## Status

Architecture approved. Phase 2 prototype is being developed on a review branch; the production site and deployment process remain unchanged.

## Decision

Move toward **shared source components with build-time generation of complete static HTML pages**.

The header and footer should each have one authoritative source. Individual research pages should retain their own content and page-specific structure. A small build step will combine the shared components with each page and produce ordinary HTML files for publication.

The site should not depend on runtime HTML injection through `worker.js`.

## Why this fits the current site

The current website is a lightweight static HTML site. Its header and footer are repeated across many pages, and there is no existing build system or framework. The homepage and research pages are independently authored HTML documents; some pages also have page-specific navigation state, such as the current-page marker.

A shared-source build addresses duplication without making the Cloudflare Worker responsible for rewriting page content. It also keeps the delivered pages complete and readable without JavaScript component loading.

## Target structure

The exact directory names can be finalized during implementation, but the intended separation is:

```text
src/
  components/
    header.html
    footer.html
  pages/
    index.html
    about.html
    contact.html
    ...individual page sources...

scripts/
  build-site.mjs

dist/
  index.html
  about.html
  contact.html
  ...generated static pages...
  assets/
```

- `src/components/` contains the shared header and footer.
- `src/pages/` contains page-specific content and page metadata or explicit component placeholders.
- `scripts/build-site.mjs` assembles the pages using Node.js built-in modules only.
- `dist/` contains the complete publishable site. Generated files are not hand-edited.

The build must preserve page-specific navigation state (including `aria-current` where appropriate), relative links, metadata, scripts, styles, and page content.

## Build requirements

1. No third-party packages, framework, external service, or runtime component loader.
2. Build output must be deterministic: the same sources produce the same files.
3. Fail clearly if a page has missing or duplicate component placeholders, or if a required shared component is absent.
4. Keep page-specific content unchanged apart from replacing shared component placeholders.
5. Preserve relative URLs and the existing public URL structure.
6. Include a validation step that checks every source page was generated and that the generated pages contain exactly one shared header and footer.
7. Keep generated output separate from editable source files.

## Migration plan

### Phase 1 — Architecture agreement

Review and approve this direction. No page files or deployment settings are changed in this phase.

### Phase 2 — Build foundation

Add the shared component files and a dependency-free build script. Establish a representative local build and compare its output with the current pages before migrating the full site.

### Phase 3 — Site-wide migration

Move or adapt all public HTML pages to the source-page structure. Preserve page content, page-specific navigation state, metadata, scripts, and current URLs. Generate the complete static site and verify all pages, links, sitemap entries, and search behavior.

The shared footer will include the agreed global links, including About and Contact.

### Phase 4 — Deployment integration

Before changing deployment, confirm how the existing Cloudflare Worker currently serves the repository files. Configure the existing deployment path to publish the generated static output, without adding runtime HTML rewriting. Verify the deployed site before considering the migration complete.

## Explicit non-goals

- No redesign of the header, footer, or individual pages.
- No change to research content or page URLs.
- No Cloudflare Worker HTML injection.
- No new paid service, third-party dependency, or frontend framework.
- No automatic deployment or production change as part of the architecture proposal.

## Acceptance criteria

- One source of truth for the global header and one for the global footer.
- All public pages are generated as complete, standalone static HTML.
- Individual page content and navigation behavior are preserved.
- The Contact link is available through the shared footer on every page.
- The build and validation process can be run locally with documented commands.
- The existing deployment method is retained or minimally adapted only after it has been inspected and tested.
