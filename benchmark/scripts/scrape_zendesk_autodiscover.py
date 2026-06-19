#!/usr/bin/env python3
"""
Zendesk Ticketing API Documentation Scraper (BFS autodiscovery)

Strategy:
  1. Start from a set of seed URLs in the Zendesk API reference.
  2. Fetch each page (server-rendered HTML, ~6.8 MB each) and parse the
     navigation sidebar which contains ~136 links to other sections.
  3. Follow links matching /api-reference/ticketing/, /api-reference/help_center/,
     or /api-reference/conversations using BFS until MAX_PAGES is reached.
  4. Convert each page's <main> content to clean Markdown via html2text.

Usage:
    uv run python benchmark/scripts/scrape_zendesk_autodiscover.py
    # or
    python benchmark/scripts/scrape_zendesk_autodiscover.py

Output:
    benchmark/datasets/zendesk/docs/
        _manifest.json
        api_ticketing_tickets_tickets.md
        api_ticketing_users_users.md
        ...
"""

import json
import re
import time
from collections import deque
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin, urlparse

import html2text
import requests
from bs4 import BeautifulSoup


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

BASE_URL   = "https://developer.zendesk.com"
OUTPUT_DIR = Path(__file__).parent.parent / "datasets" / "zendesk" / "docs"

DELAY           = 0.5   # seconds between requests — be polite
MIN_CONTENT_LEN = 200   # discard pages with fewer characters of markdown
MAX_PAGES       = 150   # BFS cap

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "en-US,en;q=0.9",
}

# BFS seed pages — each has a full sidebar with ~136 navigation links
SEED_URLS = [
    "https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/",
    "https://developer.zendesk.com/api-reference/ticketing/users/users/",
    "https://developer.zendesk.com/api-reference/ticketing/organizations/organizations/",
]

# Only follow links whose path starts with one of these prefixes
INCLUDE_PREFIXES = [
    "/api-reference/ticketing/",
    "/api-reference/help_center/",
    "/api-reference/conversations",
]

# Exclude pages that match any of these substrings
EXCLUDE_SUBSTRINGS = [
    "/changelog",
    "/introduction",
    "#",            # anchor-only fragments (belt-and-suspenders; handled below too)
]


# ---------------------------------------------------------------------------
# URL helpers
# ---------------------------------------------------------------------------

def _is_target_url(url: str) -> bool:
    """Return True if the URL belongs to a section we want to scrape."""
    parsed = urlparse(url)

    # Must be on the same host
    if parsed.netloc and parsed.netloc != "developer.zendesk.com":
        return False

    path = parsed.path
    if not any(path.startswith(pfx) for pfx in INCLUDE_PREFIXES):
        return False
    if any(excl in url for excl in EXCLUDE_SUBSTRINGS):
        return False

    return True


def _normalise(url: str) -> str:
    """Strip fragment and trailing slash variations for dedup purposes."""
    parsed = urlparse(url)
    # Drop fragment entirely
    normalised = parsed._replace(fragment="", query="").geturl()
    # Ensure a trailing slash so /tickets and /tickets/ are the same key
    if not normalised.endswith("/"):
        normalised += "/"
    return normalised


def extract_links(html: str, page_url: str) -> list[str]:
    """
    Parse all <a href> links from the page and return absolute URLs
    that pass the target-URL filter (deduplicated, no anchors).
    """
    soup = BeautifulSoup(html, "html.parser")
    found = []
    for tag in soup.find_all("a", href=True):
        href = tag["href"].strip()
        # Skip pure anchor links and javascript: hrefs
        if not href or href.startswith("#") or href.startswith("javascript:"):
            continue
        absolute = urljoin(page_url, href)
        # Drop any fragment portion
        absolute = urlparse(absolute)._replace(fragment="").geturl()
        if _is_target_url(absolute):
            found.append(absolute)
    return found


# ---------------------------------------------------------------------------
# HTML → Markdown conversion
# ---------------------------------------------------------------------------

def _build_converter() -> html2text.HTML2Text:
    h = html2text.HTML2Text()
    h.ignore_links   = False
    h.ignore_images  = True
    h.ignore_emphasis = False
    h.body_width     = 0      # don't wrap lines
    h.protect_links  = False
    h.unicode_snob   = True
    h.skip_internal_links = True
    h.single_line_break   = False
    return h


_CONVERTER = _build_converter()


def _extract_main_content(html: str) -> str:
    """
    Strip scripts / styles / noscripts, then return the HTML of the
    <main> element (or <body> as a last resort).
    """
    soup = BeautifulSoup(html, "html.parser")

    # Remove elements that add noise but no API content
    for tag in soup.find_all(["script", "style", "noscript"]):
        tag.decompose()

    main = soup.find("main")
    if main:
        return str(main)

    body = soup.find("body")
    return str(body) if body else html


def html_to_markdown(html: str) -> str:
    """Convert a Zendesk API reference HTML page to clean markdown."""
    main_html = _extract_main_content(html)
    md = _CONVERTER.handle(main_html)

    # Clean up common conversion artefacts
    md = re.sub(r"\n{4,}", "\n\n\n", md)   # collapse excessive blank lines
    md = re.sub(r"[ \t]+\n", "\n", md)      # trailing whitespace on lines
    md = re.sub(r"\[¶\]\([^)]*\)", "", md)  # remove ¶ anchor links
    md = re.sub(r"\[#\]\([^)]*\)", "", md)  # remove # anchor links
    md = md.strip()

    return md


# ---------------------------------------------------------------------------
# Title extraction
# ---------------------------------------------------------------------------

def extract_title(html: str, url: str) -> str:
    """Extract page title from <title> tag (left part before '|')."""
    soup = BeautifulSoup(html, "html.parser")

    title_tag = soup.find("title")
    if title_tag:
        title = title_tag.get_text(strip=True)
        # Zendesk titles look like "Tickets | Zendesk Developer Docs"
        title = title.split("|")[0].strip()
        if title:
            return title

    # Fallback to first <h1>
    h1 = soup.find("h1")
    if h1:
        return h1.get_text(strip=True)

    return url.rstrip("/").split("/")[-1]


# ---------------------------------------------------------------------------
# URL → filename
# ---------------------------------------------------------------------------

def url_to_filename(url: str) -> str:
    """
    Convert a Zendesk API reference URL to a local markdown filename.

    Example:
      https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/
      → api_ticketing_tickets_tickets.md
    """
    path = url.replace(BASE_URL, "").strip("/")
    # Strip the leading "api-reference/" prefix
    path = re.sub(r"^api-reference/", "", path)
    # Replace slashes and hyphens-used-as-separators with underscores
    slug = path.replace("/", "_")
    # Sanitise any remaining problematic characters
    slug = re.sub(r"[^\w.\-]", "_", slug)
    slug = slug.strip("_")
    return f"api_{slug}.md" if slug else "api_index.md"


# ---------------------------------------------------------------------------
# Page fetcher
# ---------------------------------------------------------------------------

def scrape_page(session: requests.Session, url: str) -> tuple[str, str] | None:
    """
    Fetch a single API reference page and return (title, markdown_content).
    Returns None on failure or if the content is too short.
    """
    try:
        resp = session.get(url, timeout=(5, 30))
        resp.raise_for_status()

        content_type = resp.headers.get("Content-Type", "")
        if "text/html" not in content_type:
            return None

        title = extract_title(resp.text, url)
        md    = html_to_markdown(resp.text)

        if len(md) < MIN_CONTENT_LEN:
            return None

        return title, md

    except Exception as exc:
        print(f"  ERROR fetching {url}: {exc}")
        return None


# ---------------------------------------------------------------------------
# BFS discovery + scrape loop
# ---------------------------------------------------------------------------

def main():
    # --- Backup / create output directory ---
    if OUTPUT_DIR.exists() and any(OUTPUT_DIR.iterdir()):
        backup = OUTPUT_DIR.parent / f"docs_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        print(f"Backing up existing docs -> {backup.name}")
        OUTPUT_DIR.rename(backup)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("=" * 70)
    print("Zendesk API Documentation Scraper (BFS autodiscovery)")
    print(f"Source: {BASE_URL}/api-reference/")
    print(f"Max pages: {MAX_PAGES}")
    print("=" * 70)

    session = requests.Session()
    session.headers.update(HEADERS)

    # BFS state
    queue:   deque[str] = deque()
    visited: set[str]   = set()   # normalised URLs already enqueued / done

    # Seed the queue
    for seed in SEED_URLS:
        key = _normalise(seed)
        if key not in visited:
            visited.add(key)
            queue.append(seed)

    scraped_files: list[dict] = []
    skipped: list[str]        = []
    page_count = 0

    while queue and page_count < MAX_PAGES:
        url = queue.popleft()
        page_count += 1

        filename = url_to_filename(url)
        label    = url.replace(BASE_URL, "")
        print(
            f"[{page_count:3d}/{MAX_PAGES}] {label[:60]:<60}",
            end=" ",
            flush=True,
        )

        try:
            resp = session.get(url, timeout=(5, 30))
            resp.raise_for_status()
            html = resp.text
        except Exception as exc:
            print(f"FETCH ERROR: {exc}")
            skipped.append(url)
            time.sleep(DELAY)
            continue

        # --- Discover new links from this page's sidebar ---
        new_links = extract_links(html, url)
        for link in new_links:
            key = _normalise(link)
            if key not in visited:
                visited.add(key)
                queue.append(link)

        # --- Extract content ---
        content_type = resp.headers.get("Content-Type", "")
        if "text/html" not in content_type:
            print("skip (not HTML)")
            skipped.append(url)
            time.sleep(DELAY)
            continue

        title = extract_title(html, url)
        md    = html_to_markdown(html)

        if len(md) < MIN_CONTENT_LEN:
            print(f"skip (content too short: {len(md)} chars)")
            skipped.append(url)
            time.sleep(DELAY)
            continue

        # --- Write markdown file ---
        filepath = OUTPUT_DIR / filename
        with open(filepath, "w", encoding="utf-8") as fh:
            fh.write(f"# {title}\n\n")
            fh.write(f"*Source: {url}*\n\n")
            fh.write("---\n\n")
            fh.write(md)

        lines = md.count("\n")
        print(f"ok  {lines} lines  ({len(md):,} chars)")

        scraped_files.append({
            "filename": filename,
            "title":    title,
            "url":      url,
        })

        time.sleep(DELAY)

    # --- Summary ---
    print()
    print("=" * 70)
    print(f"BFS queue exhausted or MAX_PAGES reached.")
    print(f"  Scraped : {len(scraped_files)}")
    print(f"  Skipped : {len(skipped)}")
    print(f"  URLs discovered (total visited): {len(visited)}")

    # --- Manifest ---
    manifest = {
        "source":       "Zendesk API Reference (developer.zendesk.com)",
        "scraped_from": f"{BASE_URL}/api-reference/",
        "scrape_date":  datetime.now().isoformat(),
        "total_pages":  len(scraped_files),
        "files":        scraped_files,
    }
    manifest_path = OUTPUT_DIR / "_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    print(f"\nOutput:   {OUTPUT_DIR}")
    print(f"Manifest: {manifest_path}")
    print("=" * 70)


if __name__ == "__main__":
    main()
