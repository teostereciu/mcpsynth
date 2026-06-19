from typing import Any, Dict, Optional

from .shopify_client import ShopifyClient


def calculate_refund(order_id: int, refund: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /admin/api/2026-01/orders/{order_id}/refunds/calculate.json"""
    client = client or ShopifyClient()
    return client.request("POST", f"/orders/{order_id}/refunds/calculate.json", json={"refund": refund})


def create_refund(order_id: int, refund: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /admin/api/2026-01/orders/{order_id}/refunds.json"""
    client = client or ShopifyClient()
    return client.request("POST", f"/orders/{order_id}/refunds.json", json={"refund": refund})


def list_refunds(order_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/orders/{order_id}/refunds.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/orders/{order_id}/refunds.json")


def get_refund(order_id: int, refund_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /admin/api/2026-01/orders/{order_id}/refunds/{refund_id}.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/orders/{order_id}/refunds/{refund_id}.json")
