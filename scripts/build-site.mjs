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

function markCurrentPage(nav, fileName) {
  const doubleQuotedHref = 'href="' + fileName + '"';
  const singleQuotedHref = "href='" + fileName + "'";
  let matches = 0;
  const updated = nav.replace(/<a\b[^>]*>/gi, anchor => {
    if (!anchor.includes(doubleQuotedHref) && !anchor.includes(singleQuotedHref)) return anchor;
    matches += 1;
    if (matches > 1) {
      throw new Error(fileName + ': navigation contains more than one link to the current page');
    }
    if (/\baria-current\s*=/.test(anchor)) {
      return anchor.replace(/\baria-current\s*=\s*(["'])[^"']*\1/i, 'aria-current="page"');
    }
    return anchor.replace(/>$/, ' aria-current="page">');
  });
  return updated;
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

  const navigation = markCurrentPage(navMatches[0][0], fileName);
  const header = headerTemplate.replace('{{NAVIGATION}}', navigation);
  const footer = footerTemplate;

  if (count(header, '{{NAVIGATION}}')) {
    throw new Error(fileName + ': the shared navigation slot was not replaced');
  }

  html = html.replace(headers[0][0], header).replace(footers[0][0], footer);

  if ((html.match(/<header\b/gi) ?? []).length !== 1 ||
      (html.match(/<footer\b/gi) ?? []).length !== 1) {
    throw new Error(fileName + ': generated page must contain exactly one header and footer');
  }

  const generatedHeader = html.match(/<header\\b[^>]*>[\\s\\S]*?<\\/header>/i)?.[0] ?? '';
  if (!/<a\\b[^>]*href=["']search\\.html["'][^>]*aria-label=["']Search["']/i.test(generatedHeader) ||
      !/<a\\b[^>]*href=["']ask\\.html["'][^>]*aria-label=["']Ask AI["']/i.test(generatedHeader)) {
    throw new Error(fileName + ': generated global header is missing Search or Ask quick access');
  }

  const generatedFooter = html.match(/<footer\\b[^>]*>[\\s\\S]*?<\\/footer>/i)?.[0] ?? '';
  if (!/<a\\b[^>]*href=["']contact\\.html["'][^>]*aria-label=["']Contact["']/i.test(generatedFooter)) {
    throw new Error(fileName + ': generated global footer is missing its accessible Contact link');
  }
  if (!/<button\\b[^>]*id=["']back-to-top["'][^>]*aria-label=["']Return to top["']/i.test(html) ||
      !/<script\\b[^>]*src=["']assets\\/site\\.js["']/i.test(html)) {
    throw new Error(fileName + ': generated page is missing the global Return-to-Top control');
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
    [headerTemplate, '{{NAVIGATION}}', 'header.html']
  ]) {
    if (count(template, slot) !== 1) {
      throw new Error(file + ' must contain exactly one ' + slot + ' slot');
    }
  }

  if (!/<a\b[^>]*href=["']contact\.html["'][^>]*aria-label=["']Contact["']/i.test(footerTemplate)) {
    throw new Error('Shared footer template must contain an accessible Contact link');
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
  console.log('Verified Search and Ask header icons, Contact footer link, and Return-to-Top control on all ' + built.length + ' generated page(s).');
  console.log('Copied public resources: ' + (copied.join(', ') || 'none'));
  console.log('Source HTML remains in the repository root; generated output is disposable.');
}

main().catch(error => {
  console.error('Build failed: ' + error.message);
  process.exitCode = 1;
});
