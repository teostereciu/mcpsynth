from typing import Any, Dict, Optional

from ._client import get_client


def create_draft_order(draft_order: Dict[str, Any]) -> Dict[str, Any]:
    """POST /draft_orders.json

    Doc: docs/api_draftorder.md
    Body wrapper: {"draft_order": {...}}
    """
    client = get_client()
    return client.request("POST", "/draft_orders.json", json={"draft_order": draft_order})


def list_draft_orders(
    *,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    status: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
    fields: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /draft_orders.json

    Doc: docs/api_draftorder.md
    """
    client = get_client()
    params: Dict[str, Any] = {}
    for k, v in {
        "limit": limit,
        "since_id": since_id,
        "status": status,
        "updated_at_min": updated_at_min,
        "updated_at_max": updated_at_max,
        "fields": fields,
    }.items():
        if v is not None:
            params[k] = v
    return client.request("GET", "/draft_orders.json", params=params)


def get_draft_order(draft_order_id: int, *, fields: Optional[str] = None) -> Dict[str, Any]:
    """GET /draft_orders/{draft_order_id}.json

    Doc: docs/api_draftorder.md
    """
    client = get_client()
    params = {"fields": fields} if fields else None
    return client.request("GET", f"/draft_orders/{draft_order_id}.json", params=params)


def count_draft_orders(*, status: Optional[str] = None) -> Dict[str, Any]:
    """GET /draft_orders/count.json

    Doc: docs/api_draftorder.md
    """
    client = get_client()
    params = {"status": status} if status else None
    return client.request("GET", "/draft_orders/count.json", params=params)


def update_draft_order(draft_order_id: int, draft_order: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /draft_orders/{draft_order_id}.json

    Doc: docs/api_draftorder.md
    Body wrapper: {"draft_order": {..., "id": draft_order_id}}
    """
    client = get_client()
    body = dict(draft_order)
    body.setdefault("id", draft_order_id)
    return client.request(
        "PUT", f"/draft_orders/{draft_order_id}.json", json={"draft_order": body}
    )


def delete_draft_order(draft_order_id: int) -> Dict[str, Any]:
    """DELETE /draft_orders/{draft_order_id}.json

    Doc: docs/api_draftorder.md
    """
    client = get_client()
    return client.request("DELETE", f"/draft_orders/{draft_order_id}.json")


def send_draft_order_invoice(draft_order_id: int, invoice: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /draft_orders/{draft_order_id}/send_invoice.json

    Doc: docs/api_draftorder.md
    Body wrapper: {"draft_order_invoice": {...}}
    """
    client = get_client()
    payload = {"draft_order_invoice": invoice} if invoice is not None else None
    return client.request("POST", f"/draft_orders/{draft_order_id}/send_invoice.json", json=payload)


def complete_draft_order(draft_order_id: int, *, payment_pending: Optional[bool] = None) -> Dict[str, Any]:
    """PUT /draft_orders/{draft_order_id}/complete.json

    Doc: docs/api_draftorder.md
    """
    client = get_client()
    params = {"payment_pending": payment_pending} if payment_pending is not None else None
    return client.request("PUT", f"/draft_orders/{draft_order_id}/complete.json", params=params)
