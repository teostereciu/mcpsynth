from typing import Any, Dict, Optional

from .client import EbaySellClient


def get_orders(
    *,
    filter: Optional[str] = None,
    order_ids: Optional[str] = None,
    field_groups: Optional[str] = None,
    limit: int = 50,
    offset: int = 0,
) -> Dict[str, Any]:
    """GET /order

    Search and retrieve orders.
    """
    client = EbaySellClient()
    params: Dict[str, str] = {"limit": str(limit), "offset": str(offset)}
    if filter:
        params["filter"] = filter
    if order_ids:
        params["orderIds"] = order_ids
    if field_groups:
        params["fieldGroups"] = field_groups
    return client.request("GET", "/sell/fulfillment/v1/order", params=params)


def get_order(order_id: str, *, field_groups: Optional[str] = None) -> Dict[str, Any]:
    """GET /order/{orderId}"""
    client = EbaySellClient()
    params: Dict[str, str] = {}
    if field_groups:
        params["fieldGroups"] = field_groups
    return client.request("GET", f"/sell/fulfillment/v1/order/{order_id}", params=params or None)
