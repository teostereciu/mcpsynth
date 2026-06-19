from __future__ import annotations

from typing import Any, Dict, Optional

from .http import commerce_base_url, request_json


SCOPE_CATALOG_READONLY = "https://api.ebay.com/oauth/api_scope/commerce.catalog.readonly"
SCOPE_SELL_INVENTORY = "https://api.ebay.com/oauth/api_scope/sell.inventory"


def search_product_summaries(
    *,
    q: Optional[str] = None,
    gtin: Optional[str] = None,
    mpn: Optional[str] = None,
    category_ids: Optional[str] = None,
    aspect_filter: Optional[str] = None,
    fieldgroups: Optional[str] = None,
    limit: int = 50,
    offset: Optional[int] = None,
    marketplace_id: Optional[str] = None,
    user_auth: bool = False,
) -> Dict[str, Any]:
    """GET /commerce/catalog/v1_beta/product_summary/search

    Note: docs indicate user token with either sell.inventory or commerce.catalog.readonly.
    We support both: set user_auth=True to use refresh-token flow.
    """
    params: Dict[str, Any] = {"limit": limit}
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
    if offset is not None:
        params["offset"] = offset

    headers: Dict[str, str] = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id

    scope = SCOPE_SELL_INVENTORY if user_auth else SCOPE_CATALOG_READONLY

    return request_json(
        "GET",
        commerce_base_url(),
        "/commerce/catalog/v1_beta/product_summary/search",
        params=params,
        user_auth=user_auth,
        scope=scope,
        extra_headers=headers or None,
    )


def get_product(epid: str, *, user_auth: bool = False) -> Dict[str, Any]:
    """GET /commerce/catalog/v1_beta/product/{epid}"""
    scope = SCOPE_SELL_INVENTORY if user_auth else SCOPE_CATALOG_READONLY
    return request_json(
        "GET",
        commerce_base_url(),
        f"/commerce/catalog/v1_beta/product/{epid}",
        user_auth=user_auth,
        scope=scope,
    )
