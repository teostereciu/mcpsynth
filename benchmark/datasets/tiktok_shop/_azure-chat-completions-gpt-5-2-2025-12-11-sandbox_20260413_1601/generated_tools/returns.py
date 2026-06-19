"""Return/Refund/Cancel domain tools."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .http import TikTokRequestOptions, tiktok_request


def search_returns(
    *,
    return_status: Optional[List[str]] = None,
    page_size: int = 10,
    page_token: Optional[str] = None,
    sort_field: str = "create_time",
    sort_order: str = "ASC",
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """Search returns/refunds.

    API: POST /return_refund/202602/returns/search
    """

    params: Dict[str, Any] = {
        "sort_field": sort_field,
        "sort_order": sort_order,
        "page_size": str(page_size),
    }
    if page_token is not None:
        params["page_token"] = page_token

    body: Dict[str, Any] = {}
    if return_status is not None:
        body["return_status"] = return_status

    return tiktok_request(
        "POST",
        "/return_refund/202602/returns/search",
        params=params,
        body=body,
        options=TikTokRequestOptions(use_shop_cipher=True, shop_cipher=shop_cipher),
    )


def search_cancellations(
    *,
    status: Optional[str] = None,
    page_size: int = 10,
    page_token: Optional[str] = None,
    shop_cipher: Optional[str] = None,
) -> Dict[str, Any]:
    """Search cancellations.

    API: POST /return_refund/202602/cancellations/search
    """

    params: Dict[str, Any] = {"page_size": str(page_size)}
    if page_token is not None:
        params["page_token"] = page_token

    body: Dict[str, Any] = {}
    if status is not None:
        body["cancel_status"] = [status]

    return tiktok_request(
        "POST",
        "/return_refund/202602/cancellations/search",
        params=params,
        body=body,
        options=TikTokRequestOptions(use_shop_cipher=True, shop_cipher=shop_cipher),
    )
