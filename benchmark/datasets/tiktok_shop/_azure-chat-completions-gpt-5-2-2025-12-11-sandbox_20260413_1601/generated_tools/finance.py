"""Finance domain tools."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import TikTokRequestOptions, tiktok_request


def get_statements(
    *,
    page_size: int = 20,
    page_token: Optional[str] = None,
    payment_status: Optional[str] = None,
    statement_time_ge: Optional[int] = None,
    statement_time_lt: Optional[int] = None,
    sort_order: str = "ASC",
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """Get settlement statements.

    API: GET /finance/202309/statements
    """

    params: Dict[str, Any] = {
        "sort_field": "statement_time",
        "sort_order": sort_order,
        "page_size": page_size,
    }
    if page_token is not None:
        params["page_token"] = page_token
    if payment_status is not None:
        params["payment_status"] = payment_status
    if statement_time_ge is not None:
        params["statement_time_ge"] = int(statement_time_ge)
    if statement_time_lt is not None:
        params["statement_time_lt"] = int(statement_time_lt)

    return tiktok_request(
        "GET",
        "/finance/202309/statements",
        params=params,
        options=TikTokRequestOptions(use_shop_cipher=True, shop_cipher=shop_cipher),
    )
