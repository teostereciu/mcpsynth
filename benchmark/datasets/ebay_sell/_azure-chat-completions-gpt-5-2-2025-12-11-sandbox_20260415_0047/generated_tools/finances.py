from __future__ import annotations

from typing import Any, Dict, Optional

from .http import request_json

API_ROOT = "/sell/finances/v1"
SCOPE = "https://api.ebay.com/oauth/api_scope/sell.finances"


def register(mcp):
    @mcp.tool()
    def finances_get_transactions(
        *,
        marketplace_id: str = "EBAY_US",
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        sort: Optional[str] = None,
    ) -> Dict[str, Any]:
        """GET /transaction - Get transactions."""
        params: Dict[str, Any] = {}
        if filter is not None:
            params["filter"] = filter
        if limit is not None:
            params["limit"] = str(limit)
        if offset is not None:
            params["offset"] = str(offset)
        if sort is not None:
            params["sort"] = sort
        return request_json(
            "GET",
            API_ROOT,
            "/transaction",
            scope=SCOPE,
            marketplace_id=marketplace_id,
            params=params or None,
        )

    @mcp.tool()
    def finances_get_transaction_summary(
        *,
        marketplace_id: str = "EBAY_US",
        filter: Optional[str] = None,
    ) -> Dict[str, Any]:
        """GET /transaction_summary - Get transaction summary."""
        params = {"filter": filter} if filter else None
        return request_json(
            "GET",
            API_ROOT,
            "/transaction_summary",
            scope=SCOPE,
            marketplace_id=marketplace_id,
            params=params,
        )

    @mcp.tool()
    def finances_get_payouts(
        *,
        marketplace_id: str = "EBAY_US",
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        sort: Optional[str] = None,
    ) -> Dict[str, Any]:
        """GET /payout - Get payouts."""
        params: Dict[str, Any] = {}
        if filter is not None:
            params["filter"] = filter
        if limit is not None:
            params["limit"] = str(limit)
        if offset is not None:
            params["offset"] = str(offset)
        if sort is not None:
            params["sort"] = sort
        return request_json(
            "GET",
            API_ROOT,
            "/payout",
            scope=SCOPE,
            marketplace_id=marketplace_id,
            params=params or None,
        )

    @mcp.tool()
    def finances_get_payout(payout_id: str, *, marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
        """GET /payout/{payout_Id} - Get payout."""
        return request_json(
            "GET",
            API_ROOT,
            f"/payout/{payout_id}",
            scope=SCOPE,
            marketplace_id=marketplace_id,
        )

    @mcp.tool()
    def finances_get_payout_summary(*, marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
        """GET /payout_summary - Get payout summary."""
        return request_json(
            "GET",
            API_ROOT,
            "/payout_summary",
            scope=SCOPE,
            marketplace_id=marketplace_id,
        )

    @mcp.tool()
    def finances_get_seller_funds_summary(*, marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
        """GET /seller_funds_summary - Get seller funds summary."""
        return request_json(
            "GET",
            API_ROOT,
            "/seller_funds_summary",
            scope=SCOPE,
            marketplace_id=marketplace_id,
        )

    @mcp.tool()
    def finances_get_billing_activities(
        *,
        marketplace_id: str = "EBAY_US",
        filter: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Dict[str, Any]:
        """GET /billing_activity - Get billing activities."""
        params: Dict[str, Any] = {}
        if filter is not None:
            params["filter"] = filter
        if limit is not None:
            params["limit"] = str(limit)
        if offset is not None:
            params["offset"] = str(offset)
        return request_json(
            "GET",
            API_ROOT,
            "/billing_activity",
            scope=SCOPE,
            marketplace_id=marketplace_id,
            params=params or None,
        )

    @mcp.tool()
    def finances_get_transfer(transfer_id: str, *, marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
        """GET /transfer/{transfer_Id} - Get transfer."""
        return request_json(
            "GET",
            API_ROOT,
            f"/transfer/{transfer_id}",
            scope=SCOPE,
            marketplace_id=marketplace_id,
        )
