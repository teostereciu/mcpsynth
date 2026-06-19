from typing import Any, Dict, Optional

from .http_client import get_client


def transactions_list(order_id: int) -> Dict[str, Any]:
    """GET /orders/{order_id}/transactions.json"""
    return get_client().request("GET", f"/orders/{order_id}/transactions.json")


def transactions_count(order_id: int) -> Dict[str, Any]:
    """GET /orders/{order_id}/transactions/count.json"""
    return get_client().request("GET", f"/orders/{order_id}/transactions/count.json")


def transaction_get(order_id: int, transaction_id: int) -> Dict[str, Any]:
    """GET /orders/{order_id}/transactions/{transaction_id}.json"""
    return get_client().request("GET", f"/orders/{order_id}/transactions/{transaction_id}.json")


def transaction_create(order_id: int, transaction: Dict[str, Any], *, source: Optional[str] = None) -> Dict[str, Any]:
    """POST /orders/{order_id}/transactions.json"""
    params = {"source": source} if source is not None else None
    return get_client().request(
        "POST",
        f"/orders/{order_id}/transactions.json",
        params=params,
        json_body={"transaction": transaction},
    )
