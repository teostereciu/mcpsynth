from typing import Any, Dict

from .ebay_auth import request_json


# Taxonomy API (application token)


def get_default_category_tree_id(marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/get_default_category_tree_id"""
    status, body = request_json(
        "GET",
        "/commerce/taxonomy/v1/get_default_category_tree_id",
        headers={"X-EBAY-C-MARKETPLACE-ID": marketplace_id},
        user=False,
    )
    return {"status": status, "data": body}


def get_category_tree(category_tree_id: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{categoryTreeId}"""
    status, body = request_json(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}",
        user=False,
    )
    return {"status": status, "data": body}


def get_category_subtree(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{categoryTreeId}/get_category_subtree"""
    status, body = request_json(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_subtree",
        params={"category_id": category_id},
        user=False,
    )
    return {"status": status, "data": body}


def get_item_aspects_for_category(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{categoryTreeId}/get_item_aspects_for_category"""
    status, body = request_json(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category",
        params={"category_id": category_id},
        user=False,
    )
    return {"status": status, "data": body}


def get_compatibility_properties(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    """GET /commerce/taxonomy/v1/category_tree/{categoryTreeId}/get_compatibility_properties"""
    status, body = request_json(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_properties",
        params={"category_id": category_id},
        user=False,
    )
    return {"status": status, "data": body}
