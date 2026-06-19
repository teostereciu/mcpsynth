"""
eBay Buy Browse API tools.
Covers: search, getItem, getItemByLegacyId, getItemsByItemGroup,
        checkCompatibility, getCompatibilityProperties, getCompatibilityPropertyValues.
"""

from mcp.server.fastmcp import FastMCP
from .auth import api_get, api_post

mcp = FastMCP("ebay-browse")

BROWSE_BASE = "/buy/browse/v1"


# ---------------------------------------------------------------------------
# Search
# ---------------------------------------------------------------------------

@mcp.tool()
def search_items(
    q: str = "",
    category_ids: str = "",
    filter: str = "",
    sort: str = "",
    limit: int = 50,
    offset: int = 0,
    fieldgroups: str = "",
    aspect_filter: str = "",
    charity_ids: str = "",
    compatibility_filter: str = "",
    auto_correct: str = "",
    gtin: str = "",
) -> dict:
    """
    Search for eBay items using the Browse API /item_summary/search endpoint.

    Args:
        q: Free-text keyword query (e.g. 'iphone 14 pro').
        category_ids: Comma-separated category IDs to restrict results.
        filter: eBay filter string (e.g. 'price:[10..50],itemLocationCountry:US').
        sort: Sort order (e.g. 'price', '-price', 'newlyListed', 'endingSoonest').
        limit: Number of results per page (1-200, default 50).
        offset: Pagination offset.
        fieldgroups: Comma-separated field groups (e.g. 'MATCHING_ITEMS,FULL').
        aspect_filter: Aspect filter string (e.g. 'categoryId:9355,Brand:{Apple}').
        charity_ids: Comma-separated charity IDs to filter charity listings.
        compatibility_filter: Compatibility filter for parts fitment.
        auto_correct: Enable auto-correct ('QUERY').
        gtin: Global Trade Item Number to search by.
    Returns:
        dict with itemSummaries list and pagination metadata.
    """
    params: dict = {"limit": limit, "offset": offset}
    if q:
        params["q"] = q
    if category_ids:
        params["category_ids"] = category_ids
    if filter:
        params["filter"] = filter
    if sort:
        params["sort"] = sort
    if fieldgroups:
        params["fieldgroups"] = fieldgroups
    if aspect_filter:
        params["aspect_filter"] = aspect_filter
    if charity_ids:
        params["charity_ids"] = charity_ids
    if compatibility_filter:
        params["compatibility_filter"] = compatibility_filter
    if auto_correct:
        params["auto_correct"] = auto_correct
    if gtin:
        params["gtin"] = gtin
    return api_get(f"{BROWSE_BASE}/item_summary/search", params=params)


@mcp.tool()
def search_items_by_image(
    image_base64: str,
    category_ids: str = "",
    filter: str = "",
    sort: str = "",
    limit: int = 50,
    offset: int = 0,
    aspect_filter: str = "",
) -> dict:
    """
    Search for eBay items visually similar to a provided image (Browse API).

    Args:
        image_base64: Base64-encoded image data (JPEG/PNG).
        category_ids: Comma-separated category IDs to restrict results.
        filter: eBay filter string.
        sort: Sort order.
        limit: Number of results per page (1-200).
        offset: Pagination offset.
        aspect_filter: Aspect filter string.
    Returns:
        dict with itemSummaries list and pagination metadata.
    """
    params: dict = {"limit": limit, "offset": offset}
    if category_ids:
        params["category_ids"] = category_ids
    if filter:
        params["filter"] = filter
    if sort:
        params["sort"] = sort
    if aspect_filter:
        params["aspect_filter"] = aspect_filter
    body = {"image": image_base64}
    return api_post(f"{BROWSE_BASE}/item_summary/search_by_image", body=body, params=params)


# ---------------------------------------------------------------------------
# Item retrieval
# ---------------------------------------------------------------------------

@mcp.tool()
def get_item(
    item_id: str,
    fieldgroups: str = "",
) -> dict:
    """
    Retrieve full details for a single eBay item by its item ID.

    Args:
        item_id: The eBay item ID (e.g. 'v1|123456789012|0').
        fieldgroups: Comma-separated field groups to include
                     (e.g. 'PRODUCT,ADDITIONAL_SELLER_DETAILS').
    Returns:
        dict with complete item details including price, condition, seller, etc.
    """
    params: dict = {}
    if fieldgroups:
        params["fieldgroups"] = fieldgroups
    return api_get(f"{BROWSE_BASE}/item/{item_id}", params=params or None)


@mcp.tool()
def get_item_by_legacy_id(
    legacy_item_id: str,
    legacy_variation_id: str = "",
    legacy_variation_sku: str = "",
    fieldgroups: str = "",
) -> dict:
    """
    Retrieve an eBay item using its legacy (v2) item ID.

    Args:
        legacy_item_id: The legacy eBay item ID (numeric string).
        legacy_variation_id: Legacy variation ID for multi-variation listings.
        legacy_variation_sku: Seller-defined SKU for the variation.
        fieldgroups: Comma-separated field groups to include.
    Returns:
        dict with complete item details.
    """
    params: dict = {"legacy_item_id": legacy_item_id}
    if legacy_variation_id:
        params["legacy_variation_id"] = legacy_variation_id
    if legacy_variation_sku:
        params["legacy_variation_sku"] = legacy_variation_sku
    if fieldgroups:
        params["fieldgroups"] = fieldgroups
    return api_get(f"{BROWSE_BASE}/item/get_item_by_legacy_id", params=params)


@mcp.tool()
def get_items_by_item_group(item_group_id: str) -> dict:
    """
    Retrieve all items in a multi-variation listing (item group).

    Args:
        item_group_id: The eBay item group ID.
    Returns:
        dict with items list, each containing variation-specific details.
    """
    params = {"item_group_id": item_group_id}
    return api_get(f"{BROWSE_BASE}/item/get_items_by_item_group", params=params)


@mcp.tool()
def get_items(
    item_ids: str,
    item_aspects_opt: str = "",
) -> dict:
    """
    Retrieve multiple eBay items in a single batch call (up to 20 items).

    Args:
        item_ids: Pipe-separated list of item IDs (e.g. 'v1|123|0|v1|456|0').
        item_aspects_opt: Comma-separated aspects to return.
    Returns:
        dict with items list and any errors for individual IDs.
    """
    params: dict = {"item_ids": item_ids}
    if item_aspects_opt:
        params["item_aspects_opt"] = item_aspects_opt
    return api_get(f"{BROWSE_BASE}/item/", params=params)


# ---------------------------------------------------------------------------
# Compatibility
# ---------------------------------------------------------------------------

@mcp.tool()
def check_compatibility(
    item_id: str,
    compatibility_properties: list[dict],
) -> dict:
    """
    Check whether a part/accessory item is compatible with a vehicle or device.

    Args:
        item_id: The eBay item ID to check compatibility for.
        compatibility_properties: List of name/value dicts describing the
            vehicle or device (e.g. [{"name":"Year","value":"2020"},
            {"name":"Make","value":"Toyota"}]).
    Returns:
        dict with compatibilityStatus ('COMPATIBLE', 'NOT_COMPATIBLE', 'UNDETERMINED').
    """
    body = {"compatibilityProperties": compatibility_properties}
    return api_post(f"{BROWSE_BASE}/item/{item_id}/check_compatibility", body=body)


@mcp.tool()
def get_compatibility_properties(
    category_tree_id: str,
    category_id: str,
) -> dict:
    """
    Retrieve the compatibility property names for a given category (e.g. Year, Make, Model).

    Args:
        category_tree_id: The eBay category tree ID (e.g. '0' for US).
        category_id: The leaf category ID to get compatibility properties for.
    Returns:
        dict with compatibilityProperties list.
    """
    params = {
        "category_tree_id": category_tree_id,
        "category_id": category_id,
    }
    return api_get(f"{BROWSE_BASE}/item/get_compatibility_properties", params=params)


@mcp.tool()
def get_compatibility_property_values(
    category_tree_id: str,
    category_id: str,
    compatibility_property: str,
    filter: str = "",
) -> dict:
    """
    Retrieve valid values for a specific compatibility property (e.g. all valid Makes).

    Args:
        category_tree_id: The eBay category tree ID.
        category_id: The leaf category ID.
        compatibility_property: The property name (e.g. 'Make', 'Model', 'Year').
        filter: Filter string to narrow values
                (e.g. 'Year:2020,Make:Toyota' when querying Model values).
    Returns:
        dict with compatibilityPropertyValues list.
    """
    params: dict = {
        "category_tree_id": category_tree_id,
        "category_id": category_id,
        "compatibility_property": compatibility_property,
    }
    if filter:
        params["filter"] = filter
    return api_get(
        f"{BROWSE_BASE}/item/get_compatibility_property_values", params=params
    )
