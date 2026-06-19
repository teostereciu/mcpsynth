import os
from typing import Any, Dict, Optional

import requests
from fastmcp import FastMCP

mcp = FastMCP("confluence-cloud")

BASE_URL = os.getenv("CONFLUENCE_BASE_URL", "").rstrip("/")
EMAIL = os.getenv("JIRA_EMAIL", "")
API_TOKEN = os.getenv("JIRA_API_TOKEN", "")
DEFAULT_SPACE_KEY = os.getenv("CONFLUENCE_SPACE_KEY", "")


def _auth():
    return (EMAIL, API_TOKEN)


def _headers(extra: Optional[Dict[str, str]] = None) -> Dict[str, str]:
    headers = {"Accept": "application/json"}
    if extra:
        headers.update(extra)
    return headers


def _url(path: str) -> str:
    return f"{BASE_URL}{path}"


def _request(method: str, path: str, *, params=None, json=None, data=None, headers=None, files=None):
    try:
        resp = requests.request(
            method,
            _url(path),
            params=params,
            json=json,
            data=data,
            headers=_headers(headers),
            auth=_auth(),
            files=files,
            timeout=60,
        )
        if resp.status_code >= 400:
            try:
                return {"error": resp.json()}
            except Exception:
                return {"error": resp.text, "status_code": resp.status_code}
        if not resp.text:
            return {"ok": True}
        try:
            return resp.json()
        except Exception:
            return {"text": resp.text}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def list_spaces(limit: int = 25, cursor: Optional[str] = None) -> Dict[str, Any]:
    return _request("GET", "/api/v2/spaces", params={k: v for k, v in {"limit": limit, "cursor": cursor}.items() if v is not None})


@mcp.tool()
def get_space(space_id: str) -> Dict[str, Any]:
    return _request("GET", f"/api/v2/spaces/{space_id}")


@mcp.tool()
def create_space(key: str, name: str, description: Optional[str] = None) -> Dict[str, Any]:
    payload = {"key": key, "name": name}
    if description is not None:
        payload["description"] = {"plain": {"value": description, "representation": "plain"}}
    return _request("POST", "/api/v2/spaces", json=payload)


@mcp.tool()
def delete_space(space_id: str) -> Dict[str, Any]:
    return _request("DELETE", f"/api/v2/spaces/{space_id}")


@mcp.tool()
def get_current_user() -> Dict[str, Any]:
    return _request("GET", "/rest/api/user/current")


@mcp.tool()
def get_user_by_account_id(account_id: str) -> Dict[str, Any]:
    return _request("GET", "/rest/api/user", params={"accountId": account_id})


@mcp.tool()
def search_content(cql: str, limit: int = 25, cursor: Optional[str] = None) -> Dict[str, Any]:
    params = {"cql": cql, "limit": limit}
    if cursor is not None:
        params["cursor"] = cursor
    return _request("GET", "/rest/api/search", params=params)


@mcp.tool()
def get_page(page_id: str) -> Dict[str, Any]:
    return _request("GET", f"/api/v2/pages/{page_id}")


@mcp.tool()
def create_page(space_id: Optional[str], title: str, body: str, parent_id: Optional[str] = None) -> Dict[str, Any]:
    payload = {"spaceId": space_id or DEFAULT_SPACE_KEY, "title": title, "body": {"representation": "storage", "value": body}}
    if parent_id:
        payload["parentId"] = parent_id
    return _request("POST", "/api/v2/pages", json=payload)


@mcp.tool()
def update_page(page_id: str, title: str, body: str, version: int) -> Dict[str, Any]:
    payload = {"id": page_id, "status": "current", "title": title, "body": {"representation": "storage", "value": body}, "version": {"number": version}}
    return _request("PUT", f"/api/v2/pages/{page_id}", json=payload)


@mcp.tool()
def delete_page(page_id: str) -> Dict[str, Any]:
    return _request("DELETE", f"/api/v2/pages/{page_id}")


@mcp.tool()
def get_page_children(page_id: str, limit: int = 25) -> Dict[str, Any]:
    return _request("GET", f"/api/v2/pages/{page_id}/children", params={"limit": limit})


@mcp.tool()
def get_page_ancestors(page_id: str) -> Dict[str, Any]:
    return _request("GET", f"/api/v2/pages/{page_id}/ancestors")


@mcp.tool()
def move_page(page_id: str, position: str, target_id: Optional[str] = None) -> Dict[str, Any]:
    payload = {"position": position}
    if target_id:
        payload["targetId"] = target_id
    return _request("POST", f"/api/v2/pages/{page_id}/move", json=payload)


@mcp.tool()
def list_page_versions(page_id: str, limit: int = 25) -> Dict[str, Any]:
    return _request("GET", f"/api/v2/pages/{page_id}/versions", params={"limit": limit})


@mcp.tool()
def get_page_version(page_id: str, version_number: int) -> Dict[str, Any]:
    return _request("GET", f"/api/v2/pages/{page_id}/versions/{version_number}")


@mcp.tool()
def restore_page_version(page_id: str, version_number: int) -> Dict[str, Any]:
    return _request("POST", f"/api/v2/pages/{page_id}/versions/{version_number}/restore")


@mcp.tool()
def get_page_property(page_id: str, key: str) -> Dict[str, Any]:
    return _request("GET", f"/api/v2/pages/{page_id}/properties/{key}")


@mcp.tool()
def set_page_property(page_id: str, key: str, value: Any) -> Dict[str, Any]:
    return _request("PUT", f"/api/v2/pages/{page_id}/properties/{key}", json={"value": value})


@mcp.tool()
def list_labels(page_id: str) -> Dict[str, Any]:
    return _request("GET", f"/api/v2/pages/{page_id}/labels")


@mcp.tool()
def add_label(page_id: str, label: str) -> Dict[str, Any]:
    return _request("POST", f"/api/v2/pages/{page_id}/labels", json={"prefix": "global", "name": label})


@mcp.tool()
def remove_label(page_id: str, label: str) -> Dict[str, Any]:
    return _request("DELETE", f"/api/v2/pages/{page_id}/labels/{label}")


@mcp.tool()
def list_attachments(page_id: str) -> Dict[str, Any]:
    return _request("GET", f"/api/v2/pages/{page_id}/attachments")


@mcp.tool()
def upload_attachment(page_id: str, filename: str, content: str) -> Dict[str, Any]:
    files = {"file": (filename, content.encode("utf-8"))}
    return _request("POST", f"/api/v2/pages/{page_id}/attachments", files=files, headers={"X-Atlassian-Token": "no-check"})


@mcp.tool()
def download_attachment(attachment_id: str) -> Dict[str, Any]:
    return _request("GET", f"/api/v2/attachments/{attachment_id}/download")


@mcp.tool()
def list_comments(page_id: str) -> Dict[str, Any]:
    return _request("GET", f"/api/v2/pages/{page_id}/comments")


@mcp.tool()
def create_comment(page_id: str, body: str, parent_comment_id: Optional[str] = None) -> Dict[str, Any]:
    payload = {"body": {"representation": "storage", "value": body}}
    if parent_comment_id:
        payload["parentCommentId"] = parent_comment_id
    return _request("POST", f"/api/v2/pages/{page_id}/comments", json=payload)


@mcp.tool()
def create_blog_post(space_id: str, title: str, body: str) -> Dict[str, Any]:
    return _request("POST", "/api/v2/blogposts", json={"spaceId": space_id, "title": title, "body": {"representation": "storage", "value": body}})


@mcp.tool()
def get_blog_post(blogpost_id: str) -> Dict[str, Any]:
    return _request("GET", f"/api/v2/blogposts/{blogpost_id}")


@mcp.tool()
def update_blog_post(blogpost_id: str, title: str, body: str, version: int) -> Dict[str, Any]:
    return _request("PUT", f"/api/v2/blogposts/{blogpost_id}", json={"id": blogpost_id, "status": "current", "title": title, "body": {"representation": "storage", "value": body}, "version": {"number": version}})


@mcp.tool()
def delete_blog_post(blogpost_id: str) -> Dict[str, Any]:
    return _request("DELETE", f"/api/v2/blogposts/{blogpost_id}")


if __name__ == "__main__":
    mcp.run(transport="stdio")
