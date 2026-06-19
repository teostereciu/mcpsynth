"""
eBay Sell Stores API tools.
Covers: eBay Store configuration, categories, and store details.
"""

from mcp.server.fastmcp import FastMCP
from .auth import api_get, api_put, api_post

mcp = FastMCP("ebay-stores")


@mcp.tool()
def get_store() -> dict:
    """Retrieve the authenticated seller's eBay Store details."""
    return api_get("/sell/stores/v1/store")


@mcp.tool()
def update_store(store: dict) -> dict:
    """
    Update the seller's eBay Store settings.

    Args:
        store: Dict with store fields to update (name, description, categoryStructureType, etc.).
    """
    return api_put("/sell/stores/v1/store", body=store)


@mcp.tool()
def get_store_categories() -> dict:
    """Retrieve the custom store categories for the seller's eBay Store."""
    return api_get("/sell/stores/v1/store/category")


@mcp.tool()
def create_store_category(name: str, parent_category_id: str | None = None,
                           order: int | None = None) -> dict:
    """
    Create a new custom store category.

    Args:
        name: Category name.
        parent_category_id: Optional parent category ID for nested categories.
        order: Optional display order.
    """
    body: dict = {"name": name}
    if parent_category_id:
        body["parentCategoryId"] = parent_category_id
    if order is not None:
        body["order"] = order
    return api_post("/sell/stores/v1/store/category", body=body)


@mcp.tool()
def update_store_category(category_id: str, name: str | None = None,
                           order: int | None = None) -> dict:
    """
    Update a custom store category.

    Args:
        category_id: The store category ID.
        name: New category name.
        order: New display order.
    """
    body: dict = {}
    if name:
        body["name"] = name
    if order is not None:
        body["order"] = order
    return api_put(f"/sell/stores/v1/store/category/{category_id}", body=body)
