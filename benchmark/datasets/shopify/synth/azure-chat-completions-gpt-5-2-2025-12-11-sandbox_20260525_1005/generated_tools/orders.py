from typing import Any, Dict, Optional

from .client import ShopifyClient


def create_order(order: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Any:
    """POST /orders.json"""
    client = client or ShopifyClient()
    return client.request("POST", "/orders.json", json={"order": order})


def list_orders(
    *,
    client: Optional[ShopifyClient] = None,
    status: Optional[str] = None,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
    processed_at_min: Optional[str] = None,
    processed_at_max: Optional[str] = None,
    attribution_app_id: Optional[int] = None,
    financial_status: Optional[str] = None,
    fulfillment_status: Optional[str] = None,
    fields: Optional[str] = None,
) -> Any:
    """GET /orders.json"""
    client = client or ShopifyClient()
    params: Dict[str, Any] = {}
    for k, v in {
        "status": status,
        "limit": limit,
        "since_id": since_id,
        "created_at_min": created_at_min,
        "created_at_max": created_at_max,
        "updated_at_min": updated_at_min,
        "updated_at_max": updated_at_max,
        "processed_at_min": processed_at_min,
        "processed_at_max": processed_at_max,
        "attribution_app_id": attribution_app_id,
        "financial_status": financial_status,
        "fulfillment_status": fulfillment_status,
        "fields": fields,
    }.items():
        if v is not None:
            params[k] = v
    return client.request("GET", "/orders.json", params=params or None)


def get_order(order_id: int, *, client: Optional[ShopifyClient] = None, fields: Optional[str] = None) -> Any:
    """GET /orders/{order_id}.json"""
    client = client or ShopifyClient()
    params = {"fields": fields} if fields else None
    return client.request("GET", f"/orders/{order_id}.json", params=params)


def count_orders(*, client: Optional[ShopifyClient] = None, status: Optional[str] = None) -> Any:
    """GET /orders/count.json"""
    client = client or ShopifyClient()
    params = {"status": status} if status is not None else None
    return client.request("GET", "/orders/count.json", params=params)


def update_order(order_id: int, order: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Any:
    """PUT /orders/{order_id}.json"""
    client = client or ShopifyClient()
    body = {"order": {**order, "id": order_id}}
    return client.request("PUT", f"/orders/{order_id}.json", json=body)


def delete_order(order_id: int, *, client: Optional[ShopifyClient] = None) -> Any:
    """DELETE /orders/{order_id}.json"""
    client = client or ShopifyClient()
    return client.request("DELETE", f"/orders/{order_id}.json")


def cancel_order(order_id: int, cancel: Optional[Dict[str, Any]] = None, *, client: Optional[ShopifyClient] = None) -> Any:
    """POST /orders/{order_id}/cancel.json"""
    client = client or ShopifyClient()
    return client.request("POST", f"/orders/{order_id}/cancel.json", json=cancel or {})


def close_order(order_id: int, *, client: Optional[ShopifyClient] = None) -> Any:
    """POST /orders/{order_id}/close.json"""
    client = client or ShopifyClient()
    return client.request("POST", f"/orders/{order_id}/close.json")


def open_order(order_id: int, *, client: Optional[ShopifyClient] = None) -> Any:
    """POST /orders/{order_id}/open.json"""
    client = client or ShopifyClient()
    return client.request("POST", f"/orders/{order_id}/open.json")
