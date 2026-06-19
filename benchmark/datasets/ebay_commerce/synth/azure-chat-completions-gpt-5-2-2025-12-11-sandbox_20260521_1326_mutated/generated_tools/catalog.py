from typing import Any, Dict, Optional

from .http import EbayAuth, request_json


AUTH = EbayAuth()


def get_product(epid: str, marketplace_id: Optional[str] = None) -> Dict[str, Any]:
    """GET /commerce/catalog/v1_beta/product/{epid}"""
    token = AUTH.get_app_token("https://api.ebay.com/oauth/api_scope/commerce.catalog.readonly")
    # If oauth failed, token is a JSON string; surface as error dict
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}

    headers: Dict[str, str] = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id

    return request_json(
        method="GET",
        path=f"/commerce/catalog/v1_beta/product/{epid}",
        headers=headers,
        access_token=token,
    )


def search_product_summaries(
    *,
    q: Optional[str] = None,
    category_ids: Optional[str] = None,
    aspect_filter: Optional[str] = None,
    filter: Optional[str] = None,
    fieldgroups: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    sort: Optional[str] = None,
    marketplace_id: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /commerce/catalog/v1_beta/product_summary/search"""
    token = AUTH.get_app_token("https://api.ebay.com/oauth/api_scope/commerce.catalog.readonly")
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}

    headers: Dict[str, str] = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id

    query: Dict[str, Any] = {}
    if q is not None:
        query["q"] = q
    if category_ids is not None:
        query["category_ids"] = category_ids
    if aspect_filter is not None:
        query["aspect_filter"] = aspect_filter
    if filter is not None:
        query["filter"] = filter
    if fieldgroups is not None:
        query["fieldgroups"] = fieldgroups
    if limit is not None:
        query["limit"] = limit
    if offset is not None:
        query["offset"] = offset
    if sort is not None:
        query["sort"] = sort

    return request_json(
        method="GET",
        path="/commerce/catalog/v1_beta/product_summary/search",
        query=query or None,
        headers=headers,
        access_token=token,
    )
