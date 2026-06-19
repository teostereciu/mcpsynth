import os
from typing import Any, Dict

import requests
from fastmcp import FastMCP

BASE_URL = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"

mcp = FastMCP("notion")


def _headers() -> Dict[str, str]:
    token = os.getenv("NOTION_API_KEY")
    if not token:
        return {}
    return {
        "Authorization": f"Bearer {token}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }


def _request(method: str, path: str, *, params: Dict[str, Any] | None = None, json: Dict[str, Any] | None = None) -> Dict[str, Any]:
    if not os.getenv("NOTION_API_KEY"):
        return {"error": "NOTION_API_KEY is not set"}
    try:
        resp = requests.request(method, f"{BASE_URL}{path}", headers=_headers(), params=params, json=json, timeout=30)
        if resp.status_code >= 400:
            try:
                return {"error": resp.json()}
            except Exception:
                return {"error": resp.text}
        return resp.json() if resp.content else {}
    except requests.RequestException as e:
        return {"error": str(e)}


@mcp.tool()
def search(query: str, page_size: int | None = None) -> Dict[str, Any]:
    payload: Dict[str, Any] = {"query": query}
    if page_size is not None:
        payload["page_size"] = page_size
    return _request("POST", "/search", json=payload)


@mcp.tool()
def retrieve_user(user_id: str) -> Dict[str, Any]:
    return _request("GET", f"/users/{user_id}")


@mcp.tool()
def list_users(page_size: int | None = None, start_cursor: str | None = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if page_size is not None:
        params["page_size"] = page_size
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    return _request("GET", "/users", params=params or None)


@mcp.tool()
def retrieve_page(page_id: str) -> Dict[str, Any]:
    return _request("GET", f"/pages/{page_id}")


@mcp.tool()
def create_page(parent: Dict[str, Any], properties: Dict[str, Any], children: list[Dict[str, Any]] | None = None) -> Dict[str, Any]:
    payload: Dict[str, Any] = {"parent": parent, "properties": properties}
    if children is not None:
        payload["children"] = children
    return _request("POST", "/pages", json=payload)


@mcp.tool()
def update_page(page_id: str, properties: Dict[str, Any] | None = None, archived: bool | None = None, icon: Dict[str, Any] | None = None, cover: Dict[str, Any] | None = None) -> Dict[str, Any]:
    payload: Dict[str, Any] = {}
    if properties is not None:
        payload["properties"] = properties
    if archived is not None:
        payload["archived"] = archived
    if icon is not None:
        payload["icon"] = icon
    if cover is not None:
        payload["cover"] = cover
    return _request("PATCH", f"/pages/{page_id}", json=payload)


@mcp.tool()
def retrieve_database(database_id: str) -> Dict[str, Any]:
    return _request("GET", f"/databases/{database_id}")


@mcp.tool()
def create_database(parent: Dict[str, Any], title: list[Dict[str, Any]], properties: Dict[str, Any]) -> Dict[str, Any]:
    return _request("POST", "/databases", json={"parent": parent, "title": title, "properties": properties})


@mcp.tool()
def query_database(database_id: str, filter: Dict[str, Any] | None = None, sorts: list[Dict[str, Any]] | None = None, page_size: int | None = None, start_cursor: str | None = None) -> Dict[str, Any]:
    payload: Dict[str, Any] = {}
    if filter is not None:
        payload["filter"] = filter
    if sorts is not None:
        payload["sorts"] = sorts
    if page_size is not None:
        payload["page_size"] = page_size
    if start_cursor is not None:
        payload["start_cursor"] = start_cursor
    return _request("POST", f"/databases/{database_id}/query", json=payload)


@mcp.tool()
def update_database(database_id: str, title: list[Dict[str, Any]] | None = None, properties: Dict[str, Any] | None = None, description: list[Dict[str, Any]] | None = None) -> Dict[str, Any]:
    payload: Dict[str, Any] = {}
    if title is not None:
        payload["title"] = title
    if properties is not None:
        payload["properties"] = properties
    if description is not None:
        payload["description"] = description
    return _request("PATCH", f"/databases/{database_id}", json=payload)


@mcp.tool()
def retrieve_block(block_id: str) -> Dict[str, Any]:
    return _request("GET", f"/blocks/{block_id}")


@mcp.tool()
def retrieve_block_children(block_id: str, page_size: int | None = None, start_cursor: str | None = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if page_size is not None:
        params["page_size"] = page_size
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    return _request("GET", f"/blocks/{block_id}/children", params=params or None)


@mcp.tool()
def append_block_children(block_id: str, children: list[Dict[str, Any]]) -> Dict[str, Any]:
    return _request("PATCH", f"/blocks/{block_id}/children", json={"children": children})


@mcp.tool()
def update_block(block_id: str, **fields: Any) -> Dict[str, Any]:
    return _request("PATCH", f"/blocks/{block_id}", json=fields)


@mcp.tool()
def delete_block(block_id: str) -> Dict[str, Any]:
    return _request("DELETE", f"/blocks/{block_id}")


@mcp.tool()
def create_comment(parent: Dict[str, Any], rich_text: list[Dict[str, Any]]) -> Dict[str, Any]:
    return _request("POST", "/comments", json={"parent": parent, "rich_text": rich_text})


@mcp.tool()
def retrieve_comments(block_id: str | None = None, page_id: str | None = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if block_id is not None:
        params["block_id"] = block_id
    if page_id is not None:
        params["page_id"] = page_id
    return _request("GET", "/comments", params=params or None)


if __name__ == "__main__":
    mcp.run()
