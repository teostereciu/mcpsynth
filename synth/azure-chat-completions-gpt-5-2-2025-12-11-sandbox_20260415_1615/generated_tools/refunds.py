from typing import Any, Dict

from .http_client import get_client


def refunds_list(order_id: int) -> Dict[str, Any]:
    """GET /orders/{order_id}/refunds.json"""
    return get_client().request("GET", f"/orders/{order_id}/refunds.json")


def refund_get(order_id: int, refund_id: int) -> Dict[str, Any]:
    """GET /orders/{order_id}/refunds/{refund_id}.json"""
    return get_client().request("GET", f"/orders/{order_id}/refunds/{refund_id}.json")


def refund_calculate(order_id: int, refund: Dict[str, Any]) -> Dict[str, Any]:
    """POST /orders/{order_id}/refunds/calculate.json"""
    return get_client().request(
        "POST",
        f"/orders/{order_id}/refunds/calculate.json",
        json_body={"refund": refund},
    )


def refund_create(order_id: int, refund: Dict[str, Any]) -> Dict[str, Any]:
    """POST /orders/{order_id}/refunds.json"""
    return get_client().request(
        "POST",
        f"/orders/{order_id}/refunds.json",
        json_body={"refund": refund},
    )
