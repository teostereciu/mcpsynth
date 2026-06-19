from __future__ import annotations

from typing import Any, Dict, Optional

from .client import EbayClient


def get_orders(
    *,
    filter: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    client: Optional[EbayClient] = None,
) -> Any:
    """GET /order

    Doc: docs/api_fulfillment_get-orders.md
    """
    c = client or EbayClient()
    params: Dict[str, str] = {}
    if filter is not None:
        params["filter"] = filter
    if limit is not None:
        params["limit"] = str(limit)
    if offset is not None:
        params["offset"] = str(offset)
    status, body, headers = c.request("GET", "/order", params=params or None)
    return c.ok_or_error(status, body, headers)


def get_order(order_id: str, *, client: Optional[EbayClient] = None) -> Any:
    """GET /order/{orderId}

    Doc: docs/api_fulfillment_get-order.md
    """
    c = client or EbayClient()
    status, body, headers = c.request("GET", f"/order/{order_id}")
    return c.ok_or_error(status, body, headers)


def create_shipping_fulfillment(
    order_id: str,
    fulfillment: Dict[str, Any],
    *,
    client: Optional[EbayClient] = None,
) -> Any:
    """POST /order/{orderId}/shipping_fulfillment

    Doc: docs/api_fulfillment_create-shipping-fulfillment.md
    """
    c = client or EbayClient()
    status, body, headers = c.request(
        "POST",
        f"/order/{order_id}/shipping_fulfillment",
        json=fulfillment,
        content_type="application/json",
    )
    return c.ok_or_error(status, body, headers)


def issue_refund(
    order_id: str,
    refund: Dict[str, Any],
    *,
    client: Optional[EbayClient] = None,
) -> Any:
    """POST /order/{order_id}/issue_refund

    Doc: docs/api_fulfillment_issue-refund.md
    """
    c = client or EbayClient()
    status, body, headers = c.request(
        "POST",
        f"/order/{order_id}/issue_refund",
        json=refund,
        content_type="application/json",
    )
    return c.ok_or_error(status, body, headers)
