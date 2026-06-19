from __future__ import annotations

from typing import Any, Dict, Optional

from .http import commerce_base_url, request_json


API_SCOPE = "https://api.ebay.com/oauth/api_scope"


def get_default_category_tree_id(marketplace_id: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/get_default_category_tree_id

    Args:
        marketplace_id: eBay marketplace ID (e.g., EBAY_US)
    """
    return request_json(
        "GET",
        commerce_base_url(),
        "/commerce/taxonomy/v1/get_default_category_tree_id",
        params={"marketplace_id": marketplace_id},
        user_auth=False,
        scope=API_SCOPE,
    )


def get_category_tree(category_tree_id: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{category_tree_id}"""
    return request_json(
        "GET",
        commerce_base_url(),
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}",
        user_auth=False,
        scope=API_SCOPE,
    )


def get_category_subtree(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_subtree"""
    return request_json(
        "GET",
        commerce_base_url(),
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_subtree",
        params={"category_id": category_id},
        user_auth=False,
        scope=API_SCOPE,
    )


def get_category_suggestions(category_tree_id: str, q: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_suggestions"""
    return request_json(
        "GET",
        commerce_base_url(),
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_suggestions",
        params={"q": q},
        user_auth=False,
        scope=API_SCOPE,
    )


def get_item_aspects_for_category(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category"""
    return request_json(
        "GET",
        commerce_base_url(),
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category",
        params={"category_id": category_id},
        user_auth=False,
        scope=API_SCOPE,
    )


def get_compatibility_properties(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_properties"""
    return request_json(
        "GET",
        commerce_base_url(),
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_properties",
        params={"category_id": category_id},
        user_auth=False,
        scope=API_SCOPE,
    )


def get_compatibility_property_values(
    category_tree_id: str,
    category_id: str,
    compatibility_property: str,
    *,
    filter: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_property_values"""
    params: Dict[str, Any] = {"category_id": category_id, "compatibility_property": compatibility_property}
    if filter:
        params["filter"] = filter
    return request_json(
        "GET",
        commerce_base_url(),
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_property_values",
        params=params,
        user_auth=False,
        scope=API_SCOPE,
    )


def get_expired_categories(category_tree_id: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_expired_categories"""
    return request_json(
        "GET",
        commerce_base_url(),
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_expired_categories",
        user_auth=False,
        scope=API_SCOPE,
    )
