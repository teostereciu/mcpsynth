from typing import Any, Dict, List, Optional

from ._client import request_json


def databases_create(parent: Dict[str, Any], title: List[Dict[str, Any]], properties: Dict[str, Any], *, icon: Optional[Dict[str, Any]] = None, cover: Optional[Dict[str, Any]] = None, description: Optional[List[Dict[str, Any]]] = None, is_inline: Optional[bool] = None) -> Any:
    """POST /v1/databases"""
    body: Dict[str, Any] = {"parent": parent, "title": title, "properties": properties}
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    if description is not None:
        body["description"] = description
    if is_inline is not None:
        body["is_inline"] = is_inline
    return request_json("POST", "/databases", json_body=body)


def databases_retrieve(database_id: str) -> Any:
    """GET /v1/databases/{database_id}"""
    return request_json("GET", f"/databases/{database_id}")


def databases_update(database_id: str, *, title: Optional[List[Dict[str, Any]]] = None, description: Optional[List[Dict[str, Any]]] = None, properties: Optional[Dict[str, Any]] = None, icon: Optional[Dict[str, Any]] = None, cover: Optional[Dict[str, Any]] = None, archived: Optional[bool] = None) -> Any:
    """PATCH /v1/databases/{database_id}"""
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
    if archived is not None:
        body["archived"] = archived
    return request_json("PATCH", f"/databases/{database_id}", json_body=body)


def databases_list(*, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    """GET /v1/databases"""
    params: Dict[str, Any] = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return request_json("GET", "/databases", params=params)


def databases_query(database_id: str, *, filter: Optional[Dict[str, Any]] = None, sorts: Optional[List[Dict[str, Any]]] = None, start_cursor: Optional[str] = None, page_size: Optional[int] = None, filter_properties: Optional[List[str]] = None) -> Any:
    """POST /v1/databases/{database_id}/query"""
    params: Dict[str, Any] = {}
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

    return request_json("POST", f"/databases/{database_id}/query", params=params, json_body=body)
