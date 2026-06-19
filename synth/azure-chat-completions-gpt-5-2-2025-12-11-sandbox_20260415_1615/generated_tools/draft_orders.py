from typing import Any, Dict, Optional

from .http_client import get_client


def draft_order_create(draft_order: Dict[str, Any]) -> Dict[str, Any]:
    """POST /draft_orders.json"""
    return get_client().request("POST", "/draft_orders.json", json_body={"draft_order": draft_order})


def draft_orders_list(*, limit: Optional[int] = None, since_id: Optional[int] = None) -> Dict[str, Any]:
    """GET /draft_orders.json"""
    params: Dict[str, Any] = {}
    for k, v in {"limit": limit, "since_id": since_id}.items():
        if v is not None:
            params[k] = v
    return get_client().request("GET", "/draft_orders.json", params=params or None)


def draft_order_get(draft_order_id: int) -> Dict[str, Any]:
    """GET /draft_orders/{draft_order_id}.json"""
    return get_client().request("GET", f"/draft_orders/{draft_order_id}.json")


def draft_orders_count() -> Dict[str, Any]:
    """GET /draft_orders/count.json"""
    return get_client().request("GET", "/draft_orders/count.json")


def draft_order_update(draft_order_id: int, draft_order: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /draft_orders/{draft_order_id}.json"""
    body = {"draft_order": {**draft_order, "id": draft_order_id}}
    return get_client().request("PUT", f"/draft_orders/{draft_order_id}.json", json_body=body)


def draft_order_delete(draft_order_id: int) -> Dict[str, Any]:
    """DELETE /draft_orders/{draft_order_id}.json"""
    return get_client().request("DELETE", f"/draft_orders/{draft_order_id}.json")


def draft_order_complete(draft_order_id: int, *, payment_pending: Optional[bool] = None) -> Dict[str, Any]:
    """PUT /draft_orders/{draft_order_id}/complete.json"""
    params = {"payment_pending": payment_pending} if payment_pending is not None else None
    return get_client().request("PUT", f"/draft_orders/{draft_order_id}/complete.json", params=params)


def draft_order_send_invoice(draft_order_id: int, invoice: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /draft_orders/{draft_order_id}/send_invoice.json"""
    body = {"draft_order_invoice": invoice} if invoice else None
    return get_client().request("POST", f"/draft_orders/{draft_order_id}/send_invoice.json", json_body=body)
