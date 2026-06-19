from typing import Any, Dict, Optional

from .client import request_json


# Orders

def list_orders(
    *,
    limit: int = 50,
    status: str = "any",
    financial_status: Optional[str] = None,
    fulfillment_status: Optional[str] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
    fields: Optional[str] = None,
) -> Any:
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
    return request_json("GET", "/orders.json", params=params)


def get_order(order_id: int, *, fields: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    if fields:
        params["fields"] = fields
    return request_json("GET", f"/orders/{order_id}.json", params=params)


def update_order(order_id: int, order: Dict[str, Any]) -> Any:
    return request_json("PUT", f"/orders/{order_id}.json", json={"order": order})


def close_order(order_id: int) -> Any:
    return request_json("POST", f"/orders/{order_id}/close.json")


def open_order(order_id: int) -> Any:
    return request_json("POST", f"/orders/{order_id}/open.json")


def cancel_order(order_id: int, *, reason: Optional[str] = None, email: Optional[bool] = None, restock: Optional[bool] = None) -> Any:
    payload: Dict[str, Any] = {}
    if reason:
        payload["reason"] = reason
    if email is not None:
        payload["email"] = email
    if restock is not None:
        payload["restock"] = restock
    return request_json("POST", f"/orders/{order_id}/cancel.json", json=payload if payload else None)


# Draft orders

def list_draft_orders(*, limit: int = 50, status: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {"limit": limit}
    if status:
        params["status"] = status
    return request_json("GET", "/draft_orders.json", params=params)


def get_draft_order(draft_order_id: int) -> Any:
    return request_json("GET", f"/draft_orders/{draft_order_id}.json")


def create_draft_order(draft_order: Dict[str, Any]) -> Any:
    return request_json("POST", "/draft_orders.json", json={"draft_order": draft_order})


def update_draft_order(draft_order_id: int, draft_order: Dict[str, Any]) -> Any:
    return request_json("PUT", f"/draft_orders/{draft_order_id}.json", json={"draft_order": draft_order})


def complete_draft_order(draft_order_id: int, *, payment_pending: Optional[bool] = None) -> Any:
    params: Dict[str, Any] = {}
    if payment_pending is not None:
        params["payment_pending"] = str(payment_pending).lower()
    return request_json("PUT", f"/draft_orders/{draft_order_id}/complete.json", params=params)


# Refunds

def calculate_refund(order_id: int, refund: Dict[str, Any]) -> Any:
    return request_json("POST", f"/orders/{order_id}/refunds/calculate.json", json={"refund": refund})


def create_refund(order_id: int, refund: Dict[str, Any]) -> Any:
    return request_json("POST", f"/orders/{order_id}/refunds.json", json={"refund": refund})


def list_transactions(order_id: int) -> Any:
    return request_json("GET", f"/orders/{order_id}/transactions.json")


def get_transaction(order_id: int, transaction_id: int) -> Any:
    return request_json("GET", f"/orders/{order_id}/transactions/{transaction_id}.json")


def create_transaction(order_id: int, transaction: Dict[str, Any]) -> Any:
    return request_json("POST", f"/orders/{order_id}/transactions.json", json={"transaction": transaction})
