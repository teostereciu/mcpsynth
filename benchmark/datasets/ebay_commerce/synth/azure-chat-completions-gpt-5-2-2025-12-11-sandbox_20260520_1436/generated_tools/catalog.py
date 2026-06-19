from typing import Any, Dict, Optional

from .ebay_client import EbayClient


CATALOG_READ_SCOPE = "https://api.ebay.com/oauth/api_scope/commerce.catalog.readonly"
SELL_INVENTORY_SCOPE = "https://api.ebay.com/oauth/api_scope/sell.inventory"


def get_product(epid: str, marketplace_id: Optional[str] = None, use_sell_inventory_scope: bool = False) -> Any:
    """GET /commerce/catalog/v1_beta/product/{epid}

    Doc: docs/api_commerce_catalog_resources_product_methods_getProduct.md
    """
    client = EbayClient()
    scope = SELL_INVENTORY_SCOPE if use_sell_inventory_scope else CATALOG_READ_SCOPE
    return client.request(
        "GET",
        f"/commerce/catalog/v1_beta/product/{epid}",
        marketplace_id=marketplace_id,
        user_scope=scope,
    )


def search_product_summaries(
    q: Optional[str] = None,
    category_ids: Optional[str] = None,
    gtin: Optional[str] = None,
    mpn: Optional[str] = None,
    aspects: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    marketplace_id: Optional[str] = None,
) -> Any:
    """GET /commerce/catalog/v1_beta/product_summary/search

    Doc: docs/api_commerce_catalog_resources_product_summary_methods_search.md
    """
    client = EbayClient()
    params: Dict[str, Any] = {}
    if q is not None:
        params["q"] = q
    if category_ids is not None:
        params["category_ids"] = category_ids
    if gtin is not None:
        params["gtin"] = gtin
    if mpn is not None:
        params["mpn"] = mpn
    if aspects is not None:
        params["aspects"] = aspects
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset

    return client.request(
        "GET",
        "/commerce/catalog/v1_beta/product_summary/search",
        params=params or None,
        marketplace_id=marketplace_id,
        user_scope=CATALOG_READ_SCOPE,
    )
