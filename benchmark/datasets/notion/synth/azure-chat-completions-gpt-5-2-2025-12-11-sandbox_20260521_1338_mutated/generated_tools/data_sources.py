from typing import Any, Dict, Optional

from .notion_client import request_json


def data_sources_create(parent: Dict[str, Any], title: Any, properties: Dict[str, Any]) -> Dict[str, Any]:
    """POST /v1/data_sources

    Doc: docs/create-a-data-source.md
    """
    body = {"parent": parent, "title": title, "properties": properties}
    return request_json("POST", "/data_sources", json=body)


def data_sources_retrieve(data_source_id: str) -> Dict[str, Any]:
    """GET /v1/data_sources/{data_source_id}

    Doc: docs/retrieve-a-data-source.md
    """
    return request_json("GET", f"/data_sources/{data_source_id}")


def data_sources_update(data_source_id: str, *, title: Optional[Any] = None, properties: Optional[Dict[str, Any]] = None,
                        in_trash: Optional[bool] = None, parent: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """PATCH /v1/data_sources/{data_source_id}

    Doc: docs/update-a-data-source.md
    """
    body: Dict[str, Any] = {}
    if title is not None:
        body["title"] = title
    if properties is not None:
        body["properties"] = properties
    if in_trash is not None:
        body["in_trash"] = in_trash
    if parent is not None:
        body["parent"] = parent
    return request_json("PATCH", f"/data_sources/{data_source_id}", json=body)


def data_sources_query(data_source_id: str, *, query_filter: Optional[Dict[str, Any]] = None,
                      sort_rules: Optional[list[Dict[str, Any]]] = None,
                      page_cursor: Optional[str] = None, results_per_page: Optional[int] = None,
                      filter_properties: Optional[list[str]] = None,
                      result_type_filter: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /v1/data_sources/{data_source_id}/query

    Doc: docs/query-a-data-source.md
    """
    params: Dict[str, Any] = {}
    if filter_properties:
        params["filter_properties[]"] = filter_properties
    body: Dict[str, Any] = {}
    if query_filter is not None:
        body["query_filter"] = query_filter
    if sort_rules is not None:
        body["sort_rules"] = sort_rules
    if page_cursor is not None:
        body["page_cursor"] = page_cursor
    if results_per_page is not None:
        body["results_per_page"] = results_per_page
    if result_type_filter is not None:
        body["result_type_filter"] = result_type_filter
    return request_json("POST", f"/data_sources/{data_source_id}/query", params=params, json=body)
