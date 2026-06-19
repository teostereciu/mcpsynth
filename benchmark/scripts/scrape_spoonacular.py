#!/usr/bin/env python3
"""
Spoonacular Food API Documentation Scraper

Fetches the single static HTML page at spoonacular.com/food-api/docs
and splits it by section anchor into per-section markdown files.

Usage:
    python3 benchmark/scripts/scrape_spoonacular.py
"""

import json
import re
import time
from datetime import datetime
from pathlib import Path

import html2text
import requests
from bs4 import BeautifulSoup

OUTPUT_DIR = Path(__file__).parent.parent / "datasets" / "spoonacular" / "docs"
DOCS_URL = "https://spoonacular.com/food-api/docs"
DELAY = 1.0

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
    "Accept": "text/html,application/xhtml+xml",
}

# Section anchor IDs on the page
SECTIONS = [
    ("Recipes", "Recipes"),
    ("Ingredients", "Ingredients"),
    ("Products", "Products"),
    ("Menu-Items", "Menu Items"),
    ("Meal-Planning", "Meal Planning"),
    ("Wine", "Wine"),
    ("Misc", "Misc"),
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
    print("Spoonacular Food API Documentation Scraper")
    print(f"Source: {DOCS_URL}")
    print("=" * 60)

    session = requests.Session()
    session.headers.update(HEADERS)

    print("Fetching docs page...", flush=True)
    resp = session.get(DOCS_URL, timeout=(10, 60))
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    for tag in soup.find_all(["script", "style", "noscript"]):
        tag.decompose()

    scraped_files = []

    import re as _re
    from collections import defaultdict
    from bs4 import Comment

    # Parse the sidebar to build section -> [endpoint_name] mapping.
    # Each section h4 is followed by <a> tags with v-on:click="show('Endpoint Name')"
    # (some are in HTML comments for Vue, some are rendered as real <a> tags).
    aside = soup.find("aside")
    section_endpoint_names: dict[str, list[str]] = defaultdict(list)
    current_section = None
    show_re = _re.compile(r"show\('([^']+)'\)")

    if aside:
        for node in aside.descendants:
            if hasattr(node, "name") and node.name == "h4":
                t = node.get_text(strip=True)
                if any(t == title for _, title in SECTIONS):
                    current_section = t
            elif current_section:
                text = str(node)
                for match in show_re.findall(text):
                    if match not in section_endpoint_names[current_section]:
                        section_endpoint_names[current_section].append(match)

    # Build mapping from endpoint name -> h2 block HTML
    all_h2s = soup.find_all("h2")
    h2_by_name: dict[str, str] = {}
    for h2 in all_h2s:
        name = h2.get_text(strip=True)
        parts = [str(h2)]
        for sibling in h2.find_next_siblings():
            if sibling.name == "h2":
                break
            parts.append(str(sibling))
        h2_by_name[name] = "".join(parts)

    for anchor_id, title in SECTIONS:
        filename = f"api_{anchor_id.lower().replace('-', '_')}.md"
        print(f"  {title:<25}", end=" ", flush=True)

        ep_names = section_endpoint_names.get(title, [])
        blocks = [h2_by_name[n] for n in ep_names if n in h2_by_name]
        if not blocks:
            print("x not found")
            continue

        combined_html = "\n".join(blocks)
        md = _CONVERTER.handle(combined_html)
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
        "source": "Spoonacular Food API (spoonacular.com/food-api/docs)",
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
