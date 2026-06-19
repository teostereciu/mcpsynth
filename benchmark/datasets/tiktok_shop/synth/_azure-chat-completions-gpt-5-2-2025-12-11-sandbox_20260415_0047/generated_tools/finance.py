from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .http import tiktok_request


@mcp.tool()
def finance_get_statements(page_size: int = 20, page_token: Optional[str] = None) -> Dict[str, Any]:
    """Get settlement statements.

    API: GET /finance/202309/statements
    """

    params: Dict[str, Any] = {"page_size": page_size}
    if page_token:
        params["page_token"] = page_token
    return tiktok_request("GET", "/finance/202309/statements", params=params)


@mcp.tool()
def finance_get_payments(page_size: int = 20, page_token: Optional[str] = None) -> Dict[str, Any]:
    """Get payments.

    API: GET /finance/202309/payments
    """

    params: Dict[str, Any] = {"page_size": page_size}
    if page_token:
        params["page_token"] = page_token
    return tiktok_request("GET", "/finance/202309/payments", params=params)


@mcp.tool()
def finance_get_withdrawals(page_size: int = 20, page_token: Optional[str] = None) -> Dict[str, Any]:
    """Get withdrawals.

    API: GET /finance/202309/withdrawals
    """

    params: Dict[str, Any] = {"page_size": page_size}
    if page_token:
        params["page_token"] = page_token
    return tiktok_request("GET", "/finance/202309/withdrawals", params=params)
