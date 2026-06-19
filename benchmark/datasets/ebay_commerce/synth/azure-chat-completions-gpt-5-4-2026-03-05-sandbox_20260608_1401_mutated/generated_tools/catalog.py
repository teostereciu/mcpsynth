from typing import Any, Dict, Optional

from .ebay_common import client


def get_product(epid: str, marketplace_id: Optional[str] = None) -> Dict[str, Any]:
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id} if marketplace_id else None
    return client.request(
        "GET",
        f"/commerce/catalog/v1_beta/product/{epid}",
        token_type="app",
        headers=headers,
    )


def search_catalog_products(
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
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id} if marketplace_id else None
    params = {
        "query": query,
        "gtin": gtin,
        "mpn": mpn,
        "category_id": category_id,
        "aspects": aspects,
        "field_groups": field_groups,
        "page_size": page_size,
        "offset": offset,
    }
    return client.request(
        "GET",
        "/commerce/catalog/v1_beta/product_summary/search",
        token_type="app",
        params=params,
        headers=headers,
    )
