#!/usr/bin/env python3
"""
Google Workspace APIs Documentation Scraper

Scrapes human-written HTML reference docs for:
  - Google Docs API
  - Google Slides API
  - Google Drive API v3
  - Google Calendar API v3
  - Google Gmail API

All five APIs live on developers.google.com and share the same page structure
as the Sheets API, so the same discovery + extraction logic works for all.

Discovery strategy:
  - Fetch each API's reference index page, parse href links matching the
    API's reference path prefix.
  - Combine with a hardcoded seed list of known pages.
  - Filter to method-level pages (enough path segments).

Content strategy:
  - requests + BeautifulSoup (server-rendered, no JS needed).
  - Strip nav/header/footer/sidebar, find main content, convert to markdown.

Output:
  benchmark/datasets/google_docs/docs/
  benchmark/datasets/google_slides/docs/
  benchmark/datasets/google_drive/docs/
  benchmark/datasets/google_calendar/docs/
  benchmark/datasets/google_gmail/docs/

Usage:
    python3 benchmark/scripts/scrape_google_workspace_autodiscover.py
    python3 benchmark/scripts/scrape_google_workspace_autodiscover.py --apis docs slides
"""

import argparse
import json
import re
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup


# ---------------------------------------------------------------------------
# API definitions
# ---------------------------------------------------------------------------

APIS = {
    "docs": {
        "name":        "Google Docs API",
        "index_url":   "https://developers.google.com/docs/api/reference/rest",
        "path_prefix": "/docs/api/reference/rest",
        "output_dir":  "google_docs",
        "source_label": "Google Docs API (developers.google.com)",
        "seed_pages": [
            "https://developers.google.com/docs/api/reference/rest/v1/documents/get",
            "https://developers.google.com/docs/api/reference/rest/v1/documents/create",
            "https://developers.google.com/docs/api/reference/rest/v1/documents/batchUpdate",
        ],
    },
    "slides": {
        "name":        "Google Slides API",
        "index_url":   "https://developers.google.com/slides/api/reference/rest",
        "path_prefix": "/slides/api/reference/rest",
        "output_dir":  "google_slides",
        "source_label": "Google Slides API (developers.google.com)",
        "seed_pages": [
            "https://developers.google.com/slides/api/reference/rest/v1/presentations/get",
            "https://developers.google.com/slides/api/reference/rest/v1/presentations/create",
            "https://developers.google.com/slides/api/reference/rest/v1/presentations/batchUpdate",
            "https://developers.google.com/slides/api/reference/rest/v1/presentations.pages/get",
            "https://developers.google.com/slides/api/reference/rest/v1/presentations.pages/getThumbnail",
        ],
    },
    "drive": {
        "name":        "Google Drive API v3",
        "index_url":   "https://developers.google.com/drive/api/reference/rest/v3",
        "path_prefix": "/drive/api/reference/rest",
        "output_dir":  "google_drive",
        "source_label": "Google Drive API v3 (developers.google.com)",
        "seed_pages": [
            "https://developers.google.com/drive/api/reference/rest/v3/files/get",
            "https://developers.google.com/drive/api/reference/rest/v3/files/list",
            "https://developers.google.com/drive/api/reference/rest/v3/files/create",
            "https://developers.google.com/drive/api/reference/rest/v3/files/update",
            "https://developers.google.com/drive/api/reference/rest/v3/files/delete",
            "https://developers.google.com/drive/api/reference/rest/v3/files/copy",
            "https://developers.google.com/drive/api/reference/rest/v3/files/export",
            "https://developers.google.com/drive/api/reference/rest/v3/permissions/list",
            "https://developers.google.com/drive/api/reference/rest/v3/permissions/create",
            "https://developers.google.com/drive/api/reference/rest/v3/permissions/delete",
            "https://developers.google.com/drive/api/reference/rest/v3/comments/list",
            "https://developers.google.com/drive/api/reference/rest/v3/replies/list",
            "https://developers.google.com/drive/api/reference/rest/v3/drives/list",
            "https://developers.google.com/drive/api/reference/rest/v3/drives/get",
        ],
    },
    "calendar": {
        "name":        "Google Calendar API v3",
        "index_url":   "https://developers.google.com/calendar/api/v3/reference",
        "path_prefix": "/calendar/api/v3/reference",
        "output_dir":  "google_calendar",
        "source_label": "Google Calendar API v3 (developers.google.com)",
        "seed_pages": [
            "https://developers.google.com/calendar/api/v3/reference/events/list",
            "https://developers.google.com/calendar/api/v3/reference/events/get",
            "https://developers.google.com/calendar/api/v3/reference/events/insert",
            "https://developers.google.com/calendar/api/v3/reference/events/update",
            "https://developers.google.com/calendar/api/v3/reference/events/delete",
            "https://developers.google.com/calendar/api/v3/reference/events/patch",
            "https://developers.google.com/calendar/api/v3/reference/events/move",
            "https://developers.google.com/calendar/api/v3/reference/calendarList/list",
            "https://developers.google.com/calendar/api/v3/reference/calendarList/get",
            "https://developers.google.com/calendar/api/v3/reference/calendarList/insert",
            "https://developers.google.com/calendar/api/v3/reference/calendars/get",
            "https://developers.google.com/calendar/api/v3/reference/calendars/insert",
            "https://developers.google.com/calendar/api/v3/reference/calendars/update",
            "https://developers.google.com/calendar/api/v3/reference/calendars/delete",
            "https://developers.google.com/calendar/api/v3/reference/acl/list",
            "https://developers.google.com/calendar/api/v3/reference/acl/insert",
            "https://developers.google.com/calendar/api/v3/reference/acl/delete",
            "https://developers.google.com/calendar/api/v3/reference/freebusy/query",
            "https://developers.google.com/calendar/api/v3/reference/settings/list",
            "https://developers.google.com/calendar/api/v3/reference/settings/get",
        ],
    },
    "gmail": {
        "name":        "Gmail API",
        "index_url":   "https://developers.google.com/gmail/api/reference/rest",
        "path_prefix": "/gmail/api/reference/rest",
        "output_dir":  "google_gmail",
        "source_label": "Gmail API (developers.google.com)",
        "seed_pages": [
            "https://developers.google.com/gmail/api/reference/rest/v1/users.messages/list",
            "https://developers.google.com/gmail/api/reference/rest/v1/users.messages/get",
            "https://developers.google.com/gmail/api/reference/rest/v1/users.messages/send",
            "https://developers.google.com/gmail/api/reference/rest/v1/users.messages/insert",
            "https://developers.google.com/gmail/api/reference/rest/v1/users.messages/delete",
            "https://developers.google.com/gmail/api/reference/rest/v1/users.messages/modify",
            "https://developers.google.com/gmail/api/reference/rest/v1/users.messages/trash",
            "https://developers.google.com/gmail/api/reference/rest/v1/users.messages/untrash",
            "https://developers.google.com/gmail/api/reference/rest/v1/users.messages/batchDelete",
            "https://developers.google.com/gmail/api/reference/rest/v1/users.messages/batchModify",
            "https://developers.google.com/gmail/api/reference/rest/v1/users.messages.attachments/get",
            "https://developers.google.com/gmail/api/reference/rest/v1/users.drafts/list",
            "https://developers.google.com/gmail/api/reference/rest/v1/users.drafts/get",
            "https://developers.google.com/gmail/api/reference/rest/v1/users.drafts/create",
            "https://developers.google.com/gmail/api/reference/rest/v1/users.drafts/update",
            "https://developers.google.com/gmail/api/reference/rest/v1/users.drafts/delete",
            "https://developers.google.com/gmail/api/reference/rest/v1/users.drafts/send",
            "https://developers.google.com/gmail/api/reference/rest/v1/users.labels/list",
            "https://developers.google.com/gmail/api/reference/rest/v1/users.labels/get",
            "https://developers.google.com/gmail/api/reference/rest/v1/users.labels/create",
            "https://developers.google.com/gmail/api/reference/rest/v1/users.labels/update",
            "https://developers.google.com/gmail/api/reference/rest/v1/users.labels/delete",
            "https://developers.google.com/gmail/api/reference/rest/v1/users.threads/list",
            "https://developers.google.com/gmail/api/reference/rest/v1/users.threads/get",
            "https://developers.google.com/gmail/api/reference/rest/v1/users.threads/modify",
            "https://developers.google.com/gmail/api/reference/rest/v1/users.threads/trash",
            "https://developers.google.com/gmail/api/reference/rest/v1/users.threads/delete",
            "https://developers.google.com/gmail/api/reference/rest/v1/users/getProfile",
            "https://developers.google.com/gmail/api/reference/rest/v1/users.history/list",
            "https://developers.google.com/gmail/api/reference/rest/v1/users.settings/getAutoForwarding",
            "https://developers.google.com/gmail/api/reference/rest/v1/users.settings/getImap",
            "https://developers.google.com/gmail/api/reference/rest/v1/users.settings/getPop",
            "https://developers.google.com/gmail/api/reference/rest/v1/users.settings/getVacation",
            "https://developers.google.com/gmail/api/reference/rest/v1/users.settings/updateVacation",
        ],
    },
}

BASE_URL        = "https://developers.google.com"
DELAY           = 0.5
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

DATASETS_DIR = Path(__file__).parent.parent / "datasets"


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------

def discover_urls(session: requests.Session, api: dict) -> list[str]:
    index_url   = api["index_url"]
    path_prefix = api["path_prefix"]
    seed_pages  = api["seed_pages"]

    discovered: set[str] = set(seed_pages)

    print(f"  Fetching index: {index_url}")
    try:
        resp = session.get(index_url, timeout=(10, 30))
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        time.sleep(DELAY)

        for tag in soup.find_all("a", href=True):
            href = tag["href"]
            if href.startswith("/"):
                href = BASE_URL + href
            elif not href.startswith("http"):
                href = urljoin(index_url, href)

            parsed = urlparse(href)
            if (
                parsed.netloc == "developers.google.com"
                and parsed.path.startswith(path_prefix)
                and not parsed.fragment
            ):
                clean = f"https://{parsed.netloc}{parsed.path.rstrip('/')}"
                discovered.add(clean)

        print(f"  Found {len(discovered)} URLs after index parse")
    except Exception as e:
        print(f"  WARNING: could not fetch index: {e}")

    # Keep only method-level pages (enough path depth)
    filtered = []
    for url in sorted(discovered):
        parts = urlparse(url).path.strip("/").split("/")
        if len(parts) >= 5:
            filtered.append(url)

    # Always include seeds
    for url in seed_pages:
        if url not in filtered:
            filtered.append(url)

    return sorted(set(filtered))


# ---------------------------------------------------------------------------
# HTML -> Markdown
# ---------------------------------------------------------------------------

def _tag_to_markdown(tag, depth: int = 0) -> str:
    if tag is None:
        return ""
    if isinstance(tag, str):
        return tag

    name = getattr(tag, "name", None)
    if name is None:
        return tag.get_text()

    if name in ("h1", "h2", "h3", "h4", "h5", "h6"):
        level = int(name[1])
        text = tag.get_text(" ", strip=True)
        return f"\n\n{'#' * level} {text}\n\n"

    if name == "p":
        children = "".join(_tag_to_markdown(c, depth) for c in tag.children)
        return f"\n\n{children.strip()}\n\n"

    if name == "code":
        return f"`{tag.get_text()}`"

    if name == "pre":
        return f"\n\n```\n{tag.get_text()}\n```\n\n"

    if name in ("strong", "b"):
        return f"**{tag.get_text(' ', strip=True)}**"

    if name in ("em", "i"):
        return f"*{tag.get_text(' ', strip=True)}*"

    if name == "ul":
        items = []
        for li in tag.find_all("li", recursive=False):
            item_text = "".join(_tag_to_markdown(c, depth + 1) for c in li.children).strip()
            items.append(f"- {item_text}")
        return "\n" + "\n".join(items) + "\n"

    if name == "ol":
        items = []
        for idx, li in enumerate(tag.find_all("li", recursive=False), 1):
            item_text = "".join(_tag_to_markdown(c, depth + 1) for c in li.children).strip()
            items.append(f"{idx}. {item_text}")
        return "\n" + "\n".join(items) + "\n"

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

    if name == "a":
        text = tag.get_text(" ", strip=True)
        href = tag.get("href", "")
        if href and not href.startswith("#"):
            return f"[{text}]({href})"
        return text

    if name == "hr":
        return "\n\n---\n\n"

    if name == "blockquote":
        inner = "".join(_tag_to_markdown(c, depth) for c in tag.children).strip()
        quoted = "\n".join(f"> {line}" for line in inner.split("\n"))
        return f"\n\n{quoted}\n\n"

    if name in ("div", "section", "article", "main", "span"):
        return "".join(_tag_to_markdown(c, depth) for c in tag.children)

    return "".join(_tag_to_markdown(c, depth) for c in tag.children)


def extract_main_content(html: str) -> str | None:
    soup = BeautifulSoup(html, "html.parser")

    for selector in [
        "nav", "header", "footer", "script", "style",
        "[class*='devsite-nav']", "[class*='devsite-header']",
        "[class*='devsite-footer']", "[class*='devsite-sidebar']",
        "[class*='devsite-toc']", "[class*='devsite-banner']",
        "[class*='devsite-snackbar']", "[class*='nocontent']",
        "[role='navigation']", "[role='complementary']",
        ".devsite-article-meta", ".devsite-feedback",
        ".devsite-page-rating", ".devsite-breadcrumb",
        ".l-grid--nav-offset",
        ".devsite-bookmark", "[class*='bookmark']",
        "[class*='save-favorite']",
    ]:
        for el in soup.select(selector):
            el.decompose()

    for selector in [
        "devsite-content",
        "article.devsite-article",
        "[class*='devsite-article']",
        "article",
        "[role='main']",
        "main",
    ]:
        el = soup.select_one(selector)
        if el:
            return el

    body = soup.find("body")
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
    content_el = extract_main_content(html)
    if content_el is None:
        return ""

    md = _tag_to_markdown(content_el)
    md = re.sub(r"[ \t]+\n", "\n", md)
    md = re.sub(r"\n{4,}", "\n\n\n", md)
    md = re.sub(r"\[#\]\([^)]*\)", "", md)
    md = re.sub(r"\[¶\]\([^)]*\)", "", md)
    return md.strip()


def extract_title(html: str, url: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    title_tag = soup.find("title")
    if title_tag:
        title = title_tag.get_text(strip=True).split("|")[0].strip()
        if title:
            return title
    h1 = soup.find("h1")
    if h1:
        return h1.get_text(" ", strip=True).split("\n")[0].strip()
    return url.rstrip("/").split("/")[-1]


# ---------------------------------------------------------------------------
# URL -> filename
# ---------------------------------------------------------------------------

def url_to_filename(url: str, path_prefix: str) -> str:
    path = urlparse(url).path.rstrip("/")
    # Strip up to and including the prefix
    # e.g. /gmail/api/reference/rest/v1/users.messages/list -> users.messages_list
    # or   /calendar/api/v3/reference/events/list          -> events_list
    prefix_stripped = re.sub(r"^" + re.escape(path_prefix) + r"/?", "", path)
    parts = prefix_stripped.strip("/").split("/")

    # Skip version segment (v1, v2, v3, v4) if present
    if parts and re.match(r"^v\d+$", parts[0]):
        parts = parts[1:]

    if len(parts) >= 2:
        name = f"{parts[-2]}_{parts[-1]}"
    elif parts:
        name = parts[0]
    else:
        name = "index"

    name = re.sub(r"[^\w.\-]", "_", name).strip("_")
    return f"api_{name}.md"


# ---------------------------------------------------------------------------
# Page scraper
# ---------------------------------------------------------------------------

def scrape_page(session: requests.Session, url: str) -> tuple[str, str] | None:
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
# Scrape one API
# ---------------------------------------------------------------------------

def scrape_api(session: requests.Session, api_key: str, api: dict):
    output_dir = DATASETS_DIR / api["output_dir"] / "docs"

    if output_dir.exists():
        backup = output_dir.parent / f"docs_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        print(f"  Backing up existing docs -> {backup.name}")
        output_dir.rename(backup)
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"\nDiscovering pages...")
    urls = discover_urls(session, api)
    print(f"Total pages to scrape: {len(urls)}")
    print("-" * 60)

    scraped_files = []
    skipped = []
    seen_filenames: set[str] = set()

    for i, url in enumerate(urls, 1):
        filename = url_to_filename(url, api["path_prefix"])

        # Handle collisions
        if filename in seen_filenames:
            base = filename[:-3]
            idx = 2
            while f"{base}_{idx}.md" in seen_filenames:
                idx += 1
            filename = f"{base}_{idx}.md"
        seen_filenames.add(filename)

        label = url.replace(BASE_URL, "")
        print(f"  [{i}/{len(urls)}] {label[:60]:<60}", end=" ", flush=True)

        result = scrape_page(session, url)
        time.sleep(DELAY)

        if not result:
            print("x skipped")
            skipped.append(url)
            continue

        title, content = result

        filepath = output_dir / filename
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

    print(f"\n  Scraped: {len(scraped_files)}  Skipped: {len(skipped)}")

    manifest = {
        "source":       api["source_label"],
        "scraped_from": api["index_url"],
        "scrape_date":  datetime.now().isoformat(),
        "total_pages":  len(scraped_files),
        "files":        scraped_files,
    }
    manifest_path = output_dir / "_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"  Output: {output_dir}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Scrape Google Workspace API docs")
    parser.add_argument(
        "--apis",
        nargs="+",
        choices=list(APIS.keys()),
        default=list(APIS.keys()),
        help="Which APIs to scrape (default: all)",
    )
    args = parser.parse_args()

    session = requests.Session()
    session.headers.update(HEADERS)

    for api_key in args.apis:
        api = APIS[api_key]
        print("=" * 70)
        print(f"{api['name']}")
        print("=" * 70)
        scrape_api(session, api_key, api)

    print("\n" + "=" * 70)
    print("Done.")
    print("=" * 70)


if __name__ == "__main__":
    main()
