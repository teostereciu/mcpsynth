from typing import Any, Dict, List, Optional

from generated_tools.auth import client


def search_items(
    q: Optional[str] = None,
    category_ids: Optional[List[str]] = None,
    limit: int = 10,
    offset: int = 0,
    sort: Optional[str] = None,
    filter: Optional[str] = None,
    fieldgroups: Optional[List[str]] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit, "offset": offset}
    if q:
        params["q"] = q
    if category_ids:
        params["category_ids"] = ",".join(category_ids)
    if sort:
        params["sort"] = sort
    if filter:
        params["filter"] = filter
    if fieldgroups:
        params["fieldgroups"] = ",".join(fieldgroups)
    return client.request("GET", "/buy/browse/v1/item_summary/search", params=params)


def get_item(item_id: str, fieldgroups: Optional[List[str]] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if fieldgroups:
        params["fieldgroups"] = ",".join(fieldgroups)
    return client.request("GET", f"/buy/browse/v1/item/{item_id}", params=params)


def get_items(item_ids: List[str]) -> Dict[str, Any]:
    return client.request("GET", "/buy/browse/v1/item/get_items", params={"item_ids": ",".join(item_ids)})


def get_item_by_legacy_id(legacy_item_id: str) -> Dict[str, Any]:
    return client.request("GET", "/buy/browse/v1/item/get_item_by_legacy_id", params={"legacy_item_id": legacy_item_id})


def get_items_by_item_group(item_group_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/buy/browse/v1/item/get_items_by_item_group", params={"item_group_id": item_group_id})


def get_item_by_legacy_id_and_variations(legacy_item_id: str) -> Dict[str, Any]:
    return client.request(
        "GET",
        "/buy/browse/v1/item/get_item_by_legacy_id",
        params={"legacy_item_id": legacy_item_id, "fieldgroups": "PRODUCT"},
    )


def search_by_image(image_url: str, limit: int = 10, offset: int = 0, category_ids: Optional[List[str]] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"image_url": image_url, "limit": limit, "offset": offset}
    if category_ids:
        params["category_ids"] = ",".join(category_ids)
    return client.request("GET", "/buy/browse/v1/item_summary/search_by_image", params=params)


def search_by_image_with_file(limit: int = 10, offset: int = 0) -> Dict[str, Any]:
    return {"error": "Image file upload variant is not implemented; use search_by_image with a public image URL."}
