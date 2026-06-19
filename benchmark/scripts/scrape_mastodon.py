#!/usr/bin/env python3
"""
Mastodon REST API Documentation Scraper

Fetches static HTML pages from docs.joinmastodon.org/methods/{resource}/
and converts to markdown. No JavaScript required.

Usage:
    python3 benchmark/scripts/scrape_mastodon.py
"""

import json
import re
import time
from datetime import datetime
from pathlib import Path

import html2text
import requests
from bs4 import BeautifulSoup

OUTPUT_DIR = Path(__file__).parent.parent / "datasets" / "mastodon" / "docs"
BASE_URL = "https://docs.joinmastodon.org"
DELAY = 0.5

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
    "Accept": "text/html,application/xhtml+xml",
}

# All method pages (skip admin and rarely-used endpoints)
METHODS = [
    "accounts", "blocks", "bookmarks", "domain_blocks", "endorsements",
    "favourites", "featured_tags", "filters", "follow_requests", "followed_tags",
    "mutes", "preferences", "reports", "suggestions", "tags", "profile",
    "statuses", "media", "polls", "scheduled_statuses",
    "timelines", "conversations", "lists", "markers", "streaming",
    "notifications", "push",
    "apps", "oauth",
    "instance", "announcements", "custom_emojis", "directory", "trends", "search",
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
    md = re.sub(r"\[¶\]\([^)]*\)", "", md)
    return md.strip()


def scrape_method(session, method: str):
    url = f"{BASE_URL}/methods/{method}/"
    try:
        resp = session.get(url, timeout=(10, 30))
        if resp.status_code == 404:
            return None
        resp.raise_for_status()
    except Exception as e:
        print(f"  ERROR: {e}")
        return None

    soup = BeautifulSoup(resp.text, "html.parser")
    for tag in soup.find_all(["script", "style", "noscript", "nav", "header", "footer"]):
        tag.decompose()

    title = method.replace("_", " ").title()
    h1 = soup.find("h1")
    if h1:
        title = h1.get_text(" ", strip=True)

    # Main content area
    article = soup.find("article") or soup.find("main") or soup.find("body")
    if not article:
        return None

    md = _CONVERTER.handle(str(article))
    md = _clean(md)
    if len(md) < 100:
        return None

    return title, md, url


def main():
    if OUTPUT_DIR.exists() and any(OUTPUT_DIR.glob("api_*.md")):
        backup = OUTPUT_DIR.parent / f"docs_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        print(f"Backing up existing docs -> {backup.name}")
        OUTPUT_DIR.rename(backup)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("Mastodon API Documentation Scraper")
    print(f"Source: {BASE_URL}/methods/")
    print("=" * 60)

    session = requests.Session()
    session.headers.update(HEADERS)

    scraped_files = []

    for i, method in enumerate(METHODS, 1):
        filename = f"api_{method}.md"
        print(f"[{i}/{len(METHODS)}] {method:<35}", end=" ", flush=True)

        result = scrape_method(session, method)
        time.sleep(DELAY)

        if not result:
            print("x skipped")
            continue

        title, content, url = result
        filepath = OUTPUT_DIR / filename
        filepath.write_text(
            f"# {title}\n\n*Source: {url}*\n\n---\n\n{content}",
            encoding="utf-8",
        )
        print(f"({content.count(chr(10))} lines)")

        scraped_files.append({"filename": filename, "title": title, "url": url})

    manifest = {
        "source": "Mastodon API (docs.joinmastodon.org)",
        "scraped_from": f"{BASE_URL}/methods/",
        "scrape_date": datetime.now().isoformat(),
        "total_pages": len(scraped_files),
        "files": scraped_files,
    }
    (OUTPUT_DIR / "_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    print(f"\nScraped: {len(scraped_files)}/{len(METHODS)}")
    print(f"Output:  {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
