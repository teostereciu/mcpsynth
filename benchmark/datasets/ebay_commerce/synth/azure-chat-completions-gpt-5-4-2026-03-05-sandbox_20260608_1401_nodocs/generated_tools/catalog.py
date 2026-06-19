from typing import Any, Dict, Optional

from .common import client


def get_product(epa_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/commerce/catalog/v1_beta/product/{epa_id}", "app")


def get_product_by_compatibility(q: Optional[str] = None, filter: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None) -> Dict[str, Any]:
    return client.request(
        "GET",
        "/commerce/catalog/v1_beta/product_summary/search_by_compatibility",
        "app",
        params={"q": q, "filter": filter, "limit": limit, "offset": offset},
    )


def search_products(q: Optional[str] = None, gtin: Optional[str] = None, mpn: Optional[str] = None, brand: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None, filter: Optional[str] = None) -> Dict[str, Any]:
    return client.request(
        "GET",
        "/commerce/catalog/v1_beta/product_summary/search",
        "app",
        params={
            "q": q,
            "gtin": gtin,
            "mpn": mpn,
            "brand": brand,
            "limit": limit,
            "offset": offset,
            "filter": filter,
        },
    )


def get_product_metadata(epa_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/commerce/catalog/v1_beta/product/{epa_id}/metadata", "app")
