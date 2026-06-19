"""
eBay Commerce Taxonomy API tools.
Base path: /commerce/taxonomy/v1
Auth: app token (client_credentials)
"""

from .auth import app_get

_BASE = "/commerce/taxonomy/v1"


# ---------------------------------------------------------------------------
# Category trees
# ---------------------------------------------------------------------------

def get_default_category_tree_id(marketplace_id: str = "EBAY_US") -> dict:
    """
    Get the default category tree ID for a given eBay marketplace.

    Args:
        marketplace_id: eBay marketplace identifier (e.g. EBAY_US, EBAY_GB, EBAY_DE).

    Returns:
        Dict with categoryTreeId and categoryTreeVersion.
    """
    return app_get(f"{_BASE}/get_default_category_tree_id", params={"marketplace_id": marketplace_id})


def get_category_tree(category_tree_id: str) -> dict:
    """
    Retrieve the complete category tree for the given tree ID.

    Args:
        category_tree_id: The category tree ID (e.g. "0" for eBay US).

    Returns:
        Dict with the full hierarchical category tree.
    """
    return app_get(f"{_BASE}/category_tree/{category_tree_id}")


def get_category_subtree(category_tree_id: str, category_id: str) -> dict:
    """
    Retrieve a subtree rooted at the specified category.

    Args:
        category_tree_id: The category tree ID.
        category_id: The root category ID for the subtree.

    Returns:
        Dict with the subtree rooted at category_id.
    """
    return app_get(
        f"{_BASE}/category_tree/{category_tree_id}/get_category_subtree",
        params={"category_id": category_id},
    )


def get_category_suggestions(
    category_tree_id: str,
    q: str,
) -> dict:
    """
    Get category suggestions for a search query string.

    Args:
        category_tree_id: The category tree ID.
        q: Keywords describing the item (e.g. "iphone 14 pro").

    Returns:
        Dict with categorySuggestions list ranked by relevance.
    """
    return app_get(
        f"{_BASE}/category_tree/{category_tree_id}/get_category_suggestions",
        params={"q": q},
    )


def get_item_aspects_for_category(category_tree_id: str, category_id: str) -> dict:
    """
    Get the item aspects (attributes) required or recommended for a category.

    Args:
        category_tree_id: The category tree ID.
        category_id: The leaf category ID.

    Returns:
        Dict with aspects list including names, types, and allowed values.
    """
    return app_get(
        f"{_BASE}/category_tree/{category_tree_id}/get_item_aspects_for_category",
        params={"category_id": category_id},
    )


def get_compatibility_properties(
    category_tree_id: str,
    category_id: str,
) -> dict:
    """
    Get the compatibility properties (e.g. Year, Make, Model) for a parts-compatibility category.

    Args:
        category_tree_id: The category tree ID.
        category_id: The category ID (must support parts compatibility).

    Returns:
        Dict with compatibilityProperties list.
    """
    return app_get(
        f"{_BASE}/category_tree/{category_tree_id}/get_compatibility_properties",
        params={"category_id": category_id},
    )


def get_compatibility_property_values(
    category_tree_id: str,
    category_id: str,
    compatibility_property: str,
    filter: str | None = None,
) -> dict:
    """
    Get the allowed values for a specific compatibility property (e.g. all valid "Make" values).

    Args:
        category_tree_id: The category tree ID.
        category_id: The category ID.
        compatibility_property: The property name (e.g. "Make", "Model", "Year").
        filter: Optional filter to narrow values, e.g. "Year:2020,Make:Honda".

    Returns:
        Dict with compatibilityPropertyValues list.
    """
    params: dict = {
        "category_id": category_id,
        "compatibility_property": compatibility_property,
    }
    if filter:
        params["filter"] = filter
    return app_get(
        f"{_BASE}/category_tree/{category_tree_id}/get_compatibility_property_values",
        params=params,
    )


def get_expired_categories(category_tree_id: str) -> dict:
    """
    Get a list of categories that have been deprecated/expired in the given tree.

    Args:
        category_tree_id: The category tree ID.

    Returns:
        Dict with expiredCategories list.
    """
    return app_get(f"{_BASE}/category_tree/{category_tree_id}/get_expired_categories")
