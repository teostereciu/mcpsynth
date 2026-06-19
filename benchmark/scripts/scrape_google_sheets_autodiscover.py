#!/usr/bin/env python3
"""
Google Sheets API v4 Documentation Scraper

Fetches and converts the actual human-written HTML documentation pages
from developers.google.com/sheets/api/reference/rest — no OpenAPI spec.

Discovery strategy:
  - Fetch the reference index page and parse all href links matching
    /sheets/api/reference/rest to discover pages.
  - Also scrape a known list of pages from prior investigation.
  - Deduplicate and scrape each page.

Content strategy:
  - requests + BeautifulSoup (server-rendered, no JS required).
  - Remove nav/header/footer/sidebar, find main content div,
    convert headings/paragraphs/code/tables to clean markdown.

Usage:
    python3 benchmark/scripts/scrape_google_sheets_autodiscover.py
"""

import json
import re
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
BASE_URL   = "https://developers.google.com"
INDEX_URL  = "https://developers.google.com/sheets/api/reference/rest"
OUTPUT_DIR = Path(__file__).parent.parent / "datasets" / "google_sheets" / "docs"

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

# Known pages from prior investigation — guaranteed to exist
KNOWN_PAGES = [
    "https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/batchUpdate",
    "https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/create",
    "https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/get",
    "https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/getByDataFilter",
    "https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.developerMetadata/get",
    "https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.developerMetadata/search",
    "https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.sheets/copyTo",
    "https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/append",
    "https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/batchClear",
    "https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/batchClearByDataFilter",
    "https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/batchGet",
    "https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/batchGetByDataFilter",
    "https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/batchUpdate",
    "https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/batchUpdateByDataFilter",
    "https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/clear",
    "https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/clearByDataFilter",
    "https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/get",
    "https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/update",
]

MIN_CONTENT_LEN = 200  # minimum characters to keep a page


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------

def discover_urls(session: requests.Session) -> list[str]:
    """
    Fetch the index page and parse all href links matching
    /sheets/api/reference/rest. Combine with KNOWN_PAGES, deduplicate.
    """
    discovered: set[str] = set(KNOWN_PAGES)

    print(f"Fetching index page: {INDEX_URL}")
    try:
        resp = session.get(INDEX_URL, timeout=(10, 30))
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        time.sleep(DELAY)

        for tag in soup.find_all("a", href=True):
            href = tag["href"]
            # Normalise relative links
            if href.startswith("/"):
                href = BASE_URL + href
            elif not href.startswith("http"):
                href = urljoin(INDEX_URL, href)

            # Only keep Sheets REST API reference pages
            parsed = urlparse(href)
            if (
                parsed.netloc == "developers.google.com"
                and "/sheets/api/reference/rest" in parsed.path
                and not parsed.path.endswith("/reference/rest")  # skip root index
                and not parsed.fragment                           # skip anchor links
            ):
                # Strip query strings
                clean = f"https://{parsed.netloc}{parsed.path}"
                discovered.add(clean)

        print(f"  Found {len(discovered)} unique URLs after index parse")
    except Exception as e:
        print(f"  WARNING: could not fetch index page: {e}")
        print(f"  Falling back to {len(KNOWN_PAGES)} known pages")

    # Filter: only keep pages that look like method endpoints
    # (path has at least 5 segments: /sheets/api/reference/rest/v4/resource/method)
    filtered = []
    for url in sorted(discovered):
        path_parts = urlparse(url).path.strip("/").split("/")
        if len(path_parts) >= 6:  # sheets/api/reference/rest/v4/resource[/method]
            filtered.append(url)

    # Always include known pages even if they have fewer segments
    for url in KNOWN_PAGES:
        if url not in filtered:
            filtered.append(url)

    return sorted(set(filtered))


# ---------------------------------------------------------------------------
# HTML -> Markdown conversion
# ---------------------------------------------------------------------------

def _tag_to_markdown(tag, depth: int = 0) -> str:
    """Recursively convert a BeautifulSoup tag tree to markdown text."""
    if tag is None:
        return ""

    # Plain string node
    if isinstance(tag, str):
        return tag

    name = getattr(tag, "name", None)
    if name is None:
        return tag.get_text()

    # Headings
    if name in ("h1", "h2", "h3", "h4", "h5", "h6"):
        level = int(name[1])
        text = tag.get_text(" ", strip=True)
        return f"\n\n{'#' * level} {text}\n\n"

    # Paragraphs / divs that act as paragraphs
    if name == "p":
        children = "".join(_tag_to_markdown(c, depth) for c in tag.children)
        return f"\n\n{children.strip()}\n\n"

    # Inline code
    if name == "code":
        text = tag.get_text()
        return f"`{text}`"

    # Code blocks
    if name == "pre":
        code = tag.get_text()
        return f"\n\n```\n{code}\n```\n\n"

    # Strong / bold
    if name in ("strong", "b"):
        text = tag.get_text(" ", strip=True)
        return f"**{text}**"

    # Emphasis / italic
    if name in ("em", "i"):
        text = tag.get_text(" ", strip=True)
        return f"*{text}*"

    # Unordered list
    if name == "ul":
        items = []
        for li in tag.find_all("li", recursive=False):
            item_text = "".join(_tag_to_markdown(c, depth + 1) for c in li.children).strip()
            items.append(f"- {item_text}")
        return "\n" + "\n".join(items) + "\n"

    # Ordered list
    if name == "ol":
        items = []
        for idx, li in enumerate(tag.find_all("li", recursive=False), 1):
            item_text = "".join(_tag_to_markdown(c, depth + 1) for c in li.children).strip()
            items.append(f"{idx}. {item_text}")
        return "\n" + "\n".join(items) + "\n"

    # Tables
    if name == "table":
        rows = tag.find_all("tr")
        if not rows:
            return ""
        md_rows = []
        header_done = False
        for row in rows:
            cells = row.find_all(["th", "td"])
            if not cells:
                continue
            cell_texts = [c.get_text(" ", strip=True).replace("|", "\\|") for c in cells]
            md_rows.append("| " + " | ".join(cell_texts) + " |")
            if not header_done:
                md_rows.append("|" + "|".join(["---"] * len(cell_texts)) + "|")
                header_done = True
        return "\n\n" + "\n".join(md_rows) + "\n\n"

    # Links — render text only (avoid noisy URLs)
    if name == "a":
        text = tag.get_text(" ", strip=True)
        href = tag.get("href", "")
        if href and not href.startswith("#"):
            return f"[{text}]({href})"
        return text

    # Horizontal rule
    if name == "hr":
        return "\n\n---\n\n"

    # Blockquote
    if name == "blockquote":
        inner = "".join(_tag_to_markdown(c, depth) for c in tag.children).strip()
        quoted = "\n".join(f"> {line}" for line in inner.split("\n"))
        return f"\n\n{quoted}\n\n"

    # div / section / article — just recurse
    if name in ("div", "section", "article", "main", "span"):
        return "".join(_tag_to_markdown(c, depth) for c in tag.children)

    # Default: recurse children
    return "".join(_tag_to_markdown(c, depth) for c in tag.children)


def extract_main_content(html: str) -> BeautifulSoup | None:
    """
    Find the main article/content area on a Google Developers page.
    The page is hybrid SSR — content is in the raw HTML.
    """
    soup = BeautifulSoup(html, "html.parser")

    # Remove clutter: nav, header, footer, sidebar, scripts, styles
    for selector in [
        "nav", "header", "footer", "script", "style",
        "[class*='devsite-nav']", "[class*='devsite-header']",
        "[class*='devsite-footer']", "[class*='devsite-sidebar']",
        "[class*='devsite-toc']", "[class*='devsite-banner']",
        "[class*='devsite-snackbar']", "[class*='nocontent']",
        "[role='navigation']", "[role='complementary']",
        ".devsite-article-meta", ".devsite-feedback",
        ".devsite-page-rating", ".devsite-breadcrumb",
        ".l-grid--nav-offset",   # left-nav spacer column
        ".devsite-bookmark",     # "Stay organized with collections" bookmark widget
        "[class*='bookmark']",
        "[class*='save-favorite']",
    ]:
        for el in soup.select(selector):
            el.decompose()

    # Google Developers: main content is in devsite-article or article
    for selector in [
        "devsite-content",
        "article.devsite-article",
        "[class*='devsite-article']",
        "article",
        "[role='main']",
        "main",
        ".devsite-doc-set-nav + div",
    ]:
        el = soup.select_one(selector)
        if el:
            return el

    body = soup.find("body")

    # Remove in-page jump-nav lists (lists where every <li> child is just an <a href=#...>)
    if body:
        for ul in body.find_all("ul"):
            lis = ul.find_all("li", recursive=False)
            if lis and all(
                len(li.find_all("a")) == 1 and (li.find("a") or {}).get("href", "").startswith("#")
                for li in lis
            ):
                ul.decompose()

    return body


def html_to_markdown(html: str) -> str:
    """Convert a Google Developers HTML page to clean markdown."""
    content_el = extract_main_content(html)
    if content_el is None:
        return ""

    md = _tag_to_markdown(content_el)

    # Normalise whitespace
    md = re.sub(r"[ \t]+\n", "\n", md)          # trailing spaces
    md = re.sub(r"\n{4,}", "\n\n\n", md)         # collapse 4+ blank lines -> 3
    md = re.sub(r"\[#\]\([^)]*\)", "", md)        # remove # anchor links
    md = re.sub(r"\[¶\]\([^)]*\)", "", md)        # remove paragraph anchors

    return md.strip()


def extract_title(html: str, url: str) -> str:
    """Extract page title from HTML."""
    soup = BeautifulSoup(html, "html.parser")

    # Prefer <title> tag — clean and reliable on Google Developers pages
    title_tag = soup.find("title")
    if title_tag:
        title = title_tag.get_text(strip=True)
        # Format: "Method: spreadsheets.get  |  Sheets API  |  Google for Developers"
        title = title.split("|")[0].strip()
        return title

    # Fallback to h1 but strip anything after a newline (Google appends bookmark UI text)
    h1 = soup.find("h1")
    if h1:
        return h1.get_text(" ", strip=True).split("\n")[0].strip()

    return url.rstrip("/").split("/")[-1]


# ---------------------------------------------------------------------------
# URL -> filename
# ---------------------------------------------------------------------------

def url_to_filename(url: str) -> str:
    """
    Convert a Google Sheets API reference URL to a markdown filename.

    Examples:
      .../v4/spreadsheets/get              -> api_spreadsheets_get.md
      .../v4/spreadsheets.values/batchGet  -> api_spreadsheets.values_batchGet.md
    """
    path = urlparse(url).path.rstrip("/")
    # Strip up to and including /rest/v4/
    path = re.sub(r".*/rest/v4/", "", path)
    # path is now like "spreadsheets/get" or "spreadsheets.values/batchGet"
    # Replace slash between resource and method with underscore
    parts = path.split("/")
    if len(parts) >= 2:
        # resource_name / method_name
        resource = parts[-2]
        method   = parts[-1]
        name     = f"{resource}_{method}"
    else:
        name = parts[0]

    name = re.sub(r"[^\w.\-]", "_", name).strip("_")
    return f"api_{name}.md"


# ---------------------------------------------------------------------------
# Page scraper
# ---------------------------------------------------------------------------

def scrape_page(session: requests.Session, url: str) -> tuple[str, str] | None:
    """
    Fetch a single docs page and return (title, markdown_content).
    Returns None on failure or if content is too short.
    """
    try:
        resp = session.get(url, timeout=(10, 30))
        resp.raise_for_status()

        if "text/html" not in resp.headers.get("Content-Type", ""):
            return None

        title = extract_title(resp.text, url)
        md    = html_to_markdown(resp.text)

        if len(md) < MIN_CONTENT_LEN:
            return None

        return title, md

    except Exception as e:
        print(f"  ERROR: {e}")
        return None


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    # --- Backup existing output dir ---
    if OUTPUT_DIR.exists():
        backup = OUTPUT_DIR.parent / f"docs_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        print(f"Backing up existing docs -> {backup.name}")
        OUTPUT_DIR.rename(backup)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("=" * 70)
    print("Google Sheets API v4 Documentation Scraper")
    print(f"Source: {INDEX_URL}")
    print("=" * 70)

    session = requests.Session()
    session.headers.update(HEADERS)

    # --- Discovery ---
    print("\nDiscovering pages...")
    urls = discover_urls(session)
    print(f"Total pages to scrape: {len(urls)}")
    print("=" * 70)

    scraped_files = []
    skipped = []

    for i, url in enumerate(urls, 1):
        filename = url_to_filename(url)
        label = url.replace(BASE_URL, "")
        print(f"[{i}/{len(urls)}] {label[:65]:<65}", end=" ", flush=True)

        result = scrape_page(session, url)
        time.sleep(DELAY)

        if not result:
            print("x skipped")
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
        print(f"({lines} lines)")

        scraped_files.append({
            "filename": filename,
            "title":    title,
            "url":      url,
        })

    print()
    print("=" * 70)
    print(f"Scraped: {len(scraped_files)}")
    print(f"Skipped: {len(skipped)}")

    manifest = {
        "source":       "Google Sheets API v4 (developers.google.com)",
        "scraped_from": INDEX_URL,
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
