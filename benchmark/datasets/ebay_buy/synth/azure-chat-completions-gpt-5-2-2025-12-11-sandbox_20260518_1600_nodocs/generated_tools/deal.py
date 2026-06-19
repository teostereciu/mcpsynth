from __future__ import annotations

from typing import Any, Dict, Optional

from .ebay_client import EbayClient

DEAL_SCOPE = "https://api.ebay.com/oauth/api_scope"


def get_deals(
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    sort: Optional[str] = None,
    filter: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /buy/deal/v1/deal_item"""
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    if sort is not None:
        params["sort"] = sort
    if filter is not None:
        params["filter"] = filter
    return EbayClient().request("GET", "/buy/deal/v1/deal_item", scope=DEAL_SCOPE, params=params)


def get_deal_item(deal_item_id: str) -> Dict[str, Any]:
    """GET /buy/deal/v1/deal_item/{dealItemId}"""
    return EbayClient().request("GET", f"/buy/deal/v1/deal_item/{deal_item_id}", scope=DEAL_SCOPE)


def get_events(
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    sort: Optional[str] = None,
    filter: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /buy/deal/v1/event"""
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    if sort is not None:
        params["sort"] = sort
    if filter is not None:
        params["filter"] = filter
    return EbayClient().request("GET", "/buy/deal/v1/event", scope=DEAL_SCOPE, params=params)


def get_event(event_id: str) -> Dict[str, Any]:
    """GET /buy/deal/v1/event/{eventId}"""
    return EbayClient().request("GET", f"/buy/deal/v1/event/{event_id}", scope=DEAL_SCOPE)
