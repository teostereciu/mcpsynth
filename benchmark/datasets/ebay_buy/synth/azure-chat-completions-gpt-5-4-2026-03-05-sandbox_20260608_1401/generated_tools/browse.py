from typing import Any, Dict, Optional

from generated_tools.common import client


def get_item(item_id: str, fieldgroups: Optional[str] = None, marketplace_id: Optional[str] = None) -> Dict[str, Any]:
    headers = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id} if marketplace_id else None
    return client.request("GET", f"/buy/browse/v1/item/{item_id}", params={"fieldgroups": fieldgroups}, headers=headers)


def search_items(
    q: Optional[str] = None,
    category_ids: Optional[str] = None,
    gtin: Optional[str] = None,
    epid: Optional[str] = None,
    charity_ids: Optional[str] = None,
    filter: Optional[str] = None,
    sort: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    fieldgroups: Optional[str] = None,
    aspect_filter: Optional[str] = None,
    compatibility_filter: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx
    return client.request(
        "GET",
        "/buy/browse/v1/item_summary/search",
        params={
            "q": q,
            "category_ids": category_ids,
            "gtin": gtin,
            "epid": epid,
            "charity_ids": charity_ids,
            "filter": filter,
            "sort": sort,
            "limit": limit,
            "offset": offset,
            "fieldgroups": fieldgroups,
            "aspect_filter": aspect_filter,
            "compatibility_filter": compatibility_filter,
        },
        headers=headers or None,
    )


def get_item_by_legacy_id(
    legacy_item_id: str,
    legacy_variation_id: Optional[str] = None,
    fieldgroups: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx
    return client.request(
        "GET",
        "/buy/browse/v1/item/get_item_by_legacy_id",
        params={
            "legacy_item_id": legacy_item_id,
            "legacy_variation_id": legacy_variation_id,
            "fieldgroups": fieldgroups,
        },
        headers=headers or None,
    )


def get_items(item_ids: str, marketplace_id: Optional[str] = None, enduserctx: Optional[str] = None) -> Dict[str, Any]:
    headers = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx
    return client.request("GET", "/buy/browse/v1/item", params={"item_ids": item_ids}, headers=headers or None)


def get_items_by_item_group(
    item_group_id: str,
    fieldgroups: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx
    return client.request(
        "GET",
        "/buy/browse/v1/item/get_items_by_item_group",
        params={"item_group_id": item_group_id, "fieldgroups": fieldgroups},
        headers=headers or None,
    )


def check_compatibility(
    item_id: str,
    compatibility_properties: list[dict[str, str]],
    marketplace_id: Optional[str] = None,
    accept_language: Optional[str] = None,
) -> Dict[str, Any]:
    headers = {"Content-Type": "application/json"}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if accept_language:
        headers["Accept-Language"] = accept_language
    return client.request(
        "POST",
        f"/buy/browse/v1/item/{item_id}/check_compatibility",
        json_body={"compatibilityProperties": compatibility_properties},
        headers=headers,
    )


def search_items_by_image(
    image: str,
    category_ids: Optional[str] = None,
    charity_ids: Optional[str] = None,
    filter: Optional[str] = None,
    aspect_filter: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    sort: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    headers = {"Content-Type": "application/json"}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx
    return client.request(
        "POST",
        "/buy/browse/v1/item_summary/search_by_image",
        params={
            "category_ids": category_ids,
            "charity_ids": charity_ids,
            "filter": filter,
            "aspect_filter": aspect_filter,
            "limit": limit,
            "offset": offset,
            "sort": sort,
        },
        json_body={"image": image},
        headers=headers,
    )
