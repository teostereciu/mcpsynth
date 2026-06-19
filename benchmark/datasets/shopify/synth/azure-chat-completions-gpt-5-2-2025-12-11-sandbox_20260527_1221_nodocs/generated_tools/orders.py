from typing import Any, Dict, Optional

from .client import request_json


def list_orders(
    *,
    limit: int = 50,
    status: str = "any",
    financial_status: Optional[str] = None,
    fulfillment_status: Optional[str] = None,
    since_id: Optional[int] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    fields: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit, "status": status}
    if financial_status is not None:
        params["financial_status"] = financial_status
    if fulfillment_status is not None:
        params["fulfillment_status"] = fulfillment_status
    if since_id is not None:
        params["since_id"] = since_id
    if created_at_min is not None:
        params["created_at_min"] = created_at_min
    if created_at_max is not None:
        params["created_at_max"] = created_at_max
    if fields is not None:
        params["fields"] = fields
    return request_json("GET", "/orders.json", params=params)


def get_order(order_id: int, *, fields: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if fields is not None:
        params["fields"] = fields
    return request_json("GET", f"/orders/{order_id}.json", params=params or None)


def update_order(order_id: int, order: Dict[str, Any]) -> Dict[str, Any]:
    body = {"order": {**order, "id": order_id}}
    return request_json("PUT", f"/orders/{order_id}.json", json_body=body)


def close_order(order_id: int) -> Dict[str, Any]:
    return request_json("POST", f"/orders/{order_id}/close.json")


def open_order(order_id: int) -> Dict[str, Any]:
    return request_json("POST", f"/orders/{order_id}/open.json")


def cancel_order(order_id: int, *, reason: Optional[str] = None, email: Optional[bool] = None, restock: Optional[bool] = None) -> Dict[str, Any]:
    body: Dict[str, Any] = {}
    if reason is not None:
        body["reason"] = reason
    if email is not None:
        body["email"] = email
    if restock is not None:
        body["restock"] = restock
    return request_json("POST", f"/orders/{order_id}/cancel.json", json_body=body or None)


# Draft orders

def list_draft_orders(*, limit: int = 50, since_id: Optional[int] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if since_id is not None:
        params["since_id"] = since_id
    return request_json("GET", "/draft_orders.json", params=params)


def get_draft_order(draft_order_id: int) -> Dict[str, Any]:
    return request_json("GET", f"/draft_orders/{draft_order_id}.json")


def create_draft_order(draft_order: Dict[str, Any]) -> Dict[str, Any]:
    return request_json("POST", "/draft_orders.json", json_body={"draft_order": draft_order})


def update_draft_order(draft_order_id: int, draft_order: Dict[str, Any]) -> Dict[str, Any]:
    body = {"draft_order": {**draft_order, "id": draft_order_id}}
    return request_json("PUT", f"/draft_orders/{draft_order_id}.json", json_body=body)


def complete_draft_order(draft_order_id: int, *, payment_pending: Optional[bool] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if payment_pending is not None:
        params["payment_pending"] = str(payment_pending).lower()
    return request_json("PUT", f"/draft_orders/{draft_order_id}/complete.json", params=params or None)


def delete_draft_order(draft_order_id: int) -> Dict[str, Any]:
    return request_json("DELETE", f"/draft_orders/{draft_order_id}.json")


# Refunds

def calculate_refund(order_id: int, refund: Dict[str, Any]) -> Dict[str, Any]:
    return request_json("POST", f"/orders/{order_id}/refunds/calculate.json", json_body={"refund": refund})


def create_refund(order_id: int, refund: Dict[str, Any]) -> Dict[str, Any]:
    return request_json("POST", f"/orders/{order_id}/refunds.json", json_body={"refund": refund})


def list_transactions(order_id: int) -> Dict[str, Any]:
    return request_json("GET", f"/orders/{order_id}/transactions.json")
