from typing import Any, Dict, Optional

from .ebay_auth import request_json


# Catalog API (application token)


def catalog_search(query: str, limit: int = 50, offset: int = 0, marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    """GET /commerce/catalog/v1_beta/product_summary/search"""
    status, body = request_json(
        "GET",
        "/commerce/catalog/v1_beta/product_summary/search",
        params={"q": query, "limit": limit, "offset": offset},
        headers={"X-EBAY-C-MARKETPLACE-ID": marketplace_id},
        user=False,
    )
    return {"status": status, "data": body}


def get_product(product_id: str, marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    """GET /commerce/catalog/v1_beta/product/{product_id}"""
    status, body = request_json(
        "GET",
        f"/commerce/catalog/v1_beta/product/{product_id}",
        headers={"X-EBAY-C-MARKETPLACE-ID": marketplace_id},
        user=False,
    )
    return {"status": status, "data": body}


def get_product_summary(product_id: str, marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    """GET /commerce/catalog/v1_beta/product_summary/{product_id}"""
    status, body = request_json(
        "GET",
        f"/commerce/catalog/v1_beta/product_summary/{product_id}",
        headers={"X-EBAY-C-MARKETPLACE-ID": marketplace_id},
        user=False,
    )
    return {"status": status, "data": body}


def get_product_compatibility(product_id: str, limit: int = 50, offset: int = 0, marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    """GET /commerce/catalog/v1_beta/product/{product_id}/get_compatibility_properties"""
    status, body = request_json(
        "GET",
        f"/commerce/catalog/v1_beta/product/{product_id}/get_compatibility_properties",
        params={"limit": limit, "offset": offset},
        headers={"X-EBAY-C-MARKETPLACE-ID": marketplace_id},
        user=False,
    )
    return {"status": status, "data": body}
