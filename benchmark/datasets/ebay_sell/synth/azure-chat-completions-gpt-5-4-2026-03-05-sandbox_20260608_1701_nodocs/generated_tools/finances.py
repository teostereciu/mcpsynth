from typing import Any, Dict, Optional

from .common import client


def list_transactions(limit: int = 50, offset: int = 0, filter: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    return client.request("GET", "/sell/finances/v1/transaction", params=params)


def get_transaction(transaction_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/finances/v1/transaction/{transaction_id}")


def list_payouts(limit: int = 50, offset: int = 0, filter: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    return client.request("GET", "/sell/finances/v1/payout", params=params)


def get_payout(payout_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/finances/v1/payout/{payout_id}")
