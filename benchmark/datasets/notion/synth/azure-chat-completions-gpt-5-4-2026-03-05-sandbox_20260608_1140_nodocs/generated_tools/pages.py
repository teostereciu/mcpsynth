from typing import Any, Dict, List, Optional

from generated_tools.notion_client import client


def create_page(
    parent: Dict[str, Any],
    properties: Dict[str, Any],
    children: Optional[List[Dict[str, Any]]] = None,
    icon: Optional[Dict[str, Any]] = None,
    cover: Optional[Dict[str, Any]] = None,
) -> Any:
    body: Dict[str, Any] = {"parent": parent, "properties": properties}
    if children is not None:
        body["children"] = children
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    return client.request("POST", "/pages", json_body=body)


def retrieve_page(page_id: str) -> Any:
    return client.request("GET", f"/pages/{page_id}")


def update_page(
    page_id: str,
    properties: Optional[Dict[str, Any]] = None,
    archived: Optional[bool] = None,
    in_trash: Optional[bool] = None,
    icon: Optional[Dict[str, Any]] = None,
    cover: Optional[Dict[str, Any]] = None,
    is_locked: Optional[bool] = None,
) -> Any:
    body: Dict[str, Any] = {}
    if properties is not None:
        body["properties"] = properties
    if archived is not None:
        body["archived"] = archived
    if in_trash is not None:
        body["in_trash"] = in_trash
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    if is_locked is not None:
        body["is_locked"] = is_locked
    return client.request("PATCH", f"/pages/{page_id}", json_body=body)


def retrieve_page_property_item(page_id: str, property_id: str, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return client.request("GET", f"/pages/{page_id}/properties/{property_id}", params=params or None)


def archive_page(page_id: str) -> Any:
    return update_page(page_id=page_id, archived=True)


def restore_page(page_id: str) -> Any:
    return update_page(page_id=page_id, archived=False)
