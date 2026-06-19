from typing import Any, Dict, Optional

from . import client as _shared
from .client import SCOPE_FULFILLMENT
from . import mcp

API = "/sell/fulfillment/v1"


@mcp.tool()
def fulfillment_get_orders(
    *,
    filter: Optional[str] = None,
    field_groups: Optional[str] = None,
    order_ids: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """GET /order"""
    params: Dict[str, Any] = {}
    if filter is not None:
        params["filter"] = filter
    if field_groups is not None:
        params["fieldGroups"] = field_groups
    if order_ids is not None:
        params["orderIds"] = order_ids
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    return _shared.client.request(
        "GET",
        API,
        "/order",
        scope=SCOPE_FULFILLMENT,
        marketplace_id=marketplace_id,
        params=params or None,
    )


@mcp.tool()
def fulfillment_get_order(order_id: str, *, marketplace_id: str = "EBAY_US") -> Any:
    """GET /order/{orderId}"""
    return _shared.client.request(
        "GET",
        API,
        f"/order/{order_id}",
        scope=SCOPE_FULFILLMENT,
        marketplace_id=marketplace_id,
    )


@mcp.tool()
def fulfillment_create_shipping_fulfillment(
    order_id: str,
    fulfillment: Dict[str, Any],
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """POST /order/{orderId}/shipping_fulfillment"""
    return _shared.client.request(
        "POST",
        API,
        f"/order/{order_id}/shipping_fulfillment",
        scope=SCOPE_FULFILLMENT,
        marketplace_id=marketplace_id,
        json=fulfillment,
    )


@mcp.tool()
def fulfillment_get_shipping_fulfillments(
    order_id: str,
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """GET /order/{orderId}/shipping_fulfillment"""
    return _shared.client.request(
        "GET",
        API,
        f"/order/{order_id}/shipping_fulfillment",
        scope=SCOPE_FULFILLMENT,
        marketplace_id=marketplace_id,
    )


@mcp.tool()
def fulfillment_get_shipping_fulfillment(
    order_id: str,
    fulfillment_id: str,
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """GET /order/{orderId}/shipping_fulfillment/{fulfillmentId}"""
    return _shared.client.request(
        "GET",
        API,
        f"/order/{order_id}/shipping_fulfillment/{fulfillment_id}",
        scope=SCOPE_FULFILLMENT,
        marketplace_id=marketplace_id,
    )
