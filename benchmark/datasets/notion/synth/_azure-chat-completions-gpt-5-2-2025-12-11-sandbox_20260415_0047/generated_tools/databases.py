"""Tools for Notion Databases API."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .http import notion_request


def create_database(
    *,
    parent: Dict[str, Any],
    title: List[Dict[str, Any]],
    properties: Dict[str, Any],
    description: Optional[List[Dict[str, Any]]] = None,
    is_inline: Optional[bool] = None,
    icon: Optional[Dict[str, Any]] = None,
    cover: Optional[Dict[str, Any]] = None,
    notion_version: str | None = None,
) -> Dict[str, Any]:
    """POST /v1/databases"""
    body: Dict[str, Any] = {"parent": parent, "title": title, "properties": properties}
    if description is not None:
        body["description"] = description
    if is_inline is not None:
        body["is_inline"] = is_inline
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    return notion_request("POST", "/databases", json=body, notion_version=notion_version)


def retrieve_database(*, database_id: str, notion_version: str | None = None) -> Dict[str, Any]:
    """GET /v1/databases/{database_id}"""
    return notion_request("GET", f"/databases/{database_id}", notion_version=notion_version)


def update_database(
    *,
    database_id: str,
    title: Optional[List[Dict[str, Any]]] = None,
    description: Optional[List[Dict[str, Any]]] = None,
    properties: Optional[Dict[str, Any]] = None,
    icon: Optional[Dict[str, Any]] = None,
    cover: Optional[Dict[str, Any]] = None,
    is_inline: Optional[bool] = None,
    notion_version: str | None = None,
) -> Dict[str, Any]:
    """PATCH /v1/databases/{database_id}"""
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
    if is_inline is not None:
        body["is_inline"] = is_inline
    return notion_request("PATCH", f"/databases/{database_id}", json=body, notion_version=notion_version)


def query_database(
    *,
    database_id: str,
    filter: Optional[Dict[str, Any]] = None,
    sorts: Optional[List[Dict[str, Any]]] = None,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
    filter_properties: Optional[List[str]] = None,
    notion_version: str | None = None,
) -> Dict[str, Any]:
    """POST /v1/databases/{database_id}/query"""
    body: Dict[str, Any] = {}
    if filter is not None:
        body["filter"] = filter
    if sorts is not None:
        body["sorts"] = sorts
    if start_cursor is not None:
        body["start_cursor"] = start_cursor
    if page_size is not None:
        body["page_size"] = page_size
    if filter_properties is not None:
        body["filter_properties"] = filter_properties
    return notion_request(
        "POST",
        f"/databases/{database_id}/query",
        json=body,
        notion_version=notion_version,
    )


def list_databases(
    *,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
    notion_version: str | None = None,
) -> Dict[str, Any]:
    """GET /v1/databases"""
    params: Dict[str, Any] = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return notion_request("GET", "/databases", params=params or None, notion_version=notion_version)
