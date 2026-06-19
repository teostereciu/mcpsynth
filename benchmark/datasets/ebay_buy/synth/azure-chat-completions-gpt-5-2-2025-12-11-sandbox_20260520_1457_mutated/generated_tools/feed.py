from __future__ import annotations

from typing import Any, Dict, Optional

from .client import EbayClient


_FEED_SCOPE = "https://api.ebay.com/oauth/api_scope/buy.item.feed"


def get_item_feed(
    client: EbayClient,
    *,
    feed_scope: str,
    category_id: str,
    date: Optional[str] = None,
    marketplace_id: str = "EBAY_US",
    range_header: Optional[str] = None,
) -> Dict[str, Any]:
    """Download TSV_GZIP item feed.

    Returns raw text (binary-safe handling is out of scope for stdio tools); use Range for chunking.
    """

    params: Dict[str, Any] = {"feed_scope": feed_scope, "category_id": category_id}
    if date is not None:
        params["date"] = date

    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id, "Accept": "application/gzip"}
    if range_header:
        headers["Range"] = range_header

    return client.request(
        "GET",
        "/buy/feed/v1/item",
        params=params,
        headers=headers,
        scope=_FEED_SCOPE,
        raw=True,
    )


def get_item_snapshot_feed(
    client: EbayClient,
    *,
    category_id: str,
    snapshot_date: str,
    marketplace_id: str = "EBAY_US",
    range_header: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"category_id": category_id, "snapshot_date": snapshot_date}

    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id, "Accept": "application/gzip"}
    if range_header:
        headers["Range"] = range_header

    return client.request(
        "GET",
        "/buy/feed/v1/item_snapshot",
        params=params,
        headers=headers,
        scope=_FEED_SCOPE,
        raw=True,
    )


def get_item_priority_feed(
    client: EbayClient,
    *,
    category_id: str,
    date: str,
    marketplace_id: str = "EBAY_US",
    range_header: str = "bytes=0-1048576",
) -> Dict[str, Any]:
    """Download priority item delta feed (v1_beta). Range header is required by API."""

    params: Dict[str, Any] = {"category_id": category_id, "date": date}
    headers = {
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
        "Accept": "application/gzip",
        "Range": range_header,
    }

    return client.request(
        "GET",
        "/buy/feed/v1_beta/item_priority",
        params=params,
        headers=headers,
        scope=_FEED_SCOPE,
        raw=True,
    )


def get_item_group_feed(
    client: EbayClient,
    *,
    feed_scope: str,
    category_id: str,
    date: Optional[str] = None,
    marketplace_id: str = "EBAY_US",
    range_header: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"feed_scope": feed_scope, "category_id": category_id}
    if date is not None:
        params["date"] = date

    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id, "Accept": "application/gzip"}
    if range_header:
        headers["Range"] = range_header

    return client.request(
        "GET",
        "/buy/feed/v1_beta/item_group",
        params=params,
        headers=headers,
        scope=_FEED_SCOPE,
        raw=True,
    )
