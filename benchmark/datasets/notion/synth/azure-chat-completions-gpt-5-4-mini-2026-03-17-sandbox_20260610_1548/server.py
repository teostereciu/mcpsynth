import os
import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://api.notion.com/v1"
NOTION_VERSION = "2026-03-11"

mcp = FastMCP("notion")


def _headers():
    token = os.getenv("NOTION_API_KEY")
    if not token:
        return None
    return {
        "Authorization": f"Bearer {token}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }


def _request(method, path, params=None, json=None):
    headers = _headers()
    if headers is None:
        return {"error": "NOTION_API_KEY is not set"}
    try:
        resp = requests.request(method, f"{BASE_URL}{path}", headers=headers, params=params, json=json, timeout=30)
        if resp.status_code >= 400:
            try:
                return {"error": resp.json()}
            except Exception:
                return {"error": resp.text}
        if resp.text:
            return resp.json()
        return {}
    except requests.RequestException as e:
        return {"error": str(e)}


@mcp.tool()
def list_users(page_size: int | None = None, start_cursor: str | None = None):
    params = {k: v for k, v in {"page_size": page_size, "start_cursor": start_cursor}.items() if v is not None}
    return _request("GET", "/users", params=params)


@mcp.tool()
def get_user(user_id: str):
    return _request("GET", f"/users/{user_id}")


@mcp.tool()
def get_self():
    return _request("GET", "/users/me")


@mcp.tool()
def search(query: str | None = None, sort: dict | None = None, filter: dict | None = None, start_cursor: str | None = None, page_size: int | None = None):
    body = {k: v for k, v in {"query": query, "sort": sort, "filter": filter, "start_cursor": start_cursor, "page_size": page_size}.items() if v is not None}
    return _request("POST", "/search", json=body)


@mcp.tool()
def create_page(parent: dict, properties: dict, children: list | None = None, icon: dict | None = None, cover: dict | None = None):
    body = {"parent": parent, "properties": properties}
    if children is not None:
        body["children"] = children
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    return _request("POST", "/pages", json=body)


@mcp.tool()
def retrieve_page(page_id: str, filter_properties: str | None = None):
    params = {k: v for k, v in {"filter_properties": filter_properties}.items() if v is not None}
    return _request("GET", f"/pages/{page_id}", params=params)


@mcp.tool()
def update_page(page_id: str, properties: dict | None = None, icon: dict | None = None, cover: dict | None = None, archived: bool | None = None, in_trash: bool | None = None, locked: bool | None = None, erase_content: bool | None = None, children: list | None = None):
    body = {k: v for k, v in {"properties": properties, "icon": icon, "cover": cover, "archived": archived, "in_trash": in_trash, "locked": locked, "erase_content": erase_content, "children": children}.items() if v is not None}
    return _request("PATCH", f"/pages/{page_id}", json=body)


@mcp.tool()
def trash_page(page_id: str):
    return _request("PATCH", f"/pages/{page_id}", json={"in_trash": True})


@mcp.tool()
def archive_page(page_id: str):
    return _request("PATCH", f"/pages/{page_id}", json={"archived": True})


@mcp.tool()
def move_page(page_id: str, parent: dict):
    return _request("PATCH", f"/pages/{page_id}", json={"parent": parent})


@mcp.tool()
def retrieve_page_property(page_id: str, property_id: str, start_cursor: str | None = None, page_size: int | None = None):
    params = {k: v for k, v in {"start_cursor": start_cursor, "page_size": page_size}.items() if v is not None}
    return _request("GET", f"/pages/{page_id}/properties/{property_id}", params=params)


@mcp.tool()
def retrieve_block(block_id: str):
    return _request("GET", f"/blocks/{block_id}")


@mcp.tool()
def list_block_children(block_id: str, start_cursor: str | None = None, page_size: int | None = None):
    params = {k: v for k, v in {"start_cursor": start_cursor, "page_size": page_size}.items() if v is not None}
    return _request("GET", f"/blocks/{block_id}/children", params=params)


@mcp.tool()
def append_block_children(block_id: str, children: list):
    return _request("PATCH", f"/blocks/{block_id}/children", json={"children": children})


@mcp.tool()
def update_block(block_id: str, **block):
    return _request("PATCH", f"/blocks/{block_id}", json=block)


@mcp.tool()
def delete_block(block_id: str):
    return _request("DELETE", f"/blocks/{block_id}")


@mcp.tool()
def create_database(parent: dict, title: list, properties: dict, icon: dict | None = None, cover: dict | None = None):
    body = {"parent": parent, "title": title, "properties": properties}
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    return _request("POST", "/databases", json=body)


@mcp.tool()
def retrieve_database(database_id: str):
    return _request("GET", f"/databases/{database_id}")


@mcp.tool()
def update_database(database_id: str, title: list | None = None, properties: dict | None = None, description: list | None = None, icon: dict | None = None, cover: dict | None = None):
    body = {k: v for k, v in {"title": title, "properties": properties, "description": description, "icon": icon, "cover": cover}.items() if v is not None}
    return _request("PATCH", f"/databases/{database_id}", json=body)


@mcp.tool()
def query_database(database_id: str, filter: dict | None = None, sorts: list | None = None, start_cursor: str | None = None, page_size: int | None = None):
    body = {k: v for k, v in {"filter": filter, "sorts": sorts, "start_cursor": start_cursor, "page_size": page_size}.items() if v is not None}
    return _request("POST", f"/databases/{database_id}/query", json=body)


@mcp.tool()
def create_comment(parent: dict, rich_text: list):
    return _request("POST", "/comments", json={"parent": parent, "rich_text": rich_text})


@mcp.tool()
def list_comments(block_id: str | None = None, page_id: str | None = None, start_cursor: str | None = None, page_size: int | None = None):
    params = {k: v for k, v in {"block_id": block_id, "page_id": page_id, "start_cursor": start_cursor, "page_size": page_size}.items() if v is not None}
    return _request("GET", "/comments", params=params)


@mcp.tool()
def retrieve_comment(comment_id: str):
    return _request("GET", f"/comments/{comment_id}")


@mcp.tool()
def list_file_uploads(start_cursor: str | None = None, page_size: int | None = None):
    params = {k: v for k, v in {"start_cursor": start_cursor, "page_size": page_size}.items() if v is not None}
    return _request("GET", "/file_uploads", params=params)


@mcp.tool()
def retrieve_file_upload(file_upload_id: str):
    return _request("GET", f"/file_uploads/{file_upload_id}")


@mcp.tool()
def create_file_upload(filename: str, content_type: str, file_size: int):
    return _request("POST", "/file_uploads", json={"filename": filename, "content_type": content_type, "file_size": file_size})


@mcp.tool()
def send_file_upload(file_upload_id: str):
    return _request("POST", f"/file_uploads/{file_upload_id}/send")


@mcp.tool()
def complete_file_upload(file_upload_id: str):
    return _request("POST", f"/file_uploads/{file_upload_id}/complete")


if __name__ == "__main__":
    mcp.run()
