from typing import Any, Dict, Optional

from .client import ShopifyClient


def list_orders(
    limit: int = 50,
    status: str = "any",
    financial_status: Optional[str] = None,
    fulfillment_status: Optional[str] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
    fields: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /orders.json"""
    client = ShopifyClient()
    params: Dict[str, Any] = {"limit": limit, "status": status}
    if financial_status:
        params["financial_status"] = financial_status
    if fulfillment_status:
        params["fulfillment_status"] = fulfillment_status
    if created_at_min:
        params["created_at_min"] = created_at_min
    if created_at_max:
        params["created_at_max"] = created_at_max
    if updated_at_min:
        params["updated_at_min"] = updated_at_min
    if updated_at_max:
        params["updated_at_max"] = updated_at_max
    if fields:
        params["fields"] = fields
    return client.request("GET", "/orders.json", params=params)


def get_order(order_id: int, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /orders/{order_id}.json"""
    client = ShopifyClient()
    params = {"fields": fields} if fields else None
    return client.request("GET", f"/orders/{order_id}.json", params=params)


def update_order(order_id: int, order: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /orders/{order_id}.json"""
    client = ShopifyClient()
    body = {"order": {**order, "id": order_id}}
    return client.request("PUT", f"/orders/{order_id}.json", json_body=body)


def close_order(order_id: int) -> Dict[str, Any]:
    """POST /orders/{order_id}/close.json"""
    client = ShopifyClient()
    return client.request("POST", f"/orders/{order_id}/close.json")


def open_order(order_id: int) -> Dict[str, Any]:
    """POST /orders/{order_id}/open.json"""
    client = ShopifyClient()
    return client.request("POST", f"/orders/{order_id}/open.json")


def cancel_order(order_id: int, reason: Optional[str] = None, restock: bool = True) -> Dict[str, Any]:
    """POST /orders/{order_id}/cancel.json"""
    client = ShopifyClient()
    body: Dict[str, Any] = {}
    if reason:
        body["reason"] = reason
    body["restock"] = restock
    return client.request("POST", f"/orders/{order_id}/cancel.json", json_body=body if body else None)


def list_order_transactions(order_id: int) -> Dict[str, Any]:
    """GET /orders/{order_id}/transactions.json"""
    client = ShopifyClient()
    return client.request("GET", f"/orders/{order_id}/transactions.json")


def create_refund(order_id: int, refund: Dict[str, Any]) -> Dict[str, Any]:
    """POST /orders/{order_id}/refunds.json"""
    client = ShopifyClient()
    return client.request("POST", f"/orders/{order_id}/refunds.json", json_body={"refund": refund})


def list_draft_orders(limit: int = 50, status: str = "any") -> Dict[str, Any]:
    """GET /draft_orders.json"""
    client = ShopifyClient()
    return client.request("GET", "/draft_orders.json", params={"limit": limit, "status": status})


def get_draft_order(draft_order_id: int) -> Dict[str, Any]:
    """GET /draft_orders/{draft_order_id}.json"""
    client = ShopifyClient()
    return client.request("GET", f"/draft_orders/{draft_order_id}.json")


def create_draft_order(draft_order: Dict[str, Any]) -> Dict[str, Any]:
    """POST /draft_orders.json"""
    client = ShopifyClient()
    return client.request("POST", "/draft_orders.json", json_body={"draft_order": draft_order})


def update_draft_order(draft_order_id: int, draft_order: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /draft_orders/{draft_order_id}.json"""
    client = ShopifyClient()
    body = {"draft_order": {**draft_order, "id": draft_order_id}}
    return client.request("PUT", f"/draft_orders/{draft_order_id}.json", json_body=body)


def complete_draft_order(draft_order_id: int, payment_pending: bool = False) -> Dict[str, Any]:
    """PUT /draft_orders/{draft_order_id}/complete.json"""
    client = ShopifyClient()
    params = {"payment_pending": "true" if payment_pending else "false"}
    return client.request("PUT", f"/draft_orders/{draft_order_id}/complete.json", params=params)
