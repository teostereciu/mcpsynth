from typing import Any, Dict, Optional

from .ebay_common import client


def get_default_category_tree_id(marketplace_id: str) -> Dict[str, Any]:
    return client.request(
        "GET",
        "/commerce/taxonomy/v1/get_default_category_tree_id",
        token_type="app",
        params={"marketplace_id": marketplace_id},
    )


def get_category_tree(category_tree_id: str, accept_encoding: Optional[str] = None) -> Dict[str, Any]:
    headers = {"Accept-Encoding": accept_encoding} if accept_encoding else None
    return client.request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}",
        token_type="app",
        headers=headers,
    )


def get_category_subtree(category_tree_id: str, category_id: str, accept_encoding: Optional[str] = None) -> Dict[str, Any]:
    headers = {"Accept-Encoding": accept_encoding} if accept_encoding else None
    return client.request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_subtree",
        token_type="app",
        headers=headers,
        params={"category_ids": category_id},
    )


def get_category_suggestions(category_tree_id: str, query: str) -> Dict[str, Any]:
    return client.request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_suggestions",
        token_type="app",
        params={"q": query},
    )


def get_item_aspects_for_category(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    return client.request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category",
        token_type="app",
        params={"category_ids": category_id},
    )


def fetch_item_aspects(category_tree_id: str) -> Dict[str, Any]:
    return client.request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/fetch_item_aspects",
        token_type="app",
    )


def get_compatibility_properties(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    return client.request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_properties",
        token_type="app",
        params={"category_ids": category_id},
    )


def get_compatibility_property_values(category_tree_id: str, category_id: str, compatibility_property: str, filter_value: Optional[str] = None) -> Dict[str, Any]:
    return client.request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_property_values",
        token_type="app",
        params={
            "category_ids": category_id,
            "compatibility_property": compatibility_property,
            "filter": filter_value,
        },
    )


def get_expired_categories(category_tree_id: str) -> Dict[str, Any]:
    return client.request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_expired_categories",
        token_type="app",
    )
