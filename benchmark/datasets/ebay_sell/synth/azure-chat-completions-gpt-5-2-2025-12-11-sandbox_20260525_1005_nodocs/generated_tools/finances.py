from typing import Any, Dict, Optional

from .ebay_client import EbayClient


def finances_get_transactions(
    filter: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    sort: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /sell/finances/v1/transaction"""
    c = EbayClient()
    params: Dict[str, Any] = {}
    if filter is not None:
        params["filter"] = filter
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    if sort is not None:
        params["sort"] = sort
    return c.request("GET", "/sell/finances/v1/transaction", params=params)


def finances_get_transaction(transaction_id: str) -> Dict[str, Any]:
    """GET /sell/finances/v1/transaction/{transactionId}"""
    c = EbayClient()
    return c.request("GET", f"/sell/finances/v1/transaction/{transaction_id}")


def finances_get_payouts(
    filter: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    sort: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /sell/finances/v1/payout"""
    c = EbayClient()
    params: Dict[str, Any] = {}
    if filter is not None:
        params["filter"] = filter
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    if sort is not None:
        params["sort"] = sort
    return c.request("GET", "/sell/finances/v1/payout", params=params)


def finances_get_payout(payout_id: str) -> Dict[str, Any]:
    """GET /sell/finances/v1/payout/{payoutId}"""
    c = EbayClient()
    return c.request("GET", f"/sell/finances/v1/payout/{payout_id}")
