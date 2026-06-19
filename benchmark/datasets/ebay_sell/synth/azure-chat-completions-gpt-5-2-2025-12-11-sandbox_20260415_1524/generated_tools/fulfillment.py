from typing import Any, Dict, Optional

from .ebay_client import EbayClient


def get_orders(
    *,
    filter: Optional[str] = None,
    order_ids: Optional[str] = None,
    field_groups: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /order

    Search for orders by filter or explicit orderIds.
    """
    client = EbayClient()
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
    return client.request("GET", "/sell/fulfillment/v1/order", params=params or None)


def get_order(order_id: str, *, field_groups: Optional[str] = None) -> Dict[str, Any]:
    """GET /order/{orderId}"""
    client = EbayClient()
    params = {"fieldGroups": field_groups} if field_groups else None
    return client.request("GET", f"/sell/fulfillment/v1/order/{order_id}", params=params)


def create_shipping_fulfillment(order_id: str, fulfillment: Dict[str, Any]) -> Dict[str, Any]:
    """POST /order/{orderId}/shipping_fulfillment"""
    client = EbayClient()
    return client.request(
        "POST",
        f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment",
        json=fulfillment,
        content_type="application/json",
    )


def get_shipping_fulfillments(order_id: str) -> Dict[str, Any]:
    """GET /order/{orderId}/shipping_fulfillment"""
    client = EbayClient()
    return client.request("GET", f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment")


def get_shipping_fulfillment(order_id: str, fulfillment_id: str) -> Dict[str, Any]:
    """GET /order/{orderId}/shipping_fulfillment/{fulfillmentId}"""
    client = EbayClient()
    return client.request(
        "GET", f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment/{fulfillment_id}"
    )


def get_activities(
    *,
    filter: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /activity

    Retrieve seller activities.
    """
    client = EbayClient()
    params: Dict[str, Any] = {}
    if filter is not None:
        params["filter"] = filter
    if limit is not None:
        params["limit"] = str(limit)
    if offset is not None:
        params["offset"] = str(offset)
    return client.request("GET", "/sell/fulfillment/v1/activity", params=params or None)


def issue_refund(order_id: str, refund: Dict[str, Any]) -> Dict[str, Any]:
    """POST /order/{orderId}/issue_refund"""
    client = EbayClient()
    return client.request(
        "POST",
        f"/sell/fulfillment/v1/order/{order_id}/issue_refund",
        json=refund,
        content_type="application/json",
    )
