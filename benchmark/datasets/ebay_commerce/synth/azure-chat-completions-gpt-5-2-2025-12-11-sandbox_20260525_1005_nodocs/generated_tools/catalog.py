from typing import Any, Dict, Optional

from .ebay_auth import auth_header, get_base_url, request_json


# Catalog API (application token)
# Note: docs/ is empty in this workspace; endpoints based on eBay Commerce Catalog API.


def catalog_search(q: str, limit: int = 20, offset: int = 0, fieldgroups: Optional[str] = None) -> Dict[str, Any]:
    """GET /commerce/catalog/v1_beta/product_summary/search"""
    url = get_base_url() + "/commerce/catalog/v1_beta/product_summary/search"
    params: Dict[str, Any] = {"q": q, "limit": limit, "offset": offset}
    if fieldgroups:
        params["fieldgroups"] = fieldgroups
    res, err = request_json("GET", url, headers={**auth_header(user=False)}, params=params)
    return err or res  # type: ignore


def get_product(product_id: str) -> Dict[str, Any]:
    """GET /commerce/catalog/v1_beta/product/{product_id}"""
    url = get_base_url() + f"/commerce/catalog/v1_beta/product/{product_id}"
    res, err = request_json("GET", url, headers={**auth_header(user=False)})
    return err or res  # type: ignore


def get_product_summary(product_id: str) -> Dict[str, Any]:
    """GET /commerce/catalog/v1_beta/product_summary/{product_id}"""
    url = get_base_url() + f"/commerce/catalog/v1_beta/product_summary/{product_id}"
    res, err = request_json("GET", url, headers={**auth_header(user=False)})
    return err or res  # type: ignore
