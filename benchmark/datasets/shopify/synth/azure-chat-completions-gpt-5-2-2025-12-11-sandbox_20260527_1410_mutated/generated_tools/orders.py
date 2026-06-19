from typing import Any, Dict, Optional

from .http_client import ShopifyClient


def order_create(order: Dict[str, Any]) -> Dict[str, Any]:
    """POST /admin/api/2026-01/orders.json"""
    client = ShopifyClient()
    return client.request("POST", "/orders.json", json_body={"order": order})


def orders_list(
    *,
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
    client = ShopifyClient()
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
    return client.request("GET", "/orders.json", params=params)


def order_get(order_id: int, *, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/orders/{order_id}.json"""
    client = ShopifyClient()
    params = {"fields": fields} if fields else None
    return client.request("GET", f"/orders/{order_id}.json", params=params)


def orders_count(*, status: Optional[str] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/orders/count.json"""
    client = ShopifyClient()
    params = {"status": status} if status else None
    return client.request("GET", "/orders/count.json", params=params)


def order_update(order_id: int, order: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/orders/{order_id}.json"""
    client = ShopifyClient()
    body = {"order": {**order, "id": order_id}}
    return client.request("PUT", f"/orders/{order_id}.json", json_body=body)


def order_delete(order_id: int) -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/orders/{order_id}.json"""
    client = ShopifyClient()
    return client.request("DELETE", f"/orders/{order_id}.json")


def order_cancel(order_id: int, cancel: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /admin/api/2026-01/orders/{order_id}/cancel.json"""
    client = ShopifyClient()
    return client.request(
        "POST",
        f"/orders/{order_id}/cancel.json",
        json_body={"order": cancel} if cancel else None,
    )


def order_close(order_id: int) -> Dict[str, Any]:
    """POST /admin/api/2026-01/orders/{order_id}/close.json"""
    client = ShopifyClient()
    return client.request("POST", f"/orders/{order_id}/close.json")


def order_open(order_id: int) -> Dict[str, Any]:
    """POST /admin/api/2026-01/orders/{order_id}/open.json"""
    client = ShopifyClient()
    return client.request("POST", f"/orders/{order_id}/open.json")
