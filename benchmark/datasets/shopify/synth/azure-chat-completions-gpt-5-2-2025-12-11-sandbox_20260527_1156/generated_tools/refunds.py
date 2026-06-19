from typing import Any, Dict, Optional

from ._client import get_client


def calculate_refund(order_id: int, refund: Dict[str, Any]) -> Dict[str, Any]:
    """POST /orders/{order_id}/refunds/calculate.json

    Doc: docs/api_refund.md
    Body wrapper: {"refund": {...}}
    """
    client = get_client()
    return client.request(
        "POST", f"/orders/{order_id}/refunds/calculate.json", json={"refund": refund}
    )


def create_refund(order_id: int, refund: Dict[str, Any]) -> Dict[str, Any]:
    """POST /orders/{order_id}/refunds.json

    Doc: docs/api_refund.md
    Body wrapper: {"refund": {...}}
    """
    client = get_client()
    return client.request("POST", f"/orders/{order_id}/refunds.json", json={"refund": refund})


def list_refunds(order_id: int) -> Dict[str, Any]:
    """GET /orders/{order_id}/refunds.json

    Doc: docs/api_refund.md
    """
    client = get_client()
    return client.request("GET", f"/orders/{order_id}/refunds.json")


def get_refund(order_id: int, refund_id: int) -> Dict[str, Any]:
    """GET /orders/{order_id}/refunds/{refund_id}.json

    Doc: docs/api_refund.md
    """
    client = get_client()
    return client.request("GET", f"/orders/{order_id}/refunds/{refund_id}.json")
