from typing import Any, Dict, Optional

from .http_client import request_json


def create_draft_order(draft_order: Dict[str, Any]) -> Dict[str, Any]:
    """POST /draft_orders.json

    Doc: docs/api_draftorder.md
    Body wrapper: {"draft_order": {...}}
    """
    return request_json("POST", "/draft_orders.json", json_body={"draft_order": draft_order})


def list_draft_orders(*, limit: Optional[int] = None, since_id: Optional[int] = None, status: Optional[str] = None) -> Dict[str, Any]:
    """GET /draft_orders.json

    Doc: docs/api_draftorder.md
    """
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if since_id is not None:
        params["since_id"] = since_id
    if status is not None:
        params["status"] = status
    return request_json("GET", "/draft_orders.json", params=params)


def get_draft_order(draft_order_id: int) -> Dict[str, Any]:
    """GET /draft_orders/{draft_order_id}.json

    Doc: docs/api_draftorder.md
    """
    return request_json("GET", f"/draft_orders/{draft_order_id}.json")


def count_draft_orders(*, status: Optional[str] = None) -> Dict[str, Any]:
    """GET /draft_orders/count.json

    Doc: docs/api_draftorder.md
    """
    params: Dict[str, Any] = {}
    if status is not None:
        params["status"] = status
    return request_json("GET", "/draft_orders/count.json", params=params)


def update_draft_order(draft_order_id: int, draft_order: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /draft_orders/{draft_order_id}.json

    Doc: docs/api_draftorder.md
    Body wrapper: {"draft_order": {...}}
    """
    return request_json("PUT", f"/draft_orders/{draft_order_id}.json", json_body={"draft_order": draft_order})


def delete_draft_order(draft_order_id: int) -> Dict[str, Any]:
    """DELETE /draft_orders/{draft_order_id}.json

    Doc: docs/api_draftorder.md
    """
    return request_json("DELETE", f"/draft_orders/{draft_order_id}.json")


def complete_draft_order(draft_order_id: int, *, payment_pending: Optional[bool] = None) -> Dict[str, Any]:
    """PUT /draft_orders/{draft_order_id}/complete.json

    Doc: docs/api_draftorder.md
    """
    params: Dict[str, Any] = {}
    if payment_pending is not None:
        params["payment_pending"] = payment_pending
    return request_json("PUT", f"/draft_orders/{draft_order_id}/complete.json", params=params)


def send_draft_order_invoice(draft_order_id: int, invoice: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /draft_orders/{draft_order_id}/send_invoice.json

    Doc: docs/api_draftorder.md
    Body wrapper: {"draft_order_invoice": {...}} (optional)
    """
    body = {"draft_order_invoice": invoice} if invoice is not None else None
    return request_json("POST", f"/draft_orders/{draft_order_id}/send_invoice.json", json_body=body)
