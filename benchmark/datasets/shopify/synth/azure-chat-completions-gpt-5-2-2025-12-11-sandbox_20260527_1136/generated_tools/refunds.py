from typing import Any, Dict, Optional

from .client import ShopifyClient


def calculate_refund(order_id: int, refund: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /orders/{order_id}/refunds/calculate.json"""
    client = client or ShopifyClient()
    return client.request("POST", f"/orders/{order_id}/refunds/calculate.json", json_body={"refund": refund})


def create_refund(order_id: int, refund: Dict[str, Any], *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """POST /orders/{order_id}/refunds.json"""
    client = client or ShopifyClient()
    return client.request("POST", f"/orders/{order_id}/refunds.json", json_body={"refund": refund})


def list_refunds(order_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /orders/{order_id}/refunds.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/orders/{order_id}/refunds.json")


def get_refund(order_id: int, refund_id: int, *, client: Optional[ShopifyClient] = None) -> Dict[str, Any]:
    """GET /orders/{order_id}/refunds/{refund_id}.json"""
    client = client or ShopifyClient()
    return client.request("GET", f"/orders/{order_id}/refunds/{refund_id}.json")
