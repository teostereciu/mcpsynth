from typing import Any, Dict, Optional

from generated_tools.pages import _request


def create_data_source(parent: Dict[str, Any], title: list[Dict[str, Any]], properties: Dict[str, Any], icon: Optional[Dict[str, Any]] = None, cover: Optional[Dict[str, Any]] = None) -> Any:
    body: Dict[str, Any] = {"parent": parent, "title": title, "properties": properties}
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    return _request("POST", "/data_sources", json_body=body)


def retrieve_data_source(data_source_id: str) -> Any:
    return _request("GET", f"/data_sources/{data_source_id}")


def update_data_source(data_source_id: str, title: Optional[list[Dict[str, Any]]] = None, properties: Optional[Dict[str, Any]] = None, in_trash: Optional[bool] = None, parent: Optional[Dict[str, Any]] = None, icon: Optional[Dict[str, Any]] = None, cover: Optional[Dict[str, Any]] = None) -> Any:
    body: Dict[str, Any] = {}
    if title is not None:
        body["title"] = title
    if properties is not None:
        body["properties"] = properties
    if in_trash is not None:
        body["in_trash"] = in_trash
    if parent is not None:
        body["parent"] = parent
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    return _request("PATCH", f"/data_sources/{data_source_id}", json_body=body)


def query_data_source(data_source_id: str, query_filter: Optional[Dict[str, Any]] = None, sorts: Optional[list[Dict[str, Any]]] = None, start_cursor: Optional[str] = None, page_size: Optional[int] = None, filter_properties: Optional[list[str]] = None, result_type: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    if filter_properties:
        params["filter_properties"] = filter_properties
    body: Dict[str, Any] = {}
    if query_filter is not None:
        body["filter"] = query_filter
    if sorts is not None:
        body["sorts"] = sorts
    if start_cursor is not None:
        body["start_cursor"] = start_cursor
    if page_size is not None:
        body["page_size"] = page_size
    if result_type is not None:
        body["result_type"] = result_type
    return _request("POST", f"/data_sources/{data_source_id}/query", params=params or None, json_body=body or {})


def list_data_source_templates(data_source_id: str, name: Optional[str] = None, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {}
    if name is not None:
        params["name"] = name
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return _request("GET", f"/data_sources/{data_source_id}/templates", params=params or None)


def create_database(parent: Dict[str, Any], title: list[Dict[str, Any]], description: Optional[list[Dict[str, Any]]] = None, is_inline: Optional[bool] = None, initial_data_source: Optional[Dict[str, Any]] = None, icon: Optional[Dict[str, Any]] = None, cover: Optional[Dict[str, Any]] = None) -> Any:
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
    return _request("POST", "/databases", json_body=body)


def retrieve_database(database_id: str) -> Any:
    return _request("GET", f"/databases/{database_id}")


def update_database(database_id: str, parent: Optional[Dict[str, Any]] = None, title: Optional[list[Dict[str, Any]]] = None, description: Optional[list[Dict[str, Any]]] = None, is_inline: Optional[bool] = None, icon: Optional[Dict[str, Any]] = None, cover: Optional[Dict[str, Any]] = None, in_trash: Optional[bool] = None, is_locked: Optional[bool] = None) -> Any:
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
    return _request("PATCH", f"/databases/{database_id}", json_body=body)


def list_databases() -> Any:
    return _request("GET", "/databases")
