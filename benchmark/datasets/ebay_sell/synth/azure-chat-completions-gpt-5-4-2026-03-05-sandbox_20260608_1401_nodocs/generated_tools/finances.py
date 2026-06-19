from typing import Any, Dict, Optional

from generated_tools.common import client


def get_transactions(filter: Optional[str] = None, limit: int = 50, offset: int = 0) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit, "offset": offset}
    if filter is not None:
        params["filter"] = filter
    return client.request("GET", "/sell/finances/v1/transaction", params=params)


def get_transaction(transaction_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/finances/v1/transaction/{transaction_id}")


def get_payouts(filter: Optional[str] = None, limit: int = 50, offset: int = 0) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit, "offset": offset}
    if filter is not None:
        params["filter"] = filter
    return client.request("GET", "/sell/finances/v1/payout", params=params)


def get_payout(payout_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/finances/v1/payout/{payout_id}")


def get_payout_transactions(payout_id: str, limit: int = 50, offset: int = 0) -> Dict[str, Any]:
    return client.request("GET", f"/sell/finances/v1/payout/{payout_id}/transaction", params={"limit": limit, "offset": offset})
