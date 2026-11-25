#!/usr/bin/env python3
"""Reconcile captured Yuanwushi Wiki pagination with the displayed Q&A total."""
from __future__ import annotations
import argparse
import csv
import json
import re
from html.parser import HTMLParser
from pathlib import Path

class WikiPageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.cards = 0
        self.record_ids = []
        self.page_links = set()
        self.displayed_totals = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = set((attrs.get("class") or "").split())
        if tag == "div" and {"card", "shadow-sm", "mb-3", "border-0"}.issubset(classes):
            self.cards += 1
        if tag == "a":
            href = attrs.get("href", "") or ""
            match = re.search(r"/wiki-(\d+)\.html(?:[?#].*)?$", href)
            if match:
                self.record_ids.append(match.group(1))
            page_match = re.search(r"(?:[?&])p=(\d+)", href)
            if "wiki.html" in href and page_match:
                self.page_links.add(int(page_match.group(1)))

    def handle_data(self, data):
        match = re.search(r"共\s*(\d+)\s*条答疑", data)
        if match:
            self.displayed_totals.add(int(match.group(1)))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--snapshot", type=Path, required=True)
    ap.add_argument("--report", type=Path, required=True)
    ap.add_argument("--csv", type=Path, required=True)
    ap.add_argument("--expected-total", type=int, default=2659)
    args = ap.parse_args()
    pages_dir = args.snapshot / "pages"
    paths = sorted(pages_dir.glob("wiki__p=*.html"), key=lambda p: int(re.search(r"p=(\d+)", p.name).group(1)))
    results = []
    all_ids = []
    displayed_totals = set()
    for path in paths:
        page_no = int(re.search(r"p=(\d+)", path.name).group(1))
        parser = WikiPageParser()
        parser.feed(path.read_text(encoding="utf-8", errors="replace"))
        ids = parser.record_ids
        all_ids.extend(ids)
        displayed_totals.update(parser.displayed_totals)
        results.append({
            "page_parameter": page_no,
            "file": path.name,
            "cards": parser.cards,
            "record_links": len(ids),
            "unique_record_ids_on_page": len(set(ids)),
            "duplicate_record_links_on_page": len(ids) - len(set(ids)),
            "first_record_id": ids[0] if ids else "",
            "last_record_id": ids[-1] if ids else "",
        })
    params = [r["page_parameter"] for r in results]
    expected_params = list(range(1, max(params, default=0) + 1))
    missing_pages = sorted(set(expected_params) - set(params))
    unique_ids = set(all_ids)
    duplicate_ids = len(all_ids) - len(unique_ids)
    total_cards = sum(r["cards"] for r in results)
    total_links = sum(r["record_links"] for r in results)
    args.csv.parent.mkdir(parents=True, exist_ok=True)
    with args.csv.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(results[0].keys()) if results else ["page_parameter"])
        writer.writeheader()
        writer.writerows(results)
    max_page = max(params, default=0)
    crawl_report = json.loads((args.snapshot / "crawl-report.json").read_text(encoding="utf-8"))
    discovered_max_page = int(crawl_report.get("wiki_max_page_parameter_discovered", 0))
    passed = (
        len(params) == max_page
        and params == expected_params
        and max_page == discovered_max_page
        and total_links == args.expected_total
        and len(unique_ids) == args.expected_total
        and duplicate_ids == 0
        and args.expected_total in displayed_totals
        and not missing_pages
    )
    lines = [
        "# Yuanwushi Wiki/Q&A Pagination Reconciliation",
        "",
        "Snapshot: 2026-11-25",
        "",
        f"- Captured paginated Wiki files: {len(paths):,}",
        f"- Page parameters: {min(params) if params else 'none'}–{max_page}",
        f"- Missing page parameters: {missing_pages}",
        f"- Nested card-class containers (not used as record count): {total_cards:,}",
        f"- Q&A record-link occurrences: {total_links:,}",
        f"- Unique record IDs: {len(unique_ids):,}",
        f"- Duplicate record-link occurrences: {duplicate_ids:,}",
        f"- Displayed Q&A total values found: {sorted(displayed_totals)}",
        f"- Maximum page parameter reported by crawler discovery: {discovered_max_page}",
        f"- Expected displayed total: {args.expected_total:,}",
        "",
        f"**Automated reconciliation result:** {'PASS' if passed else 'NOT RECONCILED'}",
        "",
        "Method: count /wiki-ID.html record links on each captured page, deduplicate record IDs, verify continuous page parameters 1 through the maximum discovered by the crawler, and compare the resulting unique-ID count with the displayed source total. Nested Bootstrap card containers are not treated as Q&A records. The page-level CSV records counts and first/last record IDs for every page.",
        "",
        "This checks the captured listing pagination and record locators. It does not independently verify every linked Q&A detail page body, embedded media, deleted/private records, or the accuracy of the source's own displayed total.",
        "",
    ]
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))
    if not passed:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
