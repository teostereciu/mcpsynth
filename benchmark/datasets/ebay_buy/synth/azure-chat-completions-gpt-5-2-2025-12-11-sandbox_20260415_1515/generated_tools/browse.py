from typing import Any, Dict, Optional

from .http_client import EbayClient


client = EbayClient()


def browse_search(
    q: Optional[str] = None,
    *,
    category_ids: Optional[str] = None,
    charity_ids: Optional[str] = None,
    epid: Optional[str] = None,
    gtin: Optional[str] = None,
    filter: Optional[str] = None,
    aspect_filter: Optional[str] = None,
    compatibility_filter: Optional[str] = None,
    fieldgroups: Optional[str] = None,
    sort: Optional[str] = None,
    limit: Optional[int] = 50,
    offset: Optional[int] = 0,
    marketplace_id: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if q is not None:
        params["q"] = q
    if category_ids is not None:
        params["category_ids"] = category_ids
    if charity_ids is not None:
        params["charity_ids"] = charity_ids
    if epid is not None:
        params["epid"] = epid
    if gtin is not None:
        params["gtin"] = gtin
    if filter is not None:
        params["filter"] = filter
    if aspect_filter is not None:
        params["aspect_filter"] = aspect_filter
    if compatibility_filter is not None:
        params["compatibility_filter"] = compatibility_filter
    if fieldgroups is not None:
        params["fieldgroups"] = fieldgroups
    if sort is not None:
        params["sort"] = sort
    if limit is not None:
        params["limit"] = int(limit)
    if offset is not None:
        params["offset"] = int(offset)

    headers: Dict[str, str] = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request("GET", "/buy/browse/v1/item_summary/search", params=params, headers=headers)


def browse_get_item(
    item_id: str,
    *,
    fieldgroups: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if fieldgroups is not None:
        params["fieldgroups"] = fieldgroups

    headers: Dict[str, str] = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request("GET", f"/buy/browse/v1/item/{item_id}", params=params, headers=headers)


def browse_get_item_by_legacy_id(
    legacy_item_id: str,
    *,
    legacy_variation_id: Optional[str] = None,
    fieldgroups: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"legacy_item_id": legacy_item_id}
    if legacy_variation_id is not None:
        params["legacy_variation_id"] = legacy_variation_id
    if fieldgroups is not None:
        params["fieldgroups"] = fieldgroups

    headers: Dict[str, str] = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request("GET", "/buy/browse/v1/item/get_item_by_legacy_id", params=params, headers=headers)


def browse_get_items_by_item_group(
    item_group_id: str,
    *,
    marketplace_id: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"item_group_id": item_group_id}
    headers: Dict[str, str] = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx
    return client.request("GET", "/buy/browse/v1/item/get_items_by_item_group", params=params, headers=headers)


def browse_get_items(
    *,
    item_ids: Optional[str] = None,
    item_group_ids: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    """Bulk get items by item_ids or item_group_ids (comma-separated)."""
    params: Dict[str, Any] = {}
    if item_ids is not None:
        params["item_ids"] = item_ids
    if item_group_ids is not None:
        params["item_group_ids"] = item_group_ids

    headers: Dict[str, str] = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request("GET", "/buy/browse/v1/item/", params=params, headers=headers)


def browse_check_compatibility(
    item_id: str,
    *,
    compatibility_properties: str,
    marketplace_id: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    """Check part compatibility for an item.

    compatibility_properties: e.g. "Year:2011,Make:BMW,Model:R1200GS"
    """
    headers: Dict[str, str] = {"Content-Type": "application/json"}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    payload = {"compatibilityProperties": compatibility_properties}
    return client.request("POST", f"/buy/browse/v1/item/{item_id}/check_compatibility", json=payload, headers=headers)


def browse_search_by_image(
    *,
    image_url: str,
    marketplace_id: Optional[str] = None,
    limit: Optional[int] = 50,
    offset: Optional[int] = 0,
) -> Dict[str, Any]:
    headers: Dict[str, str] = {"Content-Type": "application/json"}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id

    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = int(limit)
    if offset is not None:
        params["offset"] = int(offset)

    payload = {"imageUrl": image_url}
    return client.request("POST", "/buy/browse/v1/item_summary/search_by_image", params=params, json=payload, headers=headers)
