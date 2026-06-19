from typing import Any, Dict, Optional

from .http import request_json


def create_draft_order(draft_order: Dict[str, Any]) -> Dict[str, Any]:
    """POST /draft_orders.json"""
    return request_json("POST", "/draft_orders.json", json_body={"draft_order": draft_order})


def list_draft_orders(
    *,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    status: Optional[str] = None,
    fields: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /draft_orders.json"""
    params: Dict[str, Any] = {}
    for k, v in {
        "limit": limit,
        "since_id": since_id,
        "updated_at_min": updated_at_min,
        "updated_at_max": updated_at_max,
        "created_at_min": created_at_min,
        "created_at_max": created_at_max,
        "status": status,
        "fields": fields,
    }.items():
        if v is not None:
            params[k] = v
    return request_json("GET", "/draft_orders.json", params=params)


def get_draft_order(draft_order_id: int, *, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /draft_orders/{draft_order_id}.json"""
    params = {"fields": fields} if fields else None
    return request_json("GET", f"/draft_orders/{draft_order_id}.json", params=params)


def count_draft_orders(*, status: Optional[str] = None) -> Dict[str, Any]:
    """GET /draft_orders/count.json"""
    params = {"status": status} if status else None
    return request_json("GET", "/draft_orders/count.json", params=params)


def update_draft_order(draft_order_id: int, draft_order: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /draft_orders/{draft_order_id}.json"""
    return request_json(
        "PUT",
        f"/draft_orders/{draft_order_id}.json",
        json_body={"draft_order": draft_order},
    )


def delete_draft_order(draft_order_id: int) -> Dict[str, Any]:
    """DELETE /draft_orders/{draft_order_id}.json"""
    return request_json("DELETE", f"/draft_orders/{draft_order_id}.json")


def complete_draft_order(draft_order_id: int, *, payment_pending: Optional[bool] = None) -> Dict[str, Any]:
    """PUT /draft_orders/{draft_order_id}/complete.json"""
    params = {"payment_pending": payment_pending} if payment_pending is not None else None
    return request_json("PUT", f"/draft_orders/{draft_order_id}/complete.json", params=params)


def send_draft_order_invoice(draft_order_id: int, invoice: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /draft_orders/{draft_order_id}/send_invoice.json"""
    body = {"draft_order_invoice": invoice} if invoice is not None else None
    return request_json("POST", f"/draft_orders/{draft_order_id}/send_invoice.json", json_body=body)
