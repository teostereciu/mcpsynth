from typing import Any, Dict, List, Optional

from generated_tools.common import notion_request


def create_database(parent: Dict[str, Any], title: List[Dict[str, Any]], description: Optional[List[Dict[str, Any]]] = None, is_inline: Optional[bool] = None, initial_data_source: Optional[Dict[str, Any]] = None, icon: Optional[Dict[str, Any]] = None, cover: Optional[Dict[str, Any]] = None) -> Any:
    body: Dict[str, Any] = {"parent": parent, "title": title}
    if description is not None:
        body["description"] = description
    if is_inline is not None:
        body["is_inline"] = is_inline
    if initial_data_source is not None:
        body["initial_data_source"] = initial_data_source
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    return notion_request("POST", "/databases", json_body=body)


def retrieve_database(database_id: str) -> Any:
    return notion_request("GET", f"/databases/{database_id}")


def update_database(database_id: str, parent: Optional[Dict[str, Any]] = None, title: Optional[List[Dict[str, Any]]] = None, description: Optional[List[Dict[str, Any]]] = None, is_inline: Optional[bool] = None, icon: Optional[Dict[str, Any]] = None, cover: Optional[Dict[str, Any]] = None, in_trash: Optional[bool] = None, is_locked: Optional[bool] = None) -> Any:
    body: Dict[str, Any] = {}
    if parent is not None:
        body["parent"] = parent
    if title is not None:
        body["title"] = title
    if description is not None:
        body["description"] = description
    if is_inline is not None:
        body["is_inline"] = is_inline
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    if in_trash is not None:
        body["in_trash"] = in_trash
    if is_locked is not None:
        body["is_locked"] = is_locked
    return notion_request("PATCH", f"/databases/{database_id}", json_body=body)


def query_data_source(data_source_id: str, filter: Optional[Dict[str, Any]] = None, sorts: Optional[List[Dict[str, Any]]] = None, start_cursor: Optional[str] = None, page_size: Optional[int] = None, result_type: Optional[str] = None, filter_properties: Optional[List[str]] = None) -> Any:
    params = {}
    if result_type is not None:
        params["result_type"] = result_type
    if filter_properties is not None:
        params["filter_properties"] = filter_properties
    body: Dict[str, Any] = {}
    if filter is not None:
        body["filter"] = filter
    if sorts is not None:
        body["sorts"] = sorts
    if start_cursor is not None:
        body["start_cursor"] = start_cursor
    if page_size is not None:
        body["page_size"] = page_size
    return notion_request("POST", f"/data_sources/{data_source_id}/query", params=params or None, json_body=body or {})
