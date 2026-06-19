from __future__ import annotations

from typing import Any, Dict, Optional

from .client import EbayClient


def get_transactions(
    *,
    filter: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    client: Optional[EbayClient] = None,
) -> Any:
    """GET /transaction

    Doc: docs/api_finances_get-transactions.md
    """
    c = client or EbayClient()
    params: Dict[str, str] = {}
    if filter is not None:
        params["filter"] = filter
    if limit is not None:
        params["limit"] = str(limit)
    if offset is not None:
        params["offset"] = str(offset)
    status, body, headers = c.request("GET", "/transaction", params=params or None)
    return c.ok_or_error(status, body, headers)


def get_payouts(
    *,
    filter: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    client: Optional[EbayClient] = None,
) -> Any:
    """GET /payout

    Doc: docs/api_finances_get-payouts.md
    """
    c = client or EbayClient()
    params: Dict[str, str] = {}
    if filter is not None:
        params["filter"] = filter
    if limit is not None:
        params["limit"] = str(limit)
    if offset is not None:
        params["offset"] = str(offset)
    status, body, headers = c.request("GET", "/payout", params=params or None)
    return c.ok_or_error(status, body, headers)


def get_payout(payout_id: str, *, client: Optional[EbayClient] = None) -> Any:
    """GET /payout/{payout_Id}

    Doc: docs/api_finances_get-payout.md
    """
    c = client or EbayClient()
    status, body, headers = c.request("GET", f"/payout/{payout_id}")
    return c.ok_or_error(status, body, headers)
