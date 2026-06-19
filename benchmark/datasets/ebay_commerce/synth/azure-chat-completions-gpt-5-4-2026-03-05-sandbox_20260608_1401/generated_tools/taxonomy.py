from typing import Any, Dict, Optional

from generated_tools.catalog import client


TAXONOMY_BASE = "/commerce/taxonomy/v1"


def get_default_category_tree_id(marketplace_id: str) -> Dict[str, Any]:
    return client.request(
        "GET",
        f"{TAXONOMY_BASE}/get_default_category_tree_id",
        token_type="app",
        params={"marketplace_id": marketplace_id},
    )


def get_category_tree(category_tree_id: str, accept_encoding: Optional[str] = None) -> Dict[str, Any]:
    headers = {"Accept-Encoding": accept_encoding} if accept_encoding else None
    return client.request(
        "GET",
        f"{TAXONOMY_BASE}/category_tree/{category_tree_id}",
        token_type="app",
        headers=headers,
    )


def get_category_subtree(category_tree_id: str, category_id: str, accept_encoding: Optional[str] = None) -> Dict[str, Any]:
    headers = {"Accept-Encoding": accept_encoding} if accept_encoding else None
    return client.request(
        "GET",
        f"{TAXONOMY_BASE}/category_tree/{category_tree_id}/get_category_subtree",
        token_type="app",
        params={"category_id": category_id},
        headers=headers,
    )


def get_category_suggestions(category_tree_id: str, q: str) -> Dict[str, Any]:
    return client.request(
        "GET",
        f"{TAXONOMY_BASE}/category_tree/{category_tree_id}/get_category_suggestions",
        token_type="app",
        params={"q": q},
    )


def fetch_item_aspects(category_tree_id: str) -> Dict[str, Any]:
    return client.request(
        "GET",
        f"{TAXONOMY_BASE}/category_tree/{category_tree_id}/fetch_item_aspects",
        token_type="app",
        headers={"Accept": "application/octet-stream"},
    )


def get_item_aspects_for_category(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    return client.request(
        "GET",
        f"{TAXONOMY_BASE}/category_tree/{category_tree_id}/get_item_aspects_for_category",
        token_type="app",
        params={"category_id": category_id},
    )


def get_compatibility_properties(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    return client.request(
        "GET",
        f"{TAXONOMY_BASE}/category_tree/{category_tree_id}/get_compatibility_properties",
        token_type="app",
        params={"category_id": category_id},
    )


def get_compatibility_property_values(
    category_tree_id: str,
    category_id: str,
    compatibility_property: str,
    filter: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {
        "category_id": category_id,
        "compatibility_property": compatibility_property,
    }
    if filter is not None:
        params["filter"] = filter
    return client.request(
        "GET",
        f"{TAXONOMY_BASE}/category_tree/{category_tree_id}/get_compatibility_property_values",
        token_type="app",
        params=params,
    )
