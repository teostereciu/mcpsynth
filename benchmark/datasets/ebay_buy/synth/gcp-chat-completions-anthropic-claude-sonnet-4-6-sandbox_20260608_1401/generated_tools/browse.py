"""
eBay Buy Browse API tools.
Covers: item search, item details, item groups, compatibility checks.
"""
from typing import Optional
from . import _client as client


def search_items(
    q: Optional[str] = None,
    category_ids: Optional[str] = None,
    filter: Optional[str] = None,
    sort: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    aspect_filter: Optional[str] = None,
    fieldgroups: Optional[str] = None,
    compatibility_filter: Optional[str] = None,
    epid: Optional[str] = None,
    gtin: Optional[str] = None,
    charity_ids: Optional[str] = None,
    marketplace_id: Optional[str] = None,
) -> dict:
    """Search for eBay items by keyword, category, ePID, GTIN, or charity.

    Args:
        q: Keyword search string.
        category_ids: Comma-separated category IDs to filter results.
        filter: Field filters (e.g. 'price:[10..50],conditions:{NEW}').
        sort: Sort order (e.g. 'price', '-price', 'newlyListed', 'distance').
        limit: Max items per page (default 50, max 200).
        offset: Number of items to skip for pagination.
        aspect_filter: Filter by item aspects (e.g. 'categoryId:9355,Color:{Red}').
        fieldgroups: Controls response fields (e.g. 'EXTENDED', 'ASPECT_REFINEMENTS').
        compatibility_filter: Filter by vehicle compatibility attributes.
        epid: eBay product ID to search within.
        gtin: Global Trade Item Number (UPC, EAN, ISBN).
        charity_ids: Comma-separated charity registration IDs.
        marketplace_id: eBay marketplace ID (e.g. 'EBAY_US'). Defaults to EBAY_US.
    """
    params = {}
    if q is not None:
        params["q"] = q
    if category_ids is not None:
        params["category_ids"] = category_ids
    if filter is not None:
        params["filter"] = filter
    if sort is not None:
        params["sort"] = sort
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    if aspect_filter is not None:
        params["aspect_filter"] = aspect_filter
    if fieldgroups is not None:
        params["fieldgroups"] = fieldgroups
    if compatibility_filter is not None:
        params["compatibility_filter"] = compatibility_filter
    if epid is not None:
        params["epid"] = epid
    if gtin is not None:
        params["gtin"] = gtin
    if charity_ids is not None:
        params["charity_ids"] = charity_ids

    headers = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id

    return client.get(
        "/buy/browse/v1/item_summary/search",
        params=params,
        extra_headers=headers,
    )


def search_items_by_image(
    image_base64: str,
    category_ids: Optional[str] = None,
    filter: Optional[str] = None,
    aspect_filter: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    marketplace_id: Optional[str] = None,
) -> dict:
    """Search for eBay items using a Base64-encoded image.

    Args:
        image_base64: Base64-encoded image string.
        category_ids: Comma-separated category IDs to filter results.
        filter: Field filters (e.g. 'price:[10..50]').
        aspect_filter: Filter by item aspects.
        limit: Max items per page.
        offset: Number of items to skip for pagination.
        marketplace_id: eBay marketplace ID (e.g. 'EBAY_US').
    """
    params = {}
    if category_ids is not None:
        params["category_ids"] = category_ids
    if filter is not None:
        params["filter"] = filter
    if aspect_filter is not None:
        params["aspect_filter"] = aspect_filter
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset

    headers = {"Content-Type": "application/json"}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id

    body = {"image": image_base64}
    return client.post(
        "/buy/browse/v1/item_summary/search_by_image",
        params=params,
        json=body,
        extra_headers=headers,
    )


def get_item(
    item_id: str,
    fieldgroups: Optional[str] = None,
    marketplace_id: Optional[str] = None,
) -> dict:
    """Retrieve full details of a specific eBay item by its RESTful item ID.

    Args:
        item_id: The RESTful item ID (e.g. 'v1|123456789|0').
        fieldgroups: Optional field groups: PRODUCT, ADDITIONAL_SELLER_DETAILS,
                     CHARITY_DETAILS, or COMPACT.
        marketplace_id: eBay marketplace ID (e.g. 'EBAY_US').
    """
    params = {}
    if fieldgroups is not None:
        params["fieldgroups"] = fieldgroups

    headers = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id

    return client.get(
        f"/buy/browse/v1/item/{item_id}",
        params=params,
        extra_headers=headers,
    )


def get_item_by_legacy_id(
    legacy_item_id: str,
    legacy_variation_id: Optional[str] = None,
    legacy_variation_sku: Optional[str] = None,
    fieldgroups: Optional[str] = None,
    marketplace_id: Optional[str] = None,
) -> dict:
    """Retrieve item details using a legacy eBay item ID (from Shopping/Finding APIs).

    Args:
        legacy_item_id: The legacy item ID (numeric, as seen in eBay listing URLs).
        legacy_variation_id: Legacy variation ID for multi-SKU items.
        legacy_variation_sku: Seller-defined SKU for the variation.
        fieldgroups: Optional field groups: PRODUCT, ADDITIONAL_SELLER_DETAILS,
                     CHARITY_DETAILS.
        marketplace_id: eBay marketplace ID (e.g. 'EBAY_US').
    """
    params = {"legacy_item_id": legacy_item_id}
    if legacy_variation_id is not None:
        params["legacy_variation_id"] = legacy_variation_id
    if legacy_variation_sku is not None:
        params["legacy_variation_sku"] = legacy_variation_sku
    if fieldgroups is not None:
        params["fieldgroups"] = fieldgroups

    headers = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id

    return client.get(
        "/buy/browse/v1/item/get_item_by_legacy_id",
        params=params,
        extra_headers=headers,
    )


def get_items(
    item_ids: Optional[str] = None,
    item_group_ids: Optional[str] = None,
    marketplace_id: Optional[str] = None,
) -> dict:
    """Retrieve details for multiple eBay items by item IDs or item group IDs.

    Note: This is a Limited Release endpoint available only to select Partners.

    Args:
        item_ids: Comma-separated RESTful item IDs (e.g. 'v1|123|0,v1|456|0').
        item_group_ids: Comma-separated item group IDs.
        marketplace_id: eBay marketplace ID (e.g. 'EBAY_US').
    """
    params = {}
    if item_ids is not None:
        params["item_ids"] = item_ids
    if item_group_ids is not None:
        params["item_group_ids"] = item_group_ids

    headers = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id

    return client.get(
        "/buy/browse/v1/item/",
        params=params,
        extra_headers=headers,
    )


def get_items_by_item_group(
    item_group_id: str,
    fieldgroups: Optional[str] = None,
    marketplace_id: Optional[str] = None,
) -> dict:
    """Retrieve all item variations within an item group (e.g. different sizes/colors).

    Args:
        item_group_id: The item group ID (parent item ID for seller-defined variations).
        fieldgroups: Optional field groups: ADDITIONAL_SELLER_DETAILS, CHARITY_DETAILS.
        marketplace_id: eBay marketplace ID (e.g. 'EBAY_US').
    """
    params = {"item_group_id": item_group_id}
    if fieldgroups is not None:
        params["fieldgroups"] = fieldgroups

    headers = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id

    return client.get(
        "/buy/browse/v1/item/get_items_by_item_group",
        params=params,
        extra_headers=headers,
    )


def check_item_compatibility(
    item_id: str,
    compatibility_properties: list,
    marketplace_id: Optional[str] = None,
) -> dict:
    """Check if a part/item is compatible with a specific vehicle or product.

    Args:
        item_id: The RESTful item ID of the part to check (e.g. 'v1|123456789|0').
        compatibility_properties: List of dicts with 'name' and 'value' keys defining
            the product (e.g. [{'name': 'Make', 'value': 'Honda'},
                                {'name': 'Model', 'value': 'Civic'},
                                {'name': 'Year', 'value': '2020'}]).
        marketplace_id: eBay marketplace ID (e.g. 'EBAY_US').
    """
    headers = {"Content-Type": "application/json"}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id

    body = {"compatibilityProperties": compatibility_properties}
    return client.post(
        f"/buy/browse/v1/item/{item_id}/check_compatibility",
        json=body,
        extra_headers=headers,
    )
