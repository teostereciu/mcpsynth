from typing import Any, Dict, Optional

from .http_client import ShopifyClient


def draft_order_create(draft_order: Dict[str, Any]) -> Dict[str, Any]:
    """POST /admin/api/2026-01/draft_orders.json"""
    client = ShopifyClient()
    return client.request(
        "POST", "/draft_orders.json", json_body={"draft_order": draft_order}
    )


def draft_orders_list(
    *,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    status: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
    fields: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/draft_orders.json"""
    client = ShopifyClient()
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


def draft_order_get(draft_order_id: int) -> Dict[str, Any]:
    """GET /admin/api/2026-01/draft_orders/{draft_order_id}.json"""
    client = ShopifyClient()
    return client.request("GET", f"/draft_orders/{draft_order_id}.json")


def draft_orders_count() -> Dict[str, Any]:
    """GET /admin/api/2026-01/draft_orders/count.json"""
    client = ShopifyClient()
    return client.request("GET", "/draft_orders/count.json")


def draft_order_update(draft_order_id: int, draft_order: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/draft_orders/{draft_order_id}.json"""
    client = ShopifyClient()
    body = {"draft_order": {**draft_order, "id": draft_order_id}}
    return client.request("PUT", f"/draft_orders/{draft_order_id}.json", json_body=body)


def draft_order_delete(draft_order_id: int) -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/draft_orders/{draft_order_id}.json"""
    client = ShopifyClient()
    return client.request("DELETE", f"/draft_orders/{draft_order_id}.json")


def draft_order_complete(draft_order_id: int, *, payment_pending: Optional[bool] = None) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/draft_orders/{draft_order_id}/complete.json"""
    client = ShopifyClient()
    params = {"payment_pending": str(payment_pending).lower()} if payment_pending is not None else None
    return client.request("PUT", f"/draft_orders/{draft_order_id}/complete.json", params=params)


def draft_order_send_invoice(draft_order_id: int, invoice: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /admin/api/2026-01/draft_orders/{draft_order_id}/send_invoice.json"""
    client = ShopifyClient()
    return client.request(
        "POST",
        f"/draft_orders/{draft_order_id}/send_invoice.json",
        json_body={"draft_order_invoice": invoice} if invoice else None,
    )
