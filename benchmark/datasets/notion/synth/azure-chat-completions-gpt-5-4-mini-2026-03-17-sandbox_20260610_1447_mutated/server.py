import os
from typing import Any, Dict, Optional

import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://api.notion.com/v1"
NOTION_VERSION = "2026-03-11"

mcp = FastMCP("notion")


def _headers() -> Dict[str, str]:
    key = os.getenv("NOTION_API_KEY")
    if not key:
        raise RuntimeError("NOTION_API_KEY is not set")
    return {
        "Authorization": f"Bearer {key}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }


def _request(method: str, path: str, *, params: Optional[Dict[str, Any]] = None, json: Optional[Dict[str, Any]] = None) -> Any:
    try:
        resp = requests.request(method, f"{BASE_URL}{path}", headers=_headers(), params=params, json=json, timeout=60)
        if resp.status_code >= 400:
            try:
                return {"error": resp.json()}
            except Exception:
                return {"error": resp.text}
        if resp.text:
            return resp.json()
        return {}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def retrieve_page(page_id: str) -> Any:
    return _request("GET", f"/pages/{page_id}")


@mcp.tool()
def create_page(parent: Dict[str, Any], properties: Dict[str, Any], children: Optional[list] = None, icon: Optional[Dict[str, Any]] = None, cover: Optional[Dict[str, Any]] = None) -> Any:
    body: Dict[str, Any] = {"parent": parent, "properties": properties}
    if children is not None:
        body["children"] = children
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    return _request("POST", "/pages", json=body)


@mcp.tool()
def update_page(page_id: str, properties: Optional[Dict[str, Any]] = None, archived: Optional[bool] = None, in_trash: Optional[bool] = None, icon: Optional[Dict[str, Any]] = None, cover: Optional[Dict[str, Any]] = None) -> Any:
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
    return _request("PATCH", f"/pages/{page_id}", json=body)


@mcp.tool()
def archive_page(page_id: str, archived: bool = True) -> Any:
    return _request("PATCH", f"/pages/{page_id}", json={"archived": archived})


@mcp.tool()
def trash_page(page_id: str, in_trash: bool = True) -> Any:
    return _request("PATCH", f"/pages/{page_id}", json={"in_trash": in_trash})


@mcp.tool()
def move_page(page_id: str, parent: Dict[str, Any], after: Optional[str] = None, before: Optional[str] = None) -> Any:
    body: Dict[str, Any] = {"parent": parent}
    if after is not None:
        body["after"] = after
    if before is not None:
        body["before"] = before
    return _request("POST", f"/pages/{page_id}/move", json=body)


@mcp.tool()
def retrieve_database(database_id: str) -> Any:
    return _request("GET", f"/databases/{database_id}")


@mcp.tool()
def query_database(database_id: str, filter: Optional[Dict[str, Any]] = None, sorts: Optional[list] = None, page_size: Optional[int] = None, start_cursor: Optional[str] = None, filter_properties: Optional[list] = None) -> Any:
    body: Dict[str, Any] = {}
    if filter is not None:
        body["filter"] = filter
    if sorts is not None:
        body["sorts"] = sorts
    if page_size is not None:
        body["page_size"] = page_size
    if start_cursor is not None:
        body["start_cursor"] = start_cursor
    if filter_properties is not None:
        body["filter_properties"] = filter_properties
    return _request("POST", f"/databases/{database_id}/query", json=body)


@mcp.tool()
def create_database(parent: Dict[str, Any], title: list, properties: Dict[str, Any]) -> Any:
    return _request("POST", "/databases", json={"parent": parent, "title": title, "properties": properties})


@mcp.tool()
def update_database(database_id: str, title: Optional[list] = None, properties: Optional[Dict[str, Any]] = None, description: Optional[list] = None) -> Any:
    body: Dict[str, Any] = {}
    if title is not None:
        body["title"] = title
    if properties is not None:
        body["properties"] = properties
    if description is not None:
        body["description"] = description
    return _request("PATCH", f"/databases/{database_id}", json=body)


@mcp.tool()
def retrieve_block(block_id: str) -> Any:
    return _request("GET", f"/blocks/{block_id}")


@mcp.tool()
def list_block_children(block_id: str, page_cursor: Optional[str] = None, results_per_page: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {}
    if page_cursor is not None:
        params["page_cursor"] = page_cursor
    if results_per_page is not None:
        params["results_per_page"] = results_per_page
    return _request("GET", f"/blocks/{block_id}/children", params=params)


@mcp.tool()
def append_block_children(block_id: str, children: list) -> Any:
    return _request("PATCH", f"/blocks/{block_id}/children", json={"children": children})


@mcp.tool()
def update_block(block_id: str, **fields: Any) -> Any:
    return _request("PATCH", f"/blocks/{block_id}", json=fields)


@mcp.tool()
def delete_block(block_id: str) -> Any:
    return _request("DELETE", f"/blocks/{block_id}")


@mcp.tool()
def create_comment(parent: Dict[str, Any], rich_text: list) -> Any:
    return _request("POST", "/comments", json={"parent": parent, "rich_text": rich_text})


@mcp.tool()
def list_comments(block_id: Optional[str] = None, page_id: Optional[str] = None, page_cursor: Optional[str] = None, results_per_page: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {}
    if block_id is not None:
        params["block_id"] = block_id
    if page_id is not None:
        params["page_id"] = page_id
    if page_cursor is not None:
        params["page_cursor"] = page_cursor
    if results_per_page is not None:
        params["results_per_page"] = results_per_page
    return _request("GET", "/comments", params=params)


@mcp.tool()
def retrieve_comment(comment_id: str) -> Any:
    return _request("GET", f"/comments/{comment_id}")


@mcp.tool()
def get_self() -> Any:
    return _request("GET", "/users/me")


@mcp.tool()
def get_user(user_id: str) -> Any:
    return _request("GET", f"/users/{user_id}")


@mcp.tool()
def get_users(page_cursor: Optional[str] = None, results_per_page: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {}
    if page_cursor is not None:
        params["page_cursor"] = page_cursor
    if results_per_page is not None:
        params["results_per_page"] = results_per_page
    return _request("GET", "/users", params=params)


@mcp.tool()
def search(query: Optional[str] = None, filter: Optional[Dict[str, Any]] = None, sort: Optional[Dict[str, Any]] = None, page_size: Optional[int] = None, start_cursor: Optional[str] = None) -> Any:
    body: Dict[str, Any] = {}
    if query is not None:
        body["query"] = query
    if filter is not None:
        body["filter"] = filter
    if sort is not None:
        body["sort"] = sort
    if page_size is not None:
        body["page_size"] = page_size
    if start_cursor is not None:
        body["start_cursor"] = start_cursor
    return _request("POST", "/search", json=body)


if __name__ == "__main__":
    mcp.run()
