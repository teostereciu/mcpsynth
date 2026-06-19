from typing import Any, Dict, Optional

from .shopify_client import ShopifyClient, build_params


def create_transaction(
    order_id: int,
    transaction: Dict[str, Any],
    *,
    source: Optional[str] = None,
    client: Optional[ShopifyClient] = None,
) -> Dict[str, Any]:
    """POST /admin/api/2026-01/orders/{order_id}/transactions.json"""
    client = client or ShopifyClient()
    params = build_params(source=source)
    return client.request("POST", f"/orders/{order_id}/transactions.json", params=params, json={"transaction": transaction})


def list_transactions(order_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/orders/{order_id}/transactions.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/orders/{order_id}/transactions.json")


def get_transaction(order_id: int, transaction_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/orders/{order_id}/transactions/{transaction_id}.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/orders/{order_id}/transactions/{transaction_id}.json")


def count_transactions(order_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/orders/{order_id}/transactions/count.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/orders/{order_id}/transactions/count.json")
