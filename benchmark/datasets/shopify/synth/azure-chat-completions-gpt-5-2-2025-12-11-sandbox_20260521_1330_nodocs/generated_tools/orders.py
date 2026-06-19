from typing import Any, Dict, Optional

from .client import request_json


def list_orders(limit: int = 50, status: str = "any", **filters: Any) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit, "status": status}
    params.update({k: v for k, v in filters.items() if v is not None})
    return request_json("GET", "/orders.json", params=params)


def get_order(order_id: int) -> Dict[str, Any]:
    return request_json("GET", f"/orders/{order_id}.json")


def update_order(order_id: int, order: Dict[str, Any]) -> Dict[str, Any]:
    return request_json("PUT", f"/orders/{order_id}.json", json={"order": order})


def close_order(order_id: int) -> Dict[str, Any]:
    return request_json("POST", f"/orders/{order_id}/close.json")


def open_order(order_id: int) -> Dict[str, Any]:
    return request_json("POST", f"/orders/{order_id}/open.json")


def cancel_order(order_id: int, reason: Optional[str] = None, email: Optional[bool] = None, restock: Optional[bool] = None) -> Dict[str, Any]:
    payload: Dict[str, Any] = {}
    if reason is not None:
        payload["reason"] = reason
    if email is not None:
        payload["email"] = email
    if restock is not None:
        payload["restock"] = restock
    return request_json("POST", f"/orders/{order_id}/cancel.json", json=payload or None)


def list_transactions(order_id: int) -> Dict[str, Any]:
    return request_json("GET", f"/orders/{order_id}/transactions.json")


def create_refund(order_id: int, refund: Dict[str, Any]) -> Dict[str, Any]:
    return request_json("POST", f"/orders/{order_id}/refunds.json", json={"refund": refund})


def create_draft_order(draft_order: Dict[str, Any]) -> Dict[str, Any]:
    return request_json("POST", "/draft_orders.json", json={"draft_order": draft_order})


def get_draft_order(draft_order_id: int) -> Dict[str, Any]:
    return request_json("GET", f"/draft_orders/{draft_order_id}.json")


def complete_draft_order(draft_order_id: int, payment_pending: Optional[bool] = None) -> Dict[str, Any]:
    payload: Dict[str, Any] = {}
    if payment_pending is not None:
        payload["payment_pending"] = payment_pending
    return request_json("PUT", f"/draft_orders/{draft_order_id}/complete.json", json=payload or None)
