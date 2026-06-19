from typing import Any, Dict, Optional

from .shopify_client import ShopifyClient, build_params


def create_draft_order(
    draft_order: Dict[str, Any],
    *,
    customer_id: Optional[int] = None,
    use_customer_default_address: Optional[bool] = None,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """POST /admin/api/2026-01/draft_orders.json"""
    client = client or ShopifyClient()
    params = build_params(customer_id=customer_id, use_customer_default_address=use_customer_default_address)
    return client.request("POST", "/draft_orders.json", params=params, json={"draft_order": draft_order})


def list_draft_orders(
    *,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
    status: Optional[str] = None,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/draft_orders.json"""
    client = client or ShopifyClient()
    params = build_params(
        limit=limit,
        since_id=since_id,
        created_at_min=created_at_min,
        created_at_max=created_at_max,
        updated_at_min=updated_at_min,
        updated_at_max=updated_at_max,
        status=status,
    )
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
    return client.request("PUT", f"/draft_orders/{draft_order_id}.json", json={"draft_order": draft_order})


def complete_draft_order(
    draft_order_id: int,
    *,
    payment_pending: Optional[bool] = None,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/draft_orders/{draft_order_id}/complete.json"""
    client = client or ShopifyClient()
    params = build_params(payment_pending=payment_pending)
    return client.request("PUT", f"/draft_orders/{draft_order_id}/complete.json", params=params, json={})


def send_draft_order_invoice(
    draft_order_id: int,
    invoice: Dict[str, Any],
    *,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """POST /admin/api/2026-01/draft_orders/{draft_order_id}/send_invoice.json"""
    client = client or ShopifyClient()
    return client.request("POST", f"/draft_orders/{draft_order_id}/send_invoice.json", json={"draft_order_invoice": invoice})


def delete_draft_order(draft_order_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/draft_orders/{draft_order_id}.json"""
    client = client or ShopifyClient()
    return client.request("DELETE", f"/draft_orders/{draft_order_id}.json")
