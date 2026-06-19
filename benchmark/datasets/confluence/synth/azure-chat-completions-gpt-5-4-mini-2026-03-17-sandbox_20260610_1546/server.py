import base64
import json
import os
from typing import Any, Dict, Optional

import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("confluence-cloud")

BASE_URL = os.environ.get("CONFLUENCE_BASE_URL", "").rstrip("/")
EMAIL = os.environ.get("JIRA_EMAIL", "")
API_TOKEN = os.environ.get("JIRA_API_TOKEN", "")
SPACE_KEY = os.environ.get("CONFLUENCE_SPACE_KEY", "")


def _auth_header() -> Dict[str, str]:
    token = base64.b64encode(f"{EMAIL}:{API_TOKEN}".encode()).decode()
    return {"Authorization": f"Basic {token}"}


def _request(method: str, path: str, params: Optional[Dict[str, Any]] = None, json_body: Any = None) -> Any:
    if not BASE_URL:
        return {"error": "CONFLUENCE_BASE_URL is not set"}
    try:
        resp = requests.request(
            method,
            f"{BASE_URL}{path}",
            params=params,
            json=json_body,
            headers={**_auth_header(), "Accept": "application/json"},
            timeout=60,
        )
        if resp.status_code >= 400:
            try:
                return {"error": resp.json()}
            except Exception:
                return {"error": resp.text or f"HTTP {resp.status_code}"}
        if resp.status_code == 204:
            return {"ok": True}
        if resp.text:
            return resp.json()
        return {"ok": True}
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_pages(cql: str, limit: int = 25, cursor: Optional[str] = None):
    return _request("GET", "/api/v2/pages", params={"cql": cql, "limit": limit, "cursor": cursor})


@mcp.tool()
def get_page(page_id: str, body_format: Optional[str] = None, include_labels: bool = False, include_properties: bool = False, include_versions: bool = False):
    params = {"body-format": body_format, "include-labels": include_labels, "include-properties": include_properties, "include-versions": include_versions}
    return _request("GET", f"/api/v2/pages/{page_id}", params={k: v for k, v in params.items() if v is not None})


@mcp.tool()
def create_page(space_id: str, title: str, body: Dict[str, Any], parent_id: Optional[str] = None, status: str = "current"):
    payload = {"spaceId": space_id, "title": title, "body": body, "status": status}
    if parent_id:
        payload["parentId"] = parent_id
    return _request("POST", "/api/v2/pages", json_body=payload)


@mcp.tool()
def update_page(page_id: str, title: str, body: Dict[str, Any], version_number: int, status: str = "current"):
    payload = {"id": page_id, "status": status, "title": title, "body": body, "version": {"number": version_number}}
    return _request("PUT", f"/api/v2/pages/{page_id}", json_body=payload)


@mcp.tool()
def delete_page(page_id: str, purge: bool = False, draft: bool = False):
    return _request("DELETE", f"/api/v2/pages/{page_id}", params={"purge": purge, "draft": draft})


@mcp.tool()
def get_spaces(limit: int = 25, cursor: Optional[str] = None):
    return _request("GET", "/api/v2/spaces", params={k: v for k, v in {"limit": limit, "cursor": cursor}.items() if v is not None})


@mcp.tool()
def create_space(name: str, key: Optional[str] = None, description: Optional[Dict[str, Any]] = None):
    payload = {"name": name}
    if key:
        payload["key"] = key
    if description:
        payload["description"] = description
    return _request("POST", "/api/v2/spaces", json_body=payload)


@mcp.tool()
def get_space(space_id: str):
    return _request("GET", f"/api/v2/spaces/{space_id}")


@mcp.tool()
def search_content(cql: str, limit: int = 25, cursor: Optional[str] = None):
    return _request("GET", "/rest/api/search", params={k: v for k, v in {"cql": cql, "limit": limit, "cursor": cursor}.items() if v is not None})


@mcp.tool()
def get_footer_comments(page_id: str, limit: int = 25, cursor: Optional[str] = None):
    return _request("GET", f"/api/v2/pages/{page_id}/footer-comments", params={k: v for k, v in {"limit": limit, "cursor": cursor}.items() if v is not None})


@mcp.tool()
def create_footer_comment(page_id: str, body: Dict[str, Any]):
    return _request("POST", f"/api/v2/pages/{page_id}/footer-comments", json_body=body)


@mcp.tool()
def get_attachments(page_id: str, limit: int = 25, cursor: Optional[str] = None):
    return _request("GET", f"/api/v2/pages/{page_id}/attachments", params={k: v for k, v in {"limit": limit, "cursor": cursor}.items() if v is not None})


@mcp.tool()
def get_labels(page_id: str, limit: int = 25, cursor: Optional[str] = None):
    return _request("GET", f"/api/v2/pages/{page_id}/labels", params={k: v for k, v in {"limit": limit, "cursor": cursor}.items() if v is not None})


@mcp.tool()
def get_content_properties(page_id: str, limit: int = 25, cursor: Optional[str] = None):
    return _request("GET", f"/api/v2/pages/{page_id}/properties", params={k: v for k, v in {"limit": limit, "cursor": cursor}.items() if v is not None})


@mcp.tool()
def create_content_property(page_id: str, key: str, value: Any):
    return _request("POST", f"/api/v2/pages/{page_id}/properties", json_body={"key": key, "value": value})


@mcp.tool()
def get_blog_posts(space_id: str, limit: int = 25, cursor: Optional[str] = None):
    return _request("GET", "/api/v2/blogposts", params={k: v for k, v in {"space-id": space_id, "limit": limit, "cursor": cursor}.items() if v is not None})


@mcp.tool()
def create_blog_post(space_id: str, title: str, body: Dict[str, Any]):
    return _request("POST", "/api/v2/blogposts", json_body={"spaceId": space_id, "title": title, "body": body})


@mcp.tool()
def get_current_user():
    return _request("GET", "/api/v2/users/current")


@mcp.tool()
def get_user_by_account_ids(account_ids: list[str]):
    return _request("POST", "/api/v2/users-bulk", json_body={"accountIds": account_ids})


if __name__ == "__main__":
    mcp.run()
