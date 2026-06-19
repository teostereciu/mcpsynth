"""Additional domains (Offer API, Order API) for broader coverage.

Scenarios do not require these, but TASK.md requests comprehensive coverage.
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import request_json, tool_safe_call


_OFFER_SCOPE = "https://api.ebay.com/oauth/api_scope/buy.offer"
_ORDER_SCOPE = "https://api.ebay.com/oauth/api_scope/buy.order"


def offer_get_bidding(*, item_id: str, marketplace_id: Optional[str] = None) -> Dict[str, Any]:
    """Get bidding details for an item.

    Wraps: GET /buy/offer/v1/bidding/{item_id}
    """

    return tool_safe_call(
        request_json,
        "GET",
        f"/buy/offer/v1/bidding/{item_id}",
        marketplace_id=marketplace_id,
        scope=_OFFER_SCOPE,
    )


def offer_place_proxy_bid(
    *,
    item_id: str,
    max_amount: Dict[str, Any],
    marketplace_id: Optional[str] = None,
) -> Dict[str, Any]:
    """Place a proxy bid.

    Wraps: POST /buy/offer/v1/bidding/{item_id}/place_proxy_bid

    max_amount example: {"value": "10.00", "currency": "USD"}
    """

    body = {"maxAmount": max_amount}
    return tool_safe_call(
        request_json,
        "POST",
        f"/buy/offer/v1/bidding/{item_id}/place_proxy_bid",
        json_body=body,
        marketplace_id=marketplace_id,
        scope=_OFFER_SCOPE,
    )


def order_initiate_guest_checkout_session(
    *,
    line_item_inputs: list,
    marketplace_id: Optional[str] = None,
) -> Dict[str, Any]:
    """Initiate a guest checkout session.

    Wraps: POST /buy/order/v1/guest_checkout_session/initiate
    """

    body = {"lineItemInputs": line_item_inputs}
    return tool_safe_call(
        request_json,
        "POST",
        "/buy/order/v1/guest_checkout_session/initiate",
        json_body=body,
        marketplace_id=marketplace_id,
        scope=_ORDER_SCOPE,
    )


def order_get_guest_checkout_session(
    *,
    checkout_session_id: str,
    marketplace_id: Optional[str] = None,
) -> Dict[str, Any]:
    """Get a guest checkout session.

    Wraps: GET /buy/order/v1/guest_checkout_session/{checkout_session_id}
    """

    return tool_safe_call(
        request_json,
        "GET",
        f"/buy/order/v1/guest_checkout_session/{checkout_session_id}",
        marketplace_id=marketplace_id,
        scope=_ORDER_SCOPE,
    )
