"""Tools for Notion Pages API."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .http import notion_request


def create_page(
    *,
    parent: Dict[str, Any],
    properties: Dict[str, Any],
    children: Optional[List[Dict[str, Any]]] = None,
    icon: Optional[Dict[str, Any]] = None,
    cover: Optional[Dict[str, Any]] = None,
    content_markdown: Optional[str] = None,
    notion_version: str | None = None,
) -> Dict[str, Any]:
    """POST /v1/pages

    parent: {"page_id": ...} or {"database_id": ...} or {"data_source_id": ...}
    properties: page properties payload
    children: optional block children
    content_markdown: mutually exclusive with children
    """
    body: Dict[str, Any] = {"parent": parent, "properties": properties}
    if children is not None:
        body["children"] = children
    if content_markdown is not None:
        body["content_markdown"] = content_markdown
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    return notion_request("POST", "/pages", json=body, notion_version=notion_version)


def retrieve_page(
    *,
    page_id: str,
    filter_properties: Optional[List[str]] = None,
    notion_version: str | None = None,
) -> Dict[str, Any]:
    """GET /v1/pages/{page_id}"""
    params: Dict[str, Any] = {}
    if filter_properties:
        params["filter_properties"] = filter_properties
    return notion_request("GET", f"/pages/{page_id}", params=params or None, notion_version=notion_version)


def update_page(
    *,
    page_id: str,
    properties: Optional[Dict[str, Any]] = None,
    archived: Optional[bool] = None,
    in_trash: Optional[bool] = None,
    icon: Optional[Dict[str, Any]] = None,
    cover: Optional[Dict[str, Any]] = None,
    parent: Optional[Dict[str, Any]] = None,
    notion_version: str | None = None,
) -> Dict[str, Any]:
    """PATCH /v1/pages/{page_id}

    Supports updating properties, archived/in_trash, icon/cover, and parent (move).
    """
    body: Dict[str, Any] = {}
    if properties is not None:
        body["properties"] = properties
    if archived is not None:
        body["archived"] = archived
    if in_trash is not None:
        body["in_trash"] = in_trash
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    if parent is not None:
        body["parent"] = parent
    return notion_request("PATCH", f"/pages/{page_id}", json=body, notion_version=notion_version)


def retrieve_page_property_item(
    *,
    page_id: str,
    property_id: str,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
    notion_version: str | None = None,
) -> Dict[str, Any]:
    """GET /v1/pages/{page_id}/properties/{property_id}"""
    params: Dict[str, Any] = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return notion_request(
        "GET",
        f"/pages/{page_id}/properties/{property_id}",
        params=params or None,
        notion_version=notion_version,
    )


def move_page(
    *,
    page_id: str,
    parent: Dict[str, Any],
    notion_version: str | None = None,
) -> Dict[str, Any]:
    """POST /v1/pages/{page_id}/move"""
    return notion_request(
        "POST",
        f"/pages/{page_id}/move",
        json={"parent": parent},
        notion_version=notion_version,
    )
