#!/usr/bin/env python3
"""
Alpha Vantage API Documentation Scraper

Fetches the single static page at alphavantage.co/documentation/
and splits it by top-level section anchor into per-section markdown files.

Usage:
    python3 benchmark/scripts/scrape_alphavantage.py
"""

import json
import re
from datetime import datetime
from pathlib import Path

import html2text
import requests
from bs4 import BeautifulSoup

OUTPUT_DIR = Path(__file__).parent.parent / "datasets" / "alphavantage" / "docs"
DOCS_URL = "https://www.alphavantage.co/documentation/"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
    "Accept": "text/html,application/xhtml+xml",
}

# Top-level section anchors and friendly titles
SECTIONS = [
    ("time-series-data", "Stock Time Series"),
    ("fundamentals", "Fundamental Data"),
    ("options", "Options Data"),
    ("intelligence", "Alpha Intelligence"),
    ("fx", "Forex / FX"),
    ("digital-currency", "Digital / Crypto Currency"),
    ("commodities", "Commodities"),
    ("economic-indicators", "Economic Indicators"),
    ("technical-indicators", "Technical Indicators"),
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


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("Alpha Vantage API Documentation Scraper")
    print(f"Source: {DOCS_URL}")
    print("=" * 60)

    session = requests.Session()
    session.headers.update(HEADERS)

    print("Fetching docs page...", flush=True)
    resp = session.get(DOCS_URL, timeout=(10, 60))
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    for tag in soup.find_all(["script", "style", "noscript", "nav", "footer"]):
        tag.decompose()

    scraped_files = []

    for anchor_id, title in SECTIONS:
        filename = f"api_{anchor_id.replace('-', '_')}.md"
        print(f"  {title:<35}", end=" ", flush=True)

        section_tag = (
            soup.find(id=anchor_id)
            or soup.find(attrs={"name": anchor_id})
        )
        if not section_tag:
            print("x not found")
            continue

        # Collect content until the next top-level section
        parts = [str(section_tag)]
        for sibling in section_tag.find_next_siblings():
            # Stop at next h2 that has an id matching a known section
            if sibling.name == "h2" and sibling.get("id") in [s[0] for s in SECTIONS]:
                break
            parts.append(str(sibling))

        md = _CONVERTER.handle("".join(parts))
        md = _clean(md)

        url = f"{DOCS_URL}#{anchor_id}"
        filepath = OUTPUT_DIR / filename
        filepath.write_text(
            f"# {title}\n\n*Source: {url}*\n\n---\n\n{md}",
            encoding="utf-8",
        )
        print(f"({md.count(chr(10))} lines)")
        scraped_files.append({"filename": filename, "title": title, "url": url})

    manifest = {
        "source": "Alpha Vantage API (alphavantage.co/documentation)",
        "scraped_from": DOCS_URL,
        "scrape_date": datetime.now().isoformat(),
        "total_pages": len(scraped_files),
        "files": scraped_files,
    }
    (OUTPUT_DIR / "_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    print(f"\nScraped: {len(scraped_files)}/{len(SECTIONS)}")
    print(f"Output:  {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
