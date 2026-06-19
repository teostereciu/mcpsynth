"""
eBay Sell Catalog / Taxonomy / Metadata API tools.
Covers: category trees, category suggestions, item aspects, compatibility,
        and eBay catalog product search.
"""

from mcp.server.fastmcp import FastMCP
from .auth import api_get, api_post

mcp = FastMCP("ebay-catalog")


# ── Taxonomy ─────────────────────────────────────────────────────────────────

@mcp.tool()
def get_default_category_tree_id(marketplace_id: str) -> dict:
    """
    Retrieve the default category tree ID for a marketplace.

    Args:
        marketplace_id: eBay marketplace ID (e.g. EBAY_US).
    """
    return api_get("/commerce/taxonomy/v1/get_default_category_tree_id",
                   params={"marketplace_id": marketplace_id})


@mcp.tool()
def get_category_tree(category_tree_id: str) -> dict:
    """
    Retrieve the full category tree structure.

    Args:
        category_tree_id: The category tree ID (e.g. 0 for US).
    """
    return api_get(f"/commerce/taxonomy/v1/category_tree/{category_tree_id}")


@mcp.tool()
def get_category_subtree(category_tree_id: str, category_id: str) -> dict:
    """
    Retrieve a subtree of the category tree rooted at a specific category.

    Args:
        category_tree_id: The category tree ID.
        category_id: The root category ID for the subtree.
    """
    return api_get(f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_subtree",
                   params={"category_id": category_id})


@mcp.tool()
def get_category_suggestions(category_tree_id: str, q: str) -> dict:
    """
    Get category suggestions based on a search query.

    Args:
        category_tree_id: The category tree ID.
        q: Search query (e.g. product name or keywords).
    """
    return api_get(f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_suggestions",
                   params={"q": q})


@mcp.tool()
def get_item_aspects_for_category(category_tree_id: str, category_id: str) -> dict:
    """
    Retrieve required and recommended item aspects for a category.

    Args:
        category_tree_id: The category tree ID.
        category_id: The category ID.
    """
    return api_get(f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category",
                   params={"category_id": category_id})


@mcp.tool()
def get_categories_by_aspects(category_tree_id: str, aspects: list[dict]) -> dict:
    """
    Find categories that match a set of item aspects.

    Args:
        category_tree_id: The category tree ID.
        aspects: List of aspect dicts with aspectName and aspectValues.
    """
    return api_post(f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_categories_by_aspects",
                    body={"aspects": aspects})


@mcp.tool()
def get_compatibility_properties(category_tree_id: str, category_id: str) -> dict:
    """
    Retrieve compatibility properties (e.g. vehicle fitment) for a category.

    Args:
        category_tree_id: The category tree ID.
        category_id: The category ID.
    """
    return api_get(f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_properties",
                   params={"category_id": category_id})


@mcp.tool()
def get_compatibility_property_values(category_tree_id: str, category_id: str,
                                       compatibility_property: str,
                                       filter: str | None = None) -> dict:
    """
    Retrieve valid values for a compatibility property.

    Args:
        category_tree_id: The category tree ID.
        category_id: The category ID.
        compatibility_property: Property name (e.g. Year, Make, Model).
        filter: Optional filter to narrow values.
    """
    params: dict = {"category_id": category_id,
                    "compatibility_property": compatibility_property}
    if filter:
        params["filter"] = filter
    return api_get(f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_property_values",
                   params=params)


# ── eBay Catalog ─────────────────────────────────────────────────────────────

@mcp.tool()
def search_catalog_products(q: str | None = None,
                             category_ids: str | None = None,
                             aspect_filter: str | None = None,
                             marketplace_id: str = "EBAY_US",
                             limit: int = 10,
                             offset: int = 0) -> dict:
    """
    Search the eBay product catalog.

    Args:
        q: Keyword search query.
        category_ids: Comma-separated category IDs to filter.
        aspect_filter: Aspect filter string.
        marketplace_id: eBay marketplace ID.
        limit: Results per page.
        offset: Pagination offset.
    """
    params: dict = {"marketplace_id": marketplace_id, "limit": limit, "offset": offset}
    if q:
        params["q"] = q
    if category_ids:
        params["category_ids"] = category_ids
    if aspect_filter:
        params["aspect_filter"] = aspect_filter
    return api_get("/commerce/catalog/v1_beta/product_summary/search", params=params)


@mcp.tool()
def get_catalog_product(epid: str) -> dict:
    """
    Retrieve a specific eBay catalog product by ePID.

    Args:
        epid: The eBay Product ID (ePID).
    """
    return api_get(f"/commerce/catalog/v1_beta/product/{epid}")
