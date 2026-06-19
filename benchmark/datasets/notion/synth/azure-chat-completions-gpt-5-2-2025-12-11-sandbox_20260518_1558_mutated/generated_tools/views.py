from typing import Any, Dict, Optional

from .http_client import request_json


def views_create(*, database_id: str, data_source_id: Optional[str] = None, name: str, type: str) -> Dict[str, Any]:
    """POST /views"""
    body: Dict[str, Any] = {"database_id": database_id, "name": name, "type": type}
    if data_source_id is not None:
        body["data_source_id"] = data_source_id
    return request_json("POST", "/views", json_body=body)


def views_retrieve(view_id: str) -> Dict[str, Any]:
    """GET /views/{view_id}"""
    return request_json("GET", f"/views/{view_id}")


def views_update(view_id: str, *, name: Optional[str] = None) -> Dict[str, Any]:
    """PATCH /views/{view_id}"""
    body: Dict[str, Any] = {}
    if name is not None:
        body["name"] = name
    return request_json("PATCH", f"/views/{view_id}", json_body=body)


def views_delete(view_id: str) -> Dict[str, Any]:
    """DELETE /views/{view_id}"""
    return request_json("DELETE", f"/views/{view_id}")


def views_list(*, database_id: Optional[str] = None, data_source_id: Optional[str] = None,
              start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Dict[str, Any]:
    """GET /views

    At least one of database_id or data_source_id is required by the API.
    """
    params: Dict[str, Any] = {}
    if database_id is not None:
        params["database_id"] = database_id
    if data_source_id is not None:
        params["data_source_id"] = data_source_id
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return request_json("GET", "/views", params=params or None)


def view_queries_create(view_id: str, *, query: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /views/{view_id}/query"""
    body: Dict[str, Any] = {}
    if query is not None:
        body.update(query)
    return request_json("POST", f"/views/{view_id}/query", json_body=body)


def view_queries_delete(view_id: str, query_id: str) -> Dict[str, Any]:
    """DELETE /views/{view_id}/query/{query_id}"""
    return request_json("DELETE", f"/views/{view_id}/query/{query_id}")


def view_queries_results(view_id: str, query_id: str, *, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Dict[str, Any]:
    """GET /views/{view_id}/query/{query_id}/results"""
    params: Dict[str, Any] = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return request_json("GET", f"/views/{view_id}/query/{query_id}/results", params=params or None)
