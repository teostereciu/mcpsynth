"""Tools for eBay Buy Browse API."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .http import request_json, tool_safe_call


def browse_search(
    *,
    q: Optional[str] = None,
    category_ids: Optional[str] = None,
    filter: Optional[str] = None,
    sort: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    fieldgroups: Optional[str] = None,
    aspect_filter: Optional[str] = None,
    compatibility_filter: Optional[str] = None,
    charity_ids: Optional[str] = None,
    epids: Optional[str] = None,
    gtins: Optional[str] = None,
    marketplace_id: Optional[str] = None,
) -> Dict[str, Any]:
    """Search for item summaries.

    Wraps: GET /buy/browse/v1/item_summary/search

    Common params:
      - q: keyword
      - category_ids: comma-separated category IDs
      - filter: e.g. "price:[100..500]"
      - limit/offset
    """

    params: Dict[str, Any] = {}
    if q is not None:
        params["q"] = q
    if category_ids is not None:
        params["category_ids"] = category_ids
    if filter is not None:
        params["filter"] = filter
    if sort is not None:
        params["sort"] = sort
    if limit is not None:
        params["limit"] = int(limit)
    if offset is not None:
        params["offset"] = int(offset)
    if fieldgroups is not None:
        params["fieldgroups"] = fieldgroups
    if aspect_filter is not None:
        params["aspect_filter"] = aspect_filter
    if compatibility_filter is not None:
        params["compatibility_filter"] = compatibility_filter
    if charity_ids is not None:
        params["charity_ids"] = charity_ids
    if epids is not None:
        params["epids"] = epids
    if gtins is not None:
        params["gtins"] = gtins

    return tool_safe_call(
        request_json,
        "GET",
        "/buy/browse/v1/item_summary/search",
        params=params,
        marketplace_id=marketplace_id,
    )


def browse_get_item(*, item_id: str, fieldgroups: Optional[str] = None, marketplace_id: Optional[str] = None) -> Dict[str, Any]:
    """Get full item details.

    Wraps: GET /buy/browse/v1/item/{item_id}
    """

    params: Dict[str, Any] = {}
    if fieldgroups is not None:
        params["fieldgroups"] = fieldgroups

    return tool_safe_call(
        request_json,
        "GET",
        f"/buy/browse/v1/item/{item_id}",
        params=params or None,
        marketplace_id=marketplace_id,
    )


def browse_get_items(*, item_ids: List[str], marketplace_id: Optional[str] = None) -> Dict[str, Any]:
    """Batch get item details.

    Wraps: GET /buy/browse/v1/item/

    eBay expects item_ids as a comma-separated list in query param `item_ids`.
    """

    params = {"item_ids": ",".join(item_ids)}
    return tool_safe_call(
        request_json,
        "GET",
        "/buy/browse/v1/item/",
        params=params,
        marketplace_id=marketplace_id,
    )


def browse_get_item_by_legacy_id(
    *,
    legacy_item_id: str,
    legacy_variation_id: Optional[str] = None,
    fieldgroups: Optional[str] = None,
    marketplace_id: Optional[str] = None,
) -> Dict[str, Any]:
    """Get item details by legacy (numeric) item ID.

    Wraps: GET /buy/browse/v1/item/get_item_by_legacy_id
    """

    params: Dict[str, Any] = {"legacy_item_id": legacy_item_id}
    if legacy_variation_id is not None:
        params["legacy_variation_id"] = legacy_variation_id
    if fieldgroups is not None:
        params["fieldgroups"] = fieldgroups

    return tool_safe_call(
        request_json,
        "GET",
        "/buy/browse/v1/item/get_item_by_legacy_id",
        params=params,
        marketplace_id=marketplace_id,
    )


def browse_get_items_by_item_group(
    *,
    item_group_id: str,
    marketplace_id: Optional[str] = None,
) -> Dict[str, Any]:
    """Get items in an item group.

    Wraps: GET /buy/browse/v1/item/get_items_by_item_group
    """

    params = {"item_group_id": item_group_id}
    return tool_safe_call(
        request_json,
        "GET",
        "/buy/browse/v1/item/get_items_by_item_group",
        params=params,
        marketplace_id=marketplace_id,
    )


def browse_search_by_image(
    *,
    image_url: str,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    filter: Optional[str] = None,
    marketplace_id: Optional[str] = None,
) -> Dict[str, Any]:
    """Search for items using an image URL.

    Wraps: GET /buy/browse/v1/item_summary/search_by_image
    """

    params: Dict[str, Any] = {"image_url": image_url}
    if limit is not None:
        params["limit"] = int(limit)
    if offset is not None:
        params["offset"] = int(offset)
    if filter is not None:
        params["filter"] = filter

    return tool_safe_call(
        request_json,
        "GET",
        "/buy/browse/v1/item_summary/search_by_image",
        params=params,
        marketplace_id=marketplace_id,
    )


def browse_check_compatibility(
    *,
    item_id: str,
    compatibility_properties: str,
    marketplace_id: Optional[str] = None,
) -> Dict[str, Any]:
    """Check if an item is compatible with provided product properties.

    Wraps: GET /buy/browse/v1/item/{item_id}/check_compatibility

    compatibility_properties is a string like: "Year:2011,Make:BMW,Model:R1200GS"
    """

    params = {"compatibility_properties": compatibility_properties}
    return tool_safe_call(
        request_json,
        "GET",
        f"/buy/browse/v1/item/{item_id}/check_compatibility",
        params=params,
        marketplace_id=marketplace_id,
    )
