"""
eBay Taxonomy API tools (used by Buy API agents for category discovery).
Covers: getCategoryTree, getCategorySubtree, getCategorySuggestions,
        getItemAspectsForCategory, getDefaultCategoryTreeId.
"""

from mcp.server.fastmcp import FastMCP
from .auth import api_get

mcp = FastMCP("ebay-taxonomy")

TAXONOMY_BASE = "/commerce/taxonomy/v1"


@mcp.tool()
def get_default_category_tree_id(marketplace_id: str = "EBAY_US") -> dict:
    """
    Retrieve the default category tree ID for a given eBay marketplace.

    Args:
        marketplace_id: eBay marketplace ID (e.g. 'EBAY_US', 'EBAY_GB', 'EBAY_DE').
    Returns:
        dict with categoryTreeId and categoryTreeVersion.
    """
    params = {"marketplace_id": marketplace_id}
    return api_get(f"{TAXONOMY_BASE}/get_default_category_tree_id", params=params)


@mcp.tool()
def get_category_tree(category_tree_id: str) -> dict:
    """
    Retrieve the full eBay category tree for a given tree ID.

    Note: This returns a very large response. Consider using get_category_subtree
    for a specific branch instead.

    Args:
        category_tree_id: The category tree ID (e.g. '0' for US).
    Returns:
        dict with the complete category hierarchy.
    """
    return api_get(f"{TAXONOMY_BASE}/category_tree/{category_tree_id}")


@mcp.tool()
def get_category_subtree(
    category_tree_id: str,
    category_id: str,
) -> dict:
    """
    Retrieve a subtree of the eBay category tree rooted at a specific category.

    Args:
        category_tree_id: The category tree ID (e.g. '0' for US).
        category_id: The root category ID for the subtree.
    Returns:
        dict with the category subtree hierarchy.
    """
    params = {"category_id": category_id}
    return api_get(
        f"{TAXONOMY_BASE}/category_tree/{category_tree_id}/get_category_subtree",
        params=params,
    )


@mcp.tool()
def get_category_suggestions(
    category_tree_id: str,
    q: str,
) -> dict:
    """
    Get category suggestions for a keyword query from the eBay taxonomy.

    Args:
        category_tree_id: The category tree ID (e.g. '0' for US).
        q: Free-text query to get category suggestions for (e.g. 'iphone case').
    Returns:
        dict with categorySuggestions list ranked by relevance.
    """
    params = {"q": q}
    return api_get(
        f"{TAXONOMY_BASE}/category_tree/{category_tree_id}/get_category_suggestions",
        params=params,
    )


@mcp.tool()
def get_item_aspects_for_category(
    category_tree_id: str,
    category_id: str,
) -> dict:
    """
    Retrieve the item aspects (attributes) relevant to a specific eBay category.

    Useful for understanding what filters and aspects are available for a category
    before constructing search queries.

    Args:
        category_tree_id: The category tree ID (e.g. '0' for US).
        category_id: The leaf category ID.
    Returns:
        dict with aspects list including names, types, and allowed values.
    """
    params = {"category_id": category_id}
    return api_get(
        f"{TAXONOMY_BASE}/category_tree/{category_tree_id}/get_item_aspects_for_category",
        params=params,
    )


@mcp.tool()
def get_categories_by_level(
    category_tree_id: str,
    category_id: str = "",
    level: int = 1,
) -> dict:
    """
    Retrieve categories at a specific depth level within the eBay category tree.

    Args:
        category_tree_id: The category tree ID (e.g. '0' for US).
        category_id: Parent category ID (empty for root-level categories).
        level: Depth level to retrieve (1 = top-level, 2 = second level, etc.).
    Returns:
        dict with categories at the specified level.
    """
    params: dict = {"level": level}
    if category_id:
        params["category_id"] = category_id
    return api_get(
        f"{TAXONOMY_BASE}/category_tree/{category_tree_id}/get_categories_by_level",
        params=params,
    )
