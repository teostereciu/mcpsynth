"""Tools for eBay Buy Browse API."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .ebay_client import EbayApiError, make_buy_api_request, tool_error


def browse_search(
    q: Optional[str] = None,
    *,
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
    """Search for items and return item summaries.

    Maps to GET /buy/v1/item_summary/search

    Args:
      q: Keyword query.
      category_ids: Comma-separated category IDs.
      filter: Browse API filter string, e.g. "price:[100..500]".
      sort: Sort order.
      limit: Page size.
      offset: Result offset.
      fieldgroups: e.g. "EXTENDED".
      aspect_filter: Aspect filter string.
      compatibility_filter: Compatibility filter string.
      charity_ids: Charity IDs.
      epid: eBay product ID.
      gtin: GTIN.
      marketplace_id: Marketplace header value.
    """

    params: Dict[str, Any] = {"limit": limit, "offset": offset}
    if q is not None:
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
    if compatibility_filter:
        params["compatibility_filter"] = compatibility_filter
    if charity_ids:
        params["charity_ids"] = charity_ids
    if epid:
        params["epid"] = epid
    if gtin:
        params["gtin"] = gtin

    try:
        return make_buy_api_request(
            "GET",
            "/buy/v1/item_summary/search",
            params=params,
            marketplace_id=marketplace_id,
        )
    except EbayApiError as e:
        return tool_error(str(e))


def browse_search_by_image(
    image_url: str,
    *,
    filter: Optional[str] = None,
    sort: Optional[str] = None,
    limit: int = 50,
    offset: int = 0,
    marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    """Search for items using an image URL.

    Maps to GET /buy/v1/item_summary/search_by_image
    """

    params: Dict[str, Any] = {"image_url": image_url, "limit": limit, "offset": offset}
    if filter:
        params["filter"] = filter
    if sort:
        params["sort"] = sort

    try:
        return make_buy_api_request(
            "GET",
            "/buy/v1/item_summary/search_by_image",
            params=params,
            marketplace_id=marketplace_id,
        )
    except EbayApiError as e:
        return tool_error(str(e))


def browse_get_item(
    item_id: str,
    *,
    fieldgroups: Optional[str] = None,
    if_none_match: Optional[str] = None,
    marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    """Get full item details.

    Maps to GET /buy/v1/item/{item_id}
    """

    params: Dict[str, Any] = {}
    if fieldgroups:
        params["fieldgroups"] = fieldgroups

    extra_headers: Dict[str, str] = {}
    if if_none_match:
        extra_headers["If-None-Match"] = if_none_match

    try:
        return make_buy_api_request(
            "GET",
            f"/buy/v1/item/{item_id}",
            params=params or None,
            marketplace_id=marketplace_id,
            extra_headers=extra_headers or None,
        )
    except EbayApiError as e:
        return tool_error(str(e))


def browse_get_item_by_legacy_id(
    legacy_item_id: str,
    *,
    legacy_variation_id: Optional[str] = None,
    fieldgroups: Optional[str] = None,
    marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    """Get item details using a legacy item ID.

    Maps to GET /buy/v1/item/get_item_by_legacy_id
    """

    params: Dict[str, Any] = {"legacy_item_id": legacy_item_id}
    if legacy_variation_id:
        params["legacy_variation_id"] = legacy_variation_id
    if fieldgroups:
        params["fieldgroups"] = fieldgroups

    try:
        return make_buy_api_request(
            "GET",
            "/buy/v1/item/get_item_by_legacy_id",
            params=params,
            marketplace_id=marketplace_id,
        )
    except EbayApiError as e:
        return tool_error(str(e))


def browse_get_items(
    *,
    item_ids: Optional[List[str]] = None,
    item_group_ids: Optional[List[str]] = None,
    marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    """Get multiple items (or item groups) in one request.

    Maps to GET /buy/v1/item/

    Provide either item_ids or item_group_ids.
    """

    params: Dict[str, Any] = {}
    if item_ids:
        params["item_ids"] = ",".join(item_ids)
    if item_group_ids:
        params["item_group_ids"] = ",".join(item_group_ids)

    if not params:
        return tool_error("Provide item_ids and/or item_group_ids")

    try:
        return make_buy_api_request(
            "GET",
            "/buy/v1/item/",
            params=params,
            marketplace_id=marketplace_id,
        )
    except EbayApiError as e:
        return tool_error(str(e))


def browse_get_items_by_item_group(
    item_group_id: str,
    *,
    marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    """Get items in an item group.

    Maps to GET /buy/v1/item/get_items_by_item_group
    """

    try:
        return make_buy_api_request(
            "GET",
            "/buy/v1/item/get_items_by_item_group",
            params={"item_group_id": item_group_id},
            marketplace_id=marketplace_id,
        )
    except EbayApiError as e:
        return tool_error(str(e))


def browse_check_compatibility(
    item_id: str,
    compatibility_properties: List[Dict[str, str]],
    *,
    marketplace_id: str = "EBAY_US",
) -> Dict[str, Any]:
    """Check part compatibility for an item.

    Maps to POST /buy/v1/item/{item_id}/check_compatibility

    compatibility_properties example:
      [{"name": "Year", "value": "2011"}, {"name": "Make", "value": "BMW"}]
    """

    payload = {"compatibilityProperties": compatibility_properties}
    try:
        return make_buy_api_request(
            "POST",
            f"/buy/v1/item/{item_id}/check_compatibility",
            json=payload,
            marketplace_id=marketplace_id,
        )
    except EbayApiError as e:
        return tool_error(str(e))
