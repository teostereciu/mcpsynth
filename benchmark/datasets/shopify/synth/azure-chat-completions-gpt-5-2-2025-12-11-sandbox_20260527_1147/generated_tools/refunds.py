from typing import Any, Dict

from ._client import get_client


def list_refunds(order_id: int) -> Dict[str, Any]:
    """GET /orders/{order_id}/refunds.json

    Doc: docs/api_refund.md
    """
    return get_client().request("GET", f"/orders/{order_id}/refunds.json")


def get_refund(order_id: int, refund_id: int) -> Dict[str, Any]:
    """GET /orders/{order_id}/refunds/{refund_id}.json

    Doc: docs/api_refund.md
    """
    return get_client().request("GET", f"/orders/{order_id}/refunds/{refund_id}.json")


def calculate_refund(order_id: int, refund: Dict[str, Any]) -> Dict[str, Any]:
    """POST /orders/{order_id}/refunds/calculate.json

    Doc: docs/api_refund.md
    """
    return get_client().request("POST", f"/orders/{order_id}/refunds/calculate.json", json_body={"refund": refund})


def create_refund(order_id: int, refund: Dict[str, Any]) -> Dict[str, Any]:
    """POST /orders/{order_id}/refunds.json

    Doc: docs/api_refund.md
    """
    return get_client().request("POST", f"/orders/{order_id}/refunds.json", json_body={"refund": refund})
