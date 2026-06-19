from typing import Any, Dict, List, Optional

from generated_tools.notion_client import client


def create_database(
    parent: Dict[str, Any],
    title: List[Dict[str, Any]],
    properties: Dict[str, Any],
    icon: Optional[Dict[str, Any]] = None,
    cover: Optional[Dict[str, Any]] = None,
    description: Optional[List[Dict[str, Any]]] = None,
    is_inline: Optional[bool] = None,
) -> Any:
    body: Dict[str, Any] = {
        "parent": parent,
        "title": title,
        "properties": properties,
    }
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    if description is not None:
        body["description"] = description
    if is_inline is not None:
        body["is_inline"] = is_inline
    return client.request("POST", "/databases", json_body=body)


def retrieve_database(database_id: str) -> Any:
    return client.request("GET", f"/databases/{database_id}")


def update_database(
    database_id: str,
    title: Optional[List[Dict[str, Any]]] = None,
    description: Optional[List[Dict[str, Any]]] = None,
    properties: Optional[Dict[str, Any]] = None,
    icon: Optional[Dict[str, Any]] = None,
    cover: Optional[Dict[str, Any]] = None,
    is_inline: Optional[bool] = None,
    archived: Optional[bool] = None,
    in_trash: Optional[bool] = None,
) -> Any:
    body: Dict[str, Any] = {}
    if title is not None:
        body["title"] = title
    if description is not None:
        body["description"] = description
    if properties is not None:
        body["properties"] = properties
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    if is_inline is not None:
        body["is_inline"] = is_inline
    if archived is not None:
        body["archived"] = archived
    if in_trash is not None:
        body["in_trash"] = in_trash
    return client.request("PATCH", f"/databases/{database_id}", json_body=body)


def query_database(
    database_id: str,
    filter: Optional[Dict[str, Any]] = None,
    sorts: Optional[List[Dict[str, Any]]] = None,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
    archived: Optional[bool] = None,
    in_trash: Optional[bool] = None,
) -> Any:
    body: Dict[str, Any] = {}
    if filter is not None:
        body["filter"] = filter
    if sorts is not None:
        body["sorts"] = sorts
    if start_cursor is not None:
        body["start_cursor"] = start_cursor
    if page_size is not None:
        body["page_size"] = page_size
    if archived is not None:
        body["archived"] = archived
    if in_trash is not None:
        body["in_trash"] = in_trash
    return client.request("POST", f"/databases/{database_id}/query", json_body=body)
