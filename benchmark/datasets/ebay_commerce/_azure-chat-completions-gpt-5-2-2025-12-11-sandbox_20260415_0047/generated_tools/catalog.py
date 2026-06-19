"""Tools for eBay Commerce Catalog API."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import EbayApiError, error_dict, get_api_base_url, request_json


_CATALOG_SCOPE = "https://api.ebay.com/oauth/api_scope/commerce.catalog.readonly"


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
) -> Dict[str, Any]:
    """Search for product summaries in the eBay catalog."""
    try:
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

        headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id} if marketplace_id else None

        return request_json(
            method="GET",
            base_url=get_api_base_url(),
            path="/commerce/catalog/v1_beta/product_summary/search",
            params=params or None,
            headers=headers,
            user_auth=False,
            scope=_CATALOG_SCOPE,
        )
    except EbayApiError as e:
        return error_dict(e)


def get_product(epid: str) -> Dict[str, Any]:
    """Get full product details by ePID."""
    try:
        return request_json(
            method="GET",
            base_url=get_api_base_url(),
            path=f"/commerce/catalog/v1_beta/product/{epid}",
            user_auth=False,
            scope=_CATALOG_SCOPE,
        )
    except EbayApiError as e:
        return error_dict(e)
