from __future__ import annotations

from typing import Any, Dict, Optional

from .http import safe_call


def get_payments(
    sort_field: str = "create_time",
    sort_order: str = "DESC",
    page_size: int = 20,
    page_token: Optional[str] = None,
    create_time_ge: Optional[int] = None,
    create_time_lt: Optional[int] = None,
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /finance/202309/payments"""
    params: Dict[str, Any] = {
        "sort_field": sort_field,
        "sort_order": sort_order,
        "page_size": page_size,
        "page_token": page_token,
        "create_time_ge": create_time_ge,
        "create_time_lt": create_time_lt,
    }
    if shop_cipher:
        params["shop_cipher"] = shop_cipher
    return safe_call("GET", "/finance/202309/payments", params=params)


def get_statements(page_size: int = 20, page_token: Optional[str] = None, shop_cipher: Optional[str] = None) -> Dict[str, Any]:
    """GET /finance/202309/statements"""
    params: Dict[str, Any] = {"page_size": page_size, "page_token": page_token}
    if shop_cipher:
        params["shop_cipher"] = shop_cipher
    return safe_call("GET", "/finance/202309/statements", params=params)


def get_transactions_by_statement(
    statement_id: str,
    page_size: int = 20,
    page_token: Optional[str] = None,
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /finance/202501/statements/{statement_id}/transactions"""
    params: Dict[str, Any] = {"page_size": page_size, "page_token": page_token}
    if shop_cipher:
        params["shop_cipher"] = shop_cipher
    return safe_call("GET", f"/finance/202501/statements/{statement_id}/transactions", params=params)
