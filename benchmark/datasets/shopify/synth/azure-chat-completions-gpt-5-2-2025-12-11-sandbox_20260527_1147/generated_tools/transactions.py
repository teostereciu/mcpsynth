from typing import Any, Dict, Optional

from ._client import get_client


def list_transactions(order_id: int) -> Dict[str, Any]:
    """GET /orders/{order_id}/transactions.json

    Doc: docs/api_transaction.md
    """
    return get_client().request("GET", f"/orders/{order_id}/transactions.json")


def get_transaction(order_id: int, transaction_id: int) -> Dict[str, Any]:
    """GET /orders/{order_id}/transactions/{transaction_id}.json

    Doc: docs/api_transaction.md
    """
    return get_client().request("GET", f"/orders/{order_id}/transactions/{transaction_id}.json")


def count_transactions(order_id: int) -> Dict[str, Any]:
    """GET /orders/{order_id}/transactions/count.json

    Doc: docs/api_transaction.md
    """
    return get_client().request("GET", f"/orders/{order_id}/transactions/count.json")


def create_transaction(order_id: int, transaction: Dict[str, Any], *, source: Optional[str] = None) -> Dict[str, Any]:
    """POST /orders/{order_id}/transactions.json

    Doc: docs/api_transaction.md
    """
    params: Dict[str, Any] = {}
    if source is not None:
        params["source"] = source
    return get_client().request(
        "POST",
        f"/orders/{order_id}/transactions.json",
        params=params,
        json_body={"transaction": transaction},
    )
