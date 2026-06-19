from typing import Any, Dict, Optional

from .client import ShopifyClient


def create_order(order: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /admin/api/2026-01/orders.json"""
    client = client or ShopifyClient()
    return client.request("POST", "/orders.json", json_body={"order": order})


def cancel_order(order_id: int, cancel: Optional[Dict[str, Any]] = None, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /admin/api/2026-01/orders/{order_id}/cancel.json"""
    client = client or ShopifyClient()
    body = {"cancel": cancel} if cancel is not None else None
    return client.request("POST", f"/orders/{order_id}/cancel.json", json_body=body)


def close_order(order_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /admin/api/2026-01/orders/{order_id}/close.json"""
    client = client or ShopifyClient()
    return client.request("POST", f"/orders/{order_id}/close.json")


def open_order(order_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /admin/api/2026-01/orders/{order_id}/open.json"""
    client = client or ShopifyClient()
    return client.request("POST", f"/orders/{order_id}/open.json")


def list_orders(
    *,
    status: str = "any",
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
    processed_at_min: Optional[str] = None,
    processed_at_max: Optional[str] = None,
    attribution_app_id: Optional[int] = None,
    fields: Optional[str] = None,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/orders.json"""
    client = client or ShopifyClient()
    params: Dict[str, Any] = {"status": status}
    for k, v in {
        "limit": limit,
        "since_id": since_id,
        "created_at_min": created_at_min,
        "created_at_max": created_at_max,
        "updated_at_min": updated_at_min,
        "updated_at_max": updated_at_max,
        "processed_at_min": processed_at_min,
        "processed_at_max": processed_at_max,
        "attribution_app_id": attribution_app_id,
        "fields": fields,
    }.items():
        if v is not None:
            params[k] = v
    return client.request("GET", "/orders.json", params=params)


def get_order(order_id: int, *, fields: Optional[str] = None, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/orders/{order_id}.json"""
    client = client or ShopifyClient()
    params: Dict[str, Any] = {}
    if fields is not None:
        params["fields"] = fields
    return client.request("GET", f"/orders/{order_id}.json", params=params)


def count_orders(
    *,
    status: str = "any",
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/orders/count.json"""
    client = client or ShopifyClient()
    params: Dict[str, Any] = {"status": status}
    for k, v in {
        "created_at_min": created_at_min,
        "created_at_max": created_at_max,
        "updated_at_min": updated_at_min,
        "updated_at_max": updated_at_max,
    }.items():
        if v is not None:
            params[k] = v
    return client.request("GET", "/orders/count.json", params=params)


def update_order(order_id: int, order: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/orders/{order_id}.json"""
    client = client or ShopifyClient()
    return client.request("PUT", f"/orders/{order_id}.json", json_body={"order": order})


def delete_order(order_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/orders/{order_id}.json"""
    client = client or ShopifyClient()
    return client.request("DELETE", f"/orders/{order_id}.json")
