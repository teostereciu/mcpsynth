#!/usr/bin/env python3
"""
HubSpot API Documentation Scraper

Fetches and converts the actual human-written HTML documentation pages
from developers.hubspot.com/docs/api — no OpenAPI spec.

Discovery strategy:
  - Start from known seed URLs and the overview page.
  - BFS crawl: extract all links matching /docs/api/ from each page.
  - Deduplicate, limit to 200 pages max.

Content strategy:
  - HubSpot uses Next.js/Mintlify. Pages are 3MB+ because the JS bundle
    is inline, but the actual doc text IS server-rendered in the HTML.
  - Fetch with requests using a browser User-Agent.
  - Parse with BeautifulSoup: find article/main/content area,
    strip scripts/styles/nav, convert to markdown.

Usage:
    python3 benchmark/scripts/scrape_hubspot_autodiscover.py
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
BASE_URL   = "https://developers.hubspot.com"
DOCS_ROOT  = "/docs/api"
OUTPUT_DIR = Path(__file__).parent.parent / "datasets" / "hubspot" / "docs"

DELAY   = 0.5    # seconds between requests
MAX_PAGES = 200  # BFS cap

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "en-US,en;q=0.9",
}

MIN_CONTENT_LEN = 200  # minimum characters to keep a page

# Seed URLs — always scraped first, also used to discover more pages
SEED_URLS = [
    "https://developers.hubspot.com/docs/api/overview",
    "https://developers.hubspot.com/docs/api/crm/contacts",
    "https://developers.hubspot.com/docs/api/crm/companies",
    "https://developers.hubspot.com/docs/api/crm/deals",
    "https://developers.hubspot.com/docs/api/crm/line-items",
    "https://developers.hubspot.com/docs/api/crm/quotes",
    "https://developers.hubspot.com/docs/api/crm/tickets",
    "https://developers.hubspot.com/docs/api/marketing/emails",
    "https://developers.hubspot.com/docs/api/cms/blog-post",
    "https://developers.hubspot.com/docs/api/conversations/conversations",
    "https://developers.hubspot.com/docs/api/files/files",
    "https://developers.hubspot.com/docs/api/events/analytics",
    "https://developers.hubspot.com/docs/api/settings/users",
]


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------

def _is_api_docs_url(url: str) -> bool:
    """Return True if this URL is a HubSpot API docs page we want to scrape."""
    parsed = urlparse(url)
    return (
        parsed.netloc in ("developers.hubspot.com", "")
        and parsed.path.startswith(DOCS_ROOT)
        and not parsed.fragment            # skip anchor-only links
        and not parsed.path.endswith((".png", ".jpg", ".gif", ".svg", ".pdf"))
    )


def extract_links(html: str, base_url: str) -> list[str]:
    """Extract all /docs/api/* links from a page's HTML."""
    soup = BeautifulSoup(html, "html.parser")
    links = []
    for tag in soup.find_all("a", href=True):
        href = tag["href"]
        # Resolve relative URLs
        if href.startswith("/"):
            href = BASE_URL + href
        elif not href.startswith("http"):
            href = urljoin(base_url, href)

        # Strip query strings and fragments
        parsed = urlparse(href)
        clean = f"https://{parsed.netloc}{parsed.path}"

        if _is_api_docs_url(clean):
            links.append(clean)

    return links


def discover_urls(session: requests.Session) -> list[str]:
    """
    BFS crawl starting from SEED_URLS.
    Only follows links on developers.hubspot.com/docs/api/*.
    Returns an ordered list of URLs to scrape (max MAX_PAGES).
    """
    queue: deque[str] = deque(SEED_URLS)
    seen:  set[str]   = set(SEED_URLS)
    ordered: list[str] = []

    print(f"Starting BFS crawl from {len(SEED_URLS)} seed URLs (max {MAX_PAGES} pages)")

    while queue and len(ordered) < MAX_PAGES:
        url = queue.popleft()
        ordered.append(url)

        print(f"  [{len(ordered)}/{MAX_PAGES}] Discovering: {url.replace(BASE_URL, '')[:70]}")

        try:
            resp = session.get(url, timeout=(10, 30))
            if resp.status_code not in (200, 301, 302):
                time.sleep(DELAY)
                continue

            new_links = extract_links(resp.text, url)
            time.sleep(DELAY)

            for link in new_links:
                if link not in seen and len(seen) < MAX_PAGES * 2:
                    seen.add(link)
                    queue.append(link)

        except Exception as e:
            print(f"    WARNING: {e}")
            time.sleep(DELAY)

    print(f"  Discovery complete: {len(ordered)} URLs")
    return ordered


# ---------------------------------------------------------------------------
# HTML -> Markdown conversion
# ---------------------------------------------------------------------------

def _tag_to_markdown(tag, depth: int = 0) -> str:
    """Recursively convert a BeautifulSoup tag to markdown text."""
    if tag is None:
        return ""
    if isinstance(tag, str):
        return tag

    name = getattr(tag, "name", None)
    if name is None:
        return tag.get_text()

    # Skip invisible/noisy elements
    if name in ("script", "style", "noscript", "iframe", "svg", "button"):
        return ""

    if name in ("h1", "h2", "h3", "h4", "h5", "h6"):
        level = int(name[1])
        text = tag.get_text(" ", strip=True)
        return f"\n\n{'#' * level} {text}\n\n"

    if name == "p":
        children = "".join(_tag_to_markdown(c, depth) for c in tag.children)
        text = children.strip()
        return f"\n\n{text}\n\n" if text else ""

    if name == "code":
        text = tag.get_text()
        # Don't double-wrap if already inside a pre
        return f"`{text}`"

    if name == "pre":
        # Check if there's a code child
        code_el = tag.find("code")
        if code_el:
            lang_class = code_el.get("class", [])
            lang = ""
            for cls in (lang_class or []):
                if cls.startswith("language-"):
                    lang = cls[9:]
                    break
            code = code_el.get_text()
        else:
            lang = ""
            code = tag.get_text()
        return f"\n\n```{lang}\n{code}\n```\n\n"

    if name in ("strong", "b"):
        text = tag.get_text(" ", strip=True)
        return f"**{text}**" if text else ""

    if name in ("em", "i"):
        text = tag.get_text(" ", strip=True)
        return f"*{text}*" if text else ""

    if name == "ul":
        items = []
        for li in tag.find_all("li", recursive=False):
            item_text = "".join(_tag_to_markdown(c, depth + 1) for c in li.children).strip()
            if item_text:
                items.append(f"- {item_text}")
        return ("\n" + "\n".join(items) + "\n") if items else ""

    if name == "ol":
        items = []
        for idx, li in enumerate(tag.find_all("li", recursive=False), 1):
            item_text = "".join(_tag_to_markdown(c, depth + 1) for c in li.children).strip()
            if item_text:
                items.append(f"{idx}. {item_text}")
        return ("\n" + "\n".join(items) + "\n") if items else ""

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
        return ("\n\n" + "\n".join(md_rows) + "\n\n") if md_rows else ""

    if name == "a":
        text = tag.get_text(" ", strip=True)
        href = tag.get("href", "")
        if href and not href.startswith("#") and text:
            if href.startswith("/"):
                href = BASE_URL + href
            return f"[{text}]({href})"
        return text

    if name == "hr":
        return "\n\n---\n\n"

    if name == "br":
        return "\n"

    if name == "blockquote":
        inner = "".join(_tag_to_markdown(c, depth) for c in tag.children).strip()
        if inner:
            quoted = "\n".join(f"> {line}" for line in inner.split("\n"))
            return f"\n\n{quoted}\n\n"
        return ""

    # Containers — just recurse
    return "".join(_tag_to_markdown(c, depth) for c in tag.children)


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


def _extract_main_content(html: str) -> str:
    """
    Extract the main content from a HubSpot docs page.

    HubSpot uses Tailwind utility classes (no semantic class names), so we
    can't select by class name. Instead we locate the h1 and walk 4 levels
    up to reach the content wrapper div, which holds all the API docs.
    """
    soup = BeautifulSoup(html, "html.parser")

    # Remove scripts, styles, noscript
    for tag in soup.find_all(["script", "style", "noscript"]):
        tag.decompose()

    # Find h1, walk 4 levels up to the content container
    h1 = soup.find("h1")
    if h1:
        content_el = h1
        for _ in range(4):
            if content_el.parent:
                content_el = content_el.parent
        text = content_el.get_text().strip()
        if len(text) >= MIN_CONTENT_LEN:
            return _CONVERTER.handle(str(content_el))

    # Fallback: body
    body = soup.find("body")
    if body:
        return _CONVERTER.handle(str(body))

    return ""


def html_to_markdown(html: str) -> str:
    """Convert a HubSpot docs page HTML to clean markdown."""
    content = _extract_main_content(html)

    content = re.sub(r"[ \t]+\n", "\n", content)
    content = re.sub(r"\n{4,}", "\n\n\n", content)
    content = re.sub(r"\[#\]\([^)]*\)", "", content)
    content = re.sub(r"\[¶\]\([^)]*\)", "", content)

    return content.strip()


def extract_title(html: str, url: str) -> str:
    """Extract page title from HTML."""
    soup = BeautifulSoup(html, "html.parser")

    h1 = soup.find("h1")
    if h1:
        return h1.get_text(" ", strip=True)

    title_tag = soup.find("title")
    if title_tag:
        title = title_tag.get_text(strip=True)
        # HubSpot pages: "Contacts | HubSpot API" or "Contacts | Developers"
        title = title.split("|")[0].strip()
        return title

    # Derive from URL path
    path = urlparse(url).path.rstrip("/")
    return path.split("/")[-1].replace("-", " ").title()


# ---------------------------------------------------------------------------
# URL -> filename
# ---------------------------------------------------------------------------

def url_to_filename(url: str) -> str:
    """
    Convert a HubSpot docs URL to a markdown filename.

    Naming: api_{last-2-path-segments-joined-with-underscore}.md

    Examples:
      /docs/api/crm/contacts           -> api_crm_contacts.md
      /docs/api/marketing/emails       -> api_marketing_emails.md
      /docs/api/overview               -> api_overview.md
    """
    path = urlparse(url).path.rstrip("/")
    # Strip /docs/api/ prefix
    path = re.sub(r"^/docs/api/?", "", path)

    if not path:
        return "api_index.md"

    parts = path.split("/")
    # Join last 2 parts (or all parts if only 1)
    if len(parts) >= 2:
        name = "_".join(parts[-2:])
    else:
        name = parts[0]

    name = re.sub(r"[^\w\-]", "_", name).strip("_")
    return f"api_{name}.md"


# ---------------------------------------------------------------------------
# Page scraper
# ---------------------------------------------------------------------------

def scrape_page(session: requests.Session, url: str) -> tuple[str, str] | None:
    """
    Fetch a single HubSpot docs page and return (title, markdown_content).
    Returns None on failure or if content is too short.
    """
    try:
        resp = session.get(url, timeout=(10, 60))
        if resp.status_code == 404:
            return None
        resp.raise_for_status()

        content_type = resp.headers.get("Content-Type", "")
        if "text/html" not in content_type:
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
    print("HubSpot API Documentation Scraper")
    print(f"Source: {BASE_URL}{DOCS_ROOT}")
    print("=" * 70)

    session = requests.Session()
    session.headers.update(HEADERS)

    # --- Discovery (BFS crawl) ---
    print("\nDiscovering pages via BFS crawl...")
    urls = discover_urls(session)
    print(f"Total pages to scrape: {len(urls)}")
    print("=" * 70)

    # Deduplicate while preserving order
    seen_files: dict[str, str] = {}  # filename -> url (track collisions)
    scraped_files = []
    skipped = []

    for i, url in enumerate(urls, 1):
        filename = url_to_filename(url)

        # Handle filename collisions: append index
        if filename in seen_files:
            base = filename.replace(".md", "")
            idx  = 2
            while f"{base}_{idx}.md" in seen_files:
                idx += 1
            filename = f"{base}_{idx}.md"

        label = url.replace(BASE_URL, "")
        print(f"[{i}/{len(urls)}] {label[:65]:<65}", end=" ", flush=True)

        result = scrape_page(session, url)
        time.sleep(DELAY)

        if not result:
            print("x skipped")
            skipped.append(url)
            continue

        title, content = result

        seen_files[filename] = url
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
        "source":       "HubSpot API Documentation (developers.hubspot.com)",
        "scraped_from": f"{BASE_URL}{DOCS_ROOT}",
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
