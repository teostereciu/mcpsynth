from typing import Any, Dict, Optional

from .client import EbayClient


def get_item_feed(
    client: EbayClient,
    *,
    feed_scope: str,
    category_id: str,
    date: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    range_header: Optional[str] = None,
) -> Dict[str, Any]:
    """Download Item feed (TSV_GZIP). Returns raw text if server returns non-JSON.

    Note: Successful responses are binary gzip; this helper returns metadata only.
    Use range_header to download in chunks (e.g. 'bytes=0-1048575').
    """

    params: Dict[str, Any] = {"feed_scope": feed_scope, "category_id": category_id}
    if date is not None:
        params["date"] = date

    headers: Dict[str, str] = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if range_header:
        headers["Range"] = range_header

    # This endpoint returns TSV_GZIP; our client will return {raw, content_type}.
    return client.request("GET", "/buy/feed/v1/item", params=params, headers=headers)


def get_item_group_feed(
    client: EbayClient,
    *,
    feed_scope: str,
    category_id: str,
    date: Optional[str] = None,
    marketplace_id: str,
    range_header: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"feed_scope": feed_scope, "category_id": category_id}
    if date is not None:
        params["date"] = date

    headers: Dict[str, str] = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if range_header:
        headers["Range"] = range_header

    # Docs show /buy/feed/v1_beta/item_group, but some files list /buy/feed/v1/item_group.
    # We'll use v1_beta as per documentation file.
    return client.request("GET", "/buy/feed/v1_beta/item_group", params=params, headers=headers)


def get_item_priority_feed(
    client: EbayClient,
    *,
    category_id: str,
    date: str,
    marketplace_id: str,
    range_header: str,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"category_id": category_id, "date": date}
    headers: Dict[str, str] = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id, "Range": range_header}
    return client.request("GET", "/buy/feed/v1_beta/item_priority", params=params, headers=headers)


def get_item_snapshot_feed(
    client: EbayClient,
    *,
    category_id: str,
    snapshot_date: str,
    marketplace_id: str,
    range_header: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"category_id": category_id, "snapshot_date": snapshot_date}
    headers: Dict[str, str] = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if range_header:
        headers["Range"] = range_header
    return client.request("GET", "/buy/feed/v1_beta/item_snapshot", params=params, headers=headers)
