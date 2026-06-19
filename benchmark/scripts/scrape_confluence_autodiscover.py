#!/usr/bin/env python3
"""
Confluence Cloud REST API Documentation Scraper

Fetches and converts the HTML documentation pages from
developer.atlassian.com for both v1 and v2 Confluence Cloud REST APIs.

Discovery strategy:
  - Known API group slugs are scraped for each API version.
  - v1: https://developer.atlassian.com/cloud/confluence/rest/v1/api-group-{slug}/
  - v2: https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-{slug}/

Content strategy:
  - Pages are server-rendered; all content is in <div class="resource-section">
    elements, the same as the Jira scraper.
  - We fetch with requests, strip scripts/styles, collect resource-section divs,
    and convert to markdown with html2text.

Usage:
    python3 benchmark/scripts/scrape_confluence_autodiscover.py
"""

import json
import re
import time
from datetime import datetime
from pathlib import Path

import html2text
import requests
from bs4 import BeautifulSoup


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
BASE_URL   = "https://developer.atlassian.com"
DOCS_V1    = "https://developer.atlassian.com/cloud/confluence/rest/v1"
DOCS_V2    = "https://developer.atlassian.com/cloud/confluence/rest/v2"
OUTPUT_DIR = Path(__file__).parent.parent / "datasets" / "confluence" / "docs"

DELAY = 0.5  # seconds between requests

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "en-US,en;q=0.9",
}

MIN_CONTENT_LEN = 200

# v1 API group slugs
SLUGS_V1 = [
    "audit",
    "content",
    "content-body",
    "content-children-and-descendants",
    "content-labels",
    "content-permissions",
    "content-properties",
    "content-restrictions",
    "content-states",
    "content-versions",
    "content-watches",
    "content-attachments",
    "content-comments",
    "dynamic-modules",
    "experimental",
    "group",
    "inline-tasks",
    "label",
    "long-running-task",
    "relation",
    "search",
    "settings",
    "space",
    "space-permissions",
    "space-properties",
    "space-settings",
    "template",
    "themes",
    "users",
    "other-operations",
]

# v2 API group slugs
SLUGS_V2 = [
    "ancestor",
    "attachment",
    "blog-post",
    "comment",
    "content-properties",
    "custom-content",
    "data-policies",
    "inline-comment",
    "label",
    "operation",
    "page",
    "space",
    "space-permissions",
    "task",
    "user",
    "version",
    "whiteboard",
]


# ---------------------------------------------------------------------------
# HTML -> Markdown  (same logic as scrape_jira_autodiscover.py)
# ---------------------------------------------------------------------------

def _build_converter() -> html2text.HTML2Text:
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = True
    h.body_width = 0
    h.unicode_snob = True
    h.skip_internal_links = True
    h.single_line_break = False
    return h


_CONVERTER = _build_converter()


def extract_content(html: str) -> tuple[str, str]:
    soup = BeautifulSoup(html, "html.parser")

    for tag in soup.find_all(["script", "style", "noscript"]):
        tag.decompose()

    title = "Confluence API"
    title_tag = soup.find("title")
    if title_tag:
        t = title_tag.get_text(strip=True).split("|")[0].strip()
        if t:
            title = t
    h1 = soup.find("h1")
    if h1:
        t = h1.get_text(" ", strip=True)
        if t:
            title = t

    resource_sections = soup.find_all("div", class_="resource-section")

    if not resource_sections:
        body = soup.find("body")
        if body:
            md = _CONVERTER.handle(str(body))
            return title, _clean(md)
        return title, ""

    parts = []
    for sec in resource_sections:
        md = _CONVERTER.handle(str(sec))
        md = _clean(md)
        if md:
            parts.append(md)

    return title, "\n\n---\n\n".join(parts)


def _clean(md: str) -> str:
    md = re.sub(r"[ \t]+\n", "\n", md)
    md = re.sub(r"\n{4,}", "\n\n\n", md)
    md = re.sub(r"\[#\]\([^)]*\)", "", md)
    md = re.sub(r"\[¶\]\([^)]*\)", "", md)
    return md.strip()


# ---------------------------------------------------------------------------
# Scrape a single slug
# ---------------------------------------------------------------------------

def scrape_slug(session: requests.Session, docs_base: str, slug: str) -> tuple[str, str] | None:
    url = f"{docs_base}/api-group-{slug}/"
    try:
        resp = session.get(url, timeout=(10, 60))
        if resp.status_code == 404:
            return None
        resp.raise_for_status()
    except Exception as e:
        print(f"  ERROR fetching {url}: {e}")
        return None

    title, content = extract_content(resp.text)

    if len(content) < MIN_CONTENT_LEN:
        return None

    return title, content


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    if OUTPUT_DIR.exists():
        backup = OUTPUT_DIR.parent / f"docs_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        print(f"Backing up existing docs -> {backup.name}")
        OUTPUT_DIR.rename(backup)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("=" * 70)
    print("Confluence Cloud REST API Documentation Scraper")
    print(f"v1: {DOCS_V1}")
    print(f"v2: {DOCS_V2}")
    print("=" * 70)

    session = requests.Session()
    session.headers.update(HEADERS)

    scraped_files = []
    skipped = []

    # --- v1 ---
    print(f"\nScraping {len(SLUGS_V1)} v1 API group pages...")
    print("-" * 70)

    for i, slug in enumerate(SLUGS_V1, 1):
        filename = f"api_v1_{slug}.md"
        print(f"[v1 {i}/{len(SLUGS_V1)}] {slug:<50}", end=" ", flush=True)

        result = scrape_slug(session, DOCS_V1, slug)
        time.sleep(DELAY)

        if not result:
            print("x skipped")
            skipped.append(f"v1/{slug}")
            continue

        title, content = result
        source_url = f"{DOCS_V1}/api-group-{slug}/"

        filepath = OUTPUT_DIR / filename
        filepath.write_text(
            f"# {title}\n\n*Source: {source_url}*\n\n---\n\n{content}",
            encoding="utf-8",
        )
        print(f"({content.count(chr(10))} lines)")

        scraped_files.append({"filename": filename, "title": title, "url": source_url, "version": "v1"})

    # --- v2 ---
    print(f"\nScraping {len(SLUGS_V2)} v2 API group pages...")
    print("-" * 70)

    for i, slug in enumerate(SLUGS_V2, 1):
        filename = f"api_v2_{slug}.md"
        print(f"[v2 {i}/{len(SLUGS_V2)}] {slug:<50}", end=" ", flush=True)

        result = scrape_slug(session, DOCS_V2, slug)
        time.sleep(DELAY)

        if not result:
            print("x skipped")
            skipped.append(f"v2/{slug}")
            continue

        title, content = result
        source_url = f"{DOCS_V2}/api-group-{slug}/"

        filepath = OUTPUT_DIR / filename
        filepath.write_text(
            f"# {title}\n\n*Source: {source_url}*\n\n---\n\n{content}",
            encoding="utf-8",
        )
        print(f"({content.count(chr(10))} lines)")

        scraped_files.append({"filename": filename, "title": title, "url": source_url, "version": "v2"})

    print()
    print("=" * 70)
    print(f"Scraped: {len(scraped_files)}")
    print(f"Skipped: {len(skipped)}")
    if skipped:
        print(f"  Skipped: {', '.join(skipped)}")

    manifest = {
        "source": "Confluence Cloud REST API (developer.atlassian.com)",
        "scrape_date": datetime.now().isoformat(),
        "total_pages": len(scraped_files),
        "files": scraped_files,
    }
    (OUTPUT_DIR / "_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    print(f"\nOutput:   {OUTPUT_DIR}")
    print("=" * 70)


if __name__ == "__main__":
    main()
