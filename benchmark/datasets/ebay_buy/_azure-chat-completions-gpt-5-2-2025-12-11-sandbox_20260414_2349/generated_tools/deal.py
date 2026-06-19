"""Tools for eBay Buy Deal API."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .ebay_client import EbayApiError, make_buy_api_request, tool_error


def deal_get_deal_items(
    *,
    category_ids: Optional[str] = None,
    limit: int = 20,
    offset: int = 0,
    marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    """Get deal items (daily deals).

    Maps to GET /buy/deal/v1/deal_item
    """

    params: Dict[str, Any] = {"limit": limit, "offset": offset}
    if category_ids:
        params["category_ids"] = category_ids

    try:
        return make_buy_api_request(
            "GET",
            "/buy/deal/v1/deal_item",
            params=params,
            marketplace_id=marketplace_id,
        )
    except EbayApiError as e:
        return tool_error(str(e))


def deal_get_events(
    *,
    limit: int = 20,
    offset: int = 0,
    marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    """Get deal events.

    Maps to GET /buy/deal/v1/event
    """

    try:
        return make_buy_api_request(
            "GET",
            "/buy/deal/v1/event",
            params={"limit": limit, "offset": offset},
            marketplace_id=marketplace_id,
        )
    except EbayApiError as e:
        return tool_error(str(e))


def deal_get_event(
    event_id: str,
    *,
    marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    """Get a specific deal event.

    Maps to GET /buy/deal/v1/event/{event_id}
    """

    try:
        return make_buy_api_request(
            "GET",
            f"/buy/deal/v1/event/{event_id}",
            marketplace_id=marketplace_id,
        )
    except EbayApiError as e:
        return tool_error(str(e))


def deal_get_event_items(
    event_id: str,
    *,
    limit: int = 20,
    offset: int = 0,
    marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    """Get items for a specific deal event.

    Maps to GET /buy/deal/v1/event/{event_id}/item
    """

    try:
        return make_buy_api_request(
            "GET",
            f"/buy/deal/v1/event/{event_id}/item",
            params={"limit": limit, "offset": offset},
            marketplace_id=marketplace_id,
        )
    except EbayApiError as e:
        return tool_error(str(e))
