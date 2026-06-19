from typing import Any, Dict, Optional

from .shopify_client import ShopifyClient, build_params


def create_order(order: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /admin/api/2026-01/orders.json"""
    client = client or ShopifyClient()
    return client.request("POST", "/orders.json", json={"order": order})


def list_orders(
    *,
    status: Optional[str] = None,
    ids: Optional[str] = None,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
    processed_at_min: Optional[str] = None,
    processed_at_max: Optional[str] = None,
    attribution_app_id: Optional[int] = None,
    financial_status: Optional[str] = None,
    fulfillment_status: Optional[str] = None,
    fields: Optional[str] = None,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/orders.json"""
    client = client or ShopifyClient()
    params = build_params(
        status=status,
        ids=ids,
        limit=limit,
        since_id=since_id,
        created_at_min=created_at_min,
        created_at_max=created_at_max,
        updated_at_min=updated_at_min,
        updated_at_max=updated_at_max,
        processed_at_min=processed_at_min,
        processed_at_max=processed_at_max,
        attribution_app_id=attribution_app_id,
        financial_status=financial_status,
        fulfillment_status=fulfillment_status,
        fields=fields,
    )
    return client.request("GET", "/orders.json", params=params)


def get_order(order_id: int, *, fields: Optional[str] = None, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/orders/{order_id}.json"""
    client = client or ShopifyClient()
    params = build_params(fields=fields)
    return client.request("GET", f"/orders/{order_id}.json", params=params)


def count_orders(
    *,
    status: Optional[str] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
    processed_at_min: Optional[str] = None,
    processed_at_max: Optional[str] = None,
    financial_status: Optional[str] = None,
    fulfillment_status: Optional[str] = None,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """GET /admin/api/2026-01/orders/count.json"""
    client = client or ShopifyClient()
    params = build_params(
        status=status,
        created_at_min=created_at_min,
        created_at_max=created_at_max,
        updated_at_min=updated_at_min,
        updated_at_max=updated_at_max,
        processed_at_min=processed_at_min,
        processed_at_max=processed_at_max,
        financial_status=financial_status,
        fulfillment_status=fulfillment_status,
    )
    return client.request("GET", "/orders/count.json", params=params)


def update_order(order_id: int, order: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """PUT /admin/api/2026-01/orders/{order_id}.json"""
    client = client or ShopifyClient()
    return client.request("PUT", f"/orders/{order_id}.json", json={"order": order})


def delete_order(order_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """DELETE /admin/api/2026-01/orders/{order_id}.json"""
    client = client or ShopifyClient()
    return client.request("DELETE", f"/orders/{order_id}.json")


def cancel_order(
    order_id: int,
    *,
    amount: Optional[str] = None,
    currency: Optional[str] = None,
    email: Optional[bool] = None,
    reason: Optional[str] = None,
    restock: Optional[bool] = None,
    refund: Optional[bool] = None,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """POST /admin/api/2026-01/orders/{order_id}/cancel.json"""
    client = client or ShopifyClient()
    payload = build_params(amount=amount, currency=currency, email=email, reason=reason, restock=restock, refund=refund)
    return client.request("POST", f"/orders/{order_id}/cancel.json", json=payload or {})


def close_order(order_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /admin/api/2026-01/orders/{order_id}/close.json"""
    client = client or ShopifyClient()
    return client.request("POST", f"/orders/{order_id}/close.json", json={})


def open_order(order_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /admin/api/2026-01/orders/{order_id}/open.json"""
    client = client or ShopifyClient()
    return client.request("POST", f"/orders/{order_id}/open.json", json={})
