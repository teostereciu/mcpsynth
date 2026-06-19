from typing import Any, Dict, Optional

from .client import EbayClient


def get_orders(
    *,
    field_groups: Optional[str] = None,
    filter: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    order_ids: Optional[str] = None,
    client: Optional[EbayClient] = None,
) -> Dict[str, Any]:
    """GET /order

    Search and retrieve orders.
    """
    c = client or EbayClient()
    params: Dict[str, Any] = {}
    if field_groups is not None:
        params["fieldGroups"] = field_groups
    if filter is not None:
        params["filter"] = filter
    if limit is not None:
        params["limit"] = str(limit)
    if offset is not None:
        params["offset"] = str(offset)
    if order_ids is not None:
        params["orderIds"] = order_ids
    return c.request("GET", "/sell/fulfillment/v1/order", params=params or None)


def get_order(
    order_id: str,
    *,
    field_groups: Optional[str] = None,
    client: Optional[EbayClient] = None,
) -> Dict[str, Any]:
    """GET /order/{orderId}

    Retrieve a single order by ID.
    """
    c = client or EbayClient()
    params: Dict[str, Any] = {}
    if field_groups is not None:
        params["fieldGroups"] = field_groups
    return c.request(
        "GET",
        f"/sell/fulfillment/v1/order/{order_id}",
        params=params or None,
    )


def create_shipping_fulfillment(
    order_id: str,
    shipping_fulfillment_details: Dict[str, Any],
    *,
    client: Optional[EbayClient] = None,
) -> Dict[str, Any]:
    """POST /order/{orderId}/shipping_fulfillment

    Create a shipping fulfillment (shipment) for an order.
    """
    c = client or EbayClient()
    return c.request(
        "POST",
        f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment",
        json=shipping_fulfillment_details,
    )
