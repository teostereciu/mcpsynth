"""
eBay Buy Browse API tools.
Covers: item search, item details, item groups, compatibility checks.
"""

from __future__ import annotations
from typing import Optional
from .auth import get_auth_header, get_base_url


def search_items(
    q: Optional[str] = None,
    category_ids: Optional[str] = None,
    filter: Optional[str] = None,
    sort: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    fieldgroups: Optional[str] = None,
    aspect_filter: Optional[str] = None,
    epid: Optional[str] = None,
    gtin: Optional[str] = None,
    charity_ids: Optional[str] = None,
    compatibility_filter: Optional[str] = None,
    marketplace_id: str = "EBAY_US",
) -> dict:
    """
    Search for eBay items by keyword, category, ePID, GTIN, or charity.
    Supports filtering, sorting, pagination, and aspect refinements.

    Args:
        q: Keyword search string.
        category_ids: Comma-separated category IDs to restrict results.
        filter: Filter string (e.g. 'price:[10..50],conditions:{NEW}').
        sort: Sort order (e.g. 'price', '-price', 'newlyListed', 'distance').
        limit: Number of results per page (max 200).
        offset: Number of results to skip for pagination.
        fieldgroups: Controls response fields (e.g. 'EXTENDED', 'FULL').
        aspect_filter: Aspect filter string (e.g. 'categoryId:9355,Color:{Blue}').
        epid: eBay product ID to search within.
        gtin: Global Trade Item Number (UPC/EAN/ISBN).
        charity_ids: Comma-separated charity registration IDs.
        compatibility_filter: Compatibility filter for vehicle parts.
        marketplace_id: eBay marketplace ID (default EBAY_US).
    """
    import requests
    params = {}
    if q:
        params["q"] = q
    if category_ids:
        params["category_ids"] = category_ids
    if filter:
        params["filter"] = filter
    if sort:
        params["sort"] = sort
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    if fieldgroups:
        params["fieldgroups"] = fieldgroups
    if aspect_filter:
        params["aspect_filter"] = aspect_filter
    if epid:
        params["epid"] = epid
    if gtin:
        params["gtin"] = gtin
    if charity_ids:
        params["charity_ids"] = charity_ids
    if compatibility_filter:
        params["compatibility_filter"] = compatibility_filter

    url = f"{get_base_url()}/buy/browse/v1/item_summary/search"
    headers = get_auth_header()
    headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    try:
        resp = requests.get(url, headers=headers, params=params, timeout=30)
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def search_items_by_image(
    image_base64: str,
    category_ids: Optional[str] = None,
    filter: Optional[str] = None,
    aspect_filter: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    marketplace_id: str = "EBAY_US",
) -> dict:
    """
    Search for eBay items using a Base64-encoded image.

    Args:
        image_base64: Base64-encoded image string.
        category_ids: Comma-separated category IDs to restrict results.
        filter: Filter string (e.g. 'price:[10..50]').
        aspect_filter: Aspect filter string.
        limit: Number of results per page.
        offset: Number of results to skip.
        marketplace_id: eBay marketplace ID (default EBAY_US).
    """
    import requests
    params = {}
    if category_ids:
        params["category_ids"] = category_ids
    if filter:
        params["filter"] = filter
    if aspect_filter:
        params["aspect_filter"] = aspect_filter
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset

    url = f"{get_base_url()}/buy/browse/v1/item_summary/search_by_image"
    headers = get_auth_header()
    headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    headers["Content-Type"] = "application/json"
    body = {"image": image_base64}
    try:
        resp = requests.post(url, headers=headers, params=params, json=body, timeout=30)
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def get_item(
    item_id: str,
    fieldgroups: Optional[str] = None,
    marketplace_id: str = "EBAY_US",
) -> dict:
    """
    Retrieve full details of a specific eBay item by its RESTful item ID.

    Args:
        item_id: The RESTful item ID (e.g. 'v1|123456789|0').
        fieldgroups: Optional field groups: PRODUCT, ADDITIONAL_SELLER_DETAILS,
                     CHARITY_DETAILS, or COMPACT.
        marketplace_id: eBay marketplace ID (default EBAY_US).
    """
    import requests
    params = {}
    if fieldgroups:
        params["fieldgroups"] = fieldgroups

    url = f"{get_base_url()}/buy/browse/v1/item/{item_id}"
    headers = get_auth_header()
    headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    try:
        resp = requests.get(url, headers=headers, params=params, timeout=30)
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def get_item_by_legacy_id(
    legacy_item_id: str,
    legacy_variation_id: Optional[str] = None,
    legacy_variation_sku: Optional[str] = None,
    fieldgroups: Optional[str] = None,
    marketplace_id: str = "EBAY_US",
) -> dict:
    """
    Retrieve item details using a legacy eBay item ID (from Shopping/Finding APIs).

    Args:
        legacy_item_id: The legacy item ID (numeric string).
        legacy_variation_id: Legacy variation ID for multi-SKU listings.
        legacy_variation_sku: SKU of the variation.
        fieldgroups: Optional field groups: PRODUCT, ADDITIONAL_SELLER_DETAILS,
                     CHARITY_DETAILS.
        marketplace_id: eBay marketplace ID (default EBAY_US).
    """
    import requests
    params = {"legacy_item_id": legacy_item_id}
    if legacy_variation_id:
        params["legacy_variation_id"] = legacy_variation_id
    if legacy_variation_sku:
        params["legacy_variation_sku"] = legacy_variation_sku
    if fieldgroups:
        params["fieldgroups"] = fieldgroups

    url = f"{get_base_url()}/buy/browse/v1/item/get_item_by_legacy_id"
    headers = get_auth_header()
    headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    try:
        resp = requests.get(url, headers=headers, params=params, timeout=30)
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def get_items(
    item_ids: Optional[str] = None,
    item_group_ids: Optional[str] = None,
    marketplace_id: str = "EBAY_US",
) -> dict:
    """
    Retrieve details for multiple eBay items by item IDs or item group IDs.
    Note: Limited Release — only available to select Partners.

    Args:
        item_ids: Comma-separated list of RESTful item IDs (max 20).
        item_group_ids: Comma-separated list of item group IDs (max 10).
        marketplace_id: eBay marketplace ID (default EBAY_US).
    """
    import requests
    params = {}
    if item_ids:
        params["item_ids"] = item_ids
    if item_group_ids:
        params["item_group_ids"] = item_group_ids

    url = f"{get_base_url()}/buy/browse/v1/item/"
    headers = get_auth_header()
    headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    try:
        resp = requests.get(url, headers=headers, params=params, timeout=30)
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def get_items_by_item_group(
    item_group_id: str,
    fieldgroups: Optional[str] = None,
    marketplace_id: str = "EBAY_US",
) -> dict:
    """
    Retrieve details for all items in an item group (variations like color/size).

    Args:
        item_group_id: The item group ID.
        fieldgroups: Optional field groups: ADDITIONAL_SELLER_DETAILS, CHARITY_DETAILS.
        marketplace_id: eBay marketplace ID (default EBAY_US).
    """
    import requests
    params = {"item_group_id": item_group_id}
    if fieldgroups:
        params["fieldgroups"] = fieldgroups

    url = f"{get_base_url()}/buy/browse/v1/item/get_items_by_item_group"
    headers = get_auth_header()
    headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    try:
        resp = requests.get(url, headers=headers, params=params, timeout=30)
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def check_item_compatibility(
    listing_id: str,
    compatibility_properties: list,
    marketplace_id: str = "EBAY_US",
) -> dict:
    """
    Check if a product (e.g. car part) is compatible with a specific eBay item.

    Args:
        listing_id: The RESTful item ID of the part listing (e.g. 'v1|123|0').
        compatibility_properties: List of dicts with 'name' and 'value' keys
            describing the vehicle (e.g. [{'name': 'Make', 'value': 'Honda'},
            {'name': 'Year', 'value': '2016'}]).
        marketplace_id: eBay marketplace ID (default EBAY_US).

    Returns:
        Dict with 'compatibilityStatus': COMPATIBLE, NOT_COMPATIBLE, or UNDETERMINED.
    """
    import requests
    url = f"{get_base_url()}/buy/browse/v1/item/{listing_id}/check_compatibility"
    headers = get_auth_header()
    headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    headers["Content-Type"] = "application/json"
    body = {"compatibilityProperties": compatibility_properties}
    try:
        resp = requests.post(url, headers=headers, json=body, timeout=30)
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}
