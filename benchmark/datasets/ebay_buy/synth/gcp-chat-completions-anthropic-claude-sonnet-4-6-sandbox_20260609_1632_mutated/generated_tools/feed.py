"""
eBay Buy Feed API tools.
Covers: item feed, item group feed, item priority feed, item snapshot feed.
All feed methods return TSV_GZIP binary content (or error JSON).
Use the Range header to stream large files in chunks.
"""

from __future__ import annotations
from typing import Optional
from .auth import get_auth_header, get_base_url


def get_item_feed(
    feed_scope: str,
    category_id: str,
    date: Optional[str] = None,
    range_header: Optional[str] = None,
    marketplace_id: str = "EBAY_US",
) -> dict:
    """
    Download a TSV_GZIP Item feed file for a specific category and marketplace.
    Returns newly listed items (daily) or all active items (weekly bootstrap).

    Args:
        feed_scope: Type of feed file to return:
            - 'NEWLY_LISTED': Daily feed of newly listed items (requires date).
            - 'ALL_ACTIVE': Weekly bootstrap of all active items.
        category_id: eBay top-level category ID (e.g. '625' for Cameras & Photo).
            Must be a top-level category (not Real Estate).
        date: Date of the daily feed file in 'yyyyMMdd' format (e.g. '20230718').
            Required for NEWLY_LISTED. Must be 3-14 days in the past.
            Ignored for ALL_ACTIVE (latest file is returned).
        range_header: Byte range for chunked download (e.g. 'bytes=0-10485760').
            Required for files > 100 MB. Max chunk size: 100 MB.
        marketplace_id: eBay marketplace ID (default EBAY_US).

    Returns:
        Dict with 'content_type', 'content_range', 'content' (bytes as hex string)
        on success, or {'error': ...} on failure.
    """
    import requests
    params = {
        "feed_scope": feed_scope,
        "category_id": category_id,
    }
    if date:
        params["date"] = date

    url = f"{get_base_url()}/buy/feed/v1_beta/item"
    headers = get_auth_header()
    headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    headers["Accept"] = "application/json,text/tab-separated-values"
    if range_header:
        headers["Range"] = range_header

    try:
        resp = requests.get(url, headers=headers, params=params, timeout=60)
        if resp.status_code in (200, 206):
            return {
                "status_code": resp.status_code,
                "content_type": resp.headers.get("Content-Type", ""),
                "content_range": resp.headers.get("Content-Range", ""),
                "last_modified": resp.headers.get("Last-Modified", ""),
                "content_length": len(resp.content),
                "note": "Feed file returned as binary TSV_GZIP. Use range_header to stream chunks.",
            }
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def get_item_group_feed(
    feed_scope: str,
    category_id: str,
    date: Optional[str] = None,
    range_header: Optional[str] = None,
    marketplace_id: str = "EBAY_US",
) -> dict:
    """
    Download a TSV_GZIP Item Group feed file for a specific category.
    Contains item group (parent item) variation information.
    Combine with the Item feed using primaryItemGroupId -> itemGroupId.

    Args:
        feed_scope: Type of feed file:
            - 'NEWLY_LISTED': Daily item group feed (requires date).
            - 'ALL_ACTIVE': Weekly bootstrap item group feed.
        category_id: eBay top-level category ID. Must not be Real Estate.
        date: Date in 'yyyyMMdd' format. Required for NEWLY_LISTED.
            Must be 3-14 days in the past.
        range_header: Byte range for chunked download (e.g. 'bytes=0-10485760').
        marketplace_id: eBay marketplace ID (default EBAY_US).

    Returns:
        Dict with metadata about the feed file, or {'error': ...} on failure.
    """
    import requests
    params = {
        "feed_scope": feed_scope,
        "category_id": category_id,
    }
    if date:
        params["date"] = date

    url = f"{get_base_url()}/buy/feed/v1_beta/item_group"
    headers = get_auth_header()
    headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    headers["Accept"] = "application/json,text/tab-separated-values"
    if range_header:
        headers["Range"] = range_header

    try:
        resp = requests.get(url, headers=headers, params=params, timeout=60)
        if resp.status_code in (200, 206):
            return {
                "status_code": resp.status_code,
                "content_type": resp.headers.get("Content-Type", ""),
                "content_range": resp.headers.get("Content-Range", ""),
                "last_modified": resp.headers.get("Last-Modified", ""),
                "content_length": len(resp.content),
                "note": "Feed file returned as binary TSV_GZIP. Use range_header to stream chunks.",
            }
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def get_item_priority_feed(
    category_id: str,
    date: str,
    range_header: Optional[str] = None,
    marketplace_id: str = "EBAY_US",
) -> dict:
    """
    Download a TSV_GZIP Item Priority feed file tracking changes to priority
    (promoted) listings for a specific category and date.
    Tracks ADDED_TO_CAMPAIGN, REMOVED_FROM_CAMPAIGN, TRACKING_PAYLOAD_REFRESHED.
    Must consume daily Item and Item Group feeds before this feed.

    Args:
        category_id: eBay top-level category ID (e.g. '625' for Cameras & Photo).
        date: Date of the feed in 'yyyyMMdd' format. Up to 14 days in the past.
            Files available after 9AM MST with 48-hour latency.
        range_header: Byte range for chunked download (e.g. 'bytes=0-10485760').
            Required for large files.
        marketplace_id: eBay marketplace ID (default EBAY_US).

    Returns:
        Dict with metadata about the feed file, or {'error': ...} on failure.
    """
    import requests
    params = {
        "category_id": category_id,
        "date": date,
    }

    url = f"{get_base_url()}/buy/feed/v1_beta/item_priority"
    headers = get_auth_header()
    headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    headers["Accept"] = "application/json,text/tab-separated-values"
    if range_header:
        headers["Range"] = range_header
    else:
        headers["Range"] = "bytes=0-10485760"  # default first 10MB

    try:
        resp = requests.get(url, headers=headers, params=params, timeout=60)
        if resp.status_code in (200, 206):
            return {
                "status_code": resp.status_code,
                "content_type": resp.headers.get("Content-Type", ""),
                "content_range": resp.headers.get("Content-Range", ""),
                "last_modified": resp.headers.get("Last-Modified", ""),
                "content_length": len(resp.content),
                "note": "Feed file returned as binary TSV_GZIP. Use range_header to stream chunks.",
            }
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def get_item_snapshot_feed(
    category_id: str,
    snapshot_date: str,
    range_header: Optional[str] = None,
    marketplace_id: str = "EBAY_US",
) -> dict:
    """
    Download a TSV_GZIP Hourly Snapshot feed file of items that changed within
    a specific hour for a category. Use to track price, availability, and other
    changes to items in your database.

    Args:
        category_id: eBay top-level category ID (e.g. '625' for Cameras & Photo).
        snapshot_date: UTC datetime for the snapshot hour in ISO 8601 format
            (e.g. '2023-07-18T08:00:00.000Z'). The file for 8AM is available
            at 10AM. Convert local time to GMT.
        range_header: Byte range for chunked download (e.g. 'bytes=0-10485760').
        marketplace_id: eBay marketplace ID (default EBAY_US).

    Returns:
        Dict with metadata about the feed file, or {'error': ...} on failure.
    """
    import requests
    params = {
        "category_id": category_id,
        "snapshot_date": snapshot_date,
    }

    url = f"{get_base_url()}/buy/feed/v1_beta/item_snapshot"
    headers = get_auth_header()
    headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    headers["Accept"] = "application/json,text/tab-separated-values"
    if range_header:
        headers["Range"] = range_header
    else:
        headers["Range"] = "bytes=0-10485760"  # default first 10MB

    try:
        resp = requests.get(url, headers=headers, params=params, timeout=60)
        if resp.status_code in (200, 206):
            return {
                "status_code": resp.status_code,
                "content_type": resp.headers.get("Content-Type", ""),
                "content_range": resp.headers.get("Content-Range", ""),
                "last_modified": resp.headers.get("Last-Modified", ""),
                "content_length": len(resp.content),
                "note": "Feed file returned as binary TSV_GZIP. Use range_header to stream chunks.",
            }
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}
