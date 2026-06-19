"""Tools for eBay Buy Browse API."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .http import request_json


def search_items(
    *,
    q: Optional[str] = None,
    category_ids: Optional[str] = None,
    filter: Optional[str] = None,
    sort: Optional[str] = None,
    limit: int = 50,
    offset: int = 0,
    fieldgroups: Optional[str] = None,
    aspect_filter: Optional[str] = None,
    compatibility_filter: Optional[str] = None,
    charity_ids: Optional[str] = None,
    epid: Optional[str] = None,
    gtin: Optional[str] = None,
    marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    """Search for item summaries.

    Wraps: GET /buy/v1/item_summary/search
    """

    params: Dict[str, Any] = {
        "q": q,
        "category_ids": category_ids,
        "filter": filter,
        "sort": sort,
        "limit": limit,
        "offset": offset,
        "fieldgroups": fieldgroups,
        "aspect_filter": aspect_filter,
        "compatibility_filter": compatibility_filter,
        "charity_ids": charity_ids,
        "epid": epid,
        "gtin": gtin,
    }
    params = {k: v for k, v in params.items() if v is not None}

    return request_json(
        "GET",
        "/buy/v1/item_summary/search",
        params=params,
        marketplace_id=marketplace_id,
    )


def get_item(
    *,
    item_id: str,
    fieldgroups: Optional[str] = None,
    marketplace_id: str = "EBAY_US",
    if_modified_since: Optional[str] = None,
) -> Dict[str, Any]:
    """Get full item details.

    Wraps: GET /buy/v1/item/{item_id}
    """

    params = {"fieldgroups": fieldgroups} if fieldgroups else None
    extra_headers = {"If-Modified-Since": if_modified_since} if if_modified_since else None

    return request_json(
        "GET",
        f"/buy/v1/item/{item_id}",
        params=params,
        marketplace_id=marketplace_id,
        extra_headers=extra_headers,
    )


def get_items(
    *,
    item_ids: Optional[List[str]] = None,
    item_group_ids: Optional[List[str]] = None,
    marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    """Get multiple items (or item groups) in one call.

    Wraps: GET /buy/v1/item/
    """

    params: Dict[str, Any] = {}
    if item_ids:
        params["item_ids"] = ",".join(item_ids)
    if item_group_ids:
        params["item_group_ids"] = ",".join(item_group_ids)

    return request_json(
        "GET",
        "/buy/v1/item/",
        params=params or None,
        marketplace_id=marketplace_id,
    )


def get_item_by_legacy_id(
    *,
    legacy_item_id: str,
    legacy_variation_id: Optional[str] = None,
    fieldgroups: Optional[str] = None,
    marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    """Get item details using legacy item ID.

    Wraps: GET /buy/v1/item/get_item_by_legacy_id
    """

    params: Dict[str, Any] = {"legacy_item_id": legacy_item_id}
    if legacy_variation_id:
        params["legacy_variation_id"] = legacy_variation_id
    if fieldgroups:
        params["fieldgroups"] = fieldgroups

    return request_json(
        "GET",
        "/buy/v1/item/get_item_by_legacy_id",
        params=params,
        marketplace_id=marketplace_id,
    )


def get_items_by_item_group(
    *,
    item_group_id: str,
    marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    """Get items in an item group.

    Wraps: GET /buy/v1/item_group/{item_group_id}
    """

    return request_json(
        "GET",
        f"/buy/v1/item_group/{item_group_id}",
        marketplace_id=marketplace_id,
    )


def search_by_image(
    *,
    image_url: str,
    limit: int = 50,
    offset: int = 0,
    marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    """Search for items using an image URL.

    Wraps: GET /buy/v1/item_summary/search_by_image
    """

    params = {"image_url": image_url, "limit": limit, "offset": offset}
    return request_json(
        "GET",
        "/buy/v1/item_summary/search_by_image",
        params=params,
        marketplace_id=marketplace_id,
    )


def check_compatibility(
    *,
    item_id: str,
    compatibility_properties: Dict[str, Any],
    marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    """Check if an item is compatible with a product (e.g., vehicle).

    Wraps: POST /buy/v1/item/{item_id}/check_compatibility
    """

    return request_json(
        "POST",
        f"/buy/v1/item/{item_id}/check_compatibility",
        json_body=compatibility_properties,
        marketplace_id=marketplace_id,
    )
