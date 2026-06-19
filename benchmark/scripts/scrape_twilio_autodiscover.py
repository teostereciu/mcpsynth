#!/usr/bin/env python3
"""
Twilio REST API Documentation Scraper

Strategy:
  1. Fetch https://www.twilio.com/docs/sitemap.xml  →  extract all URLs
     matching core Twilio REST API product paths.
     (7110 URLs, plain XML, no nested sitemaps.)
  2. For each matching page, GET the URL with a plain requests call.
     Pages are server-rendered, so content is in the raw HTML.
  3. Strip <script>/<style>/<noscript>, find <article>, convert HTML →
     clean Markdown using html2text, write to docs/.

Usage:
    uv run python benchmark/scripts/scrape_twilio_autodiscover.py
    # or
    python benchmark/scripts/scrape_twilio_autodiscover.py

Output:
    benchmark/datasets/twilio/docs/
        _manifest.json
        api_messaging_api_...md
        api_voice_api_...md
        ...
"""

import json
import re
import time
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

import html2text
import requests
from bs4 import BeautifulSoup


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

BASE_URL   = "https://www.twilio.com"
DOCS_BASE  = f"{BASE_URL}/docs"
SITEMAP    = f"{DOCS_BASE}/sitemap.xml"
OUTPUT_DIR = Path(__file__).parent.parent / "datasets" / "twilio" / "docs"

DELAY = 0.5          # seconds between requests — be polite
MIN_CONTENT_LEN = 200

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "en-US,en;q=0.9",
}

# Product prefixes to include.
# For messaging we only want paths containing /api (not generic guides).
INCLUDE_PREFIXES = [
    "/docs/voice/api",
    "/docs/verify/api",
    "/docs/conversations/api",
    "/docs/phone-numbers/api",
    "/docs/usage/api",
    "/docs/sms/api",
]

# Messaging is special: include only if path contains /api
MESSAGING_PREFIX = "/docs/messaging/"

EXCLUDE_SUBSTRINGS = [
    "/api/errors/",   # individual error code pages — too many
    "changelog",
    "alpha",
    "enterprise",
    "quickstart",
    "tutorial",
]


# ---------------------------------------------------------------------------
# Sitemap discovery
# ---------------------------------------------------------------------------

def _url_is_included(url: str) -> bool:
    """Return True if the URL should be scraped."""
    parsed = urlparse(url)
    path = parsed.path

    # Check static product prefixes
    for prefix in INCLUDE_PREFIXES:
        if path.startswith(prefix):
            # Apply exclusions
            if not any(exc in url for exc in EXCLUDE_SUBSTRINGS):
                return True

    # Messaging: only include paths that contain /api
    if path.startswith(MESSAGING_PREFIX) and "/api" in path:
        if not any(exc in url for exc in EXCLUDE_SUBSTRINGS):
            return True

    return False


def fetch_sitemap_urls(session: requests.Session) -> list[str]:
    """Fetch sitemap.xml and return all URLs matching our include/exclude rules."""
    print(f"Fetching sitemap: {SITEMAP}")
    resp = session.get(SITEMAP, timeout=30)
    resp.raise_for_status()

    root = ET.fromstring(resp.content)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

    all_urls = [loc.text.strip() for loc in root.findall(".//sm:loc", ns) if loc.text]
    print(f"  Total URLs in sitemap: {len(all_urls)}")

    filtered = [url for url in all_urls if _url_is_included(url)]
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
    Extract the main article content from a Twilio docs page.

    Remove noise tags first, then prefer the <article> element.
    Falls back to <main> or <body>.
    """
    soup = BeautifulSoup(html, "html.parser")

    # Remove noisy tags entirely
    for tag in soup.find_all(["script", "style", "noscript"]):
        tag.decompose()

    # Prefer <article> element — Twilio's main content wrapper
    article = soup.find("article")
    if article:
        return str(article)

    # Fall back to <main>
    main = soup.find("main")
    if main:
        return str(main)

    # Last resort: full body
    body = soup.find("body")
    return str(body) if body else html


def html_to_markdown(html: str) -> str:
    """Convert a Twilio docs HTML page to clean markdown."""
    main_html = _extract_main_content(html)
    md = _CONVERTER.handle(main_html)

    # Clean up common conversion artefacts
    md = re.sub(r"\n{4,}", "\n\n\n", md)   # collapse excessive blank lines
    md = re.sub(r"[ \t]+\n", "\n", md)      # trailing whitespace
    md = re.sub(r"\[¶\]\([^)]*\)", "", md)  # remove ¶ anchor links
    md = re.sub(r"\[#\]\([^)]*\)", "", md)  # remove # anchor links
    md = md.strip()

    return md


# ---------------------------------------------------------------------------
# URL → filename
# ---------------------------------------------------------------------------

def url_to_filename(url: str) -> str:
    """
    Convert a Twilio docs URL to a local markdown filename.

    Strip the https://www.twilio.com/docs/ prefix, replace / with _,
    sanitize, then prefix with 'api_'.

    Examples:
      .../voice/api/call          →  api_voice_api_call.md
      .../messaging/api/message   →  api_messaging_api_message.md
    """
    # Strip base docs prefix
    slug = url.replace(f"{DOCS_BASE}/", "").strip("/")
    # Replace path separators with underscores
    slug = slug.replace("/", "_")
    # Sanitize: allow word chars, dots, hyphens
    slug = re.sub(r"[^\w.\-]", "_", slug)
    slug = slug.strip("_")
    return f"api_{slug}.md" if slug else "api_index.md"


def extract_title(html: str, url: str) -> str:
    """Extract page title from HTML <title> tag."""
    soup = BeautifulSoup(html, "html.parser")

    title_tag = soup.find("title")
    if title_tag:
        title = title_tag.get_text(strip=True)
        # Twilio titles are "Page Name | Twilio" — take the left part
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
    Returns None on failure or when content is too short.
    """
    try:
        resp = session.get(url, timeout=(5, 20))
        resp.raise_for_status()

        if "text/html" not in resp.headers.get("Content-Type", ""):
            return None

        title = extract_title(resp.text, url)
        md = html_to_markdown(resp.text)

        if len(md) < MIN_CONTENT_LEN:
            return None

        return title, md

    except Exception as e:
        print(f"  ERROR: {e}")
        return None


def main():
    # Backup existing docs directory before writing
    if OUTPUT_DIR.exists() and any(OUTPUT_DIR.iterdir()):
        backup = OUTPUT_DIR.parent / f"docs_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        print(f"Backing up existing docs → {backup.name}")
        OUTPUT_DIR.rename(backup)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("=" * 70)
    print("Twilio REST API Documentation Scraper")
    print(f"Source: {DOCS_BASE}")
    print("=" * 70)

    session = requests.Session()
    session.headers.update(HEADERS)

    # --- Discovery via sitemap ---
    urls = fetch_sitemap_urls(session)
    print()

    print(f"Scraping {len(urls)} pages")
    print("=" * 70)

    scraped_files = []
    skipped = []

    for i, url in enumerate(urls, 1):
        filename = url_to_filename(url)
        label = url.replace(DOCS_BASE, "")
        print(f"[{i:3d}/{len(urls)}] {label[:60]:<60}", end=" ", flush=True)

        result = scrape_page(session, url)
        time.sleep(DELAY)

        if not result:
            print("SKIP skipped")
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
        print(f"OK {lines} lines")

        scraped_files.append({
            "filename": filename,
            "title": title,
            "url": url,
        })

    print()
    print("=" * 70)
    print(f"Scraped: {len(scraped_files)}")
    print(f"Skipped: {len(skipped)}")

    manifest = {
        "source": "Twilio REST API Documentation (twilio.com/docs)",
        "scraped_from": DOCS_BASE,
        "scrape_date": datetime.now().isoformat(),
        "total_pages": len(scraped_files),
        "files": scraped_files,
    }
    manifest_path = OUTPUT_DIR / "_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    print(f"\nOutput:   {OUTPUT_DIR}")
    print(f"Manifest: {manifest_path}")
    print("=" * 70)


if __name__ == "__main__":
    main()
