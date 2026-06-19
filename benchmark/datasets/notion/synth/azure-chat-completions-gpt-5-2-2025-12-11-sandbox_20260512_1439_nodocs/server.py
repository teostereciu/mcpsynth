import os
import json
from typing import Any, Dict, Optional

import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://api.notion.com/v1"
DEFAULT_NOTION_VERSION = os.getenv("NOTION_VERSION", "2022-06-28")


def _headers() -> Dict[str, str]:
    token = os.getenv("NOTION_API_KEY")
    if not token:
        return {}
    return {
        "Authorization": f"Bearer {token}",
        "Notion-Version": DEFAULT_NOTION_VERSION,
        "Content-Type": "application/json",
    }


def _request(method: str, path: str, *, params: Optional[dict] = None, json_body: Optional[dict] = None) -> Any:
    if not os.getenv("NOTION_API_KEY"):
        return {"error": "NOTION_API_KEY is not set"}

    url = f"{BASE_URL}{path}"
    try:
        resp = requests.request(method, url, headers=_headers(), params=params, json=json_body, timeout=60)
    except requests.RequestException as e:
        return {"error": f"request_failed: {str(e)}"}

    content_type = resp.headers.get("content-type", "")
    data: Any
    if "application/json" in content_type:
        try:
            data = resp.json()
        except Exception:
            data = {"error": "invalid_json_response", "status": resp.status_code, "text": resp.text}
    else:
        data = {"status": resp.status_code, "text": resp.text}

    if resp.status_code >= 400:
        return {"error": "notion_api_error", "status": resp.status_code, "response": data}
    return data


mcp = FastMCP("notion")


# --- Users ---
@mcp.tool()
def notion_users_list() -> Any:
    """List all users."""
    return _request("GET", "/users")


@mcp.tool()
def notion_users_retrieve(user_id: str) -> Any:
    """Retrieve a user by ID."""
    return _request("GET", f"/users/{user_id}")


@mcp.tool()
def notion_users_me() -> Any:
    """Retrieve the bot user associated with the integration."""
    return _request("GET", "/users/me")


# --- Search ---
@mcp.tool()
def notion_search(query: Optional[str] = None, filter: Optional[dict] = None, sort: Optional[dict] = None, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    """Search pages and databases."""
    body: Dict[str, Any] = {}
    if query is not None:
        body["query"] = query
    if filter is not None:
        body["filter"] = filter
    if sort is not None:
        body["sort"] = sort
    if start_cursor is not None:
        body["start_cursor"] = start_cursor
    if page_size is not None:
        body["page_size"] = page_size
    return _request("POST", "/search", json_body=body)


# --- Pages ---
@mcp.tool()
def notion_pages_create(parent: dict, properties: dict, children: Optional[list] = None, icon: Optional[dict] = None, cover: Optional[dict] = None) -> Any:
    """Create a page."""
    body: Dict[str, Any] = {"parent": parent, "properties": properties}
    if children is not None:
        body["children"] = children
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    return _request("POST", "/pages", json_body=body)


@mcp.tool()
def notion_pages_retrieve(page_id: str) -> Any:
    """Retrieve a page."""
    return _request("GET", f"/pages/{page_id}")


@mcp.tool()
def notion_pages_update(page_id: str, properties: Optional[dict] = None, archived: Optional[bool] = None, icon: Optional[dict] = None, cover: Optional[dict] = None) -> Any:
    """Update page properties or archive/unarchive."""
    body: Dict[str, Any] = {}
    if properties is not None:
        body["properties"] = properties
    if archived is not None:
        body["archived"] = archived
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    return _request("PATCH", f"/pages/{page_id}", json_body=body)


# --- Databases ---
@mcp.tool()
def notion_databases_create(parent: dict, title: list, properties: dict, icon: Optional[dict] = None, cover: Optional[dict] = None, description: Optional[list] = None, is_inline: Optional[bool] = None) -> Any:
    """Create a database."""
    body: Dict[str, Any] = {"parent": parent, "title": title, "properties": properties}
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    if description is not None:
        body["description"] = description
    if is_inline is not None:
        body["is_inline"] = is_inline
    return _request("POST", "/databases", json_body=body)


@mcp.tool()
def notion_databases_retrieve(database_id: str) -> Any:
    """Retrieve a database."""
    return _request("GET", f"/databases/{database_id}")


@mcp.tool()
def notion_databases_update(database_id: str, title: Optional[list] = None, description: Optional[list] = None, properties: Optional[dict] = None, icon: Optional[dict] = None, cover: Optional[dict] = None, archived: Optional[bool] = None, is_inline: Optional[bool] = None) -> Any:
    """Update database schema and metadata."""
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
    if archived is not None:
        body["archived"] = archived
    if is_inline is not None:
        body["is_inline"] = is_inline
    return _request("PATCH", f"/databases/{database_id}", json_body=body)


@mcp.tool()
def notion_databases_query(database_id: str, filter: Optional[dict] = None, sorts: Optional[list] = None, start_cursor: Optional[str] = None, page_size: Optional[int] = None, filter_properties: Optional[list] = None) -> Any:
    """Query a database with optional filter/sorts/pagination."""
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
    return _request("POST", f"/databases/{database_id}/query", json_body=body)


# --- Blocks ---
@mcp.tool()
def notion_blocks_retrieve(block_id: str) -> Any:
    """Retrieve a block."""
    return _request("GET", f"/blocks/{block_id}")


@mcp.tool()
def notion_blocks_update(block_id: str, block: dict) -> Any:
    """Update a block. Provide the block-type payload under `block` (e.g. {"paragraph": {...}})."""
    return _request("PATCH", f"/blocks/{block_id}", json_body=block)


@mcp.tool()
def notion_blocks_delete(block_id: str) -> Any:
    """Delete (archive) a block."""
    return _request("DELETE", f"/blocks/{block_id}")


@mcp.tool()
def notion_blocks_children_list(block_id: str, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    """List block children."""
    params: Dict[str, Any] = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return _request("GET", f"/blocks/{block_id}/children", params=params)


@mcp.tool()
def notion_blocks_children_append(block_id: str, children: list, after: Optional[str] = None) -> Any:
    """Append children blocks to a block."""
    body: Dict[str, Any] = {"children": children}
    if after is not None:
        body["after"] = after
    return _request("PATCH", f"/blocks/{block_id}/children", json_body=body)


# --- Comments ---
@mcp.tool()
def notion_comments_list(block_id: Optional[str] = None, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    """List comments, optionally for a specific block."""
    params: Dict[str, Any] = {}
    if block_id is not None:
        params["block_id"] = block_id
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return _request("GET", "/comments", params=params)


@mcp.tool()
def notion_comments_create(parent: dict, rich_text: list) -> Any:
    """Create a comment."""
    body = {"parent": parent, "rich_text": rich_text}
    return _request("POST", "/comments", json_body=body)


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
