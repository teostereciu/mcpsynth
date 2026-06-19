from __future__ import annotations

from typing import Any, Dict, Optional

from .http import safe_call


def search_returns(
    return_status: Optional[list[str]] = None,
    page_size: int = 10,
    page_token: Optional[str] = None,
    sort_field: str = "create_time",
    sort_order: str = "ASC",
    locale: Optional[str] = None,
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /return_refund/202602/returns/search"""
    params: Dict[str, Any] = {
        "sort_field": sort_field,
        "sort_order": sort_order,
        "page_size": page_size,
        "page_token": page_token,
    }
    if shop_cipher:
        params["shop_cipher"] = shop_cipher

    body: Dict[str, Any] = {
        "return_status": return_status,
        "locale": locale,
    }
    return safe_call("POST", "/return_refund/202602/returns/search", params=params, body=body)


def search_cancellations(
    status: Optional[str] = None,
    page_size: int = 10,
    page_token: Optional[str] = None,
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /return_refund/202602/cancellations/search"""
    params: Dict[str, Any] = {"page_size": page_size, "page_token": page_token}
    if shop_cipher:
        params["shop_cipher"] = shop_cipher
    body: Dict[str, Any] = {"status": status}
    return safe_call("POST", "/return_refund/202602/cancellations/search", params=params, body=body)
