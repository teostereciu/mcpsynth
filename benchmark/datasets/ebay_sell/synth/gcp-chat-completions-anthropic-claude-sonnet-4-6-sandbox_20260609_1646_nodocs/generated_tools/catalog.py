"""
eBay Catalog & Taxonomy API tools.
Covers: category tree, category suggestions, item aspects, compatibility,
        eBay catalog product search.
"""

from typing import Optional
from auth import api_get, api_post


# ---------------------------------------------------------------------------
# Taxonomy — Category Tree
# ---------------------------------------------------------------------------

def get_default_category_tree_id(marketplace_id: str) -> dict:
    """Get the default category tree ID for a marketplace."""
    return api_get("/commerce/taxonomy/v1/get_default_category_tree_id",
                   params={"marketplace_id": marketplace_id})


def get_category_tree(category_tree_id: str) -> dict:
    """Get the full category tree for a given tree ID."""
    return api_get(f"/commerce/taxonomy/v1/category_tree/{category_tree_id}")


def get_category_subtree(category_tree_id: str, category_id: str) -> dict:
    """Get a subtree rooted at a specific category."""
    return api_get(f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_subtree",
                   params={"category_id": category_id})


def get_category_suggestions(category_tree_id: str, q: str) -> dict:
    """Get category suggestions for a search query string."""
    return api_get(
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_suggestions",
        params={"q": q},
    )


def get_item_aspects_for_category(category_tree_id: str, category_id: str) -> dict:
    """Get the required and recommended item aspects for a category."""
    return api_get(
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category",
        params={"category_id": category_id},
    )


def get_compatible_vehicles(category_tree_id: str, category_id: str) -> dict:
    """Get compatible vehicle information for a parts-compatibility category."""
    return api_get(
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatible_vehicles",
        params={"category_id": category_id},
    )


def get_categories_by_aspect_query(category_tree_id: str, aspect_filter: str) -> dict:
    """Get categories that match a given aspect filter query."""
    return api_get(
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_categories_by_aspect_query",
        params={"aspect_filter": aspect_filter},
    )


# ---------------------------------------------------------------------------
# eBay Catalog — Product Search
# ---------------------------------------------------------------------------

def search_catalog_products(
    q: Optional[str] = None,
    category_ids: Optional[str] = None,
    aspect_filter: Optional[str] = None,
    fieldgroups: Optional[str] = None,
    limit: int = 10,
    offset: int = 0,
) -> dict:
    """
    Search the eBay product catalog.

    q: keyword query
    category_ids: comma-separated category IDs
    aspect_filter: e.g. "categoryId:9355,Brand:{Apple}"
    fieldgroups: e.g. "ASPECT_REFINEMENTS"
    """
    params: dict = {"limit": limit, "offset": offset}
    if q:
        params["q"] = q
    if category_ids:
        params["category_ids"] = category_ids
    if aspect_filter:
        params["aspect_filter"] = aspect_filter
    if fieldgroups:
        params["fieldgroups"] = fieldgroups
    return api_get("/commerce/catalog/v1_beta/product_summary/search", params=params)


def get_catalog_product(epid: str) -> dict:
    """Get a specific eBay catalog product by ePID (eBay Product ID)."""
    return api_get(f"/commerce/catalog/v1_beta/product/{epid}")
