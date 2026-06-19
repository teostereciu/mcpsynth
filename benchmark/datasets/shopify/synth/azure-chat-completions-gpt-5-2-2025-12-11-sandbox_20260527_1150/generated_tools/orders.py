from typing import Any, Dict, Optional

from .http_client import ShopifyAdminClient


def create_order(order: Dict[str, Any], *, api_version: str = "2026-01") -> Dict[str, Any]:
    """POST /admin/api/2026-01/orders.json"""
    client = ShopifyAdminClient(api_version=api_version)
    return client.request("POST", "/orders.json", json_body={"order": order})


def list_orders(
    *,
    api_version: str = "2026-01",
    status: Optional[str] = None,
    ids: Optional[str] = None,
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
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/orders.json"""
    client = ShopifyAdminClient(api_version=api_version)
    params: Dict[str, Any] = {}
    for k, v in {
        "status": status,
        "ids": ids,
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


def get_order(order_id: int, *, api_version: str = "2026-01", fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/orders/{order_id}.json"""
    client = ShopifyAdminClient(api_version=api_version)
    params = {"fields": fields} if fields else None
    return client.request("GET", f"/orders/{order_id}.json", params=params)


def count_orders(
    *,
    api_version: str = "2026-01",
    status: Optional[str] = None,
    financial_status: Optional[str] = None,
    fulfillment_status: Optional[str] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/orders/count.json"""
    client = ShopifyAdminClient(api_version=api_version)
    params: Dict[str, Any] = {}
    for k, v in {
        "status": status,
        "financial_status": financial_status,
        "fulfillment_status": fulfillment_status,
        "created_at_min": created_at_min,
        "created_at_max": created_at_max,
        "updated_at_min": updated_at_min,
        "updated_at_max": updated_at_max,
    }.items():
        if v is not None:
            params[k] = v
    return client.request("GET", "/orders/count.json", params=params or None)


def update_order(order_id: int, order: Dict[str, Any], *, api_version: str = "2026-01") -> Dict[str, Any]:
    """PUT /admin/api/2026-01/orders/{order_id}.json"""
    client = ShopifyAdminClient(api_version=api_version)
    body = {"order": {**order, "id": order_id}}
    return client.request("PUT", f"/orders/{order_id}.json", json_body=body)


def delete_order(order_id: int, *, api_version: str = "2026-01") -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/orders/{order_id}.json"""
    client = ShopifyAdminClient(api_version=api_version)
    return client.request("DELETE", f"/orders/{order_id}.json")


def cancel_order(order_id: int, cancel: Optional[Dict[str, Any]] = None, *, api_version: str = "2026-01") -> Dict[str, Any]:
    """POST /admin/api/2026-01/orders/{order_id}/cancel.json"""
    client = ShopifyAdminClient(api_version=api_version)
    return client.request("POST", f"/orders/{order_id}/cancel.json", json_body=cancel or {})


def close_order(order_id: int, *, api_version: str = "2026-01") -> Dict[str, Any]:
    """POST /admin/api/2026-01/orders/{order_id}/close.json"""
    client = ShopifyAdminClient(api_version=api_version)
    return client.request("POST", f"/orders/{order_id}/close.json", json_body={})


def open_order(order_id: int, *, api_version: str = "2026-01") -> Dict[str, Any]:
    """POST /admin/api/2026-01/orders/{order_id}/open.json"""
    client = ShopifyAdminClient(api_version=api_version)
    return client.request("POST", f"/orders/{order_id}/open.json", json_body={})
