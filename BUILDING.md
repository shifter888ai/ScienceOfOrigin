# Building the Site

## Current status

The build foundation is in place. The site-wide build now reads the existing root-level HTML pages as source, assembles the shared header and footer, and writes complete static HTML files to `dist/`. Source pages remain in their current locations; no content relocation is required.

## Requirements

- Node.js 18 or later
- No package installation and no third-party dependencies

## Build

From the repository root:

```sh
npm run build
```

The builder processes every root-level `.html` file. It extracts each page's existing brand link, navigation element and footer content, then inserts them into the shared component wrappers in `src/components/`.

Page-specific navigation, including `aria-current`, remains unchanged. Existing footer content and links are retained; About and Contact links are added to a page's footer only when missing.

The generated `dist/` directory contains the complete HTML pages and copies the public `assets/` and `materials/` directories, `robots.txt`, `sitemap.xml` and `search-index.json`.

The generated `dist/` directory is disposable build output. Edit the original root-level HTML and component source files, not generated files.

## Validation and deployment

The build fails if a page does not contain exactly one header and footer, or if its header does not contain exactly one brand link and one navigation element. Do not point production hosting at `dist/` until the build has been run locally, all output pages and links have been checked, and the current Cloudflare Pages deployment settings have been confirmed.
