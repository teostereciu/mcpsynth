from typing import Any, Dict, Optional

from .http import EbayAuth, request_json


AUTH = EbayAuth()


def get_default_category_tree_id(marketplace_id: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/get_default_category_tree_id"""
    token = AUTH.get_app_token("https://api.ebay.com/oauth/api_scope")
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}
    return request_json(
        method="GET",
        path="/commerce/taxonomy/v1/get_default_category_tree_id",
        query={"marketplace_id": marketplace_id},
        access_token=token,
    )


def get_category_tree(category_tree_id: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{category_tree_id}"""
    token = AUTH.get_app_token("https://api.ebay.com/oauth/api_scope")
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}
    return request_json(
        method="GET",
        path=f"/commerce/taxonomy/v1/category_tree/{category_tree_id}",
        access_token=token,
    )


def get_category_subtree(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_subtree"""
    token = AUTH.get_app_token("https://api.ebay.com/oauth/api_scope")
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}
    return request_json(
        method="GET",
        path=f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_subtree",
        query={"category_ids": category_id},
        access_token=token,
    )


def get_category_suggestions(category_tree_id: str, q: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_suggestions"""
    token = AUTH.get_app_token("https://api.ebay.com/oauth/api_scope")
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}
    return request_json(
        method="GET",
        path=f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_suggestions",
        query={"q": q},
        access_token=token,
    )


def get_item_aspects_for_category(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category"""
    token = AUTH.get_app_token("https://api.ebay.com/oauth/api_scope")
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}
    return request_json(
        method="GET",
        path=f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category",
        query={"category_ids": category_id},
        access_token=token,
    )


def fetch_item_aspects(category_tree_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """POST /commerce/taxonomy/v1/category_tree/{category_tree_id}/fetch_item_aspects"""
    token = AUTH.get_app_token("https://api.ebay.com/oauth/api_scope")
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}
    return request_json(
        method="POST",
        path=f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/fetch_item_aspects",
        json_body=payload,
        access_token=token,
    )


def get_expired_categories(category_tree_id: str, date: Optional[str] = None) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_expired_categories"""
    token = AUTH.get_app_token("https://api.ebay.com/oauth/api_scope")
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}
    query: Dict[str, Any] = {}
    if date is not None:
        query["date"] = date
    return request_json(
        method="GET",
        path=f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_expired_categories",
        query=query or None,
        access_token=token,
    )


def get_compatibility_properties(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_properties"""
    token = AUTH.get_app_token("https://api.ebay.com/oauth/api_scope")
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}
    return request_json(
        method="GET",
        path=f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_properties",
        query={"category_ids": category_id},
        access_token=token,
    )


def get_compatibility_property_values(
    category_tree_id: str,
    category_id: str,
    compatibility_property: str,
    filter: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_property_values"""
    token = AUTH.get_app_token("https://api.ebay.com/oauth/api_scope")
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}
    query: Dict[str, Any] = {"category_ids": category_id, "compatibility_property": compatibility_property}
    if filter is not None:
        query["filter"] = filter
    return request_json(
        method="GET",
        path=f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_property_values",
        query=query,
        access_token=token,
    )
