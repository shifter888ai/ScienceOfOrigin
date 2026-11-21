# External Web Source Capture Protocol

## 1. Identity before interpretation

For each submitted URL, record:

- Exact submitted URL.
- Final URL after redirects, if different.
- Canonical URL declared by the page, if available.
- Original title and displayed title.
- Author, creator, organization, or publisher as displayed.
- Platform or publication.
- Publication date and last-updated date, keeping the two distinct.
- Access date and time (UTC).
- Language(s).
- Source type and version/edition, if known.
- Whether the item appears to be an original, mirror, repost, translation, excerpt, or commentary.

Do not infer missing metadata. Mark it unknown or not stated.

## 2. Capture the source object

Capture the most complete accessible version that can be preserved appropriately:

- Webpage: page content plus relevant images, tables, captions, footnotes, and linked documents where feasible.
- PDF/document: original downloadable file, retaining filename and document metadata.
- Video/audio: original URL, creator, title, date, duration, available transcript/captions, and relevant timestamps. Do not treat an automatically generated transcript as verified verbatim text.
- Image/diagram: original image file or stable source URL, caption, creator, surrounding context, and page location.
- Dataset: original download or repository, version, schema, licence, and any accompanying methodology.
- Dynamic or inaccessible page: record the limitation and any legitimate archive or alternate capture; do not pretend the capture is complete.

Where possible, retain a faithful source capture and calculate a SHA-256 checksum for the captured file. Record the capture method and tool. A checksum identifies the captured bytes; it does not prove the publisher's authenticity or the source's truth.

## 3. Preserve source layers separately

Keep these distinct and linked:

1. Original source as published.
2. Captured copy or snapshot.
3. Extracted text or transcript.
4. OCR or transcription corrections.
5. Translation.
6. Summary or analytical notes.

Never overwrite the original capture with corrected OCR, normalized text, a translation, or a later edition. Register a new version when the source changes.

## 4. Record exact locators

When extracting records, preserve the most precise available locator:

- Webpage section or heading and URL fragment.
- PDF page number (and printed page number if different).
- Video/audio timestamp.
- Forum thread, post, and comment identifier.
- Image filename and figure/caption number.
- Dataset table, sheet, row, column, or record key.

Include enough surrounding context to avoid detaching a quotation or claim from its meaning.

## 5. Provenance and reliability are separate

Record where the material came from and how it was obtained. Separately assess what the source supports.

Do not equate:
- Publisher identity with correctness.
- Peer review with automatic truth.
- A citation with confirmation that the cited work supports the claim.
- Multiple reposts with independent corroboration.
- A personal account with independent verification.
- A missing or inaccessible source with evidence that it never existed.

Where possible, trace a citation back to the cited original work. Preserve both the citing source and the cited source as separate objects.

## 6. Rights, privacy, and access

A publicly reachable page is not automatically free to reproduce in full. Before storing or redistributing complete copyrighted works, check the applicable licence, permission, and repository policy. When full-text preservation is not permitted, retain bibliographic metadata, the URL, permitted excerpts, a source locator, and analytical notes as allowed.

Do not place private communications, personal data, restricted material, or sensitive information into a public repository without appropriate authorization and access controls. Mark unresolved rights or privacy questions for review.

## 7. Completeness and change monitoring

Record whether the capture is complete, partial, excerpted, blocked, damaged, or uncertain. Note missing images, scripts, attachments, comments, and pagination.

For mutable pages, retain capture date and version. A later page update should create a new capture linked to the earlier one; it should not silently replace the historical capture.

## 8. Registration gate

A source becomes formally registered only when it has:

- A stable source identifier.
- A traceable original URL or source location.
- Basic identity metadata (unknown values explicitly marked).
- A recorded acquisition/capture status.
- Provenance and access/rights status.
- A clear link to its preserved object or an explanation of why preservation is partial or unavailable.

Research-topic mapping is not a prerequisite for intake. Preserve first; discover relationships through research.
