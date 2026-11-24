#!/usr/bin/env python3
"""Conservative, robots-aware archival crawler for public Yuanwushi pages.

Original response bytes are preserved unchanged. Derived manifests and reports are
kept separate. The crawler is intentionally same-origin and rate-limited.
"""
from __future__ import annotations
import hashlib, json, os, re, sys, time
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse, parse_qs, unquote, quote, urlunsplit
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from urllib.robotparser import RobotFileParser

BASE = "https://www.yuanwushi.org/"
UA = "ScienceOfOriginResearchArchive/1.0 (+https://github.com/shifter888ai/ScienceOfOrigin; archival research; contact repository maintainers)"
OUT = Path(os.environ.get("OUTPUT_DIR", "materials/yuanwushi/snapshots"))
STAMP = os.environ.get("CAPTURE_DATE", datetime.now(timezone.utc).strftime("%Y-%m-%d"))
ROOT = OUT / STAMP
DELAY = float(os.environ.get("CRAWL_DELAY_SECONDS", "0.8"))
MAX_ATTACHMENT = int(os.environ.get("MAX_ATTACHMENT_BYTES", str(25 * 1024 * 1024)))
MAX_TOTAL = int(os.environ.get("MAX_TOTAL_ATTACHMENT_BYTES", str(200 * 1024 * 1024)))
MAX_WIKI_PAGES = int(os.environ.get("MAX_WIKI_PAGES", "500"))
EXTS = {".pdf",".doc",".docx",".xls",".xlsx",".ppt",".pptx",".zip",".rar",".7z",
        ".jpg",".jpeg",".png",".gif",".webp",".svg",".mp3",".mp4",".mov",".m4a"}
records = []
total_attachment_bytes = 0
last_request = 0.0

class Links(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.urls=[]
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        for k in ("href","src","data-src","data-original"):
            v=a.get(k)
            if v: self.urls.append((tag,k,v))

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def safe_name(url: str, default="index.html") -> Path:
    p=urlparse(url)
    path=unquote(p.path).lstrip("/")
    if not path or path.endswith("/"): path += default
    path=Path(path)
    if any(x in ("..","") for x in path.parts): raise ValueError("unsafe path")
    if p.query:
        q=re.sub(r"[^A-Za-z0-9._=-]+","_",p.query)[:100]
        path=path.with_name(path.stem+"__"+q+path.suffix)
    return path

def record(**kw):
    records.append({"capture_date":STAMP, **kw})

def robots_policy():
    robots_url=urljoin(BASE,"robots.txt")
    req=Request(robots_url,headers={"User-Agent":UA})
    try:
        with urlopen(req,timeout=30) as r:
            data=r.read()
            if r.status != 200: raise RuntimeError(f"robots.txt status {r.status}; refusing to crawl")
        text=data.decode("utf-8","replace")
        rp=RobotFileParser()
        rp.set_url(robots_url)
        rp.parse(text.splitlines())
        record(url=robots_url,kind="robots",status=200,bytes=len(data),sha256=sha256(data),
               stored=False,notes="Policy file checked; response not duplicated in source capture.")
        return rp
    except Exception as e:
        raise RuntimeError(f"Could not verify robots.txt; fail-closed: {e}")

def request_safe_url(url: str) -> str:
    """Percent-encode non-ASCII URL characters for urllib without changing the source URL."""
    p = urlparse(url)
    path = quote(p.path, safe="/%:@!$&'()*+,;=-._~")
    query = quote(p.query, safe="=&?/:;+,%@!$'()*-._~")
    fragment = quote(p.fragment, safe="=&?/:;+,%@!$'()*-._~")
    return urlunsplit((p.scheme, p.netloc, path, query, fragment))

def canonical_url(url: str) -> str:
    """Fragments identify positions within a page, not separate source resources."""
    p = urlparse(url)
    return urlunsplit((p.scheme, p.netloc, p.path, p.query, ""))

def allowed(rp,url):
    return (urlparse(url).netloc == urlparse(BASE).netloc
            and rp.can_fetch(UA,request_safe_url(url)))

def fetch(url, rp, kind, parent=None, store=True, attachment=False):
    global last_request,total_attachment_bytes
    url=canonical_url(urljoin(BASE,url))
    parsed=urlparse(url)
    if parsed.scheme not in ("http","https") or parsed.netloc != urlparse(BASE).netloc:
        record(url=url,kind=kind,parent=parent,status="skipped",stored=False,notes="Outside source origin.")
        return None
    if not allowed(rp,url):
        record(url=url,kind=kind,parent=parent,status="robots_disallowed",stored=False)
        return None
    now=time.monotonic()
    wait=DELAY-(now-last_request)
    if wait>0: time.sleep(wait)
    last_request=time.monotonic()
    req=Request(request_safe_url(url),headers={"User-Agent":UA,"Accept":"text/html,application/pdf,image/*,*/*;q=0.5"})
    try:
        with urlopen(req,timeout=45) as response:
            status=response.status
            final=response.geturl()
            if urlparse(final).netloc != urlparse(BASE).netloc:
                record(url=url,kind=kind,parent=parent,status=status,stored=False,notes="Redirected off source origin; body not stored.")
                return None
            data=response.read()
            headers=dict(response.headers.items())
    except HTTPError as e:
        record(url=url,kind=kind,parent=parent,status=e.code,stored=False,notes=str(e.reason))
        return None
    except Exception as e:
        record(url=url,kind=kind,parent=parent,status="error",stored=False,notes=str(e))
        return None
    if attachment:
        if len(data)>MAX_ATTACHMENT or total_attachment_bytes+len(data)>MAX_TOTAL:
            record(url=url,kind=kind,parent=parent,status=status,bytes=len(data),sha256=sha256(data),
                   stored=False,notes="Attachment storage cap reached; locator and checksum retained.")
            return data
        total_attachment_bytes += len(data)
    rel=safe_name(url)
    dest=ROOT/("attachments" if attachment else "pages")/rel
    dest.parent.mkdir(parents=True,exist_ok=True)
    if store: dest.write_bytes(data)
    record(url=url,kind=kind,parent=parent,status=status,bytes=len(data),sha256=sha256(data),
           stored=store,path=str(dest).replace("\\","/") if store else None,
           content_type=headers.get("Content-Type"),last_modified=headers.get("Last-Modified"),
           etag=headers.get("ETag"))
    return data

def parse_links(data):
    parser=Links()
    parser.feed(data.decode("utf-8","replace"))
    return parser.urls

def main():
    ROOT.mkdir(parents=True,exist_ok=True)
    rp=robots_policy()
    queue=[]
    seen=set()
    def add(url,kind,parent=None):
        url=canonical_url(urljoin(BASE,url))
        if url not in seen and urlparse(url).netloc==urlparse(BASE).netloc:
            seen.add(url); queue.append((url,kind,parent))
    add(BASE,"homepage")
    # Core public indexes and known entry points.
    add("/cxclub/","cxclub-index")
    add("/wiki.html","wiki-index")
    add("/rss.xml","rss")
    # Fetch homepage first and discover its six article categories.
    home=fetch(BASE,rp,"homepage")
    if home:
        for tag,attr,href in parse_links(home):
            u=urljoin(BASE,href)
            path=urlparse(u).path
            if re.fullmatch(r"/article-\d+-\d+\.html",path):
                add(u,"article")
            elif path.startswith("/cxclub/") and re.search(r"/lesson\d+\.html$",path):
                add(u,"cxclub-lesson")
    # Process index pages before route discovery from their contents.
    idx=[]
    for u,k in [ (urljoin(BASE,"/cxclub/"),"cxclub-index"),
                 (urljoin(BASE,"/wiki.html"),"wiki-index"),
                 (urljoin(BASE,"/rss.xml"),"rss") ]:
        if u not in {x[0] for x in idx}: idx.append((u,k))
    wiki_max=None
    for u,k in idx:
        data=fetch(u,rp,k,parent=BASE)
        if not data: continue
        links=parse_links(data)
        for tag,attr,href in links:
            target=urljoin(u,href)
            path=urlparse(target).path
            if re.fullmatch(r"/cxclub/lesson\d+\.html",path):
                add(target,"cxclub-lesson")
            if path.endswith("/all.pdf") or path.endswith(".pdf"):
                add(target,"pdf-attachment")
            if path=="/wiki.html":
                qs=parse_qs(urlparse(target).query)
                if "p" in qs:
                    try: wiki_max=max(wiki_max or 0,int(qs["p"][0]))
                    except ValueError: pass
        # capture pagination links discovered on wiki index
    if wiki_max:
        if wiki_max>MAX_WIKI_PAGES:
            record(url=urljoin(BASE,"/wiki.html"),kind="wiki-pagination",status="bounded",
                   stored=False,notes=f"Discovered page parameter {wiki_max}, exceeds safety cap {MAX_WIKI_PAGES}.")
            wiki_max=MAX_WIKI_PAGES
        for n in range(1,wiki_max+1):
            add(f"/wiki.html?p={n}","wiki-page")
    else:
        record(url=urljoin(BASE,"/wiki.html"),kind="wiki-pagination",status="unresolved",
               stored=False,notes="No maximum page parameter discovered from live pagination controls; no page count inferred.")
    # Queue now includes articles and lessons discovered from homepage/index.
    while queue:
        url,kind,parent=queue.pop(0)
        if kind in ("homepage","cxclub-index","wiki-index","rss"): continue
        data=fetch(url,rp,kind,parent=parent or BASE,attachment=(kind=="attachment"))
        if not data: continue
        # Capture only same-origin linked original documents and media, not scripts/styles.
        for tag,attr,href in parse_links(data):
            target=canonical_url(urljoin(url,href))
            p=urlparse(target)
            ext=Path(p.path).suffix.lower()
            if p.netloc==urlparse(BASE).netloc and ext in EXTS:
                if target not in seen:
                    seen.add(target); queue.append((target,"attachment",url))
            # Discover additional article and lesson links on source pages.
            if p.netloc==urlparse(BASE).netloc:
                if re.fullmatch(r"/article-\d+-\d+\.html",p.path) and target not in seen:
                    seen.add(target); queue.append((target,"article",url))
                if re.fullmatch(r"/cxclub/lesson\d+\.html",p.path) and target not in seen:
                    seen.add(target); queue.append((target,"cxclub-lesson",url))
    # Attachments are deliberately downloaded after page captures.
    # The queue loop above captures them as exact binary originals.
    manifest=ROOT/"capture-manifest.jsonl"
    manifest.write_text("".join(json.dumps(x,ensure_ascii=False)+"\n" for x in records),encoding="utf-8")
    counts={}
    for x in records: counts[x["kind"]]=counts.get(x["kind"],0)+1
    report={
      "source":"https://www.yuanwushi.org/",
      "capture_date":STAMP,
      "robots_checked":True,
      "same_origin_only":True,
      "original_response_bytes_preserved":True,
      "rate_delay_seconds":DELAY,
      "record_count":len(records),
      "records_by_kind":counts,
      "stored_records":sum(bool(x.get("stored")) for x in records),
      "stored_files":len({x["path"] for x in records if x.get("stored") and x.get("path")}),
      "failed_or_skipped":sum(x.get("status") not in (200,304) for x in records),
      "wiki_max_page_parameter_discovered":wiki_max,
      "attachment_bytes_stored_or_considered":total_attachment_bytes,
      "limitations":[
        "Only public same-origin routes discoverable from captured indexes/pages are included.",
        "robots.txt is checked before every request; disallowed or inaccessible routes are not fetched.",
        "Attachments over configured caps are recorded with URL and checksum but not stored.",
        "Dynamic content requiring login, scripts, forms, or interaction is not captured.",
        "A discovered wiki maximum is recorded from live pagination links; absence is not guessed."
      ]
    }
    (ROOT/"crawl-report.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    (ROOT/"SOURCE-NOTICE.txt").write_text(
      "Source: Yuanwushi website (https://www.yuanwushi.org/)\n"
      "The site footer observed in the 2026-11-24 homepage snapshot displayed a CC BY-NC-ND 4.0 badge "
      "and requested that reprints preserve original content unchanged. This archive preserves downloaded "
      "response bytes unchanged. Confirm current license terms on the live source before redistribution.\n"
      "This capture is for non-commercial research preservation. Original source wording and authorship "
      "remain with their respective rights holders. Derived indexes are stored separately.\n",encoding="utf-8")
    print(json.dumps(report,ensure_ascii=False,indent=2))
    if report["stored_files"]==0: sys.exit("No source files were preserved; inspect access and robots policy.")
if __name__=="__main__": main()
