from typing import Any, Dict, Optional

from . import client as _shared
from .client import SCOPE_FINANCES
from . import mcp

API = "/sell/finances/v1"


@mcp.tool()
def finances_get_transactions(
    *,
    filter: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    sort: Optional[str] = None,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """GET /transaction"""
    params: Dict[str, Any] = {}
    if filter is not None:
        params["filter"] = filter
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    if sort is not None:
        params["sort"] = sort
    return _shared.client.request(
        "GET",
        API,
        "/transaction",
        scope=SCOPE_FINANCES,
        marketplace_id=marketplace_id,
        params=params or None,
    )


@mcp.tool()
def finances_get_transaction_summary(
    *,
    filter: Optional[str] = None,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """GET /transaction_summary"""
    params = {"filter": filter} if filter else None
    return _shared.client.request(
        "GET",
        API,
        "/transaction_summary",
        scope=SCOPE_FINANCES,
        marketplace_id=marketplace_id,
        params=params,
    )


@mcp.tool()
def finances_get_payouts(
    *,
    filter: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """GET /payout"""
    params: Dict[str, Any] = {}
    if filter is not None:
        params["filter"] = filter
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    return _shared.client.request(
        "GET",
        API,
        "/payout",
        scope=SCOPE_FINANCES,
        marketplace_id=marketplace_id,
        params=params or None,
    )


@mcp.tool()
def finances_get_payout(payout_id: str, *, marketplace_id: str = "EBAY_US") -> Any:
    """GET /payout/{payout_id}"""
    return _shared.client.request(
        "GET",
        API,
        f"/payout/{payout_id}",
        scope=SCOPE_FINANCES,
        marketplace_id=marketplace_id,
    )


@mcp.tool()
def finances_get_payout_summary(*, marketplace_id: str = "EBAY_US") -> Any:
    """GET /payout_summary"""
    return _shared.client.request(
        "GET",
        API,
        "/payout_summary",
        scope=SCOPE_FINANCES,
        marketplace_id=marketplace_id,
    )


@mcp.tool()
def finances_get_billing_activities(
    *,
    filter: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """GET /billing_activity"""
    params: Dict[str, Any] = {}
    if filter is not None:
        params["filter"] = filter
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    return _shared.client.request(
        "GET",
        API,
        "/billing_activity",
        scope=SCOPE_FINANCES,
        marketplace_id=marketplace_id,
        params=params or None,
    )
