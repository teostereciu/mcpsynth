from typing import Any, Dict, Optional

from .ebay_auth import auth_header, get_base_url, request_json


# Taxonomy API (application token)


def get_default_category_tree_id(marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/get_default_category_tree_id"""
    url = get_base_url() + "/commerce/taxonomy/v1/get_default_category_tree_id"
    params = {"marketplace_id": marketplace_id}
    res, err = request_json("GET", url, headers={**auth_header(user=False)}, params=params)
    return err or res  # type: ignore


def get_category_tree(category_tree_id: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{categoryTreeId}"""
    url = get_base_url() + f"/commerce/taxonomy/v1/category_tree/{category_tree_id}"
    res, err = request_json("GET", url, headers={**auth_header(user=False)})
    return err or res  # type: ignore


def get_category_subtree(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{categoryTreeId}/get_category_subtree"""
    url = get_base_url() + f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_subtree"
    params = {"category_id": category_id}
    res, err = request_json("GET", url, headers={**auth_header(user=False)}, params=params)
    return err or res  # type: ignore


def get_category_suggestions(category_tree_id: str, q: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{categoryTreeId}/get_category_suggestions"""
    url = get_base_url() + f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_suggestions"
    params = {"q": q}
    res, err = request_json("GET", url, headers={**auth_header(user=False)}, params=params)
    return err or res  # type: ignore


def get_item_aspects_for_category(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{categoryTreeId}/get_item_aspects_for_category"""
    url = get_base_url() + f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category"
    params = {"category_id": category_id}
    res, err = request_json("GET", url, headers={**auth_header(user=False)}, params=params)
    return err or res  # type: ignore


def get_compatibility_properties(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{categoryTreeId}/get_compatibility_properties"""
    url = get_base_url() + f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_properties"
    params = {"category_id": category_id}
    res, err = request_json("GET", url, headers={**auth_header(user=False)}, params=params)
    return err or res  # type: ignore


def get_compatibility_property_values(
    category_tree_id: str,
    category_id: str,
    compatibility_property: str,
    filter: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{categoryTreeId}/get_compatibility_property_values"""
    url = get_base_url() + f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_property_values"
    params: Dict[str, Any] = {"category_id": category_id, "compatibility_property": compatibility_property}
    if filter:
        params["filter"] = filter
    res, err = request_json("GET", url, headers={**auth_header(user=False)}, params=params)
    return err or res  # type: ignore
