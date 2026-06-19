"""Tools for eBay Buy Deal API."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import request_json


DEAL_SCOPE = "https://api.ebay.com/oauth/api_scope/buy.deal"


def get_events(
    *,
    limit: int = 20,
    offset: int = 0,
    marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    """Get deal events.

    Wraps: GET /buy/deal/v1/event
    """

    params = {"limit": limit, "offset": offset}
    return request_json(
        "GET",
        "/buy/deal/v1/event",
        params=params,
        marketplace_id=marketplace_id,
        scope=DEAL_SCOPE,
    )


def get_event(
    *,
    event_id: str,
    marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    """Get a specific deal event.

    Wraps: GET /buy/deal/v1/event/{event_id}
    """

    return request_json(
        "GET",
        f"/buy/deal/v1/event/{event_id}",
        marketplace_id=marketplace_id,
        scope=DEAL_SCOPE,
    )


def get_event_items(
    *,
    event_id: str,
    limit: int = 20,
    offset: int = 0,
    marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    """Get items for a deal event.

    Wraps: GET /buy/deal/v1/event/{event_id}/item
    """

    params = {"limit": limit, "offset": offset}
    return request_json(
        "GET",
        f"/buy/deal/v1/event/{event_id}/item",
        params=params,
        marketplace_id=marketplace_id,
        scope=DEAL_SCOPE,
    )


def get_deal_items(
    *,
    category_ids: Optional[str] = None,
    limit: int = 20,
    offset: int = 0,
    marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    """Get deal items (daily deals).

    Wraps: GET /buy/deal/v1/deal_item
    """

    params: Dict[str, Any] = {"limit": limit, "offset": offset}
    if category_ids:
        params["category_ids"] = category_ids

    return request_json(
        "GET",
        "/buy/deal/v1/deal_item",
        params=params,
        marketplace_id=marketplace_id,
        scope=DEAL_SCOPE,
    )
