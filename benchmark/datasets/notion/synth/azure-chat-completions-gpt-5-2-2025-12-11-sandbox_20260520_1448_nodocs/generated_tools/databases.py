from typing import Any, Dict, Optional

from notion_client import NotionClient


def databases_create(parent: Dict[str, Any], title: list, properties: Dict[str, Any], *, icon: Optional[Dict[str, Any]] = None, cover: Optional[Dict[str, Any]] = None, description: Optional[list] = None, is_inline: Optional[bool] = None) -> Any:
    """POST /databases"""
    client = NotionClient()
    body: Dict[str, Any] = {"parent": parent, "title": title, "properties": properties}
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    if description is not None:
        body["description"] = description
    if is_inline is not None:
        body["is_inline"] = is_inline
    return client.request("POST", "/databases", json=body)


def databases_retrieve(database_id: str) -> Any:
    """GET /databases/{database_id}"""
    client = NotionClient()
    return client.request("GET", f"/databases/{database_id}")


def databases_update(database_id: str, *, title: Optional[list] = None, description: Optional[list] = None, properties: Optional[Dict[str, Any]] = None, archived: Optional[bool] = None, icon: Optional[Dict[str, Any]] = None, cover: Optional[Dict[str, Any]] = None) -> Any:
    """PATCH /databases/{database_id}"""
    client = NotionClient()
    body: Dict[str, Any] = {}
    if title is not None:
        body["title"] = title
    if description is not None:
        body["description"] = description
    if properties is not None:
        body["properties"] = properties
    if archived is not None:
        body["archived"] = archived
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    return client.request("PATCH", f"/databases/{database_id}", json=body)


def databases_query(database_id: str, *, filter: Optional[Dict[str, Any]] = None, sorts: Optional[list] = None, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    """POST /databases/{database_id}/query"""
    client = NotionClient()
    body: Dict[str, Any] = {}
    if filter is not None:
        body["filter"] = filter
    if sorts is not None:
        body["sorts"] = sorts
    if start_cursor is not None:
        body["start_cursor"] = start_cursor
    if page_size is not None:
        body["page_size"] = page_size
    return client.request("POST", f"/databases/{database_id}/query", json=body)
