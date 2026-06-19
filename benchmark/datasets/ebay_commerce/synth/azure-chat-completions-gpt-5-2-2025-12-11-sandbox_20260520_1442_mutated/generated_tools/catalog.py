from typing import Any, Dict, Optional

from .ebay_client import EbayClient


CATALOG_SCOPE = "https://api.ebay.com/oauth/api_scope/commerce.catalog.readonly"


def get_product(epid: str, marketplace_id: Optional[str] = None) -> Dict[str, Any]:
    """GET /commerce/catalog/v1_beta/product/{epid}"""
    client = EbayClient()
    headers = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    return client.request(
        "GET",
        client.api_base,
        f"/commerce/catalog/v1_beta/product/{epid}",
        headers=headers,
        auth="app",
        scope=CATALOG_SCOPE,
    )


def search_product_summaries(
    *,
    query: Optional[str] = None,
    gtin: Optional[str] = None,
    mpn: Optional[str] = None,
    category_id: Optional[str] = None,
    aspects: Optional[str] = None,
    field_groups: Optional[str] = None,
    page_size: Optional[int] = None,
    offset: Optional[int] = None,
    marketplace_id: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /commerce/catalog/v1_beta/product_summary/search"""
    client = EbayClient()
    headers = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id

    params: Dict[str, Any] = {}
    if query is not None:
        params["query"] = query
    if gtin is not None:
        params["gtin"] = gtin
    if mpn is not None:
        params["mpn"] = mpn
    if category_id is not None:
        params["category_id"] = category_id
    if aspects is not None:
        params["aspects"] = aspects
    if field_groups is not None:
        params["field_groups"] = field_groups
    if page_size is not None:
        params["page_size"] = page_size
    if offset is not None:
        params["offset"] = offset

    return client.request(
        "GET",
        client.api_base,
        "/commerce/catalog/v1_beta/product_summary/search",
        params=params,
        headers=headers,
        auth="app",
        scope=CATALOG_SCOPE,
    )
