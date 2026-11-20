#!/usr/bin/env node
/**
 * Dependency-free static-site builder.
 * Each source page retains its own navigation and footer content while the
 * shared header/footer structure is assembled into complete static HTML.
 */
import { cp, mkdir, readFile, readdir, rm, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const pagesDir = path.join(root, 'src', 'pages');
const componentsDir = path.join(root, 'src', 'components');
const outputDir = path.join(root, 'dist');

const HEADER_MARKER = '<!-- @site-header -->';
const NAV_START = '<!-- @page-navigation-start -->';
const NAV_END = '<!-- @page-navigation-end -->';
const FOOTER_START = '<!-- @site-footer-start -->';
const FOOTER_END = '<!-- @site-footer-end -->';

function count(source, token) {
  return source.split(token).length - 1;
}

function requireOne(source, token, label, file) {
  const occurrences = count(source, token);
  if (occurrences !== 1) {
    throw new Error(`${file}: expected exactly one ${label}; found ${occurrences}`);
  }
}

async function collectHtml(directory, relative = '') {
  const entries = await readdir(directory, { withFileTypes: true });
  const files = [];
  for (const entry of entries.sort((a, b) => a.name.localeCompare(b.name))) {
    const childRelative = path.join(relative, entry.name);
    const childAbsolute = path.join(directory, entry.name);
    if (entry.isDirectory()) {
      files.push(...await collectHtml(childAbsolute, childRelative));
    } else if (entry.isFile() && entry.name.toLowerCase().endsWith('.html')) {
      files.push(childRelative);
    }
  }
  return files;
}

async function buildPage(relativePath, headerTemplate, footerTemplate) {
  const sourcePath = path.join(pagesDir, relativePath);
  const outputPath = path.join(outputDir, relativePath);
  const pageName = relativePath.split(path.sep).join('/');
  let html = await readFile(sourcePath, 'utf8');

  requireOne(html, HEADER_MARKER, 'header marker', pageName);
  requireOne(html, NAV_START, 'navigation start marker', pageName);
  requireOne(html, NAV_END, 'navigation end marker', pageName);
  requireOne(html, FOOTER_START, 'footer start marker', pageName);
  requireOne(html, FOOTER_END, 'footer end marker', pageName);

  const navStart = html.indexOf(NAV_START);
  const navEnd = html.indexOf(NAV_END);
  const footerStart = html.indexOf(FOOTER_START);
  const footerEnd = html.indexOf(FOOTER_END);
  if (navEnd < navStart) throw new Error(`${pageName}: navigation end marker precedes start marker`);
  if (footerEnd < footerStart) throw new Error(`${pageName}: footer end marker precedes start marker`);

  const navigation = html.slice(navStart + NAV_START.length, navEnd).trim();
  const footerContent = html.slice(footerStart + FOOTER_START.length, footerEnd).trim();
  if ((navigation.match(/<nav\\b/gi) ?? []).length !== 1 ||
      !/<nav\\b[\\s\\S]*<\\/nav>/i.test(navigation)) {
    throw new Error(`${pageName}: navigation slot must contain exactly one complete nav element`);
  }
  if (!footerContent || /<footer\\b/i.test(footerContent)) {
    throw new Error(`${pageName}: footer slot must contain footer content, not a footer wrapper`);
  }

  html = html.slice(0, footerStart) + html.slice(footerEnd + FOOTER_END.length);
  const navStartAfterFooter = html.indexOf(NAV_START);
  const navEndAfterFooter = html.indexOf(NAV_END);
  html = html.slice(0, navStartAfterFooter) + html.slice(navEndAfterFooter + NAV_END.length);

  const header = headerTemplate.replace('{{NAVIGATION}}', navigation);
  const footer = footerTemplate.replace('{{FOOTER_CONTENT}}', footerContent);
  html = html.replace(HEADER_MARKER, header);
  if (count(html, '{{FOOTER_CONTENT}}') || count(footer, '{{FOOTER_CONTENT}}')) {
    throw new Error(`${pageName}: shared component slot was not replaced`);
  }
  const footerMarker = '<!-- @site-footer -->';
  requireOne(html, footerMarker, 'footer component marker', pageName);
  html = html.replace(footerMarker, footer);

  if (html.includes('@site-header') || html.includes('@site-footer') ||
      html.includes('@page-navigation-') || html.includes('@site-footer-')) {
    throw new Error(`${pageName}: an unprocessed component marker remains`);
  }
  if ((html.match(/<header\\b/gi) ?? []).length !== 1 ||
      (html.match(/<footer\\b/gi) ?? []).length !== 1) {
    throw new Error(`${pageName}: generated page must contain exactly one header and footer`);
  }

  await mkdir(path.dirname(outputPath), { recursive: true });
  await writeFile(outputPath, html, 'utf8');
  return pageName;
}

async function copyIfPresent(source, destination) {
  try {
    await cp(source, destination, { recursive: true });
    return true;
  } catch (error) {
    if (error.code === 'ENOENT') return false;
    throw error;
  }
}

async function main() {
  const [headerTemplate, footerTemplate] = await Promise.all([
    readFile(path.join(componentsDir, 'header.html'), 'utf8'),
    readFile(path.join(componentsDir, 'footer.html'), 'utf8')
  ]);
  if (count(headerTemplate, '{{NAVIGATION}}') !== 1) {
    throw new Error('header.html must contain exactly one {{NAVIGATION}} slot');
  }
  if (count(footerTemplate, '{{FOOTER_CONTENT}}') !== 1) {
    throw new Error('footer.html must contain exactly one {{FOOTER_CONTENT}} slot');
  }

  const pages = await collectHtml(pagesDir);
  if (!pages.length) throw new Error('No HTML source pages found in src/pages/');

  await rm(outputDir, { recursive: true, force: true });
  await mkdir(outputDir, { recursive: true });
  const built = [];
  for (const page of pages) built.push(await buildPage(page, headerTemplate, footerTemplate));

  const copied = [];
  for (const name of ['assets', 'materials']) {
    if (await copyIfPresent(path.join(root, name), path.join(outputDir, name))) copied.push(name + '/');
  }
  for (const name of ['robots.txt', 'sitemap.xml', 'search-index.json']) {
    if (await copyIfPresent(path.join(root, name), path.join(outputDir, name))) copied.push(name);
  }

  console.log(`Built ${built.length} HTML page(s) into dist/:`);
  for (const page of built) console.log(`  - ${page}`);
  console.log(`Copied public resources: ${copied.join(', ') || 'none'}`);
  console.log('Output is complete static HTML; source pages remain unchanged.');
}

main().catch(error => {
  console.error(`Build failed: ${error.message}`);
  process.exitCode = 1;
});
