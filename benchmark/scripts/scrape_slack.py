#!/usr/bin/env python3
"""
Slack API Documentation Scraper

Strategy:
  1. Fetch docs.slack.dev/sitemap.xml  →  extract all /reference/methods/* URLs
     (306 method pages, no JS needed — the sitemap is a plain XML file)
  2. For each method page, GET the URL with a plain requests call.
     Docusaurus v3 server-side-renders the content, so all parameters,
     prose, response examples, and error tables are in the raw HTML.
  3. Convert HTML → clean Markdown using html2text, write to docs/.

Usage:
    uv run python benchmark/scripts/scrape_slack.py
    # or
    python benchmark/scripts/scrape_slack.py

Output:
    benchmark/datasets/slack/docs/
        _manifest.json
        chat.postMessage.md
        conversations.list.md
        ...
"""

import json
import re
import time
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path

import requests

import html2text
from bs4 import BeautifulSoup


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

BASE_URL   = "https://docs.slack.dev"
SITEMAP    = f"{BASE_URL}/sitemap.xml"
OUTPUT_DIR = Path(__file__).parent.parent / "datasets" / "slack" / "docs"

DELAY = 0.5   # seconds between requests — be polite

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "en-US,en;q=0.9",
}

# Sections of the docs to include (we want methods + supporting reference pages)
# Exclude: changelog, tools (SDK reference), legacy
INCLUDE_PATHS = [
    "/reference/methods",
    "/reference/events",
    "/reference/block-kit",
    "/reference/messaging",
    "/reference/objects",
    "/apis/",
    "/messaging/",
    "/authentication/",
]

EXCLUDE_PATHS = [
    "/changelog/",
    "/tools/",
    "/legacy/",
    "/reference/methods/admin.",   # admin.* methods require grid/enterprise
]


# ---------------------------------------------------------------------------
# Sitemap discovery
# ---------------------------------------------------------------------------

def fetch_sitemap_urls(session: requests.Session) -> list[str]:
    """Fetch sitemap.xml and return all URLs matching our include/exclude rules."""
    print(f"Fetching sitemap: {SITEMAP}")
    resp = session.get(SITEMAP, timeout=30)
    resp.raise_for_status()

    root = ET.fromstring(resp.content)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

    all_urls = [loc.text.strip() for loc in root.findall(".//sm:loc", ns) if loc.text]
    print(f"  Total URLs in sitemap: {len(all_urls)}")

    filtered = []
    for url in all_urls:
        path = url.replace(BASE_URL, "")
        if any(path.startswith(inc) for inc in INCLUDE_PATHS):
            if not any(exc in path for exc in EXCLUDE_PATHS):
                filtered.append(url)

    print(f"  After filtering: {len(filtered)} URLs to scrape")
    return filtered


# ---------------------------------------------------------------------------
# HTML → Markdown conversion
# ---------------------------------------------------------------------------

def _build_converter() -> html2text.HTML2Text:
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = True
    h.ignore_emphasis = False
    h.body_width = 0          # don't wrap lines
    h.protect_links = False
    h.unicode_snob = True
    h.skip_internal_links = True
    h.single_line_break = False
    return h


_CONVERTER = _build_converter()


def _extract_main_content(html: str) -> str:
    """
    Extract the main article content from Docusaurus page HTML.

    Docusaurus wraps content in <article> or a div with class "theme-doc-markdown".
    We strip the nav, header, footer, sidebar, and interactive widgets before
    converting to markdown.
    """
    soup = BeautifulSoup(html, "html.parser")

    # Remove navigation, sidebar, footer, header, interactive widgets
    for selector in [
        "nav", "header", "footer",
        "[class*='sidebar']", "[class*='navbar']",
        "[class*='pagination']", "[class*='toc']",
        "[class*='breadcrumbs']", "[class*='edit-this-page']",
        "[class*='DocSearch']", "[id*='search']",
        # The interactive "Call generator" widget
        "[class*='call-generator']", "[class*='playground']",
    ]:
        for el in soup.select(selector):
            el.decompose()

    # Prefer <article> element (Docusaurus main content wrapper)
    article = soup.find("article")
    if article:
        return str(article)

    # Fall back to the main content div
    main = soup.find("main") or soup.find("div", {"id": "main-content"})
    if main:
        return str(main)

    # Last resort: full body
    body = soup.find("body")
    return str(body) if body else html


def html_to_markdown(html: str, url: str) -> str:
    """Convert a Docusaurus HTML page to clean markdown."""
    main_html = _extract_main_content(html)
    md = _CONVERTER.handle(main_html)

    # Clean up common conversion artefacts
    md = re.sub(r"\n{4,}", "\n\n\n", md)          # collapse excessive blank lines
    md = re.sub(r"[ \t]+\n", "\n", md)             # trailing whitespace
    md = re.sub(r"\[¶\]\([^)]*\)", "", md)         # remove ¶ anchor links
    md = re.sub(r"\[#\]\([^)]*\)", "", md)         # remove # anchor links
    md = md.strip()

    return md


# ---------------------------------------------------------------------------
# URL → filename
# ---------------------------------------------------------------------------

def url_to_filename(url: str) -> str:
    """
    Convert a docs URL to a local markdown filename.

    Examples:
      .../reference/methods/chat.postMessage  →  chat.postMessage.md
      .../reference/events/message            →  events_message.md
      .../apis/web-api/                       →  apis_web-api.md
    """
    path = url.replace(BASE_URL, "").strip("/")
    # Strip /reference/ prefix for method pages — keep just the method name
    path = re.sub(r"^reference/methods/", "", path)
    # For other pages, replace / with _
    path = path.replace("/", "_")
    # Sanitize
    path = re.sub(r"[^\w.\-]", "_", path)
    path = path.strip("_")
    return f"{path}.md" if path else "index.md"


def extract_title(html: str, url: str) -> str:
    """Extract page title from HTML <title> or <h1>."""
    soup = BeautifulSoup(html, "html.parser")

    # Prefer <title> tag — it's clean: "chat.postMessage | Slack"
    title_tag = soup.find("title")
    if title_tag:
        title = title_tag.get_text(strip=True)
        # Docusaurus titles are "Page Name | Slack" — take the left part
        title = title.split("|")[0].strip()
        if title:
            return title

    # Fall back to h1 text
    h1 = soup.find("h1")
    if h1:
        return h1.get_text(strip=True)

    return url.rstrip("/").split("/")[-1]


# ---------------------------------------------------------------------------
# Main scrape loop
# ---------------------------------------------------------------------------

def scrape_page(session: requests.Session, url: str) -> tuple[str, str] | None:
    """
    Fetch a single docs page and return (title, markdown_content).
    Returns None on failure.
    """
    try:
        resp = session.get(url, timeout=(5, 20))
        resp.raise_for_status()

        if "text/html" not in resp.headers.get("Content-Type", ""):
            return None

        title = extract_title(resp.text, url)
        md = html_to_markdown(resp.text, url)

        if len(md) < 100:
            return None

        return title, md

    except Exception as e:
        print(f"  ERROR: {e}")
        return None


def main():
    if OUTPUT_DIR.exists() and any(OUTPUT_DIR.iterdir()):
        backup = OUTPUT_DIR.parent / f"docs_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        print(f"Backing up existing docs → {backup.name}")
        OUTPUT_DIR.rename(backup)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("=" * 70)
    print("Slack API Documentation Scraper")
    print(f"Source: {BASE_URL}")
    print("=" * 70)

    session = requests.Session()
    session.headers.update(HEADERS)

    # --- Discovery via sitemap ---
    urls = fetch_sitemap_urls(session)
    print()

    # Prioritize methods pages first, then others
    method_urls = [u for u in urls if "/reference/methods/" in u]
    other_urls  = [u for u in urls if "/reference/methods/" not in u]
    ordered_urls = method_urls + other_urls

    print(f"Scraping {len(method_urls)} method pages + {len(other_urls)} reference pages")
    print("=" * 70)

    scraped_files = []
    skipped = []

    for i, url in enumerate(ordered_urls, 1):
        filename = url_to_filename(url)
        label = url.replace(BASE_URL, "")
        print(f"[{i:3d}/{len(ordered_urls)}] {label[:60]:<60}", end=" ", flush=True)

        result = scrape_page(session, url)
        time.sleep(DELAY)

        if not result:
            print("✗ skipped")
            skipped.append(url)
            continue

        title, content = result

        filepath = OUTPUT_DIR / filename
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"# {title}\n\n")
            f.write(f"*Source: {url}*\n\n")
            f.write("---\n\n")
            f.write(content)

        lines = content.count("\n")
        print(f"✓ {lines} lines")

        scraped_files.append({
            "filename": filename,
            "title": title,
            "url": url,
        })

    print()
    print("=" * 70)
    print(f"✓ Scraped: {len(scraped_files)}")
    print(f"✗ Skipped: {len(skipped)}")

    manifest = {
        "source": "Slack API Documentation (docs.slack.dev)",
        "scraped_from": BASE_URL,
        "scrape_date": datetime.now().isoformat(),
        "total_pages": len(scraped_files),
        "method_pages": len([f for f in scraped_files if not f["filename"].startswith(("apis_", "events_", "reference_", "messaging_", "authentication_"))]),
        "files": scraped_files,
    }
    manifest_path = OUTPUT_DIR / "_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    print(f"\nOutput:   {OUTPUT_DIR}")
    print(f"Manifest: {manifest_path}")
    print("=" * 70)


if __name__ == "__main__":
    main()
