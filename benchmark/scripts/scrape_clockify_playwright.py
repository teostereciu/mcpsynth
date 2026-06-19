#!/usr/bin/env python3
"""
Clockify API Documentation Scraper (Playwright)

The Clockify docs (docs.clockify.me) are a Redoc SPA that requires
JavaScript to render. This scraper uses Playwright to render each
tag section and extract the content as markdown.

Setup:
    uv pip install playwright
    playwright install chromium

Usage:
    python3 benchmark/scripts/scrape_clockify_playwright.py
"""

import json
import re
import time
from datetime import datetime
from pathlib import Path

import html2text

OUTPUT_DIR = Path(__file__).parent.parent / "datasets" / "clockify" / "docs"
DOCS_URL = "https://docs.clockify.me"

# Tag sections in the Redoc sidebar (in order)
TAGS = [
    "User",
    "Workspace",
    "Client",
    "Project",
    "Task",
    "Tag",
    "Time entry",
    "Approval",
    "Expense",
    "Invoice",
    "Group",
    "Time Off",
    "Balance",
    "Policy",
    "Scheduling",
    "Webhooks",
]


def _build_converter():
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = True
    h.body_width = 0
    h.unicode_snob = True
    h.skip_internal_links = True
    return h


_CONVERTER = _build_converter()


def _clean(md: str) -> str:
    md = re.sub(r"[ \t]+\n", "\n", md)
    md = re.sub(r"\n{4,}", "\n\n\n", md)
    md = re.sub(r"\[#\]\([^)]*\)", "", md)
    return md.strip()


def scrape_with_playwright():
    from playwright.sync_api import sync_playwright

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    scraped_files = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        print(f"Loading {DOCS_URL}...", flush=True)
        page.goto(DOCS_URL, wait_until="networkidle", timeout=60000)
        time.sleep(3)  # let Redoc fully render

        from bs4 import BeautifulSoup
        import requests as _requests

        # Fetch the OpenAPI spec to get all operationIds grouped by tag
        spec_resp = _requests.get("https://docs.clockify.me/openapi.json", timeout=30)
        spec = spec_resp.json()
        from collections import defaultdict
        ops_by_tag: dict[str, list[str]] = defaultdict(list)
        for path, path_item in spec.get("paths", {}).items():
            for method, op in path_item.items():
                if method not in ("get", "post", "put", "patch", "delete"):
                    continue
                op_id = op.get("operationId")
                tags = op.get("tags", [])
                if op_id and tags and tags[0] in TAGS:
                    ops_by_tag[tags[0]].append(op_id)

        for tag in TAGS:
            filename = f"api_{tag.lower().replace(' ', '_')}.md"
            print(f"  {tag:<25}", end=" ", flush=True)

            op_ids = ops_by_tag.get(tag, [])
            if not op_ids:
                print("x no operations")
                continue

            tag_parts = []
            for op_id in op_ids:
                # Navigate to the operation-specific URL — Redoc renders it fully
                op_url = f"{DOCS_URL}/#tag/{tag.replace(' ', '%20')}/operation/{op_id}"
                try:
                    page.goto(op_url, wait_until="networkidle", timeout=30000)
                    time.sleep(1.5)

                    # The highlighted/expanded operation panel
                    # Redoc marks active operations with aria-expanded or a specific class
                    op_html = page.content()
                    soup = BeautifulSoup(op_html, "html.parser")

                    # Find the operation section — look for the element with the op_id anchor.
                    # Redoc slugifies spaces to hyphens in aria-labels (e.g. "Time entry" → "Time-entry").
                    tag_hyphen = tag.replace(" ", "-")
                    anchor = (
                        soup.find("a", attrs={"aria-label": f"tag/{tag_hyphen}/operation/{op_id}"})
                        or soup.find("a", attrs={"aria-label": f"tag/{tag}/operation/{op_id}"})
                    )
                    if anchor:
                        # Walk up until we find a div with substantial content
                        el = anchor.parent
                        for _ in range(8):
                            if el and len(el.get_text(strip=True)) > 150:
                                tag_parts.append(str(el))
                                break
                            el = el.parent if el else None
                except Exception as e:
                    pass  # skip failed operations silently

            if not tag_parts:
                print("x empty")
                continue

            combined_html = "\n".join(tag_parts)
            md = _CONVERTER.handle(combined_html)
            md = _clean(md)

            if len(md) < 50:
                print("x too short")
                continue

            url = f"{DOCS_URL}/#tag/{tag.replace(' ', '%20')}"
            (OUTPUT_DIR / filename).write_text(
                f"# {tag}\n\n*Source: {url}*\n\n---\n\n{md}",
                encoding="utf-8",
            )
            print(f"({md.count(chr(10))} lines)")
            scraped_files.append({"filename": filename, "title": tag, "url": url})

        browser.close()

    manifest = {
        "source": "Clockify API (docs.clockify.me)",
        "scraped_from": DOCS_URL,
        "scrape_date": datetime.now().isoformat(),
        "total_pages": len(scraped_files),
        "files": scraped_files,
    }
    (OUTPUT_DIR / "_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"\nScraped: {len(scraped_files)}/{len(TAGS)}")
    print(f"Output:  {OUTPUT_DIR}")


def main():
    print("=" * 60)
    print("Clockify API Documentation Scraper (Playwright)")
    print(f"Source: {DOCS_URL}")
    print("=" * 60)

    try:
        import playwright
        scrape_with_playwright()
    except ImportError:
        print("Playwright not installed. Run:")
        print("  uv pip install playwright && playwright install chromium")
        raise


if __name__ == "__main__":
    main()
