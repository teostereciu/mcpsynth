from typing import Any, Dict, Optional

from .http_client import ShopifyClient


def create_order(order: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /orders.json"""
    client = client or ShopifyClient()
    return client.request("POST", "/orders.json", json_body={"order": order})


def list_orders(
    *,
    client: Optional[ShopifyClient] = None,
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
) -> Dict[str, Any]:
    """GET /orders.json"""
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


def get_order(order_id: int, *, client: Optional[ShopifyClient] = None, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /orders/{order_id}.json"""
    client = client or ShopifyClient()
    params = {"fields": fields} if fields else None
    return client.request("GET", f"/orders/{order_id}.json", params=params)


def count_orders(*, client: Optional[ShopifyClient] = None, status: str = "any") -> Dict[str, Any]:
    """GET /orders/count.json"""
    client = client or ShopifyClient()
    return client.request("GET", "/orders/count.json", params={"status": status})


def update_order(order_id: int, order: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """PUT /orders/{order_id}.json"""
    client = client or ShopifyClient()
    body = {"order": {**order, "id": order_id}}
    return client.request("PUT", f"/orders/{order_id}.json", json_body=body)


def delete_order(order_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """DELETE /orders/{order_id}.json"""
    client = client or ShopifyClient()
    return client.request("DELETE", f"/orders/{order_id}.json")


def cancel_order(order_id: int, cancel: Optional[Dict[str, Any]] = None, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /orders/{order_id}/cancel.json"""
    client = client or ShopifyClient()
    return client.request("POST", f"/orders/{order_id}/cancel.json", json_body=cancel)


def close_order(order_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /orders/{order_id}/close.json"""
    client = client or ShopifyClient()
    return client.request("POST", f"/orders/{order_id}/close.json")


def open_order(order_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /orders/{order_id}/open.json"""
    client = client or ShopifyClient()
    return client.request("POST", f"/orders/{order_id}/open.json")


# Draft orders

def create_draft_order(draft_order: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /draft_orders.json"""
    client = client or ShopifyClient()
    return client.request("POST", "/draft_orders.json", json_body={"draft_order": draft_order})


def list_draft_orders(
    *,
    client: Optional[ShopifyClient] = None,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
    status: Optional[str] = None,
    fields: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /draft_orders.json"""
    client = client or ShopifyClient()
    params: Dict[str, Any] = {}
    for k, v in {
        "limit": limit,
        "since_id": since_id,
        "updated_at_min": updated_at_min,
        "updated_at_max": updated_at_max,
        "status": status,
        "fields": fields,
    }.items():
        if v is not None:
            params[k] = v
    return client.request("GET", "/draft_orders.json", params=params or None)


def get_draft_order(draft_order_id: int, *, client: Optional[ShopifyClient] = None, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /draft_orders/{draft_order_id}.json"""
    client = client or ShopifyClient()
    params = {"fields": fields} if fields else None
    return client.request("GET", f"/draft_orders/{draft_order_id}.json", params=params)


def count_draft_orders(*, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /draft_orders/count.json"""
    client = client or ShopifyClient()
    return client.request("GET", "/draft_orders/count.json")


def update_draft_order(draft_order_id: int, draft_order: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """PUT /draft_orders/{draft_order_id}.json"""
    client = client or ShopifyClient()
    body = {"draft_order": {**draft_order, "id": draft_order_id}}
    return client.request("PUT", f"/draft_orders/{draft_order_id}.json", json_body=body)


def complete_draft_order(
    draft_order_id: int,
    *,
    client: Optional[ShopifyClient] = None,
    payment_pending: Optional[bool] = None,
) -> Dict[str, Any]:
    """PUT /draft_orders/{draft_order_id}/complete.json"""
    client = client or ShopifyClient()
    params = {"payment_pending": payment_pending} if payment_pending is not None else None
    return client.request("PUT", f"/draft_orders/{draft_order_id}/complete.json", params=params)


def send_draft_order_invoice(
    draft_order_id: int,
    invoice: Optional[Dict[str, Any]] = None,
    *,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """POST /draft_orders/{draft_order_id}/send_invoice.json"""
    client = client or ShopifyClient()
    return client.request("POST", f"/draft_orders/{draft_order_id}/send_invoice.json", json_body=invoice)


def delete_draft_order(draft_order_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """DELETE /draft_orders/{draft_order_id}.json"""
    client = client or ShopifyClient()
    return client.request("DELETE", f"/draft_orders/{draft_order_id}.json")
