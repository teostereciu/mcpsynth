from typing import Any, Dict, Optional

from .common import client


def get_default_category_tree_id(marketplace_id: str = "EBAY_US") -> Dict[str, Any]:
    return client.request(
        "GET",
        "/commerce/taxonomy/v1/get_default_category_tree_id",
        "app",
        headers={"X-EBAY-C-MARKETPLACE-ID": marketplace_id},
    )


def get_category_tree(category_tree_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/commerce/taxonomy/v1/category_tree/{category_tree_id}", "app")


def get_category_subtree(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_subtree", "app", params={"category_id": category_id})


def get_category_suggestions(category_tree_id: str, q: str) -> Dict[str, Any]:
    return client.request("GET", f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_suggestions", "app", params={"q": q})


def get_item_aspects_for_category(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category", "app", params={"category_id": category_id})


def get_compatibility_properties(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_properties", "app", params={"category_id": category_id})


def get_compatibility_property_values(category_tree_id: str, category_id: str, property_name: str) -> Dict[str, Any]:
    return client.request("GET", f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_property_values", "app", params={"category_id": category_id, "property_name": property_name})
