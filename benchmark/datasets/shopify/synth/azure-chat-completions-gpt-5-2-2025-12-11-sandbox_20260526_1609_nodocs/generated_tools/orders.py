from typing import Any, Dict, Optional

from .client import ShopifyClient


def list_orders(limit: int = 50, status: str = "any", page_info: Optional[str] = None, **filters: Any) -> Dict[str, Any]:
    """GET /orders.json"""
    params: Dict[str, Any] = {"limit": limit, "status": status}
    if page_info:
        params["page_info"] = page_info
    params.update({k: v for k, v in filters.items() if v is not None})
    return ShopifyClient().request("GET", "/orders.json", params=params)


def get_order(order_id: int) -> Dict[str, Any]:
    """GET /orders/{id}.json"""
    return ShopifyClient().request("GET", f"/orders/{order_id}.json")


def update_order(order_id: int, order: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /orders/{id}.json"""
    return ShopifyClient().request("PUT", f"/orders/{order_id}.json", json={"order": order})


def close_order(order_id: int) -> Dict[str, Any]:
    """POST /orders/{id}/close.json"""
    return ShopifyClient().request("POST", f"/orders/{order_id}/close.json")


def open_order(order_id: int) -> Dict[str, Any]:
    """POST /orders/{id}/open.json"""
    return ShopifyClient().request("POST", f"/orders/{order_id}/open.json")


def cancel_order(order_id: int, **body: Any) -> Dict[str, Any]:
    """POST /orders/{id}/cancel.json"""
    return ShopifyClient().request("POST", f"/orders/{order_id}/cancel.json", json=body or None)


def create_draft_order(draft_order: Dict[str, Any]) -> Dict[str, Any]:
    """POST /draft_orders.json"""
    return ShopifyClient().request("POST", "/draft_orders.json", json={"draft_order": draft_order})


def list_draft_orders(limit: int = 50) -> Dict[str, Any]:
    """GET /draft_orders.json"""
    return ShopifyClient().request("GET", "/draft_orders.json", params={"limit": limit})


def get_draft_order(draft_order_id: int) -> Dict[str, Any]:
    """GET /draft_orders/{id}.json"""
    return ShopifyClient().request("GET", f"/draft_orders/{draft_order_id}.json")


def update_draft_order(draft_order_id: int, draft_order: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /draft_orders/{id}.json"""
    return ShopifyClient().request("PUT", f"/draft_orders/{draft_order_id}.json", json={"draft_order": draft_order})


def complete_draft_order(draft_order_id: int, payment_pending: bool = False) -> Dict[str, Any]:
    """PUT /draft_orders/{id}/complete.json"""
    params = {"payment_pending": "true" if payment_pending else "false"}
    return ShopifyClient().request("PUT", f"/draft_orders/{draft_order_id}/complete.json", params=params)


def create_refund(order_id: int, refund: Dict[str, Any]) -> Dict[str, Any]:
    """POST /orders/{id}/refunds.json"""
    return ShopifyClient().request("POST", f"/orders/{order_id}/refunds.json", json={"refund": refund})


def list_transactions(order_id: int) -> Dict[str, Any]:
    """GET /orders/{id}/transactions.json"""
    return ShopifyClient().request("GET", f"/orders/{order_id}/transactions.json")


def create_transaction(order_id: int, transaction: Dict[str, Any]) -> Dict[str, Any]:
    """POST /orders/{id}/transactions.json"""
    return ShopifyClient().request("POST", f"/orders/{order_id}/transactions.json", json={"transaction": transaction})
