import base64
import json
import os
from typing import Any, Dict, Optional

import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("confluence-cloud")

BASE_URL = os.environ.get("CONFLUENCE_BASE_URL", "").rstrip("/")
EMAIL = os.environ.get("JIRA_EMAIL", "")
TOKEN = os.environ.get("JIRA_API_TOKEN", "")
SPACE_KEY = os.environ.get("CONFLUENCE_SPACE_KEY", "")


def _auth_headers() -> Dict[str, str]:
    token = base64.b64encode(f"{EMAIL}:{TOKEN}".encode()).decode()
    return {"Authorization": f"Basic {token}", "Accept": "application/json"}


def _request(method: str, path: str, params: Optional[Dict[str, Any]] = None, json_body: Any = None) -> Any:
    if not BASE_URL:
        return {"error": "CONFLUENCE_BASE_URL is not set"}
    try:
        resp = requests.request(
            method,
            f"{BASE_URL}{path}",
            headers=_auth_headers(),
            params={k: v for k, v in (params or {}).items() if v is not None},
            json=json_body,
            timeout=60,
        )
        if resp.status_code >= 400:
            try:
                return {"error": resp.json()}
            except Exception:
                return {"error": resp.text, "status_code": resp.status_code}
        if resp.status_code == 204:
            return {"ok": True}
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


@mcp.tool()
def list_tools() -> Dict[str, Any]:
    return {"tools": ["get_page", "create_page", "update_page", "delete_page", "get_pages", "get_space", "create_space", "get_spaces", "get_attachment", "get_attachments", "get_page_attachments", "get_blog_post", "create_blog_post", "update_blog_post", "delete_blog_post", "get_comments_for_page", "create_footer_comment", "get_labels_for_page", "get_content_property", "create_content_property", "update_content_property", "delete_content_property", "get_page_versions", "get_current_user", "get_user_by_account_id"]}


@mcp.tool()
def get_pages(limit: Optional[int] = None, cursor: Optional[str] = None, space_id: Optional[str] = None, title: Optional[str] = None) -> Any:
    return _request("GET", "/api/v2/pages", {"limit": limit, "cursor": cursor, "space-id": space_id, "title": title})


@mcp.tool()
def get_page(page_id: str) -> Any:
    return _request("GET", f"/api/v2/pages/{page_id}")


@mcp.tool()
def create_page(space_id: str, title: str, body_value: str, parent_id: Optional[str] = None, status: str = "current") -> Any:
    return _request("POST", "/api/v2/pages", json_body={"spaceId": space_id, "title": title, "parentId": parent_id, "status": status, "body": {"representation": "storage", "value": body_value}})


@mcp.tool()
def update_page(page_id: str, title: str, body_value: str, status: str, version_number: int, space_id: Optional[str] = None, parent_id: Optional[str] = None) -> Any:
    payload = {"id": page_id, "title": title, "status": status, "body": {"representation": "storage", "value": body_value}, "version": {"number": version_number}}
    if space_id is not None:
        payload["spaceId"] = space_id
    if parent_id is not None:
        payload["parentId"] = parent_id
    return _request("PUT", f"/api/v2/pages/{page_id}", json_body=payload)


@mcp.tool()
def delete_page(page_id: str, purge: Optional[bool] = None, draft: Optional[bool] = None) -> Any:
    return _request("DELETE", f"/api/v2/pages/{page_id}", {"purge": purge, "draft": draft})


@mcp.tool()
def get_spaces(limit: Optional[int] = None, cursor: Optional[str] = None, keys: Optional[str] = None) -> Any:
    return _request("GET", "/api/v2/spaces", {"limit": limit, "cursor": cursor, "keys": keys})


@mcp.tool()
def get_space(space_id: str) -> Any:
    return _request("GET", f"/api/v2/spaces/{space_id}")


@mcp.tool()
def create_space(name: str, key: Optional[str] = None, description: Optional[str] = None) -> Any:
    payload = {"name": name, "key": key or SPACE_KEY}
    if description:
        payload["description"] = {"value": description, "representation": "plain"}
    return _request("POST", "/api/v2/spaces", json_body=payload)


@mcp.tool()
def get_attachments(limit: Optional[int] = None, cursor: Optional[str] = None, filename: Optional[str] = None) -> Any:
    return _request("GET", "/api/v2/attachments", {"limit": limit, "cursor": cursor, "filename": filename})


@mcp.tool()
def get_attachment(attachment_id: str) -> Any:
    return _request("GET", f"/api/v2/attachments/{attachment_id}")


@mcp.tool()
def get_page_attachments(page_id: str, limit: Optional[int] = None, cursor: Optional[str] = None) -> Any:
    return _request("GET", f"/api/v2/pages/{page_id}/attachments", {"limit": limit, "cursor": cursor})


@mcp.tool()
def get_blog_post(blog_post_id: str) -> Any:
    return _request("GET", f"/api/v2/blogposts/{blog_post_id}")


@mcp.tool()
def create_blog_post(space_id: str, title: str, body_value: str) -> Any:
    return _request("POST", "/api/v2/blogposts", json_body={"spaceId": space_id, "title": title, "body": {"representation": "storage", "value": body_value}})


@mcp.tool()
def update_blog_post(blog_post_id: str, title: str, body_value: str, status: str, version_number: int) -> Any:
    return _request("PUT", f"/api/v2/blogposts/{blog_post_id}", json_body={"id": blog_post_id, "title": title, "status": status, "body": {"representation": "storage", "value": body_value}, "version": {"number": version_number}})


@mcp.tool()
def delete_blog_post(blog_post_id: str) -> Any:
    return _request("DELETE", f"/api/v2/blogposts/{blog_post_id}")


@mcp.tool()
def get_comments_for_page(page_id: str) -> Any:
    return _request("GET", "/api/v2/comments", {"page-id": page_id})


@mcp.tool()
def create_footer_comment(page_id: str, body_value: str) -> Any:
    return _request("POST", "/api/v2/comments", json_body={"pageId": page_id, "body": {"representation": "storage", "value": body_value}})


@mcp.tool()
def get_labels_for_page(page_id: str) -> Any:
    return _request("GET", f"/api/v2/pages/{page_id}", {"include-labels": True})


@mcp.tool()
def get_content_property(page_id: str, property_id: str) -> Any:
    return _request("GET", f"/api/v2/pages/{page_id}/properties/{property_id}")


@mcp.tool()
def create_content_property(page_id: str, key: str, value: Any) -> Any:
    return _request("POST", f"/api/v2/pages/{page_id}/properties", json_body={"key": key, "value": value})


@mcp.tool()
def update_content_property(page_id: str, property_id: str, key: str, value: Any, version_number: int) -> Any:
    return _request("PUT", f"/api/v2/pages/{page_id}/properties/{property_id}", json_body={"key": key, "value": value, "version": {"number": version_number}})


@mcp.tool()
def delete_content_property(page_id: str, property_id: str) -> Any:
    return _request("DELETE", f"/api/v2/pages/{page_id}/properties/{property_id}")


@mcp.tool()
def get_page_versions(page_id: str) -> Any:
    return _request("GET", f"/api/v2/pages/{page_id}/versions")


@mcp.tool()
def get_current_user() -> Any:
    return _request("GET", "/api/v2/users/current")


@mcp.tool()
def get_user_by_account_id(account_id: str) -> Any:
    return _request("GET", "/api/v2/users", {"account-id": account_id})


if __name__ == "__main__":
    mcp.run(transport="stdio")
