from typing import Any, Dict, Optional

from ._client import get_client


def create_draft_order(draft_order: Dict[str, Any]) -> Dict[str, Any]:
    """POST /draft_orders.json

    Doc: docs/api_draftorder.md
    """
    return get_client().request("POST", "/draft_orders.json", json_body={"draft_order": draft_order})


def list_draft_orders(*, limit: Optional[int] = None, since_id: Optional[int] = None) -> Dict[str, Any]:
    """GET /draft_orders.json

    Doc: docs/api_draftorder.md
    """
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if since_id is not None:
        params["since_id"] = since_id
    return get_client().request("GET", "/draft_orders.json", params=params)


def get_draft_order(draft_order_id: int) -> Dict[str, Any]:
    """GET /draft_orders/{draft_order_id}.json

    Doc: docs/api_draftorder.md
    """
    return get_client().request("GET", f"/draft_orders/{draft_order_id}.json")


def count_draft_orders() -> Dict[str, Any]:
    """GET /draft_orders/count.json

    Doc: docs/api_draftorder.md
    """
    return get_client().request("GET", "/draft_orders/count.json")


def update_draft_order(draft_order_id: int, draft_order: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /draft_orders/{draft_order_id}.json

    Doc: docs/api_draftorder.md
    """
    return get_client().request(
        "PUT",
        f"/draft_orders/{draft_order_id}.json",
        json_body={"draft_order": {**draft_order, "id": draft_order_id}},
    )


def delete_draft_order(draft_order_id: int) -> Dict[str, Any]:
    """DELETE /draft_orders/{draft_order_id}.json

    Doc: docs/api_draftorder.md
    """
    return get_client().request("DELETE", f"/draft_orders/{draft_order_id}.json")


def complete_draft_order(draft_order_id: int, *, payment_pending: Optional[bool] = None) -> Dict[str, Any]:
    """PUT /draft_orders/{draft_order_id}/complete.json

    Doc: docs/api_draftorder.md
    """
    params: Dict[str, Any] = {}
    if payment_pending is not None:
        params["payment_pending"] = str(payment_pending).lower()
    return get_client().request("PUT", f"/draft_orders/{draft_order_id}/complete.json", params=params)


def send_draft_order_invoice(draft_order_id: int, invoice: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /draft_orders/{draft_order_id}/send_invoice.json

    Doc: docs/api_draftorder.md
    """
    body = {"draft_order_invoice": invoice} if invoice is not None else None
    return get_client().request("POST", f"/draft_orders/{draft_order_id}/send_invoice.json", json_body=body)
