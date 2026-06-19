"""
eBay Sell Catalog / Taxonomy / Metadata API tools.
Covers: category suggestions, item aspects, eBay catalog product search,
        and marketplace metadata.
"""

from mcp.server.fastmcp import FastMCP
from .auth import ebay_request

mcp = FastMCP("ebay-catalog")

# ---------------------------------------------------------------------------
# Taxonomy
# ---------------------------------------------------------------------------

@mcp.tool()
def get_default_category_tree_id(marketplace_id: str) -> dict:
    """
    Retrieve the default category tree ID for a marketplace.

    Args:
        marketplace_id: eBay marketplace ID, e.g. 'EBAY_US'.
    """
    return ebay_request(
        "GET",
        "/commerce/taxonomy/v1/get_default_category_tree_id",
        params={"marketplace_id": marketplace_id},
    )


@mcp.tool()
def get_category_tree(category_tree_id: str) -> dict:
    """
    Retrieve the full category tree for a given tree ID.

    Args:
        category_tree_id: The category tree ID (obtained from get_default_category_tree_id).
    """
    return ebay_request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}",
    )


@mcp.tool()
def get_category_subtree(category_tree_id: str, category_id: str) -> dict:
    """
    Retrieve a subtree of the category tree starting from a given category.

    Args:
        category_tree_id: The category tree ID.
        category_id: The root category ID for the subtree.
    """
    return ebay_request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_subtree",
        params={"category_id": category_id},
    )


@mcp.tool()
def get_category_suggestions(category_tree_id: str, q: str) -> dict:
    """
    Get category suggestions for a product based on a search query.

    Args:
        category_tree_id: The category tree ID.
        q: Search query describing the product, e.g. 'iPhone 14 case'.
    """
    return ebay_request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_suggestions",
        params={"q": q},
    )


@mcp.tool()
def get_item_aspects_for_category(category_tree_id: str, category_id: str) -> dict:
    """
    Retrieve the item aspects (specifics) required or recommended for a category.

    Args:
        category_tree_id: The category tree ID.
        category_id: The category ID to get aspects for.
    """
    return ebay_request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category",
        params={"category_id": category_id},
    )


@mcp.tool()
def get_compatible_vehicles(category_tree_id: str, category_id: str) -> dict:
    """
    Retrieve compatible vehicle information for a parts-compatibility category.

    Args:
        category_tree_id: The category tree ID.
        category_id: The parts-compatibility category ID.
    """
    return ebay_request(
        "GET",
        f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatible_vehicles",
        params={"category_id": category_id},
    )


# ---------------------------------------------------------------------------
# eBay Catalog Product Search
# ---------------------------------------------------------------------------

@mcp.tool()
def search_catalog_products(
    q: str | None = None,
    category_ids: str | None = None,
    aspect_filter: str | None = None,
    marketplace_id: str = "EBAY_US",
    limit: int = 10,
    offset: int = 0,
) -> dict:
    """
    Search the eBay product catalog to find matching catalog products.

    Args:
        q: Search query string (optional if category_ids provided).
        category_ids: Comma-separated category IDs to filter by (optional).
        aspect_filter: Aspect filter string, e.g. 'Brand:Apple' (optional).
        marketplace_id: eBay marketplace ID (default 'EBAY_US').
        limit: Number of results to return (default 10, max 200).
        offset: Pagination offset (default 0).
    """
    params: dict = {"marketplace_id": marketplace_id, "limit": limit, "offset": offset}
    if q:
        params["q"] = q
    if category_ids:
        params["category_ids"] = category_ids
    if aspect_filter:
        params["aspect_filter"] = aspect_filter
    return ebay_request("GET", "/commerce/catalog/v1_beta/product_summary/search", params=params)


@mcp.tool()
def get_catalog_product(epid: str) -> dict:
    """
    Retrieve a specific eBay catalog product by its ePID.

    Args:
        epid: The eBay Product ID (ePID) of the catalog product.
    """
    return ebay_request("GET", f"/commerce/catalog/v1_beta/product/{epid}")


# ---------------------------------------------------------------------------
# Marketplace Metadata (Sell Metadata API)
# ---------------------------------------------------------------------------

@mcp.tool()
def get_return_policies_metadata(marketplace_id: str) -> dict:
    """
    Retrieve return policy metadata (allowed values) for a marketplace.

    Args:
        marketplace_id: eBay marketplace ID, e.g. 'EBAY_US'.
    """
    return ebay_request(
        "GET",
        f"/sell/metadata/v1/marketplace/{marketplace_id}/get_return_policies",
    )


@mcp.tool()
def get_listing_structure_policies(marketplace_id: str, category_id: str | None = None) -> dict:
    """
    Retrieve listing structure policies (e.g. multi-variation support) for a marketplace.

    Args:
        marketplace_id: eBay marketplace ID, e.g. 'EBAY_US'.
        category_id: Filter by category ID (optional).
    """
    params: dict = {}
    if category_id:
        params["filter"] = f"categoryId:{category_id}"
    return ebay_request(
        "GET",
        f"/sell/metadata/v1/marketplace/{marketplace_id}/get_listing_structure_policies",
        params=params or None,
    )


@mcp.tool()
def get_negotiated_price_policies(marketplace_id: str, category_id: str | None = None) -> dict:
    """
    Retrieve negotiated price (Best Offer) policies for a marketplace.

    Args:
        marketplace_id: eBay marketplace ID, e.g. 'EBAY_US'.
        category_id: Filter by category ID (optional).
    """
    params: dict = {}
    if category_id:
        params["filter"] = f"categoryId:{category_id}"
    return ebay_request(
        "GET",
        f"/sell/metadata/v1/marketplace/{marketplace_id}/get_negotiated_price_policies",
        params=params or None,
    )


@mcp.tool()
def get_item_condition_policies(marketplace_id: str, category_id: str | None = None) -> dict:
    """
    Retrieve item condition policies (allowed conditions) for a marketplace/category.

    Args:
        marketplace_id: eBay marketplace ID, e.g. 'EBAY_US'.
        category_id: Filter by category ID (optional).
    """
    params: dict = {}
    if category_id:
        params["filter"] = f"categoryId:{category_id}"
    return ebay_request(
        "GET",
        f"/sell/metadata/v1/marketplace/{marketplace_id}/get_item_condition_policies",
        params=params or None,
    )


@mcp.tool()
def get_automotive_parts_compatibility_policies(
    marketplace_id: str, category_id: str | None = None
) -> dict:
    """
    Retrieve automotive parts compatibility policies for a marketplace.

    Args:
        marketplace_id: eBay marketplace ID, e.g. 'EBAY_US'.
        category_id: Filter by category ID (optional).
    """
    params: dict = {}
    if category_id:
        params["filter"] = f"categoryId:{category_id}"
    return ebay_request(
        "GET",
        f"/sell/metadata/v1/marketplace/{marketplace_id}/get_automotive_parts_compatibility_policies",
        params=params or None,
    )


@mcp.tool()
def get_extended_producer_responsibility_policies(
    marketplace_id: str, category_id: str | None = None
) -> dict:
    """
    Retrieve extended producer responsibility (EPR) policies for a marketplace.

    Args:
        marketplace_id: eBay marketplace ID, e.g. 'EBAY_US'.
        category_id: Filter by category ID (optional).
    """
    params: dict = {}
    if category_id:
        params["filter"] = f"categoryId:{category_id}"
    return ebay_request(
        "GET",
        f"/sell/metadata/v1/marketplace/{marketplace_id}/get_extended_producer_responsibility_policies",
        params=params or None,
    )
