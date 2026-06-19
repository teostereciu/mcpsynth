from __future__ import annotations

import os
from typing import Any, Dict, Optional

import httpx
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://api.notion.com/v1"
NOTION_VERSION = "2026-03-11"

mcp = FastMCP("notion")


def _headers() -> Dict[str, str]:
    token = os.getenv("NOTION_API_KEY")
    if not token:
        raise RuntimeError("NOTION_API_KEY is not set")
    return {
        "Authorization": f"Bearer {token}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }


def _request(method: str, path: str, params: Optional[Dict[str, Any]] = None, json: Any = None) -> Any:
    with httpx.Client(timeout=60.0) as client:
        resp = client.request(method, f"{BASE_URL}{path}", headers=_headers(), params=params, json=json)
        resp.raise_for_status()
        return resp.json()


@mcp.tool()
def retrieve_page(page_id: str, filter_properties: Optional[list[str]] = None) -> Any:
    params = {}
    if filter_properties:
        params["filter_properties"] = filter_properties
    return _request("GET", f"/pages/{page_id}", params=params or None)


@mcp.tool()
def create_page(parent: dict, properties: dict, children: Optional[list[dict]] = None, icon: Optional[dict] = None, cover: Optional[dict] = None) -> Any:
    payload: Dict[str, Any] = {"parent": parent, "properties": properties}
    if children is not None:
        payload["children"] = children
    if icon is not None:
        payload["icon"] = icon
    if cover is not None:
        payload["cover"] = cover
    return _request("POST", "/pages", json=payload)


@mcp.tool()
def update_page(page_id: str, properties: Optional[dict] = None, archived: Optional[bool] = None, in_trash: Optional[bool] = None, is_locked: Optional[bool] = None, icon: Optional[dict] = None, cover: Optional[dict] = None) -> Any:
    payload: Dict[str, Any] = {}
    if properties is not None:
        payload["properties"] = properties
    if archived is not None:
        payload["archived"] = archived
    if in_trash is not None:
        payload["in_trash"] = in_trash
    if is_locked is not None:
        payload["is_locked"] = is_locked
    if icon is not None:
        payload["icon"] = icon
    if cover is not None:
        payload["cover"] = cover
    return _request("PATCH", f"/pages/{page_id}", json=payload)


@mcp.tool()
def retrieve_database(database_id: str) -> Any:
    return _request("GET", f"/databases/{database_id}")


@mcp.tool()
def create_database(parent: dict, title: list[dict], properties: dict, is_inline: Optional[bool] = None, description: Optional[list[dict]] = None) -> Any:
    payload: Dict[str, Any] = {"parent": parent, "title": title, "properties": properties}
    if is_inline is not None:
        payload["is_inline"] = is_inline
    if description is not None:
        payload["description"] = description
    return _request("POST", "/databases", json=payload)


@mcp.tool()
def update_database(database_id: str, title: Optional[list[dict]] = None, description: Optional[list[dict]] = None, is_inline: Optional[bool] = None, archived: Optional[bool] = None, is_locked: Optional[bool] = None, icon: Optional[dict] = None, cover: Optional[dict] = None, parent: Optional[dict] = None, properties: Optional[dict] = None) -> Any:
    payload: Dict[str, Any] = {}
    if title is not None:
        payload["title"] = title
    if description is not None:
        payload["description"] = description
    if is_inline is not None:
        payload["is_inline"] = is_inline
    if archived is not None:
        payload["archived"] = archived
    if is_locked is not None:
        payload["is_locked"] = is_locked
    if icon is not None:
        payload["icon"] = icon
    if cover is not None:
        payload["cover"] = cover
    if parent is not None:
        payload["parent"] = parent
    if properties is not None:
        payload["properties"] = properties
    return _request("PATCH", f"/databases/{database_id}", json=payload)


@mcp.tool()
def query_database(database_id: str, filter: Optional[dict] = None, sorts: Optional[list[dict]] = None, page_size: Optional[int] = None, start_cursor: Optional[str] = None, filter_properties: Optional[list[str]] = None) -> Any:
    payload: Dict[str, Any] = {}
    if filter is not None:
        payload["filter"] = filter
    if sorts is not None:
        payload["sorts"] = sorts
    if page_size is not None:
        payload["page_size"] = page_size
    if start_cursor is not None:
        payload["start_cursor"] = start_cursor
    if filter_properties is not None:
        payload["filter_properties"] = filter_properties
    return _request("POST", f"/databases/{database_id}/query", json=payload)


@mcp.tool()
def list_block_children(block_id: str, page_cursor: Optional[str] = None, results_per_page: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {}
    if page_cursor is not None:
        params["start_cursor"] = page_cursor
    if results_per_page is not None:
        params["page_size"] = results_per_page
    return _request("GET", f"/blocks/{block_id}/children", params=params or None)


@mcp.tool()
def list_users(page_cursor: Optional[str] = None, results_per_page: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {}
    if page_cursor is not None:
        params["start_cursor"] = page_cursor
    if results_per_page is not None:
        params["page_size"] = results_per_page
    return _request("GET", "/users", params=params or None)


@mcp.tool()
def get_self() -> Any:
    return _request("GET", "/users/me")
