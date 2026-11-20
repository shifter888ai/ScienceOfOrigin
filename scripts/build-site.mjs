#!/usr/bin/env node
/**
 * Dependency-free static-site builder.
 * Existing root-level HTML pages remain the editable source. The build
 * assembles shared header/footer wrappers into complete HTML under dist/.
 */
import { cp, mkdir, readFile, readdir, rm, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const componentsDir = path.join(root, 'src', 'components');
const outputDir = path.join(root, 'dist');

function count(source, token) {
  return source.split(token).length - 1;
}

function requireOne(source, token, label, file) {
  const occurrences = count(source, token);
  if (occurrences !== 1) {
    throw new Error(file + ': expected exactly one ' + label + '; found ' + occurrences);
  }
}

async function collectRootHtml() {
  const entries = await readdir(root, { withFileTypes: true });
  return entries
    .filter(entry => entry.isFile() && entry.name.toLowerCase().endsWith('.html'))
    .map(entry => entry.name)
    .sort((a, b) => a.localeCompare(b));
}

function ensureGlobalFooterLinks(content) {
  const missing = [];
  if (!/<a\b[^>]*href=["']about\.html["']/i.test(content)) {
    missing.push('<a href="about.html">About this project</a>');
  }
  if (!/<a\b[^>]*href=["']contact\.html["']/i.test(content)) {
    missing.push('<a href="contact.html">Contact</a>');
  }
  if (!missing.length) return content;
  return content + '\n<p class="site-footer-links">' + missing.join(' · ') + '</p>';
}

async function buildPage(fileName, headerTemplate, footerTemplate) {
  const sourcePath = path.join(root, fileName);
  const outputPath = path.join(outputDir, fileName);
  let html = await readFile(sourcePath, 'utf8');

  const headers = [...html.matchAll(/<header\b[^>]*>[\s\S]*?<\/header>/gi)];
  const footers = [...html.matchAll(/<footer\b[^>]*>([\s\S]*?)<\/footer>/gi)];
  if (headers.length !== 1) {
    throw new Error(fileName + ': expected exactly one source header; found ' + headers.length);
  }
  if (footers.length !== 1) {
    throw new Error(fileName + ': expected exactly one source footer; found ' + footers.length);
  }

  const headerContent = headers[0][0];
  const brandMatches = [...headerContent.matchAll(/<a\b[^>]*class=["'][^"']*\bbrand\b[^"']*["'][^>]*>[\s\S]*?<\/a>/gi)];
  const navMatches = [...headerContent.matchAll(/<nav\b[^>]*>[\s\S]*?<\/nav>/gi)];
  if (brandMatches.length !== 1) {
    throw new Error(fileName + ': expected exactly one brand link in the header; found ' + brandMatches.length);
  }
  if (navMatches.length !== 1) {
    throw new Error(fileName + ': expected exactly one navigation element in the header; found ' + navMatches.length);
  }

  const footerContent = ensureGlobalFooterLinks(footers[0][1].trim());
  if (!footerContent || /<footer\b/i.test(footerContent)) {
    throw new Error(fileName + ': source footer must contain content, not another footer wrapper');
  }

  const header = headerTemplate
    .replace('{{BRAND}}', brandMatches[0][0])
    .replace('{{NAVIGATION}}', navMatches[0][0]);
  const footer = footerTemplate.replace('{{FOOTER_CONTENT}}', footerContent);

  if (count(header, '{{BRAND}}') || count(header, '{{NAVIGATION}}') ||
      count(footer, '{{FOOTER_CONTENT}}')) {
    throw new Error(fileName + ': a shared component slot was not replaced');
  }

  html = html.replace(headers[0][0], header).replace(footers[0][0], footer);

  if ((html.match(/<header\b/gi) ?? []).length !== 1 ||
      (html.match(/<footer\b/gi) ?? []).length !== 1) {
    throw new Error(fileName + ': generated page must contain exactly one header and footer');
  }

  await writeFile(outputPath, html, 'utf8');
  return fileName;
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
  for (const [template, slot, file] of [
    [headerTemplate, '{{BRAND}}', 'header.html'],
    [headerTemplate, '{{NAVIGATION}}', 'header.html'],
    [footerTemplate, '{{FOOTER_CONTENT}}', 'footer.html']
  ]) {
    if (count(template, slot) !== 1) {
      throw new Error(file + ' must contain exactly one ' + slot + ' slot');
    }
  }

  const pages = await collectRootHtml();
  if (!pages.length) throw new Error('No root-level HTML source pages found');

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

  console.log('Built ' + built.length + ' HTML page(s) into dist/:');
  for (const page of built) console.log('  - ' + page);
  console.log('Copied public resources: ' + (copied.join(', ') || 'none'));
  console.log('Source HTML remains in the repository root; generated output is disposable.');
}

main().catch(error => {
  console.error('Build failed: ' + error.message);
  process.exitCode = 1;
});
