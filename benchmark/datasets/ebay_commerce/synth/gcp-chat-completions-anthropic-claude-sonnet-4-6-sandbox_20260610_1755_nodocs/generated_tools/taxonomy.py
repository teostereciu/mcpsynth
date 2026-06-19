"""
eBay Commerce Taxonomy API tools.
Base: /commerce/taxonomy/v1
Auth: app token (client_credentials)
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
        marketplace_id: eBay marketplace ID, e.g. 'EBAY_US', 'EBAY_GB'.
    """
    try:
        resp = requests.get(
            f"{_BASE}/get_default_category_tree_id",
            headers=app_headers(),
            params={"marketplace_id": marketplace_id},
            timeout=15,
        )
        return safe_json(resp)
    except Exception as e:
        return {"error": str(e)}


def get_category_tree(category_tree_id: str) -> dict:
    """
    Retrieve the complete category tree for the given tree ID.

    Args:
        category_tree_id: The category tree ID (e.g. '0' for eBay US).
    """
    try:
        resp = requests.get(
            f"{_BASE}/category_tree/{category_tree_id}",
            headers=app_headers(),
            timeout=30,
        )
        return safe_json(resp)
    except Exception as e:
        return {"error": str(e)}


def get_category_subtree(category_tree_id: str, category_id: str) -> dict:
    """
    Retrieve a subtree of the category tree rooted at the given category.

    Args:
        category_tree_id: The category tree ID.
        category_id: The root category ID for the subtree.
    """
    try:
        resp = requests.get(
            f"{_BASE}/category_tree/{category_tree_id}/get_category_subtree",
            headers=app_headers(),
            params={"category_id": category_id},
            timeout=15,
        )
        return safe_json(resp)
    except Exception as e:
        return {"error": str(e)}


def get_category_suggestions(category_tree_id: str, q: str) -> dict:
    """
    Return category suggestions for a free-text query string.

    Args:
        category_tree_id: The category tree ID.
        q: Free-text search query (e.g. 'iphone 14 case').
    """
    try:
        resp = requests.get(
            f"{_BASE}/category_tree/{category_tree_id}/get_category_suggestions",
            headers=app_headers(),
            params={"q": q},
            timeout=15,
        )
        return safe_json(resp)
    except Exception as e:
        return {"error": str(e)}


def get_item_aspects_for_category(category_tree_id: str, category_id: str) -> dict:
    """
    Return the aspects (item specifics) required or recommended for a category.

    Args:
        category_tree_id: The category tree ID.
        category_id: The leaf category ID.
    """
    try:
        resp = requests.get(
            f"{_BASE}/category_tree/{category_tree_id}/get_item_aspects_for_category",
            headers=app_headers(),
            params={"category_id": category_id},
            timeout=15,
        )
        return safe_json(resp)
    except Exception as e:
        return {"error": str(e)}


def get_compatibility_properties(category_tree_id: str, category_id: str) -> dict:
    """
    Return the compatibility properties (e.g. Year, Make, Model) for a category.

    Args:
        category_tree_id: The category tree ID.
        category_id: The category ID (e.g. for auto parts).
    """
    try:
        resp = requests.get(
            f"{_BASE}/category_tree/{category_tree_id}/get_compatibility_properties",
            headers=app_headers(),
            params={"category_id": category_id},
            timeout=15,
        )
        return safe_json(resp)
    except Exception as e:
        return {"error": str(e)}


def get_compatibility_property_values(
    category_tree_id: str,
    category_id: str,
    compatibility_property: str,
    filter: Optional[str] = None,
) -> dict:
    """
    Return the allowed values for a specific compatibility property.

    Args:
        category_tree_id: The category tree ID.
        category_id: The category ID.
        compatibility_property: Property name, e.g. 'Make'.
        filter: Optional filter string to narrow results (e.g. 'Year:2020').
    """
    try:
        params: dict = {
            "category_id": category_id,
            "compatibility_property": compatibility_property,
        }
        if filter:
            params["filter"] = filter
        resp = requests.get(
            f"{_BASE}/category_tree/{category_tree_id}/get_compatibility_property_values",
            headers=app_headers(),
            params=params,
            timeout=15,
        )
        return safe_json(resp)
    except Exception as e:
        return {"error": str(e)}


def get_expired_categories(category_tree_id: str) -> dict:
    """
    Return categories that have been removed or expired from the tree.

    Args:
        category_tree_id: The category tree ID.
    """
    try:
        resp = requests.get(
            f"{_BASE}/category_tree/{category_tree_id}/get_expired_categories",
            headers=app_headers(),
            timeout=15,
        )
        return safe_json(resp)
    except Exception as e:
        return {"error": str(e)}


def get_categories_by_taxonomy(category_tree_id: str) -> dict:
    """
    Return a flat list of all categories in the tree.

    Args:
        category_tree_id: The category tree ID.
    """
    try:
        resp = requests.get(
            f"{_BASE}/category_tree/{category_tree_id}/get_categories_by_taxonomy",
            headers=app_headers(),
            timeout=30,
        )
        return safe_json(resp)
    except Exception as e:
        return {"error": str(e)}
