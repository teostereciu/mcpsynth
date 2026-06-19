from __future__ import annotations

from typing import Any, Dict, Optional

from .client import EbayClient


_BULK_SCOPE = "https://api.ebay.com/oauth/api_scope/buy.item.bulk"


def browse_search(
    client: EbayClient,
    *,
    q: Optional[str] = None,
    category_ids: Optional[str] = None,
    epid: Optional[str] = None,
    gtin: Optional[str] = None,
    charity_ids: Optional[str] = None,
    filter: Optional[str] = None,
    aspect_filter: Optional[str] = None,
    compatibility_filter: Optional[str] = None,
    fieldgroups: Optional[str] = None,
    sort: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    marketplace_id: str = "EBAY_US",
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if q is not None:
        params["q"] = q
    if category_ids is not None:
        params["category_ids"] = category_ids
    if epid is not None:
        params["epid"] = epid
    if gtin is not None:
        params["gtin"] = gtin
    if charity_ids is not None:
        params["charity_ids"] = charity_ids
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

    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request("GET", "/buy/browse/v1/item_summary/search", params=params, headers=headers)


def get_item(
    client: EbayClient,
    *,
    item_id: str,
    fieldgroups: Optional[str] = None,
    marketplace_id: str = "EBAY_US",
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if fieldgroups is not None:
        params["fieldgroups"] = fieldgroups

    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request("GET", f"/buy/browse/v1/item/{item_id}", params=params, headers=headers)


def browse_search_by_image(
    client: EbayClient,
    *,
    image: str,
    category_ids: Optional[str] = None,
    filter: Optional[str] = None,
    aspect_filter: Optional[str] = None,
    fieldgroups: Optional[str] = None,
    sort: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    marketplace_id: str = "EBAY_US",
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if category_ids is not None:
        params["category_ids"] = category_ids
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

    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    payload = {"image": image}
    return client.request(
        "POST",
        "/buy/browse/v1/item_summary/search_by_image",
        params=params,
        json=payload,
        headers=headers,
    )


def get_item_by_legacy_id(
    client: EbayClient,
    *,
    legacy_item_id: str,
    legacy_variation_id: Optional[str] = None,
    fieldgroups: Optional[str] = None,
    marketplace_id: str = "EBAY_US",
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"legacy_item_id": legacy_item_id}
    if legacy_variation_id is not None:
        params["legacy_variation_id"] = legacy_variation_id
    if fieldgroups is not None:
        params["fieldgroups"] = fieldgroups

    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request("GET", "/buy/browse/v1/item/get_item_by_legacy_id", params=params, headers=headers)


def get_items_bulk(
    client: EbayClient,
    *,
    item_ids: Optional[str] = None,
    item_group_ids: Optional[str] = None,
    marketplace_id: str = "EBAY_US",
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    """Limited-release bulk item details.

    Provide either item_ids (comma-separated RESTful item IDs) or item_group_ids.
    """

    params: Dict[str, Any] = {}
    if item_ids is not None:
        params["item_ids"] = item_ids
    if item_group_ids is not None:
        params["item_group_ids"] = item_group_ids

    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request("GET", "/buy/browse/v1/item/", params=params, headers=headers, scope=_BULK_SCOPE)


def get_items_by_item_group(
    client: EbayClient,
    *,
    item_group_id: str,
    fieldgroups: Optional[str] = None,
    marketplace_id: str = "EBAY_US",
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"item_group_id": item_group_id}
    if fieldgroups is not None:
        params["fieldgroups"] = fieldgroups

    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id}
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request(
        "GET",
        "/buy/browse/v1/item/get_items_by_item_group",
        params=params,
        headers=headers,
    )


def check_compatibility(
    client: EbayClient,
    *,
    item_id: str,
    compatibility_properties: list[dict[str, str]],
    marketplace_id: str = "EBAY_US",
    accept_language: Optional[str] = None,
) -> Dict[str, Any]:
    headers = {
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
        "Content-Type": "application/json",
    }
    if accept_language:
        headers["Accept-Language"] = accept_language

    payload = {"compatibilityProperties": compatibility_properties}
    return client.request(
        "POST",
        f"/buy/browse/v1/item/{item_id}/check_compatibility",
        json=payload,
        headers=headers,
    )
