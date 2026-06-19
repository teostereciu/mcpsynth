from typing import Any, Dict, Optional

from ._client import request_json


def views_create(
    *,
    database_id: Optional[str] = None,
    data_source_id: Optional[str] = None,
    name: str,
    type: str,
    payload: Optional[Dict[str, Any]] = None,
) -> Any:
    body: Dict[str, Any] = {"name": name, "type": type}
    if database_id is not None:
        body["database_id"] = database_id
    if data_source_id is not None:
        body["data_source_id"] = data_source_id
    if payload:
        body.update(payload)
    return request_json("POST", "/views", json=body)


def views_retrieve(view_id: str) -> Any:
    return request_json("GET", f"/views/{view_id}")


def views_update(view_id: str, payload: Dict[str, Any]) -> Any:
    return request_json("PATCH", f"/views/{view_id}", json=payload)


def views_delete(view_id: str) -> Any:
    return request_json("DELETE", f"/views/{view_id}")


def views_list(*, database_id: Optional[str] = None, data_source_id: Optional[str] = None, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
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


def view_queries_create(view_id: str, *, payload: Optional[Dict[str, Any]] = None) -> Any:
    body = payload or {}
    return request_json("POST", f"/views/{view_id}/queries", json=body)


def view_queries_results(view_id: str, query_id: str) -> Any:
    return request_json("GET", f"/views/{view_id}/queries/{query_id}/results")


def view_queries_delete(view_id: str, query_id: str) -> Any:
    return request_json("DELETE", f"/views/{view_id}/queries/{query_id}")
