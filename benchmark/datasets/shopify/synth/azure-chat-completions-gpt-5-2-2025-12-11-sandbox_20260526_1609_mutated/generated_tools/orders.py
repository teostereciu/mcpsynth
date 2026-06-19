from typing import Any, Dict, Optional

from .http import ShopifyClient


def list_orders(
    *,
    status: str = "any",
    limit: int = 50,
    since_id: Optional[int] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
    financial_status: Optional[str] = None,
    fulfillment_status: Optional[str] = None,
    fields: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/orders.json?status=any"""
    params: Dict[str, Any] = {"status": status, "limit": limit}
    if since_id is not None:
        params["since_id"] = since_id
    if created_at_min:
        params["created_at_min"] = created_at_min
    if created_at_max:
        params["created_at_max"] = created_at_max
    if updated_at_min:
        params["updated_at_min"] = updated_at_min
    if updated_at_max:
        params["updated_at_max"] = updated_at_max
    if financial_status:
        params["financial_status"] = financial_status
    if fulfillment_status:
        params["fulfillment_status"] = fulfillment_status
    if fields:
        params["fields"] = fields
    return ShopifyClient().request("GET", "/orders.json", params=params)


def get_order(*, order_id: int, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/orders/{order_id}.json"""
    params: Dict[str, Any] = {}
    if fields:
        params["fields"] = fields
    return ShopifyClient().request("GET", f"/orders/{order_id}.json", params=params)


def count_orders(*, status: str = "any") -> Dict[str, Any]:
    """GET /admin/api/2026-01/orders/count.json?status=any"""
    return ShopifyClient().request("GET", "/orders/count.json", params={"status": status})


def create_order(*, order: Dict[str, Any]) -> Dict[str, Any]:
    """POST /admin/api/2026-01/orders.json"""
    return ShopifyClient().request("POST", "/orders.json", json={"order": order})


def update_order(*, order_id: int, order: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/orders/{order_id}.json"""
    body = {"order": {**order, "id": order_id}}
    return ShopifyClient().request("PUT", f"/orders/{order_id}.json", json=body)


def delete_order(*, order_id: int) -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/orders/{order_id}.json"""
    return ShopifyClient().request("DELETE", f"/orders/{order_id}.json")


def cancel_order(*, order_id: int, reason: Optional[str] = None, email: Optional[bool] = None) -> Dict[str, Any]:
    """POST /admin/api/2026-01/orders/{order_id}/cancel.json"""
    payload: Dict[str, Any] = {}
    if reason:
        payload["reason"] = reason
    if email is not None:
        payload["email"] = email
    return ShopifyClient().request("POST", f"/orders/{order_id}/cancel.json", json=payload or None)


def close_order(*, order_id: int) -> Dict[str, Any]:
    """POST /admin/api/2026-01/orders/{order_id}/close.json"""
    return ShopifyClient().request("POST", f"/orders/{order_id}/close.json")


def open_order(*, order_id: int) -> Dict[str, Any]:
    """POST /admin/api/2026-01/orders/{order_id}/open.json"""
    return ShopifyClient().request("POST", f"/orders/{order_id}/open.json")
