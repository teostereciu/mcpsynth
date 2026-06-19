from typing import Any, Dict, Optional

from .http_client import EbayClient


CATALOG_SCOPE_APP = "https://api.ebay.com/oauth/api_scope/commerce.catalog.readonly"
CATALOG_SCOPE_SELL_INVENTORY = "https://api.ebay.com/oauth/api_scope/sell.inventory"


def get_product(epid: str, marketplace_id: Optional[str] = None, use_sell_inventory_scope: bool = False) -> Dict[str, Any]:
    """GET /commerce/catalog/v1_beta/product/{epid}

    Doc: docs/api_commerce_catalog_resources_product_methods_getProduct.md
    """
    scope = CATALOG_SCOPE_SELL_INVENTORY if use_sell_inventory_scope else CATALOG_SCOPE_APP
    client = EbayClient()
    return client.request(
        "GET",
        f"/commerce/catalog/v1_beta/product/{epid}",
        marketplace_id=marketplace_id,
        scope=scope,
        user_token=False,
    )


def search_product_summaries(
    q: Optional[str] = None,
    category_ids: Optional[str] = None,
    gtin: Optional[str] = None,
    mpn: Optional[str] = None,
    aspect_filter: Optional[str] = None,
    filter: Optional[str] = None,
    fieldgroups: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    sort: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    use_sell_inventory_scope: bool = False,
) -> Dict[str, Any]:
    """GET /commerce/catalog/v1_beta/product_summary/search

    Doc: docs/api_commerce_catalog_resources_product_summary_methods_search.md
    """
    scope = CATALOG_SCOPE_SELL_INVENTORY if use_sell_inventory_scope else CATALOG_SCOPE_APP
    params: Dict[str, Any] = {}
    if q is not None:
        params["q"] = q
    if category_ids is not None:
        params["category_ids"] = category_ids
    if gtin is not None:
        params["gtin"] = gtin
    if mpn is not None:
        params["mpn"] = mpn
    if aspect_filter is not None:
        params["aspect_filter"] = aspect_filter
    if filter is not None:
        params["filter"] = filter
    if fieldgroups is not None:
        params["fieldgroups"] = fieldgroups
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    if sort is not None:
        params["sort"] = sort

    client = EbayClient()
    return client.request(
        "GET",
        "/commerce/catalog/v1_beta/product_summary/search",
        params=params or None,
        marketplace_id=marketplace_id,
        scope=scope,
        user_token=False,
    )
