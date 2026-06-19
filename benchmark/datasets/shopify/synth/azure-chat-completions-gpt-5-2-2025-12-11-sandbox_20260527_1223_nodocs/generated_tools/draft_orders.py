from typing import Any, Dict, Optional

from .client import shopify_request


def list_draft_orders(*, limit: int = 50, since_id: Optional[int] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if since_id is not None:
        params["since_id"] = since_id
    return shopify_request("GET", "/draft_orders.json", params=params)


def get_draft_order(*, draft_order_id: int) -> Dict[str, Any]:
    return shopify_request("GET", f"/draft_orders/{draft_order_id}.json")


def create_draft_order(*, draft_order: Dict[str, Any]) -> Dict[str, Any]:
    return shopify_request("POST", "/draft_orders.json", json_body={"draft_order": draft_order})


def update_draft_order(*, draft_order_id: int, draft_order: Dict[str, Any]) -> Dict[str, Any]:
    body = {"draft_order": {**draft_order, "id": draft_order_id}}
    return shopify_request("PUT", f"/draft_orders/{draft_order_id}.json", json_body=body)


def delete_draft_order(*, draft_order_id: int) -> Dict[str, Any]:
    return shopify_request("DELETE", f"/draft_orders/{draft_order_id}.json")


def complete_draft_order(*, draft_order_id: int, payment_pending: Optional[bool] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if payment_pending is not None:
        params["payment_pending"] = payment_pending
    return shopify_request("PUT", f"/draft_orders/{draft_order_id}/complete.json", params=params if params else None)


def send_draft_order_invoice(*, draft_order_id: int, invoice: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    body = {"draft_order_invoice": invoice or {}}
    return shopify_request("POST", f"/draft_orders/{draft_order_id}/send_invoice.json", json_body=body)
