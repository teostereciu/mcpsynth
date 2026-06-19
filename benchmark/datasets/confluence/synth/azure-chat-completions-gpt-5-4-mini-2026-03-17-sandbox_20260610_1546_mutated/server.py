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


def _auth_headers() -> Dict[str, str]:
    token = base64.b64encode(f"{EMAIL}:{API_TOKEN}".encode()).decode()
    return {"Authorization": f"Basic {token}", "Accept": "application/json"}


def _request(method: str, path: str, *, params: Optional[Dict[str, Any]] = None, json_body: Any = None) -> Any:
    if not BASE_URL:
        return {"error": "CONFLUENCE_BASE_URL is not set"}
    try:
        resp = requests.request(
            method,
            f"{BASE_URL}{path}",
            headers=_auth_headers(),
            params=params,
            json=json_body,
            timeout=60,
        )
        if resp.status_code >= 400:
            try:
                return {"error": resp.json()}
            except Exception:
                return {"error": resp.text}
        if resp.status_code == 204:
            return {"ok": True}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def list_tools() -> Dict[str, Any]:
    return {"tools": ["get_page", "create_page", "update_page", "delete_page", "get_current_user"]}


@mcp.tool()
def get_page(id: str) -> Any:
    return _request("GET", f"/api/v2/pages/{id}")


@mcp.tool()
def create_page(title: str, body: str, space_id: Optional[str] = None, parent_id: Optional[str] = None) -> Any:
    payload: Dict[str, Any] = {"title": title, "spaceId": space_id or SPACE_KEY, "body": {"representation": "storage", "value": body}}
    if parent_id:
        payload["parentId"] = parent_id
    return _request("POST", "/api/v2/pages", json_body=payload)


@mcp.tool()
def update_page(id: str, title: str, body: str, content_status: str = "current", version_number: Optional[int] = None) -> Any:
    payload: Dict[str, Any] = {"id": id, "content_status": content_status, "title": title, "body": {"representation": "storage", "value": body}, "version": {"number": version_number or 1}}
    return _request("PUT", f"/api/v2/pages/{id}", json_body=payload)


@mcp.tool()
def delete_page(id: str) -> Any:
    return _request("DELETE", f"/api/v2/pages/{id}")


@mcp.tool()
def get_current_user() -> Any:
    return _request("GET", "/rest/api/user/current")


if __name__ == "__main__":
    mcp.run()
