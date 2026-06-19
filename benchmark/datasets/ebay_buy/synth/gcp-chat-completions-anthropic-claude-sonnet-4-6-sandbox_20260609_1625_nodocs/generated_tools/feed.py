"""
eBay Buy Feed API tools.
Covers: getItemFeed, getItemGroupFeed, getItemSnapshotFeed,
        getFile (feed file metadata), getFiles (list feed files),
        getAccess (feed access entitlements).
"""

from mcp.server.fastmcp import FastMCP
from .auth import api_get, auth_headers, get_base_url
import requests

mcp = FastMCP("ebay-feed")

FEED_BASE = "/buy/feed/v1_beta"
FEED_V1 = "/buy/feed/v1"


def _get_feed_bytes(path: str, params: dict, byte_range: str = "") -> dict:
    """
    Internal helper: download a feed file (or chunk) and return metadata.
    Feed files are gzip-compressed TSV; we return info rather than raw bytes.
    """
    url = get_base_url() + path
    headers = auth_headers()
    if byte_range:
        headers["Range"] = f"bytes={byte_range}"
    try:
        resp = requests.get(url, headers=headers, params=params, timeout=120, stream=True)
        if not resp.ok:
            return {"error": resp.text, "status_code": resp.status_code}
        content_range = resp.headers.get("Content-Range", "")
        content_length = resp.headers.get("Content-Length", "")
        last_modified = resp.headers.get("Last-Modified", "")
        return {
            "status_code": resp.status_code,
            "content_range": content_range,
            "content_length": content_length,
            "last_modified": last_modified,
            "note": (
                "Feed file is a gzip-compressed TSV. "
                "Use byte_range parameter to download in chunks. "
                "Full content not returned inline."
            ),
        }
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Item Feed
# ---------------------------------------------------------------------------

@mcp.tool()
def get_item_feed(
    feed_scope: str,
    category_id: str,
    date: str,
    marketplace_id: str = "EBAY_US",
    byte_range: str = "",
) -> dict:
    """
    Retrieve metadata/chunk info for an eBay item feed file.

    Feed files contain all active listings for a category on a given date.
    Files are large gzip-compressed TSVs; use byte_range to download in chunks.

    Args:
        feed_scope: Feed type — 'ALL_ACTIVE' (full) or 'NEWLY_LISTED' (daily delta).
        category_id: The leaf category ID for the feed.
        date: Date of the feed in UTC format 'YYYYMMDD' (e.g. '20240101').
              Required for NEWLY_LISTED; for ALL_ACTIVE use the most recent Sunday.
        marketplace_id: eBay marketplace (default 'EBAY_US').
        byte_range: Byte range for chunked download (e.g. '0-99999999').
    Returns:
        dict with feed file metadata and download info.
    """
    params = {
        "feed_scope": feed_scope,
        "category_id": category_id,
        "date": date,
    }
    headers_extra = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    url = get_base_url() + f"{FEED_BASE}/item"
    try:
        import requests as req
        h = auth_headers(headers_extra)
        if byte_range:
            h["Range"] = f"bytes={byte_range}"
        resp = req.get(url, headers=h, params=params, timeout=120, stream=True)
        if not resp.ok:
            return {"error": resp.text, "status_code": resp.status_code}
        return {
            "status_code": resp.status_code,
            "content_range": resp.headers.get("Content-Range", ""),
            "content_length": resp.headers.get("Content-Length", ""),
            "last_modified": resp.headers.get("Last-Modified", ""),
            "feed_scope": feed_scope,
            "category_id": category_id,
            "date": date,
            "note": "Feed is a gzip-compressed TSV. Download in chunks using byte_range.",
        }
    except Exception as exc:
        return {"error": str(exc)}


@mcp.tool()
def get_item_group_feed(
    feed_scope: str,
    category_id: str,
    date: str,
    marketplace_id: str = "EBAY_US",
    byte_range: str = "",
) -> dict:
    """
    Retrieve metadata/chunk info for an eBay item group feed file.

    Item group feeds contain multi-variation listing group data.

    Args:
        feed_scope: Feed type — 'ALL_ACTIVE' or 'NEWLY_LISTED'.
        category_id: The leaf category ID for the feed.
        date: Date of the feed in UTC format 'YYYYMMDD'.
        marketplace_id: eBay marketplace (default 'EBAY_US').
        byte_range: Byte range for chunked download (e.g. '0-99999999').
    Returns:
        dict with feed file metadata and download info.
    """
    params = {
        "feed_scope": feed_scope,
        "category_id": category_id,
        "date": date,
    }
    url = get_base_url() + f"{FEED_BASE}/item_group"
    try:
        import requests as req
        h = auth_headers({"X-EBAY-C-MARKETPLACE-ID": marketplace_id})
        if byte_range:
            h["Range"] = f"bytes={byte_range}"
        resp = req.get(url, headers=h, params=params, timeout=120, stream=True)
        if not resp.ok:
            return {"error": resp.text, "status_code": resp.status_code}
        return {
            "status_code": resp.status_code,
            "content_range": resp.headers.get("Content-Range", ""),
            "content_length": resp.headers.get("Content-Length", ""),
            "last_modified": resp.headers.get("Last-Modified", ""),
            "feed_scope": feed_scope,
            "category_id": category_id,
            "date": date,
            "note": "Feed is a gzip-compressed TSV. Download in chunks using byte_range.",
        }
    except Exception as exc:
        return {"error": str(exc)}


@mcp.tool()
def get_item_snapshot_feed(
    category_id: str,
    snapshot_date: str,
    marketplace_id: str = "EBAY_US",
    byte_range: str = "",
) -> dict:
    """
    Retrieve metadata/chunk info for an eBay item snapshot feed.

    Snapshot feeds contain items whose details changed within a one-hour window.

    Args:
        category_id: The leaf category ID for the feed.
        snapshot_date: Snapshot hour in ISO 8601 format
                       (e.g. '2024-01-01T10:00:00.000Z').
        marketplace_id: eBay marketplace (default 'EBAY_US').
        byte_range: Byte range for chunked download (e.g. '0-99999999').
    Returns:
        dict with feed file metadata and download info.
    """
    params = {
        "category_id": category_id,
        "snapshot_date": snapshot_date,
    }
    url = get_base_url() + f"{FEED_BASE}/item_snapshot"
    try:
        import requests as req
        h = auth_headers({"X-EBAY-C-MARKETPLACE-ID": marketplace_id})
        if byte_range:
            h["Range"] = f"bytes={byte_range}"
        resp = req.get(url, headers=h, params=params, timeout=120, stream=True)
        if not resp.ok:
            return {"error": resp.text, "status_code": resp.status_code}
        return {
            "status_code": resp.status_code,
            "content_range": resp.headers.get("Content-Range", ""),
            "content_length": resp.headers.get("Content-Length", ""),
            "last_modified": resp.headers.get("Last-Modified", ""),
            "category_id": category_id,
            "snapshot_date": snapshot_date,
            "note": "Snapshot feed is a gzip-compressed TSV. Download in chunks using byte_range.",
        }
    except Exception as exc:
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Feed File Catalog (v1)
# ---------------------------------------------------------------------------

@mcp.tool()
def get_feed_files(
    feed_scope: str = "",
    category_id: str = "",
    marketplace_id: str = "EBAY_US",
    feed_type_id: str = "",
    limit: int = 20,
    offset: int = 0,
) -> dict:
    """
    List available eBay feed files with optional filtering.

    Args:
        feed_scope: Filter by scope ('ALL_ACTIVE', 'NEWLY_LISTED', 'RECENTLY_SOLD').
        category_id: Filter by category ID.
        marketplace_id: eBay marketplace (default 'EBAY_US').
        feed_type_id: Filter by feed type ID.
        limit: Number of results per page.
        offset: Pagination offset.
    Returns:
        dict with feedFiles list and pagination metadata.
    """
    params: dict = {
        "limit": limit,
        "offset": offset,
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
    }
    if feed_scope:
        params["feed_scope"] = feed_scope
    if category_id:
        params["category_id"] = category_id
    if feed_type_id:
        params["feed_type_id"] = feed_type_id
    return api_get(f"{FEED_V1}/file", params=params)


@mcp.tool()
def get_feed_file(file_id: str) -> dict:
    """
    Retrieve metadata for a specific eBay feed file by its file ID.

    Args:
        file_id: The unique feed file ID.
    Returns:
        dict with feed file metadata including size, dates, and download info.
    """
    return api_get(f"{FEED_V1}/file/{file_id}")


@mcp.tool()
def get_feed_access() -> dict:
    """
    Retrieve the feed access entitlements for the current application.

    Returns:
        dict listing which feed types and categories the app is entitled to access.
    """
    return api_get(f"{FEED_V1}/access")
