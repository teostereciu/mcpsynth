from typing import Any, Dict, Optional, List

from ._client import request_json


def data_sources_create(
    parent: Dict[str, Any],
    title: List[Dict[str, Any]],
    properties: Dict[str, Any],
    *,
    icon: Optional[Dict[str, Any]] = None,
    cover: Optional[Dict[str, Any]] = None,
    description: Optional[List[Dict[str, Any]]] = None,
) -> Any:
    body: Dict[str, Any] = {"parent": parent, "title": title, "properties": properties}
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    if description is not None:
        body["description"] = description
    return request_json("POST", "/data_sources", json=body)


def data_sources_retrieve(data_source_id: str) -> Any:
    return request_json("GET", f"/data_sources/{data_source_id}")


def data_sources_update(
    data_source_id: str,
    *,
    title: Optional[List[Dict[str, Any]]] = None,
    description: Optional[List[Dict[str, Any]]] = None,
    properties: Optional[Dict[str, Any]] = None,
    icon: Optional[Dict[str, Any]] = None,
    cover: Optional[Dict[str, Any]] = None,
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
    return request_json("PATCH", f"/data_sources/{data_source_id}", json=body)


def data_sources_list_templates(data_source_id: str) -> Any:
    return request_json("GET", f"/data_sources/{data_source_id}/templates")


def data_sources_query(
    data_source_id: str,
    *,
    filter: Optional[Dict[str, Any]] = None,
    sorts: Optional[list] = None,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
    filter_properties: Optional[list] = None,
    result_type: Optional[str] = None,
) -> Any:
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
    if result_type is not None:
        body["result_type"] = result_type

    return request_json("POST", f"/data_sources/{data_source_id}/query", params=params or None, json=body or {})
