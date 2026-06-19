"""Tools for eBay Commerce Catalog API."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import request_json


def search_product_summaries(
    *,
    q: Optional[str] = None,
    gtin: Optional[str] = None,
    mpn: Optional[str] = None,
    category_ids: Optional[str] = None,
    aspect_filter: Optional[str] = None,
    fieldgroups: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    marketplace_id: Optional[str] = None,
    user_auth: bool = False,
) -> Dict[str, Any]:
    """Search for product summaries in the eBay catalog.

    Docs: GET /commerce/catalog/v1_beta/product_summary/search
    Auth: user token (sell.inventory or commerce.catalog.readonly) per docs; allow app token via user_auth=False.
    """

    params: Dict[str, Any] = {}
    if q is not None:
        params["q"] = q
    if gtin is not None:
        params["gtin"] = gtin
    if mpn is not None:
        params["mpn"] = mpn
    if category_ids is not None:
        params["category_ids"] = category_ids
    if aspect_filter is not None:
        params["aspect_filter"] = aspect_filter
    if fieldgroups is not None:
        params["fieldgroups"] = fieldgroups
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset

    headers: Dict[str, str] = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id

    status, data, _ = request_json(
        "GET",
        "/commerce/catalog/v1_beta/product_summary/search",
        params=params or None,
        user_auth=user_auth,
        media=False,
        extra_headers=headers or None,
    )
    return data


def get_product(epid: str, *, marketplace_id: Optional[str] = None, user_auth: bool = False) -> Dict[str, Any]:
    """Get full product details by ePID.

    Docs: GET /commerce/catalog/v1_beta/product/{epid}
    Auth: user token per docs; allow app token via user_auth=False.
    """

    headers: Dict[str, str] = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id

    status, data, _ = request_json(
        "GET",
        f"/commerce/catalog/v1_beta/product/{epid}",
        user_auth=user_auth,
        media=False,
        extra_headers=headers or None,
    )
    return data
