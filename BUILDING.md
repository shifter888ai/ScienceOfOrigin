# Building the Site

## Current status

The build system is in its Phase 2 prototype. It currently builds the homepage source only; the remaining public pages have not yet been migrated. The production site and deployment process are unchanged.

## Requirements

- Node.js with ES module support (Node.js 18 or later)
- No package installation and no third-party dependencies

## Build

From the repository root:

```sh
npm run build
```

The command reads the HTML source pages in `src/pages/`, combines each page with the shared components in `src/components/`, and writes complete static HTML files to `dist/`. The existing `assets/` directory is copied into the output when present.

The generated `dist/` directory is disposable build output. Edit source files, not generated files.

## Page component markers

Each source page uses one `<!-- @site-header -->` marker, one `<!-- @site-footer -->` marker, and a navigation slot delimited by:

- `<!-- @page-navigation-start -->`
- `<!-- @page-navigation-end -->`

The navigation remains page-specific in this prototype so its existing links and current-page marker can be preserved exactly. The shared header owns the site identity and header structure; the shared footer owns the global footer links.

## Important

This prototype is not yet a complete deployable site build. Do not point production hosting at `dist/` until all public pages and required root-level files (including sitemap, robots and search assets where applicable) have been migrated and validated, and the existing deployment path has been confirmed.
