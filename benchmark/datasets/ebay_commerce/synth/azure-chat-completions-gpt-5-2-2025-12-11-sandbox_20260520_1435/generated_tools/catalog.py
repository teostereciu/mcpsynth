from typing import Any, Dict, Optional

from .http_client import EbayHTTP


CATALOG_SCOPE_APP = "https://api.ebay.com/oauth/api_scope/commerce.catalog.readonly"
CATALOG_SCOPE_SELL_INVENTORY = "https://api.ebay.com/oauth/api_scope/sell.inventory"


def get_product(epid: str, marketplace_id: Optional[str] = None, *, use_sell_inventory_scope: bool = False) -> Dict[str, Any]:
    """GET /commerce/catalog/v1_beta/product/{epid}

    Doc: docs/api_commerce_catalog_resources_product_methods_getProduct.md
    """
    http = EbayHTTP()
    headers = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    scope = CATALOG_SCOPE_SELL_INVENTORY if use_sell_inventory_scope else CATALOG_SCOPE_APP
    return http.request(
        "GET",
        http.oauth.api_base,
        f"/commerce/catalog/v1_beta/product/{epid}",
        scope=scope,
        headers=headers,
    )


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
    use_sell_inventory_scope: bool = False,
) -> Dict[str, Any]:
    """GET /commerce/catalog/v1_beta/product_summary/search

    Doc: docs/api_commerce_catalog_resources_product_summary_methods_search.md

    Notes:
      - eBay requires at least one of q, category_ids, gtin, or mpn.
      - Some combinations are disallowed (see doc). This tool does not enforce; API will error.
    """
    http = EbayHTTP()
    headers = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
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
        params["limit"] = str(limit)
    if offset is not None:
        params["offset"] = str(offset)

    scope = CATALOG_SCOPE_SELL_INVENTORY if use_sell_inventory_scope else CATALOG_SCOPE_APP
    return http.request(
        "GET",
        http.oauth.api_base,
        "/commerce/catalog/v1_beta/product_summary/search",
        scope=scope,
        headers=headers,
        params=params,
    )
