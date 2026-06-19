from typing import Any, Dict, Optional

from .client import EbayClient


def get_item(
    item_id: str,
    fieldgroups: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /buy/v1/item/{item_id}"""
    client = EbayClient()
    params: Dict[str, Any] = {}
    if fieldgroups is not None:
        params["fieldgroups"] = fieldgroups

    headers: Dict[str, str] = {}
    if marketplace_id is not None:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if enduserctx is not None:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request("GET", f"/buy/v1/item/{item_id}", params=params, headers=headers)


def get_item_by_legacy_id(
    legacy_item_id: str,
    legacy_variation_id: Optional[str] = None,
    fieldgroups: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /buy/v1/item/get_item_by_legacy_id"""
    client = EbayClient()
    params: Dict[str, Any] = {"legacy_item_id": legacy_item_id}
    if legacy_variation_id is not None:
        params["legacy_variation_id"] = legacy_variation_id
    if fieldgroups is not None:
        params["fieldgroups"] = fieldgroups

    headers: Dict[str, str] = {}
    if marketplace_id is not None:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if enduserctx is not None:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request("GET", "/buy/v1/item/get_item_by_legacy_id", params=params, headers=headers)


def get_items(
    item_ids: Optional[str] = None,
    item_group_ids: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /buy/v1/item/ (bulk getItems)"""
    client = EbayClient()
    params: Dict[str, Any] = {}
    if item_ids is not None:
        params["item_ids"] = item_ids
    if item_group_ids is not None:
        params["item_group_ids"] = item_group_ids

    headers: Dict[str, str] = {}
    if marketplace_id is not None:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if enduserctx is not None:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    # Endpoint path in docs is not explicit; Buy Browse bulk get is /buy/v1/item/
    return client.request("GET", "/buy/v1/item/", params=params, headers=headers)


def get_items_by_item_group(
    item_group_id: str,
    fieldgroups: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /buy/v1/item/get_items_by_item_group"""
    client = EbayClient()
    params: Dict[str, Any] = {"item_group_id": item_group_id}
    if fieldgroups is not None:
        params["fieldgroups"] = fieldgroups

    headers: Dict[str, str] = {}
    if marketplace_id is not None:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if enduserctx is not None:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request("GET", "/buy/v1/item/get_items_by_item_group", params=params, headers=headers)


def check_compatibility(
    item_id: str,
    compatibility_properties: list[dict],
    marketplace_id: Optional[str] = None,
    accept_language: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /buy/browse/v1/item/{item_id}/check_compatibility"""
    client = EbayClient()
    headers: Dict[str, str] = {"Content-Type": "application/json"}
    if marketplace_id is not None:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if accept_language is not None:
        headers["Accept-Language"] = accept_language

    body = {"compatibilityProperties": compatibility_properties}
    return client.request("POST", f"/buy/browse/v1/item/{item_id}/check_compatibility", headers=headers, json=body)


def search_items_by_image(
    image: str,
    category_ids: Optional[str] = None,
    filter: Optional[str] = None,
    aspect_filter: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    sort: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /buy/v1/item_summary/search_by_image"""
    client = EbayClient()
    params: Dict[str, Any] = {}
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
    if sort is not None:
        params["sort"] = sort

    headers: Dict[str, str] = {"Content-Type": "application/json"}
    if marketplace_id is not None:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if enduserctx is not None:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    body = {"image": image}
    return client.request("POST", "/buy/v1/item_summary/search_by_image", params=params, headers=headers, json=body)


def search_items(
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
    auto_correct: Optional[bool] = None,
    marketplace_id: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /buy/v1/item_summary/search"""
    client = EbayClient()
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
    if fieldgroups is not None:
        params["fieldgroups"] = fieldgroups
    if aspect_filter is not None:
        params["aspect_filter"] = aspect_filter
    if compatibility_filter is not None:
        params["compatibility_filter"] = compatibility_filter
    if charity_ids is not None:
        params["charity_ids"] = charity_ids
    if auto_correct is not None:
        params["auto_correct"] = str(auto_correct).lower()

    headers: Dict[str, str] = {}
    if marketplace_id is not None:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if enduserctx is not None:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request("GET", "/buy/v1/item_summary/search", params=params, headers=headers)
