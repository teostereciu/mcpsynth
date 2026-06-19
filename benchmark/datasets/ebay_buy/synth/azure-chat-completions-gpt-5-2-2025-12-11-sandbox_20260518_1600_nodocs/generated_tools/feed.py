from __future__ import annotations

from typing import Any, Dict, Optional

from .ebay_client import EbayClient

FEED_SCOPE = "https://api.ebay.com/oauth/api_scope"


def get_item_feed(
    feed_type: str,
    date: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /buy/feed/v1/item"""
    params: Dict[str, Any] = {"feed_type": feed_type}
    if date is not None:
        params["date"] = date
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    return EbayClient().request("GET", "/buy/feed/v1/item", scope=FEED_SCOPE, params=params)


def get_item_snapshot(feed_scope: str, date: Optional[str] = None) -> Dict[str, Any]:
    """GET /buy/feed/v1/item_snapshot"""
    params: Dict[str, Any] = {"feed_scope": feed_scope}
    if date is not None:
        params["date"] = date
    return EbayClient().request("GET", "/buy/feed/v1/item_snapshot", scope=FEED_SCOPE, params=params)


def get_item_snapshot_feed(feed_scope: str, date: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None) -> Dict[str, Any]:
    """GET /buy/feed/v1/item_snapshot_feed"""
    params: Dict[str, Any] = {"feed_scope": feed_scope}
    if date is not None:
        params["date"] = date
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    return EbayClient().request("GET", "/buy/feed/v1/item_snapshot_feed", scope=FEED_SCOPE, params=params)
