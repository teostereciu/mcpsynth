from typing import Any, Dict, Optional

from .ebay_http import EbayClient, compact


USER_SCOPE = None
APP_SCOPE = "https://api.ebay.com/oauth/api_scope"


def get_product(product_id: str, *, marketplace_id: Optional[str] = None) -> Dict[str, Any]:
    """GET /commerce/catalog/v1/product/{product_id}"""
    c = EbayClient()
    headers = c.build_headers(marketplace_id=marketplace_id)
    return c.request(
        "GET",
        f"/commerce/catalog/v1/product/{product_id}",
        headers=headers,
        user_scope=USER_SCOPE,
        app_scope=APP_SCOPE,
    )


def search_products(
    *,
    q: Optional[str] = None,
    gtin: Optional[str] = None,
    epid: Optional[str] = None,
    mpn: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    marketplace_id: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /commerce/catalog/v1/product_summary/search"""
    c = EbayClient()
    headers = c.build_headers(marketplace_id=marketplace_id)
    params = compact({"q": q, "gtin": gtin, "epid": epid, "mpn": mpn, "limit": limit, "offset": offset})
    return c.request(
        "GET",
        "/commerce/catalog/v1/product_summary/search",
        params=params,
        headers=headers,
        user_scope=USER_SCOPE,
        app_scope=APP_SCOPE,
    )
