from typing import Any, Dict, Optional

from .ebay_client import EbayClient


CATALOG_SCOPE_APP = "https://api.ebay.com/oauth/api_scope/commerce.catalog.readonly"
CATALOG_SCOPE_SELL_INVENTORY = "https://api.ebay.com/oauth/api_scope/sell.inventory"


def get_product(epid: str, marketplace_id: Optional[str] = None, use_sell_inventory_scope: bool = False) -> Dict[str, Any]:
    """Get catalog product details by ePID.

    Docs: commerce/catalog/resources/product/methods/getProduct
    GET /commerce/catalog/v1_beta/product/{epid}
    OAuth: user token (authorization code grant) with either sell.inventory or commerce.catalog.readonly.
    """
    client = EbayClient()
    headers = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    scope = CATALOG_SCOPE_SELL_INVENTORY if use_sell_inventory_scope else CATALOG_SCOPE_APP
    return client.request(
        "GET",
        f"/commerce/catalog/v1_beta/product/{epid}",
        headers=headers,
        scope=scope,
        user=True,
        is_media=False,
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
    """Search catalog product summaries.

    Docs: commerce/catalog/resources/product_summary/methods/search
    GET /commerce/catalog/v1_beta/product_summary/search

    At least one of q, category_ids, gtin, mpn must be provided.
    Note: eBay docs state q cannot be used with gtin or mpn; aspect_filter cannot be used with gtin or mpn.
    """
    client = EbayClient()
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
    return client.request(
        "GET",
        "/commerce/catalog/v1_beta/product_summary/search",
        params=params,
        headers=headers,
        scope=scope,
        user=True,
        is_media=False,
    )
