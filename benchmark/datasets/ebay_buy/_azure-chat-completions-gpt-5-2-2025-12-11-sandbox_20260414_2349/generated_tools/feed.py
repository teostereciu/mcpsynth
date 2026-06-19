"""Tools for eBay Buy Feed API.

Note: Many feed endpoints return binary TSV_GZIP files. These tools return the
feed download URL (when available) or a small JSON error payload.
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from .ebay_client import EbayApiError, make_buy_api_request, tool_error


def feed_get_item_feed(
    category_id: str,
    *,
    date: Optional[str] = None,
    feed_scope: str = "NEWLY_LISTED",
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    """Get an item feed file metadata / download response.

    Maps to GET /buy/feed/v1/item

    Args:
      category_id: Leaf or parent category ID.
      date: Feed date (yyyyMMdd). Optional; if omitted, eBay uses most recent.
      feed_scope: NEWLY_LISTED (daily) or ALL_ACTIVE (weekly bootstrap).
    """

    params: Dict[str, Any] = {"category_id": category_id, "feed_scope": feed_scope}
    if date:
        params["date"] = date
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset

    try:
        return make_buy_api_request(
            "GET",
            "/buy/feed/v1/item",
            params=params,
            marketplace_id=marketplace_id,
        )
    except EbayApiError as e:
        return tool_error(str(e))


def feed_get_item_group_feed(
    category_id: str,
    *,
    date: Optional[str] = None,
    feed_scope: str = "NEWLY_LISTED",
    marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    """Get an item group feed.

    Maps to GET /buy/feed/v1/item_group
    """

    params: Dict[str, Any] = {"category_id": category_id, "feed_scope": feed_scope}
    if date:
        params["date"] = date

    try:
        return make_buy_api_request(
            "GET",
            "/buy/feed/v1/item_group",
            params=params,
            marketplace_id=marketplace_id,
        )
    except EbayApiError as e:
        return tool_error(str(e))


def feed_get_item_priority_feed(
    category_id: str,
    *,
    date: Optional[str] = None,
    feed_scope: str = "NEWLY_LISTED",
    marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    """Get an item priority feed.

    Maps to GET /buy/feed/v1/item_priority
    """

    params: Dict[str, Any] = {"category_id": category_id, "feed_scope": feed_scope}
    if date:
        params["date"] = date

    try:
        return make_buy_api_request(
            "GET",
            "/buy/feed/v1/item_priority",
            params=params,
            marketplace_id=marketplace_id,
        )
    except EbayApiError as e:
        return tool_error(str(e))


def feed_get_item_snapshot_feed(
    category_id: str,
    *,
    date: Optional[str] = None,
    feed_scope: str = "ALL_ACTIVE",
    marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    """Get an item snapshot feed.

    Maps to GET /buy/feed/v1/item_snapshot
    """

    params: Dict[str, Any] = {"category_id": category_id, "feed_scope": feed_scope}
    if date:
        params["date"] = date

    try:
        return make_buy_api_request(
            "GET",
            "/buy/feed/v1/item_snapshot",
            params=params,
            marketplace_id=marketplace_id,
        )
    except EbayApiError as e:
        return tool_error(str(e))
