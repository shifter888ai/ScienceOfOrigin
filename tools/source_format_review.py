#!/usr/bin/env python3
"""Compare Chinese PDF/TXT compilation pages and Entropy DOCX/RTF versions."""
from __future__ import annotations
import csv, re, sys, zipfile, unicodedata, shutil, subprocess
from difflib import SequenceMatcher
from pathlib import Path
from pypdf import PdfReader
import pymupdf as fitz
from PIL import Image, ImageDraw, ImageFont
from docx import Document
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
from docx.table import Table
from docx.text.paragraph import Paragraph
from striprtf.striprtf import rtf_to_text

ROOT=Path("."); OUT=Path("source-review-artifacts"); LIB=Path("library/coverage")
OUT.mkdir(exist_ok=True); LIB.mkdir(parents=True,exist_ok=True)

def safe_text(s):
    return s.encode("utf-8", "backslashreplace").decode("utf-8")

def norm(s):
    s=safe_text(unicodedata.normalize("NFKC",s))
    return "".join(ch for ch in s if not ch.isspace())

def txt_pages(path):
    text=path.read_text(encoding="utf-8-sig")
    matches=list(re.finditer(r"(?m)^--- Page (\d+) ---\s*$",text))
    pages={}
    for i,m in enumerate(matches):
        end=matches[i+1].start() if i+1<len(matches) else len(text)
        pages[int(m.group(1))]=text[m.end():end].strip()
    return pages

def pdf_extract(paths):
    all_text=[]; meta=[]
    for path in paths:
        reader=PdfReader(str(path))
        meta.append({"file":str(path),"pages":len(reader.pages),"metadata":{str(k):str(v) for k,v in (reader.metadata or {}).items()}})
        for i,page in enumerate(reader.pages,1):
            try: all_text.append(page.extract_text() or "")
            except Exception as exc:
                all_text.append("")
                print(f"PDF extraction warning: {path} page {i}: {exc}",file=sys.stderr)
    return all_text,meta

def contact_sheets(pdf_paths,page_numbers):
    if not page_numbers: return 0
    docs=[fitz.open(str(p)) for p in pdf_paths]
    combined=[(doc,i) for doc in docs for i in range(len(doc))]
    font=ImageFont.load_default(); made=0
    for batch_start in range(0,len(page_numbers),12):
        batch=page_numbers[batch_start:batch_start+12]; cells=[]
        for page_no in batch:
            if not 1<=page_no<=len(combined): continue
            doc,idx=combined[page_no-1]
            pix=doc[idx].get_pixmap(matrix=fitz.Matrix(0.38,0.38),alpha=False)
            image=Image.frombytes("RGB",[pix.width,pix.height],pix.samples); image.thumbnail((260,340))
            cell=Image.new("RGB",(280,380),"white"); cell.paste(image,((280-image.width)//2,24))
            ImageDraw.Draw(cell).text((8,6),f"PDF page {page_no}",fill="black",font=font); cells.append(cell)
        if cells:
            sheet=Image.new("RGB",(840,1520),"white")
            for i,cell in enumerate(cells): sheet.paste(cell,((i%3)*280,(i//3)*380))
            sheet.save(OUT/f"chinese-no-text-contact-sheet-{batch_start//12+1:02d}.jpg",quality=82); made+=1
    for doc in docs: doc.close()
    return made

def ocr_pages(pdf_paths, page_numbers):
    if not shutil.which("tesseract"):
        return [], "Tesseract unavailable"
    docs=[fitz.open(str(p)) for p in pdf_paths]
    combined=[(doc,i) for doc in docs for i in range(len(doc))]
    results=[]
    for page_no in page_numbers:
        if not 1 <= page_no <= len(combined):
            continue
        doc,idx=combined[page_no-1]
        pix=doc[idx].get_pixmap(matrix=fitz.Matrix(2,2),alpha=False)
        image_path=OUT/f"ocr-page-{page_no}.png"
        pix.save(str(image_path))
        proc=subprocess.run(["tesseract",str(image_path),"stdout","-l","chi_sim+eng","--psm","6"],
            capture_output=True,text=True,encoding="utf-8",errors="replace")
        text=safe_text(proc.stdout).strip()
        results.append({"page_number":page_no,"ocr_characters":len(text),
            "status":"ocr-text-found" if len(norm(text))>=10 else "no-usable-ocr-text",
            "text":text,"return_code":proc.returncode})
        image_path.unlink(missing_ok=True)
    for doc in docs: doc.close()
    return results, "tesseract chi_sim+eng --psm 6"

def extract_docx(path):
    doc=Document(str(path)); chunks=[]
    for child in doc.element.body.iterchildren():
        if isinstance(child,CT_P):
            value=Paragraph(child,doc).text
            if value: chunks.append(value)
        elif isinstance(child,CT_Tbl):
            table=Table(child,doc)
            for row in table.rows: chunks.append(" | ".join(cell.text for cell in row.cells))
    with zipfile.ZipFile(path) as zf:
        media=sum(1 for n in zf.namelist() if n.startswith("word/media/") and not n.endswith("/"))
    return "\n".join(chunks),{"paragraph_count":len(doc.paragraphs),"table_count":len(doc.tables),
        "inline_shape_count":len(doc.inline_shapes),"embedded_media_files":media,"section_count":len(doc.sections)}

def main():
    pdf_paths=[Path("materials/元吾氏集录20210203-1.pdf"),Path("materials/元吾氏集录20210203-2.pdf")]
    pages=txt_pages(Path("materials/元吾氏集录20210203.txt"))
    pdf_text,pdf_meta=pdf_extract(pdf_paths)
    rows=[]
    for n in sorted(set(pages)|set(range(1,len(pdf_text)+1))):
        t=pages.get(n,""); p=pdf_text[n-1] if 1<=n<=len(pdf_text) else ""
        tn,pn=norm(t),norm(p)
        ratio=SequenceMatcher(None,tn,pn,autojunk=False).ratio() if tn or pn else 1.0
        if n not in pages: status="pdf-page-without-txt-marker"
        elif n>len(pdf_text): status="txt-page-without-pdf-page"
        elif not tn and not pn: status="both-no-extracted-text"
        elif not tn: status="txt-no-text-pdf-has-text"
        elif not pn: status="pdf-no-extracted-text"
        elif tn==pn: status="exact-normalized-match"
        elif ratio>=.90: status="high-similarity"
        elif ratio>=.60: status="partial-similarity"
        else: status="low-similarity"
        rows.append({"page_number":n,"txt_characters":len(t),"pdf_characters":len(p),
            "normalized_similarity":f"{ratio:.4f}","status":status,
            "txt_excerpt":safe_text(t[:100]).replace("\n"," "),"pdf_excerpt":safe_text(p[:100]).replace("\n"," ")})
    csv_path=LIB/"chinese-compilation-pdf-text-comparison-2026-11-25.csv"
    with csv_path.open("w",encoding="utf-8-sig",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0].keys())); writer.writeheader(); writer.writerows(rows)
    txt_no=[n for n,v in pages.items() if not norm(v)]
    pdf_no=[i+1 for i,v in enumerate(pdf_text) if not norm(v)]
    visual=sorted(set(txt_no)|set(pdf_no)); sheets=contact_sheets(pdf_paths,visual)
    ocr_results, ocr_method=ocr_pages(pdf_paths,pdf_no)
    ocr_csv=OUT/"chinese-image-page-ocr.csv"
    with ocr_csv.open("w",encoding="utf-8-sig",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=["page_number","ocr_characters","status","return_code","text"])
        writer.writeheader()
        writer.writerows(ocr_results)
    (OUT/"chinese-image-page-ocr.txt").write_text(safe_text("\n\n".join(
        f"--- PDF page {row['page_number']} ---\n{row['text']}" for row in ocr_results)),encoding="utf-8")
    (OUT/"chinese-pdf-extracted-pages.txt").write_text(safe_text("\n\n".join(f"--- PDF page {i+1} ---\n{v}" for i,v in enumerate(pdf_text))),encoding="utf-8")
    dtext,dmeta=extract_docx(Path("materials/熵值检测点RR部分.docx"))
    rtf_raw=Path("materials/熵值检测点RR部分.rtf").read_text(encoding="utf-8",errors="replace")
    rtext=rtf_to_text(rtf_raw); dn,rn=norm(dtext),norm(rtext)
    matcher=SequenceMatcher(None,dn,rn,autojunk=False)
    eratio=matcher.ratio() if dn or rn else 1.0
    differences=[op for op in matcher.get_opcodes() if op[0]!="equal"]
    entropy_body_note="No single-block TOC-only difference was established by this comparison."
    if len(differences)==1 and differences[0][0]=="insert":
        _,i1,i2,j1,j2=differences[0]
        if dn[:i1]==rn[:j1] and dn[i2:]==rn[j2:] and "目录" in rn[j1:j2]:
            entropy_body_note=f"The only normalized text difference is an RTF-only table-of-contents block of {j2-j1:,} characters inserted after the opening {i1:,} characters. After excluding that block, the DOCX and RTF body text matches exactly."
    ocr_found=sum(1 for row in ocr_results if row["status"]=="ocr-text-found")
    ocr_chars=sum(row["ocr_characters"] for row in ocr_results)
    (OUT/"entropy-docx-extracted.txt").write_text(safe_text(dtext),encoding="utf-8")
    (OUT/"entropy-rtf-extracted.txt").write_text(safe_text(rtext),encoding="utf-8")
    counts={}
    for row in rows: counts[row["status"]]=counts.get(row["status"],0)+1
    volume_text=", ".join([f"{m['file']} ({m['pages']} pages)" for m in pdf_meta])
    lines=["# Source Format Comparison — 2026-11-25","",
        "## Chinese compilation: two PDFs vs TXT","",
        f"- TXT page markers: {len(pages):,} (Page 1–{max(pages) if pages else 0})",
        f"- PDF page count: {len(pdf_text):,}",f"- PDF volumes: {volume_text}",
        f"- TXT pages without extracted nonblank text: {len(txt_no):,}",
        f"- PDF pages without extractable text: {len(pdf_no):,}",
        f"- Contact sheets created for visual inspection: {sheets}",
        f"- OCR method: {ocr_method}",
        f"- Image-only PDF pages with usable OCR text: {ocr_found:,} / {len(ocr_results):,}",
        f"- OCR characters recovered: {ocr_chars:,}",
        f"- Page-comparison rows: {len(rows):,}","","### Page comparison status counts",""]
    for key,value in sorted(counts.items()): lines.append(f"- {key}: {value:,}")
    lines += ["","Similarity is computed after Unicode NFKC normalization and whitespace removal. It is a triage measure, not proof of transcription fidelity. Page-number alignment assumes TXT Page N corresponds to combined PDF page N; volume offsets and inserted cover pages must be checked before interpreting low similarity as omission.",
        "Contact sheets are review aids only. OCR is a machine-generated derivative and has not been manually corrected; a blank OCR result does not prove a page is blank. No visual page has been declared complete by this automated pass.","",
        "## Entropy assessment: DOCX vs RTF","",
        f"- DOCX extracted characters: {len(dtext):,}",f"- RTF extracted characters: {len(rtext):,}",
        f"- Normalized text similarity: {eratio:.4f}",f"- Exact normalized text equality: {'yes' if dn==rn else 'no'}",
        f"- DOCX structure: {dmeta['paragraph_count']} paragraphs, {dmeta['table_count']} tables, {dmeta['inline_shape_count']} inline shapes, {dmeta['embedded_media_files']} embedded media files, {dmeta['section_count']} sections",
        "","DOCX extraction preserves paragraph and table-cell text in document-body order. RTF text was extracted with striprtf. Similarity does not assess layout, images, formulas, footnotes, comments, or semantic equivalence. Inspect differences and embedded objects before deciding whether one format faithfully represents the other.","",
        "Detailed extracted text, OCR outputs, and contact sheets are in the workflow artifact source-format-review. Original files remain unchanged.",""]
    report=LIB/"source-format-comparison-2026-11-25.md"
    report.write_text("\n".join(lines),encoding="utf-8")
    print("\n".join(lines))
    return 0

if __name__=="__main__": raise SystemExit(main())
