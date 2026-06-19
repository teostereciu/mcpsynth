from typing import Any, Dict, Optional

from ._client import request_json


def pages_create(
    parent: Dict[str, Any],
    properties: Dict[str, Any],
    *,
    children: Optional[list] = None,
    content: Optional[str] = None,
    icon: Optional[Dict[str, Any]] = None,
    cover: Optional[Dict[str, Any]] = None,
    template: Optional[Dict[str, Any]] = None,
) -> Any:
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
    return request_json("POST", "/pages", json=body)


def pages_retrieve(page_id: str) -> Any:
    return request_json("GET", f"/pages/{page_id}")


def pages_update(
    page_id: str,
    *,
    properties: Optional[Dict[str, Any]] = None,
    icon: Optional[Dict[str, Any]] = None,
    cover: Optional[Dict[str, Any]] = None,
    in_trash: Optional[bool] = None,
    archived: Optional[bool] = None,
) -> Any:
    body: Dict[str, Any] = {}
    if properties is not None:
        body["properties"] = properties
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    if in_trash is not None:
        body["in_trash"] = in_trash
    if archived is not None:
        body["archived"] = archived
    return request_json("PATCH", f"/pages/{page_id}", json=body)


def pages_trash(page_id: str) -> Any:
    return pages_update(page_id, in_trash=True)


def pages_restore(page_id: str) -> Any:
    return pages_update(page_id, in_trash=False)


def pages_move(page_id: str, parent: Dict[str, Any]) -> Any:
    return request_json("POST", f"/pages/{page_id}/move", json={"parent": parent})


def pages_properties_retrieve(page_id: str, property_id: str, *, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return request_json("GET", f"/pages/{page_id}/properties/{property_id}", params=params or None)


def pages_retrieve_markdown(page_id: str) -> Any:
    return request_json("GET", f"/pages/{page_id}/markdown")


def pages_update_markdown(page_id: str, payload: Dict[str, Any]) -> Any:
    # payload should match Notion's updateMarkdown body (type + update_content/append_content/etc.)
    return request_json("PATCH", f"/pages/{page_id}/markdown", json=payload)
