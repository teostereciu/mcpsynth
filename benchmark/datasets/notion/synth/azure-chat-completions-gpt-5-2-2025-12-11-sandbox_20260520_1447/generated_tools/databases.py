from typing import Any, Dict, Optional

from .notion_client import NotionClient


def databases_create(
    parent: Dict[str, Any],
    title: Any,
    *,
    description: Optional[Any] = None,
    is_inline: Optional[bool] = None,
    data_sources: Optional[Any] = None,
    icon: Optional[Dict[str, Any]] = None,
    cover: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """POST /v1/databases

    Doc: docs/create-a-database.md
    """
    body: Dict[str, Any] = {"parent": parent, "title": title}
    if description is not None:
        body["description"] = description
    if is_inline is not None:
        body["is_inline"] = is_inline
    if data_sources is not None:
        body["data_sources"] = data_sources
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover

    client = NotionClient()
    return client.request("POST", "/databases", json_body=body)


def databases_update(
    database_id: str,
    *,
    parent: Optional[Dict[str, Any]] = None,
    title: Optional[Any] = None,
    description: Optional[Any] = None,
    is_inline: Optional[bool] = None,
    icon: Optional[Dict[str, Any]] = None,
    cover: Optional[Dict[str, Any]] = None,
    in_trash: Optional[bool] = None,
    locked: Optional[bool] = None,
) -> Dict[str, Any]:
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
    if locked is not None:
        body["locked"] = locked

    client = NotionClient()
    return client.request("PATCH", f"/databases/{database_id}", json_body=body)


def databases_query(
    database_id: str,
    *,
    filter: Optional[Dict[str, Any]] = None,
    sorts: Optional[Any] = None,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
    filter_properties: Optional[Any] = None,
) -> Dict[str, Any]:
    """POST /v1/databases/{database_id}/query

    Doc: docs/post-database-query.md
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

    client = NotionClient()
    return client.request(
        "POST",
        f"/databases/{database_id}/query",
        params=params or None,
        json_body=body or None,
    )


def databases_list(
    *,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /v1/databases

    Doc: docs/get-databases.md
    """
    params: Dict[str, Any] = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    client = NotionClient()
    return client.request("GET", "/databases", params=params or None)


def databases_retrieve(database_id: str) -> Dict[str, Any]:
    """GET /v1/databases/{database_id}

    Doc: docs/retrieve-a-database.md
    """
    client = NotionClient()
    return client.request("GET", f"/databases/{database_id}")
