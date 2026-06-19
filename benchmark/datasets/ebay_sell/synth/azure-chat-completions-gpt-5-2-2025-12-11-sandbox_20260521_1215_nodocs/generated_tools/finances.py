from typing import Any, Dict, Optional

from .ebay_client import EbayClient, omit_none


client = EbayClient()


def finances_get_transactions(
    filter: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    params = omit_none({"filter": filter, "limit": limit, "offset": offset})
    return client.request("GET", "/sell/finances/v1/transaction", params=params)


def finances_get_transaction(transaction_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/finances/v1/transaction/{transaction_id}")


def finances_get_payouts(
    filter: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    params = omit_none({"filter": filter, "limit": limit, "offset": offset})
    return client.request("GET", "/sell/finances/v1/payout", params=params)


def finances_get_payout(payout_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/sell/finances/v1/payout/{payout_id}")
