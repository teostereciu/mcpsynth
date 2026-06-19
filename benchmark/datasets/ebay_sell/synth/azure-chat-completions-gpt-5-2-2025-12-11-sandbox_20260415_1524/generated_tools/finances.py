from typing import Any, Dict, Optional

from .ebay_client import EbayClient


def get_transactions(
    *,
    filter: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /transaction"""
    client = EbayClient()
    params: Dict[str, Any] = {}
    if filter is not None:
        params["filter"] = filter
    if limit is not None:
        params["limit"] = str(limit)
    if offset is not None:
        params["offset"] = str(offset)
    return client.request("GET", "/sell/finances/v1/transaction", params=params or None)


def get_transaction_summary(*, filter: Optional[str] = None) -> Dict[str, Any]:
    """GET /transaction_summary"""
    client = EbayClient()
    params = {"filter": filter} if filter else None
    return client.request("GET", "/sell/finances/v1/transaction_summary", params=params)


def get_payouts(
    *,
    filter: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /payout"""
    client = EbayClient()
    params: Dict[str, Any] = {}
    if filter is not None:
        params["filter"] = filter
    if limit is not None:
        params["limit"] = str(limit)
    if offset is not None:
        params["offset"] = str(offset)
    return client.request("GET", "/sell/finances/v1/payout", params=params or None)


def get_payout(payout_id: str) -> Dict[str, Any]:
    """GET /payout/{payoutId}"""
    client = EbayClient()
    return client.request("GET", f"/sell/finances/v1/payout/{payout_id}")


def get_payout_summary() -> Dict[str, Any]:
    """GET /payout_summary"""
    client = EbayClient()
    return client.request("GET", "/sell/finances/v1/payout_summary")
