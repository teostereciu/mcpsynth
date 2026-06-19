from __future__ import annotations

from typing import Any, Dict, Optional

from .ebay_client import EbayClient


# Scopes (best-effort defaults)
BROWSE_SCOPE = "https://api.ebay.com/oauth/api_scope"


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
    auto_correct: Optional[bool] = None,
    charity_ids: Optional[str] = None,
    epid: Optional[str] = None,
    gtin: Optional[str] = None,
    buyer_postal_code: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /buy/browse/v1/item_summary/search"""
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
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    if aspect_filter is not None:
        params["aspect_filter"] = aspect_filter
    if fieldgroups is not None:
        params["fieldgroups"] = fieldgroups
    if compatibility_filter is not None:
        params["compatibility_filter"] = compatibility_filter
    if auto_correct is not None:
        params["auto_correct"] = str(auto_correct).lower()
    if charity_ids is not None:
        params["charity_ids"] = charity_ids
    if epid is not None:
        params["epid"] = epid
    if gtin is not None:
        params["gtin"] = gtin
    if buyer_postal_code is not None:
        params["buyerPostalCode"] = buyer_postal_code

    return EbayClient().request("GET", "/buy/browse/v1/item_summary/search", scope=BROWSE_SCOPE, params=params)


def get_item(item_id: str, fieldgroups: Optional[str] = None) -> Dict[str, Any]:
    """GET /buy/browse/v1/item/{item_id}"""
    params: Dict[str, Any] = {}
    if fieldgroups is not None:
        params["fieldgroups"] = fieldgroups
    return EbayClient().request("GET", f"/buy/browse/v1/item/{item_id}", scope=BROWSE_SCOPE, params=params)


def get_item_by_legacy_id(legacy_item_id: str) -> Dict[str, Any]:
    """GET /buy/browse/v1/item/get_item_by_legacy_id"""
    params = {"legacy_item_id": legacy_item_id}
    return EbayClient().request("GET", "/buy/browse/v1/item/get_item_by_legacy_id", scope=BROWSE_SCOPE, params=params)


def get_items_by_item_group(item_group_id: str) -> Dict[str, Any]:
    """GET /buy/browse/v1/item/get_items_by_item_group"""
    params = {"item_group_id": item_group_id}
    return EbayClient().request("GET", "/buy/browse/v1/item/get_items_by_item_group", scope=BROWSE_SCOPE, params=params)


def get_item_group(item_group_id: str) -> Dict[str, Any]:
    """GET /buy/browse/v1/item_group/{item_group_id}"""
    return EbayClient().request("GET", f"/buy/browse/v1/item_group/{item_group_id}", scope=BROWSE_SCOPE)


def check_item_compatibility(item_id: str, compatibility_properties: str) -> Dict[str, Any]:
    """GET /buy/browse/v1/item/{item_id}/check_compatibility"""
    params = {"compatibility_properties": compatibility_properties}
    return EbayClient().request(
        "GET", f"/buy/browse/v1/item/{item_id}/check_compatibility", scope=BROWSE_SCOPE, params=params
    )


def get_item_compatibility(item_id: str, limit: Optional[int] = None, offset: Optional[int] = None) -> Dict[str, Any]:
    """GET /buy/browse/v1/item/{item_id}/get_compatibility"""
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    return EbayClient().request(
        "GET", f"/buy/browse/v1/item/{item_id}/get_compatibility", scope=BROWSE_SCOPE, params=params
    )


def get_item_merchandising(item_id: str) -> Dict[str, Any]:
    """GET /buy/browse/v1/item/{item_id}/get_merchandising"""
    return EbayClient().request("GET", f"/buy/browse/v1/item/{item_id}/get_merchandising", scope=BROWSE_SCOPE)


def get_item_location(item_id: str) -> Dict[str, Any]:
    """GET /buy/browse/v1/item/{item_id}/get_item_location"""
    return EbayClient().request("GET", f"/buy/browse/v1/item/{item_id}/get_item_location", scope=BROWSE_SCOPE)


def get_item_snapshot_feed(feed_scope: str, date: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None) -> Dict[str, Any]:
    """GET /buy/browse/v1/item_snapshot_feed"""
    params: Dict[str, Any] = {"feed_scope": feed_scope}
    if date is not None:
        params["date"] = date
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    return EbayClient().request("GET", "/buy/browse/v1/item_snapshot_feed", scope=BROWSE_SCOPE, params=params)
