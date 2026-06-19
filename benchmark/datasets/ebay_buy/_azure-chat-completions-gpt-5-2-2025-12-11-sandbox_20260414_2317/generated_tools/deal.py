"""Tools for eBay Buy Deal API."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import request_json, tool_safe_call


_DEAL_SCOPE = "https://api.ebay.com/oauth/api_scope/buy.deal"


def deal_get_deal_items(
    *,
    category_ids: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    commissionable: Optional[bool] = None,
    delivery_country: Optional[str] = None,
    marketplace_id: Optional[str] = None,
) -> Dict[str, Any]:
    """Get deal items (daily deals).

    Wraps: GET /buy/deal/v1/deal_item
    """

    params: Dict[str, Any] = {}
    if category_ids is not None:
        params["category_ids"] = category_ids
    if limit is not None:
        params["limit"] = int(limit)
    if offset is not None:
        params["offset"] = int(offset)
    if commissionable is not None:
        params["commissionable"] = str(bool(commissionable)).lower()
    if delivery_country is not None:
        params["delivery_country"] = delivery_country

    return tool_safe_call(
        request_json,
        "GET",
        "/buy/deal/v1/deal_item",
        params=params or None,
        marketplace_id=marketplace_id,
        scope=_DEAL_SCOPE,
    )


def deal_get_events(
    *,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    marketplace_id: Optional[str] = None,
) -> Dict[str, Any]:
    """Get deal events.

    Wraps: GET /buy/deal/v1/event
    """

    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = int(limit)
    if offset is not None:
        params["offset"] = int(offset)

    return tool_safe_call(
        request_json,
        "GET",
        "/buy/deal/v1/event",
        params=params or None,
        marketplace_id=marketplace_id,
        scope=_DEAL_SCOPE,
    )


def deal_get_event(*, event_id: str, marketplace_id: Optional[str] = None) -> Dict[str, Any]:
    """Get a specific deal event.

    Wraps: GET /buy/deal/v1/event/{event_id}
    """

    return tool_safe_call(
        request_json,
        "GET",
        f"/buy/deal/v1/event/{event_id}",
        marketplace_id=marketplace_id,
        scope=_DEAL_SCOPE,
    )


def deal_get_event_items(
    *,
    event_id: str,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    marketplace_id: Optional[str] = None,
) -> Dict[str, Any]:
    """Get items for a deal event.

    Wraps: GET /buy/deal/v1/event/{event_id}/item
    """

    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = int(limit)
    if offset is not None:
        params["offset"] = int(offset)

    return tool_safe_call(
        request_json,
        "GET",
        f"/buy/deal/v1/event/{event_id}/item",
        params=params or None,
        marketplace_id=marketplace_id,
        scope=_DEAL_SCOPE,
    )
