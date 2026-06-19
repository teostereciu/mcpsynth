from typing import Any, Dict, Optional, List

from .http_client import request_json


def databases_create(*, parent: Dict[str, Any], title: List[Dict[str, Any]], properties: Dict[str, Any], icon: Optional[Dict[str, Any]] = None,
                    cover: Optional[Dict[str, Any]] = None, description: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
    """POST /databases"""
    body: Dict[str, Any] = {"parent": parent, "title": title, "properties": properties}
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    if description is not None:
        body["description"] = description
    return request_json("POST", "/databases", json_body=body)


def databases_retrieve(database_id: str) -> Dict[str, Any]:
    """GET /databases/{database_id}"""
    return request_json("GET", f"/databases/{database_id}")


def databases_update(database_id: str, *, title: Optional[List[Dict[str, Any]]] = None, properties: Optional[Dict[str, Any]] = None,
                    description: Optional[List[Dict[str, Any]]] = None, icon: Optional[Dict[str, Any]] = None,
                    cover: Optional[Dict[str, Any]] = None, archived: Optional[bool] = None, in_trash: Optional[bool] = None) -> Dict[str, Any]:
    """PATCH /databases/{database_id}"""
    body: Dict[str, Any] = {}
    if title is not None:
        body["title"] = title
    if properties is not None:
        body["properties"] = properties
    if description is not None:
        body["description"] = description
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    if archived is not None:
        body["archived"] = archived
    if in_trash is not None:
        body["in_trash"] = in_trash
    return request_json("PATCH", f"/databases/{database_id}", json_body=body)


def databases_list(*, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Dict[str, Any]:
    """GET /databases"""
    params: Dict[str, Any] = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return request_json("GET", "/databases", params=params or None)


def databases_query(database_id: str, *, query_filter: Optional[Dict[str, Any]] = None, sort_rules: Optional[list] = None,
                   start_cursor: Optional[str] = None, page_size: Optional[int] = None,
                   filter_properties: Optional[List[str]] = None) -> Dict[str, Any]:
    """POST /databases/{database_id}/query

    Note: filter_properties is a querystring param in Notion.
    """
    params: Dict[str, Any] = {}
    if filter_properties is not None:
        params["filter_properties"] = filter_properties

    body: Dict[str, Any] = {}
    if query_filter is not None:
        body["query_filter"] = query_filter
    if sort_rules is not None:
        body["sort_rules"] = sort_rules
    if start_cursor is not None:
        body["start_cursor"] = start_cursor
    if page_size is not None:
        body["page_size"] = page_size

    return request_json("POST", f"/databases/{database_id}/query", params=params or None, json_body=body)
