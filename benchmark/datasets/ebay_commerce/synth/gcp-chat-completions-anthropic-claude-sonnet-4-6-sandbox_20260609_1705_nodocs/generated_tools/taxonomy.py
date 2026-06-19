"""
eBay Commerce Taxonomy API tools.
Uses app-token (client_credentials).
Base: /commerce/taxonomy/v1
"""

from typing import Optional
import requests
from .auth import BASE_URL, app_headers, safe_json

_BASE = f"{BASE_URL}/commerce/taxonomy/v1"


# ── Category Trees ────────────────────────────────────────────────────────────

def get_default_category_tree_id(marketplace_id: str) -> dict:
    """
    Return the default category tree ID for a given eBay marketplace.

    Args:
        marketplace_id: eBay marketplace ID (e.g. EBAY_US, EBAY_GB, EBAY_DE).
    """
    url = f"{_BASE}/get_default_category_tree_id"
    resp = requests.get(url, headers=app_headers(), params={"marketplace_id": marketplace_id}, timeout=15)
    return safe_json(resp)


def get_category_tree(category_tree_id: str) -> dict:
    """
    Retrieve the complete category tree for the given tree ID.

    Args:
        category_tree_id: The ID of the category tree (e.g. '0' for eBay US).
    """
    url = f"{_BASE}/category_tree/{category_tree_id}"
    resp = requests.get(url, headers=app_headers(), timeout=30)
    return safe_json(resp)


def get_category_subtree(category_tree_id: str, category_id: str) -> dict:
    """
    Retrieve a subtree of the category tree rooted at the given category.

    Args:
        category_tree_id: The ID of the category tree.
        category_id: The ID of the root category for the subtree.
    """
    url = f"{_BASE}/category_tree/{category_tree_id}/get_category_subtree"
    resp = requests.get(url, headers=app_headers(), params={"category_id": category_id}, timeout=15)
    return safe_json(resp)


def get_category_suggestions(category_tree_id: str, q: str) -> dict:
    """
    Return category suggestions for a free-text query string.

    Args:
        category_tree_id: The ID of the category tree.
        q: Free-text query (e.g. 'iphone case').
    """
    url = f"{_BASE}/category_tree/{category_tree_id}/get_category_suggestions"
    resp = requests.get(url, headers=app_headers(), params={"q": q}, timeout=15)
    return safe_json(resp)


def get_item_aspects_for_category(category_tree_id: str, category_id: str) -> dict:
    """
    Return the aspects (item specifics) required or recommended for a category.

    Args:
        category_tree_id: The ID of the category tree.
        category_id: The leaf category ID.
    """
    url = f"{_BASE}/category_tree/{category_tree_id}/get_item_aspects_for_category"
    resp = requests.get(url, headers=app_headers(), params={"category_id": category_id}, timeout=15)
    return safe_json(resp)


def get_compatibility_properties(category_tree_id: str, category_id: str) -> dict:
    """
    Return the compatibility properties for a vehicle-parts category.

    Args:
        category_tree_id: The ID of the category tree.
        category_id: The parts-compatibility category ID.
    """
    url = f"{_BASE}/category_tree/{category_tree_id}/get_compatibility_properties"
    resp = requests.get(url, headers=app_headers(), params={"category_id": category_id}, timeout=15)
    return safe_json(resp)


def get_compatibility_property_values(
    category_tree_id: str,
    category_id: str,
    compatibility_property: str,
    filter: Optional[str] = None,
) -> dict:
    """
    Return the allowed values for a compatibility property (e.g. Make, Model, Year).

    Args:
        category_tree_id: The ID of the category tree.
        category_id: The parts-compatibility category ID.
        compatibility_property: Name of the property (e.g. 'Make').
        filter: Optional filter string to narrow results (e.g. 'Make:Toyota').
    """
    url = f"{_BASE}/category_tree/{category_tree_id}/get_compatibility_property_values"
    params: dict = {"category_id": category_id, "compatibility_property": compatibility_property}
    if filter:
        params["filter"] = filter
    resp = requests.get(url, headers=app_headers(), params=params, timeout=15)
    return safe_json(resp)


def get_categories_by_taxonomy(category_tree_id: str) -> dict:
    """
    Return a flat list of all categories in the given category tree.

    Args:
        category_tree_id: The ID of the category tree.
    """
    url = f"{_BASE}/category_tree/{category_tree_id}/get_categories_by_taxonomy"
    resp = requests.get(url, headers=app_headers(), timeout=30)
    return safe_json(resp)
