from typing import Any, Dict

from .http_client import request_json


def create_transaction(order_id: int, transaction: Dict[str, Any]) -> Dict[str, Any]:
    """POST /orders/{order_id}/transactions.json

    Doc: docs/api_transaction.md
    Body wrapper: {"transaction": {...}}
    """
    return request_json("POST", f"/orders/{order_id}/transactions.json", json_body={"transaction": transaction})


def list_transactions(order_id: int) -> Dict[str, Any]:
    """GET /orders/{order_id}/transactions.json

    Doc: docs/api_transaction.md
    """
    return request_json("GET", f"/orders/{order_id}/transactions.json")


def get_transaction(order_id: int, transaction_id: int) -> Dict[str, Any]:
    """GET /orders/{order_id}/transactions/{transaction_id}.json

    Doc: docs/api_transaction.md
    """
    return request_json("GET", f"/orders/{order_id}/transactions/{transaction_id}.json")


def count_transactions(order_id: int) -> Dict[str, Any]:
    """GET /orders/{order_id}/transactions/count.json

    Doc: docs/api_transaction.md
    """
    return request_json("GET", f"/orders/{order_id}/transactions/count.json")
