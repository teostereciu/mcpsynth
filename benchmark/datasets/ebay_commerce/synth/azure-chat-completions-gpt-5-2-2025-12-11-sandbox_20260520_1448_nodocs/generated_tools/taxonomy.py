from typing import Any, Dict, Optional

from .ebay_http import EbayClient, compact


APP_SCOPE = "https://api.ebay.com/oauth/api_scope"


def get_default_category_tree_id(*, marketplace_id: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/get_default_category_tree_id"""
    c = EbayClient()
    headers = c.build_headers(marketplace_id=marketplace_id)
    return c.request(
        "GET",
        "/commerce/taxonomy/v1/get_default_category_tree_id",
        headers=headers,
        app_scope=APP_SCOPE,
    )


def get_category_tree(category_tree_id: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{categoryTreeId}"""
    c = EbayClient()
    return c.request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}",
        app_scope=APP_SCOPE,
    )


def get_category_subtree(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{categoryTreeId}/get_category_subtree"""
    c = EbayClient()
    params = {"category_id": category_id}
    return c.request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_subtree",
        params=params,
        app_scope=APP_SCOPE,
    )


def get_category_suggestions(*, category_tree_id: str, q: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{categoryTreeId}/get_category_suggestions"""
    c = EbayClient()
    params = {"q": q}
    return c.request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_suggestions",
        params=params,
        app_scope=APP_SCOPE,
    )


def get_item_aspects_for_category(
    category_tree_id: str,
    category_id: str,
    *,
    marketplace_id: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{categoryTreeId}/get_item_aspects_for_category"""
    c = EbayClient()
    headers = c.build_headers(marketplace_id=marketplace_id)
    params = {"category_id": category_id}
    return c.request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category",
        params=params,
        headers=headers,
        app_scope=APP_SCOPE,
    )


def get_compatibility_properties(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{categoryTreeId}/get_compatibility_properties"""
    c = EbayClient()
    params = {"category_id": category_id}
    return c.request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_properties",
        params=params,
        app_scope=APP_SCOPE,
    )


def get_compatibility_property_values(
    category_tree_id: str,
    category_id: str,
    compatibility_property: str,
    *,
    filter: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{categoryTreeId}/get_compatibility_property_values"""
    c = EbayClient()
    params = compact(
        {
            "category_id": category_id,
            "compatibility_property": compatibility_property,
            "filter": filter,
            "limit": limit,
            "offset": offset,
        }
    )
    return c.request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_property_values",
        params=params,
        app_scope=APP_SCOPE,
    )
