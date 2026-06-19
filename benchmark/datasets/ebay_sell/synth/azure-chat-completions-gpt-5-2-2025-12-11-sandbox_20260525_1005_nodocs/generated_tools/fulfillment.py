from typing import Any, Dict, Optional

from .ebay_client import EbayClient


def fulfillment_get_orders(
    filter: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    order_ids: Optional[str] = None,
    sort: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /sell/fulfillment/v1/order"""
    c = EbayClient()
    params: Dict[str, Any] = {}
    if filter is not None:
        params["filter"] = filter
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    if order_ids is not None:
        params["orderIds"] = order_ids
    if sort is not None:
        params["sort"] = sort
    return c.request("GET", "/sell/fulfillment/v1/order", params=params)


def fulfillment_get_order(order_id: str) -> Dict[str, Any]:
    """GET /sell/fulfillment/v1/order/{orderId}"""
    c = EbayClient()
    return c.request("GET", f"/sell/fulfillment/v1/order/{order_id}")


def fulfillment_create_shipping_fulfillment(order_id: str, fulfillment: Dict[str, Any]) -> Dict[str, Any]:
    """POST /sell/fulfillment/v1/order/{orderId}/shipping_fulfillment"""
    c = EbayClient()
    return c.request(
        "POST",
        f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment",
        json=fulfillment,
    )


def fulfillment_get_shipping_fulfillments(order_id: str) -> Dict[str, Any]:
    """GET /sell/fulfillment/v1/order/{orderId}/shipping_fulfillment"""
    c = EbayClient()
    return c.request("GET", f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment")


def fulfillment_get_shipping_fulfillment(order_id: str, fulfillment_id: str) -> Dict[str, Any]:
    """GET /sell/fulfillment/v1/order/{orderId}/shipping_fulfillment/{fulfillmentId}"""
    c = EbayClient()
    return c.request(
        "GET",
        f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment/{fulfillment_id}",
    )
