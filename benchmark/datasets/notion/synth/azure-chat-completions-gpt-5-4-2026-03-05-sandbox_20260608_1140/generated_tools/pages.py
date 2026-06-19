from typing import Any, Dict, List, Optional

from generated_tools.common import notion_request


def retrieve_page(page_id: str, filter_properties: Optional[List[str]] = None) -> Any:
    params = {}
    if filter_properties:
        params["filter_properties"] = filter_properties
    return notion_request("GET", f"/pages/{page_id}", params=params or None)


def create_page(parent: Dict[str, Any], properties: Dict[str, Any], children: Optional[List[Dict[str, Any]]] = None, content: Optional[str] = None, icon: Optional[Dict[str, Any]] = None, cover: Optional[Dict[str, Any]] = None, template: Optional[Dict[str, Any]] = None) -> Any:
    body: Dict[str, Any] = {"parent": parent, "properties": properties}
    if children is not None:
        body["children"] = children
    if content is not None:
        body["content"] = content
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    if template is not None:
        body["template"] = template
    return notion_request("POST", "/pages", json_body=body)


def update_page(page_id: str, properties: Optional[Dict[str, Any]] = None, icon: Optional[Dict[str, Any]] = None, cover: Optional[Dict[str, Any]] = None, in_trash: Optional[bool] = None, is_locked: Optional[bool] = None, template: Optional[Dict[str, Any]] = None, erase_content: Optional[bool] = None) -> Any:
    body: Dict[str, Any] = {}
    if properties is not None:
        body["properties"] = properties
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    if in_trash is not None:
        body["in_trash"] = in_trash
    if is_locked is not None:
        body["is_locked"] = is_locked
    if template is not None:
        body["template"] = template
    if erase_content is not None:
        body["erase_content"] = erase_content
    return notion_request("PATCH", f"/pages/{page_id}", json_body=body)


def retrieve_page_property(page_id: str, property_id: str, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    params = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return notion_request("GET", f"/pages/{page_id}/properties/{property_id}", params=params or None)


def move_page(page_id: str, parent: Dict[str, Any]) -> Any:
    return notion_request("POST", f"/pages/{page_id}/move", json_body={"parent": parent})
