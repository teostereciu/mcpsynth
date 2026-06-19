from typing import Any, Dict, List, Optional

from .notion_client import NotionClient, omit_none


def databases_retrieve(*, database_id: str) -> Dict[str, Any]:
    """GET /databases/{database_id}

    Source: docs/retrieve-a-database.md
    """
    return NotionClient().request("GET", f"/databases/{database_id}")


def databases_query(
    *,
    database_id: str,
    filter: Optional[Dict[str, Any]] = None,
    sorts: Optional[List[Dict[str, Any]]] = None,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
    filter_properties: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """POST /databases/{database_id}/query

    Source: docs/post-database-query.md
    """
    params: Dict[str, Any] = {}
    if filter_properties:
        params["filter_properties"] = filter_properties

    body = omit_none(
        {
            "filter": filter,
            "sorts": sorts,
            "start_cursor": start_cursor,
            "page_size": page_size,
        }
    )
    return NotionClient().request(
        "POST", f"/databases/{database_id}/query", params=params or None, json=body or {}
    )


def databases_create(
    *,
    parent: Dict[str, Any],
    title: List[Dict[str, Any]],
    description: Optional[List[Dict[str, Any]]] = None,
    is_inline: Optional[bool] = None,
    data_sources: Optional[List[Dict[str, Any]]] = None,
    icon: Optional[Dict[str, Any]] = None,
    cover: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """POST /databases

    Source: docs/create-a-database.md
    """
    body = omit_none(
        {
            "parent": parent,
            "title": title,
            "description": description,
            "is_inline": is_inline,
            "data_sources": data_sources,
            "icon": icon,
            "cover": cover,
        }
    )
    return NotionClient().request("POST", "/databases", json=body)


def databases_update(
    *,
    database_id: str,
    parent: Optional[Dict[str, Any]] = None,
    title: Optional[List[Dict[str, Any]]] = None,
    description: Optional[List[Dict[str, Any]]] = None,
    is_inline: Optional[bool] = None,
    icon: Optional[Dict[str, Any]] = None,
    cover: Optional[Dict[str, Any]] = None,
    in_trash: Optional[bool] = None,
    locked: Optional[bool] = None,
    properties: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """PATCH /databases/{database_id}

    Source: docs/update-a-database.md
    """
    body = omit_none(
        {
            "parent": parent,
            "title": title,
            "description": description,
            "is_inline": is_inline,
            "icon": icon,
            "cover": cover,
            "in_trash": in_trash,
            "locked": locked,
            "properties": properties,
        }
    )
    return NotionClient().request("PATCH", f"/databases/{database_id}", json=body)
