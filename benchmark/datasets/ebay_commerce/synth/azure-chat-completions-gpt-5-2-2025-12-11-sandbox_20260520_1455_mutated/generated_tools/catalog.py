from __future__ import annotations

from typing import Any, Dict, Optional

from .ebay_client import EbayClient


def search_product_summaries(
    query: Optional[str] = None,
    gtin: Optional[str] = None,
    mpn: Optional[str] = None,
    category_id: Optional[str] = None,
    aspects: Optional[str] = None,
    field_groups: Optional[str] = None,
    page_size: Optional[int] = None,
    marketplace_id: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /product_summary/search

    Notes:
      - eBay docs require at least one of: query, category_id, gtin, mpn
      - Some combinations are disallowed (e.g., query with gtin/mpn)
      - `aspects` is passed as a raw string in eBay's expected syntax.

    OAuth scopes (one of): sell.inventory, commerce.catalog.readonly
    """
    client = EbayClient.for_standard_api(user_scoped=True)
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

    return client.request(
        "GET",
        "/commerce/catalog/v1_beta/product_summary/search",
        headers=headers,
        params=params,
    )


def get_product(epid: str, marketplace_id: Optional[str] = None) -> Dict[str, Any]:
    """GET /product/{epid}

    OAuth scopes (one of): sell.inventory, commerce.catalog.readonly
    """
    client = EbayClient.for_standard_api(user_scoped=True)
    headers = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    return client.request(
        "GET",
        f"/commerce/catalog/v1_beta/product/{epid}",
        headers=headers,
    )
