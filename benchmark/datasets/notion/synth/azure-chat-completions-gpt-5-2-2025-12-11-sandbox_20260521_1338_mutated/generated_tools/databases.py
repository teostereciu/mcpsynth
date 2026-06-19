from typing import Any, Dict, Optional

from .notion_client import request_json


def databases_create(parent: Dict[str, Any], title: Any, *, description: Optional[Any] = None,
                     is_inline: Optional[bool] = None, data_source: Optional[Dict[str, Any]] = None,
                     icon: Optional[Dict[str, Any]] = None, cover: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /v1/databases

    Doc: docs/create-a-database.md
    """
    body: Dict[str, Any] = {"parent": parent, "title": title}
    if description is not None:
        body["description"] = description
    if is_inline is not None:
        body["is_inline"] = is_inline
    if data_source is not None:
        body["data_source"] = data_source
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    return request_json("POST", "/databases", json=body)


def databases_retrieve(database_id: str) -> Dict[str, Any]:
    """GET /v1/databases/{database_id}

    Doc: docs/retrieve-a-database.md
    """
    return request_json("GET", f"/databases/{database_id}")


def databases_update(database_id: str, *, parent: Optional[Dict[str, Any]] = None, title: Optional[Any] = None,
                     description: Optional[Any] = None, is_inline: Optional[bool] = None,
                     icon: Optional[Dict[str, Any]] = None, cover: Optional[Dict[str, Any]] = None,
                     in_trash: Optional[bool] = None, is_locked: Optional[bool] = None) -> Dict[str, Any]:
    """PATCH /v1/databases/{database_id}

    Doc: docs/update-a-database.md
    """
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
    return request_json("PATCH", f"/databases/{database_id}", json=body)


def databases_query(database_id: str, *, query_filter: Optional[Dict[str, Any]] = None,
                    sorts: Optional[list[Dict[str, Any]]] = None,
                    start_cursor: Optional[str] = None, page_size: Optional[int] = None,
                    filter_properties: Optional[list[str]] = None) -> Dict[str, Any]:
    """POST /v1/databases/{database_id}/query

    Doc: docs/post-database-query.md (filter details: docs/post-database-query-filter.md)
    """
    params: Dict[str, Any] = {}
    if filter_properties:
        params["filter_properties"] = filter_properties
    body: Dict[str, Any] = {}
    if query_filter is not None:
        body["query_filter"] = query_filter
    if sorts is not None:
        body["sorts"] = sorts
    if start_cursor is not None:
        body["start_cursor"] = start_cursor
    if page_size is not None:
        body["page_size"] = page_size
    return request_json("POST", f"/databases/{database_id}/query", params=params, json=body)
