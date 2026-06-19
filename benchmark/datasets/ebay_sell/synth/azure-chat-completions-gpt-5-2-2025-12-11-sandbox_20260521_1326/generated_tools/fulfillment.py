from typing import Any, Dict, Optional

from .client import EbayClient


def get_order(order_id: str, *, field_groups: Optional[str] = None) -> Dict[str, Any]:
    """GET /order/{orderId}

    Retrieves a single order by orderId.

    Doc: docs/api_fulfillment_get-order.md
    """

    params: Dict[str, Any] = {}
    if field_groups is not None:
        params["fieldGroups"] = field_groups

    client = EbayClient()
    return client.request_json("GET", f"/sell/fulfillment/v1/order/{order_id}", params=params or None)


def create_shipping_fulfillment(order_id: str, fulfillment: Dict[str, Any]) -> Dict[str, Any]:
    """POST /order/{orderId}/shipping_fulfillment

    Creates a shipping fulfillment for an order/package.

    Doc: docs/api_fulfillment_create-shipping-fulfillment.md
    """

    client = EbayClient()
    return client.request_json(
        "POST",
        f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment",
        json=fulfillment,
        content_type="application/json",
    )


def get_orders(
    *,
    filter: Optional[str] = None,
    order_ids: Optional[str] = None,
    field_groups: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /order

    Searches for and retrieves orders.

    Doc: docs/api_fulfillment_get-orders.md
    """

    params: Dict[str, Any] = {}
    if order_ids is not None:
        params["orderIds"] = order_ids
    if filter is not None:
        params["filter"] = filter
    if field_groups is not None:
        params["fieldGroups"] = field_groups
    if limit is not None:
        params["limit"] = str(limit)
    if offset is not None:
        params["offset"] = str(offset)

    client = EbayClient()
    return client.request_json("GET", "/sell/fulfillment/v1/order", params=params or None)
