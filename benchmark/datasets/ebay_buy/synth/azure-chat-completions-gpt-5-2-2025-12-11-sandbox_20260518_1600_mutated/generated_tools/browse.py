from typing import Any, Dict, List, Optional

from .client import EbayClient


# Note: Some Browse endpoints require additional OAuth scopes (e.g., buy.item.bulk).
# This server uses the base application scope by default; calls may fail if your app
# is not allowlisted or lacks the required scopes.


def search_items(
    client: EbayClient,
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
    auto_correct: Optional[bool] = None,
    marketplace_id: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
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
    if auto_correct is not None:
        params["auto_correct"] = str(auto_correct).lower()

    headers: Dict[str, str] = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request("GET", "/buy/browse/v1/item_summary/search", params=params, headers=headers)


def get_item(
    client: EbayClient,
    *,
    item_id: str,
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


def search_items_by_image(
    client: EbayClient,
    *,
    image_base64: str,
    category_ids: Optional[str] = None,
    filter: Optional[str] = None,
    sort: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    aspect_filter: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
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

    headers: Dict[str, str] = {"Content-Type": "application/json"}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    payload = {"image": image_base64}
    return client.request(
        "POST",
        "/buy/browse/v1/item_summary/search_by_image",
        params=params,
        json=payload,
        headers=headers,
    )


def get_items(
    client: EbayClient,
    *,
    item_ids: List[str],
    marketplace_id: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    """Bulk get item details (limited release; may require buy.item.bulk scope)."""

    params: Dict[str, Any] = {"item_ids": ",".join(item_ids)}

    headers: Dict[str, str] = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request("GET", "/buy/browse/v1/item/", params=params, headers=headers)


def get_item_by_legacy_id(
    client: EbayClient,
    *,
    legacy_item_id: str,
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


def get_items_by_item_group(
    client: EbayClient,
    *,
    item_group_id: str,
    fieldgroups: Optional[str] = None,
    marketplace_id: Optional[str] = None,
    enduserctx: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"item_group_id": item_group_id}
    if fieldgroups is not None:
        params["fieldgroups"] = fieldgroups

    headers: Dict[str, str] = {}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if enduserctx:
        headers["X-EBAY-C-ENDUSERCTX"] = enduserctx

    return client.request("GET", "/buy/browse/v1/item/get_items_by_item_group", params=params, headers=headers)


def check_compatibility(
    client: EbayClient,
    *,
    item_id: str,
    compatibility_properties: List[Dict[str, str]],
    marketplace_id: Optional[str] = None,
    accept_language: Optional[str] = None,
) -> Dict[str, Any]:
    headers: Dict[str, str] = {"Content-Type": "application/json"}
    if marketplace_id:
        headers["X-EBAY-C-MARKETPLACE-ID"] = marketplace_id
    if accept_language:
        headers["Accept-Language"] = accept_language

    payload = {"compatibilityProperties": compatibility_properties}
    return client.request(
        "POST",
        f"/buy/browse/v1/item/{item_id}/check_compatibility",
        json=payload,
        headers=headers,
    )
