from typing import Any, Dict, List, Optional

from .client import EbayClient


def browse_search(
    client: EbayClient,
    *,
    q: Optional[str] = None,
    category_ids: Optional[str] = None,
    charity_ids: Optional[str] = None,
    epid: Optional[str] = None,
    gtin: Optional[str] = None,
    filter: Optional[str] = None,
    aspect_filter: Optional[str] = None,
    compatibility_filter: Optional[str] = None,
    fieldgroups: Optional[str] = None,
    sort: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
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
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset

    headers: Dict[str, str] = {}
    if marketplace_id is not None:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if enduserctx is not None:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request("GET", "/buy/v1/item_summary/search", params=params, headers=headers)


def browse_search_by_image(
    client: EbayClient,
    *,
    image_url: str,
    filter: Optional[str] = None,
    aspect_filter: Optional[str] = None,
    fieldgroups: Optional[str] = None,
    sort: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    marketplace_id: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"image_url": image_url}
    if filter is not None:
        params["filter"] = filter
    if aspect_filter is not None:
        params["aspect_filter"] = aspect_filter
    if fieldgroups is not None:
        params["fieldgroups"] = fieldgroups
    if sort is not None:
        params["sort"] = sort
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset

    headers: Dict[str, str] = {}
    if marketplace_id is not None:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if enduserctx is not None:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request("GET", "/buy/v1/item_summary/search_by_image", params=params, headers=headers)


def browse_get_item(
    client: EbayClient,
    item_id: str,
    *,
    fieldgroups: Optional[str] = None,
    if_none_match: Optional[str] = None,
    marketplace_id: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if fieldgroups is not None:
        params["fieldgroups"] = fieldgroups

    headers: Dict[str, str] = {}
    if if_none_match is not None:
        headers["If-None-Match"] = if_none_match
    if marketplace_id is not None:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id

    return client.request("GET", f"/buy/v1/item/{item_id}", params=params, headers=headers)


def browse_get_item_by_legacy_id(
    client: EbayClient,
    legacy_item_id: str,
    *,
    legacy_variation_id: Optional[str] = None,
    fieldgroups: Optional[str] = None,
    marketplace_id: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"legacy_item_id": legacy_item_id}
    if legacy_variation_id is not None:
        params["legacy_variation_id"] = legacy_variation_id
    if fieldgroups is not None:
        params["fieldgroups"] = fieldgroups

    headers: Dict[str, str] = {}
    if marketplace_id is not None:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id

    return client.request("GET", "/buy/v1/item/get_item_by_legacy_id", params=params, headers=headers)


def browse_get_items(
    client: EbayClient,
    *,
    item_ids: Optional[List[str]] = None,
    item_group_ids: Optional[List[str]] = None,
    marketplace_id: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if item_ids:
        params["item_ids"] = ",".join(item_ids)
    if item_group_ids:
        params["item_group_ids"] = ",".join(item_group_ids)

    headers: Dict[str, str] = {}
    if marketplace_id is not None:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id

    return client.request("GET", "/buy/v1/item/", params=params, headers=headers)


def browse_get_items_by_item_group(
    client: EbayClient,
    item_group_id: str,
    *,
    marketplace_id: Optional[str] = None,
) -> Dict[str, Any]:
    headers: Dict[str, str] = {}
    if marketplace_id is not None:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id

    return client.request("GET", f"/buy/v1/item/get_items_by_item_group?item_group_id={item_group_id}", headers=headers)


def browse_check_compatibility(
    client: EbayClient,
    item_id: str,
    *,
    compatibility_properties: List[Dict[str, str]],
    marketplace_id: Optional[str] = None,
) -> Dict[str, Any]:
    headers: Dict[str, str] = {}
    if marketplace_id is not None:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id

    payload = {"compatibilityProperties": compatibility_properties}
    return client.request("POST", f"/buy/v1/item/{item_id}/check_compatibility", json=payload, headers=headers)
