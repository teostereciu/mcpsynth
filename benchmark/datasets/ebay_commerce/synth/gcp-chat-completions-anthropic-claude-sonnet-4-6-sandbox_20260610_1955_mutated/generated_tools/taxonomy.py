"""
eBay Commerce Taxonomy API tools.
Uses app token (client_credentials).
Base: /commerce/taxonomy/v1
"""
from typing import Optional
import requests
from .auth import BASE_URL, app_headers, safe_json

TAXONOMY_BASE = f"{BASE_URL}/commerce/taxonomy/v1"


def get_default_category_tree_id(marketplace_id: str) -> dict:
    """
    Retrieve the default category tree ID for a given eBay marketplace.
    Returns categoryTreeId and categoryTreeVersion.

    Common marketplace IDs: EBAY_US, EBAY_GB, EBAY_DE, EBAY_AU, EBAY_FR,
    EBAY_IT, EBAY_ES, EBAY_CA, EBAY_AT, EBAY_BE, EBAY_CH, EBAY_PL.

    Args:
        marketplace_id: The eBay marketplace ID (e.g. 'EBAY_US').
    """
    try:
        resp = requests.get(
            f"{TAXONOMY_BASE}/get_default_category_tree_id",
            headers=app_headers(marketplace_id),
            params={"marketplace_id": marketplace_id},
            timeout=30,
        )
        return safe_json(resp)
    except Exception as e:
        return {"error": str(e)}


def get_category_tree(category_tree_id: str) -> dict:
    """
    Retrieve the complete category tree for the specified tree ID.
    Returns all nodes from root to leaf. This can be a very large response.
    Tip: Use get_category_subtree for a smaller portion of the tree.

    Args:
        category_tree_id: The unique identifier of the eBay category tree
                          (obtained from get_default_category_tree_id).
    """
    try:
        headers = app_headers()
        headers["Accept-Encoding"] = "gzip"
        resp = requests.get(
            f"{TAXONOMY_BASE}/category_tree/{category_tree_id}",
            headers=headers,
            timeout=60,
        )
        return safe_json(resp)
    except Exception as e:
        return {"error": str(e)}


def get_category_subtree(category_tree_id: str, category_id: str) -> dict:
    """
    Retrieve the subtree of a category tree starting from a specified category node.
    Returns all descendant categories down to leaf nodes.

    Args:
        category_tree_id: The unique identifier of the eBay category tree.
        category_id: The unique identifier of the category at the top of the subtree.
    """
    try:
        headers = app_headers()
        headers["Accept-Encoding"] = "gzip"
        resp = requests.get(
            f"{TAXONOMY_BASE}/category_tree/{category_tree_id}/get_category_subtree",
            headers=headers,
            params={"category_id": category_id},
            timeout=60,
        )
        return safe_json(resp)
    except Exception as e:
        return {"error": str(e)}


def get_category_suggestions(category_tree_id: str, query: str) -> dict:
    """
    Get suggested leaf categories for a product based on a keyword query.
    Returns categories sorted by eBay's confidence of relevance.
    Note: Not supported in Sandbox (returns random category names).

    Args:
        category_tree_id: The unique identifier of the eBay category tree.
        query: Free-form text describing the item (e.g. 'iphone', 'vintage guitar').
    """
    try:
        resp = requests.get(
            f"{TAXONOMY_BASE}/category_tree/{category_tree_id}/get_category_suggestions",
            headers=app_headers(),
            params={"query": query},
            timeout=30,
        )
        return safe_json(resp)
    except Exception as e:
        return {"error": str(e)}


def get_item_aspects_for_category(category_tree_id: str, category_id: str) -> dict:
    """
    Retrieve all aspects (item attributes) for a specific leaf category.
    Returns aspect names, data types, required/optional status, allowed values,
    and whether aspects can be used for item variations.

    Args:
        category_tree_id: The unique identifier of the eBay category tree.
        category_id: The unique identifier of the leaf category (must be a leaf node).
    """
    try:
        resp = requests.get(
            f"{TAXONOMY_BASE}/category_tree/{category_tree_id}/get_item_aspects_for_category",
            headers=app_headers(),
            params={"category_id": category_id},
            timeout=30,
        )
        return safe_json(resp)
    except Exception as e:
        return {"error": str(e)}


def fetch_item_aspects(category_tree_id: str) -> dict:
    """
    Fetch a complete list of aspects for ALL leaf categories in an eBay marketplace.
    Returns a gzipped JSON payload (very large — over 100 MB compressed).
    Use get_item_aspects_for_category for a single category instead.

    Args:
        category_tree_id: The unique identifier of the eBay category tree.
    """
    try:
        resp = requests.get(
            f"{TAXONOMY_BASE}/category_tree/{category_tree_id}/fetch_item_aspects",
            headers=app_headers(),
            timeout=120,
        )
        return safe_json(resp)
    except Exception as e:
        return {"error": str(e)}


def get_compatibility_properties(category_tree_id: str, category_id: str) -> dict:
    """
    Retrieve compatible vehicle aspects (e.g. Make, Model, Year, Engine, Trim)
    for a parts-compatibility-enabled category.
    Supported marketplaces: US, Canada, UK, Germany, Australia, France, Italy, Spain.

    Category tree IDs: US=0, US Motors=100, Canada=2, UK=3, Germany=77,
    Australia=15, France=71, Italy=101, Spain=186.

    Args:
        category_tree_id: The category tree ID for the marketplace.
        category_id: A category that supports parts compatibility.
    """
    try:
        resp = requests.get(
            f"{TAXONOMY_BASE}/category_tree/{category_tree_id}/get_compatibility_properties",
            headers=app_headers(),
            params={"category_id": category_id},
            timeout=30,
        )
        return safe_json(resp)
    except Exception as e:
        return {"error": str(e)}


def get_compatibility_property_values(
    category_tree_id: str,
    category_id: str,
    compatibility_property: str,
    filter_str: Optional[str] = None,
) -> dict:
    """
    Retrieve valid values for a specific compatible vehicle property (e.g. all 2018 Honda models).
    Use get_compatibility_properties first to find valid property names.

    Args:
        category_tree_id: The category tree ID for the marketplace.
        category_id: A category that supports parts compatibility.
        compatibility_property: The vehicle property to get values for (e.g. 'Model', 'Trim').
        filter_str: Optional comma-separated name:value pairs to narrow results
                    (e.g. 'Year:2018,Make:Honda'). Use backslash before commas in values.
    """
    try:
        params: dict = {
            "category_id": category_id,
            "compatibility_property": compatibility_property,
        }
        if filter_str:
            params["filter"] = filter_str

        resp = requests.get(
            f"{TAXONOMY_BASE}/category_tree/{category_tree_id}/get_compatibility_property_values",
            headers=app_headers(),
            params=params,
            timeout=30,
        )
        return safe_json(resp)
    except Exception as e:
        return {"error": str(e)}


def get_expired_categories(category_tree_id: str) -> dict:
    """
    Retrieve mappings of expired leaf categories to their active replacements.
    Useful for migrating listings from old categories to new ones.

    Args:
        category_tree_id: The unique identifier of the eBay category tree.
    """
    try:
        resp = requests.get(
            f"{TAXONOMY_BASE}/category_tree/{category_tree_id}/get_expired_categories",
            headers=app_headers(),
            timeout=30,
        )
        return safe_json(resp)
    except Exception as e:
        return {"error": str(e)}
