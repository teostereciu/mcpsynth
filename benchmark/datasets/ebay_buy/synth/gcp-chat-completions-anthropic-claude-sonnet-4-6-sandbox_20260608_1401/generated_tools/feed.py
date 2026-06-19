"""
eBay Buy Feed API tools.
Covers: item feed, item group feed, item priority feed, item snapshot feed.

Note: Feed endpoints return TSV_GZIP binary data. These tools return the raw
bytes as a base64-encoded string in a dict, along with response headers.
Large files must be streamed in chunks using the byte_range parameter.
"""
from typing import Optional
import base64
from . import _client as client


def get_item_feed(
    feed_scope: str,
    category_id: str,
    marketplace_id: str,
    date: Optional[str] = None,
    byte_range: Optional[str] = None,
) -> dict:
    """Download a TSV_GZIP item feed file for a category and marketplace.

    Returns newly listed items (daily) or all active items (weekly bootstrap).
    The response is a gzip-compressed TSV file returned as base64-encoded content.

    Args:
        feed_scope: Type of feed file. Values:
            - 'NEWLY_LISTED': Daily feed of newly listed items (requires date).
            - 'ALL_ACTIVE': Weekly bootstrap of all active items.
        category_id: Top-level eBay category ID (e.g. '625' for Cameras & Photo).
            Must not be Real Estate.
        marketplace_id: eBay marketplace ID (e.g. 'EBAY_US').
        date: Date of the feed file in yyyyMMdd format (required for NEWLY_LISTED).
            Must be 3-14 days in the past.
        byte_range: Byte range for chunked download (e.g. 'bytes=0-10485760').
            Required for files larger than 100 MB.
    """
    params = {
        "feed_scope": feed_scope,
        "category_id": category_id,
    }
    if date is not None:
        params["date"] = date

    headers = {
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
        "Accept": "application/json,text/tab-separated-values",
    }
    if byte_range is not None:
        headers["Range"] = byte_range

    return client.get_binary(
        "/buy/feed/v1_beta/item",
        params=params,
        extra_headers=headers,
    )


def get_item_group_feed(
    feed_scope: str,
    category_id: str,
    marketplace_id: str,
    date: Optional[str] = None,
    byte_range: Optional[str] = None,
) -> dict:
    """Download a TSV_GZIP item group feed file for a category and marketplace.

    Item group feeds contain variation information (color, size, etc.) for items
    that belong to item groups. Use alongside the item feed.

    Args:
        feed_scope: Type of feed file. Values:
            - 'NEWLY_LISTED': Daily item group feed (requires date).
            - 'ALL_ACTIVE': Weekly bootstrap of all active item groups.
        category_id: Top-level eBay category ID.
        marketplace_id: eBay marketplace ID (e.g. 'EBAY_US').
        date: Date in yyyyMMdd format (required for NEWLY_LISTED, 3-14 days past).
        byte_range: Byte range for chunked download (e.g. 'bytes=0-10485760').
    """
    params = {
        "feed_scope": feed_scope,
        "category_id": category_id,
    }
    if date is not None:
        params["date"] = date

    headers = {
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
        "Accept": "application/json,text/tab-separated-values",
    }
    if byte_range is not None:
        headers["Range"] = byte_range

    return client.get_binary(
        "/buy/feed/v1_beta/item_group",
        params=params,
        extra_headers=headers,
    )


def get_item_priority_feed(
    category_id: str,
    date: str,
    marketplace_id: str,
    byte_range: Optional[str] = None,
) -> dict:
    """Download a TSV_GZIP item priority feed file tracking priority listing changes.

    Tracks changes (deltas) in the status of priority items, such as when an item
    is added or removed from a campaign. Consume daily Item and Item Group feeds first.

    Args:
        category_id: Top-level eBay category ID (e.g. '625' for Cameras & Photo).
        date: Date of the feed in yyyyMMdd format (up to 14 days in the past).
        marketplace_id: eBay marketplace ID (e.g. 'EBAY_US').
        byte_range: Byte range for chunked download (e.g. 'bytes=0-10485760').
    """
    params = {
        "category_id": category_id,
        "date": date,
    }

    headers = {
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
        "Accept": "application/json,text/tab-separated-values",
    }
    if byte_range is not None:
        headers["Range"] = byte_range

    return client.get_binary(
        "/buy/feed/v1_beta/item_priority",
        params=params,
        extra_headers=headers,
    )


def get_item_snapshot_feed(
    category_id: str,
    snapshot_date: str,
    marketplace_id: str,
    byte_range: Optional[str] = None,
) -> dict:
    """Download a TSV_GZIP hourly snapshot feed of changed items for a category.

    Returns all items that changed within the specified hour. Use to keep your
    item database up to date with price, availability, and other changes.

    Args:
        category_id: Top-level eBay category ID (e.g. '625' for Cameras & Photo).
        snapshot_date: UTC datetime for the snapshot hour in ISO 8601 format
            (e.g. '2021-07-18T08:00:00.000Z'). The file for 8AM is available at 10AM.
        marketplace_id: eBay marketplace ID (e.g. 'EBAY_US').
        byte_range: Byte range for chunked download (e.g. 'bytes=0-10485760').
    """
    params = {
        "category_id": category_id,
        "snapshot_date": snapshot_date,
    }

    headers = {
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
        "Accept": "application/json,text/tab-separated-values",
    }
    if byte_range is not None:
        headers["Range"] = byte_range

    return client.get_binary(
        "/buy/feed/v1_beta/item_snapshot",
        params=params,
        extra_headers=headers,
    )
