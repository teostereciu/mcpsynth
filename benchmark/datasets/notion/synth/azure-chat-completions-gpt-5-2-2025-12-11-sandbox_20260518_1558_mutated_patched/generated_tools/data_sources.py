from typing import Any, Dict, List, Optional

from .http_client import request_json


def data_sources_create(*, parent: Dict[str, Any], title: List[Dict[str, Any]], properties: Dict[str, Any]) -> Dict[str, Any]:
    """POST /data_sources"""
    body: Dict[str, Any] = {"parent": parent, "title": title, "properties": properties}
    return request_json("POST", "/data_sources", json_body=body)


def data_sources_retrieve(data_source_id: str) -> Dict[str, Any]:
    """GET /data_sources/{data_source_id}"""
    return request_json("GET", f"/data_sources/{data_source_id}")


def data_sources_update(data_source_id: str, *, title: Optional[List[Dict[str, Any]]] = None, properties: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """PATCH /data_sources/{data_source_id}"""
    body: Dict[str, Any] = {}
    if title is not None:
        body["title"] = title
    if properties is not None:
        body["properties"] = properties
    return request_json("PATCH", f"/data_sources/{data_source_id}", json_body=body)


def data_sources_list_templates(data_source_id: str, *, name: Optional[str] = None,
                              start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Dict[str, Any]:
    """GET /data_sources/{data_source_id}/templates"""
    params: Dict[str, Any] = {}
    if name is not None:
        params["name"] = name
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return request_json("GET", f"/data_sources/{data_source_id}/templates", params=params or None)


def data_sources_query(data_source_id: str, *, query_filter: Optional[Dict[str, Any]] = None, sort_rules: Optional[list] = None,
                      start_cursor: Optional[str] = None, page_size: Optional[int] = None,
                      filter_properties: Optional[List[str]] = None) -> Dict[str, Any]:
    """POST /data_sources/{data_source_id}/query"""
    params: Dict[str, Any] = {}
    if filter_properties is not None:
        params["filter_properties"] = filter_properties

    body: Dict[str, Any] = {}
    if query_filter is not None:
        body["filter"] = query_filter
    if sort_rules is not None:
        body["sorts"] = sort_rules
    if start_cursor is not None:
        body["start_cursor"] = start_cursor
    if page_size is not None:
        body["page_size"] = page_size

    return request_json("POST", f"/data_sources/{data_source_id}/query", params=params or None, json_body=body)
