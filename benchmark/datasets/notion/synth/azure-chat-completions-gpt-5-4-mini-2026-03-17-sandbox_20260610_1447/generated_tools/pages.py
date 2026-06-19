from typing import Any, Dict
from .notion_client import NotionClient

client = NotionClient()


def create_page(parent: Dict[str, Any], properties: Dict[str, Any], children: Any = None, icon: Any = None, cover: Any = None, is_locked: Any = None) -> Dict[str, Any]:
    body: Dict[str, Any] = {"parent": parent, "properties": properties}
    if children is not None:
        body["children"] = children
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    if is_locked is not None:
        body["is_locked"] = is_locked
    return client.request("POST", "/pages", json=body)


def retrieve_page(page_id: str, filter_properties: Any = None) -> Dict[str, Any]:
    params = {}
    if filter_properties is not None:
        params["filter_properties"] = filter_properties
    return client.request("GET", f"/pages/{page_id}", params=params or None)


def update_page(page_id: str, properties: Dict[str, Any] = None, archived: Any = None, in_trash: Any = None, is_locked: Any = None, icon: Any = None, cover: Any = None, erase_content: Any = None, children: Any = None) -> Dict[str, Any]:
    body: Dict[str, Any] = {}
    if properties is not None:
        body["properties"] = properties
    if archived is not None:
        body["archived"] = archived
    if in_trash is not None:
        body["in_trash"] = in_trash
    if is_locked is not None:
        body["is_locked"] = is_locked
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    if erase_content is not None:
        body["erase_content"] = erase_content
    if children is not None:
        body["children"] = children
    return client.request("PATCH", f"/pages/{page_id}", json=body)


def archive_page(page_id: str) -> Dict[str, Any]:
    return update_page(page_id, archived=True)


def trash_page(page_id: str) -> Dict[str, Any]:
    return update_page(page_id, in_trash=True)
