from typing import Any, Dict, Optional

from .client import ShopifyClient


def create_draft_order(draft_order: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /admin/api/2026-01/draft_orders.json"""
    client = client or ShopifyClient()
    return client.request("POST", "/draft_orders.json", json_body={"draft_order": draft_order})


def send_draft_order_invoice(
    draft_order_id: int,
    invoice: Optional[Dict[str, Any]] = None,
    *,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """POST /admin/api/2026-01/draft_orders/{draft_order_id}/send_invoice.json"""
    client = client or ShopifyClient()
    body = {"draft_order_invoice": invoice} if invoice is not None else None
    return client.request("POST", f"/draft_orders/{draft_order_id}/send_invoice.json", json_body=body)


def list_draft_orders(
    *,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
    status: Optional[str] = None,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/draft_orders.json"""
    client = client or ShopifyClient()
    params: Dict[str, Any] = {}
    for k, v in {
        "limit": limit,
        "since_id": since_id,
        "updated_at_min": updated_at_min,
        "updated_at_max": updated_at_max,
        "status": status,
    }.items():
        if v is not None:
            params[k] = v
    return client.request("GET", "/draft_orders.json", params=params)


def get_draft_order(draft_order_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/draft_orders/{draft_order_id}.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/draft_orders/{draft_order_id}.json")


def count_draft_orders(*, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/draft_orders/count.json"""
    client = client or ShopifyClient()
    return client.request("GET", "/draft_orders/count.json")


def update_draft_order(draft_order_id: int, draft_order: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/draft_orders/{draft_order_id}.json"""
    client = client or ShopifyClient()
    return client.request("PUT", f"/draft_orders/{draft_order_id}.json", json_body={"draft_order": draft_order})


def complete_draft_order(
    draft_order_id: int,
    *,
    payment_pending: Optional[bool] = None,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/draft_orders/{draft_order_id}/complete.json"""
    client = client or ShopifyClient()
    params: Dict[str, Any] = {}
    if payment_pending is not None:
        params["payment_pending"] = str(payment_pending).lower()
    return client.request("PUT", f"/draft_orders/{draft_order_id}/complete.json", params=params)


def delete_draft_order(draft_order_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/draft_orders/{draft_order_id}.json"""
    client = client or ShopifyClient()
    return client.request("DELETE", f"/draft_orders/{draft_order_id}.json")
