from typing import Any, Dict, Optional

from .notion_client import NotionClient


def data_sources_query(
    data_source_id: str,
    *,
    filter: Optional[Dict[str, Any]] = None,
    sorts: Optional[Any] = None,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
    filter_properties: Optional[Any] = None,
    result_type: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/data_sources/{data_source_id}/query

    Doc: docs/query-a-data-source.md
    """
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

    client = NotionClient()
    return client.request(
        "POST",
        f"/data_sources/{data_source_id}/query",
        params=params or None,
        json_body=body or None,
    )


def data_sources_update(
    data_source_id: str,
    *,
    title: Optional[Any] = None,
    properties: Optional[Dict[str, Any]] = None,
    in_trash: Optional[bool] = None,
    parent: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
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

    client = NotionClient()
    return client.request("PATCH", f"/data_sources/{data_source_id}", json_body=body)


def data_sources_create(
    parent: Dict[str, Any],
    title: Any,
    properties: Dict[str, Any],
) -> Dict[str, Any]:
    """POST /v1/data_sources

    Doc: docs/create-a-data-source.md
    """
    body: Dict[str, Any] = {"parent": parent, "title": title, "properties": properties}
    client = NotionClient()
    return client.request("POST", "/data_sources", json_body=body)


def data_sources_list_templates(
    data_source_id: str,
    *,
    name: Optional[str] = None,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /v1/data_sources/{data_source_id}/templates

    Doc: docs/list-data-source-templates.md
    """
    params: Dict[str, Any] = {}
    if name is not None:
        params["name"] = name
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    client = NotionClient()
    return client.request("GET", f"/data_sources/{data_source_id}/templates", params=params or None)


def data_sources_retrieve(data_source_id: str) -> Dict[str, Any]:
    """GET /v1/data_sources/{data_source_id}

    Doc: docs/retrieve-a-data-source.md
    """
    client = NotionClient()
    return client.request("GET", f"/data_sources/{data_source_id}")
