from __future__ import annotations

import base64
import json
import os
from typing import Any, Dict, Optional

import requests
from fastmcp import FastMCP

mcp = FastMCP("confluence-cloud")

BASE_URL = os.getenv("CONFLUENCE_BASE_URL", "").rstrip("/")
EMAIL = os.getenv("JIRA_EMAIL", "")
API_TOKEN = os.getenv("JIRA_API_TOKEN", "")
SPACE_KEY = os.getenv("CONFLUENCE_SPACE_KEY", "")


def _auth_header() -> Dict[str, str]:
    token = base64.b64encode(f"{EMAIL}:{API_TOKEN}".encode()).decode()
    return {"Authorization": f"Basic {token}"}


def _request(method: str, path: str, *, params: Optional[dict] = None, json_body: Any = None, headers: Optional[dict] = None, files: Any = None) -> Any:
    if not BASE_URL:
        return {"error": "CONFLUENCE_BASE_URL is not set"}
    url = f"{BASE_URL}{path}"
    req_headers = {**_auth_header(), **(headers or {})}
    try:
        resp = requests.request(method, url, params=params, json=json_body, headers=req_headers, files=files, timeout=60)
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
            return resp.text
    except requests.RequestException as e:
        return {"error": str(e)}


@mcp.tool()
def list_spaces(limit: int = 25, cursor: Optional[str] = None):
    return _request("GET", "/api/v2/spaces", params={k: v for k, v in {"limit": limit, "cursor": cursor}.items() if v is not None})


@mcp.tool()
def get_space(space_id: str):
    return _request("GET", f"/api/v2/spaces/{space_id}")


@mcp.tool()
def create_space(key: str, name: str, description: Optional[str] = None):
    body = {"key": key, "name": name}
    if description is not None:
        body["description"] = {"plain": {"value": description, "representation": "plain"}}
    return _request("POST", "/api/v2/spaces", json_body=body)


@mcp.tool()
def delete_space(space_id: str):
    return _request("DELETE", f"/api/v2/spaces/{space_id}")


@mcp.tool()
def get_current_user():
    return _request("GET", "/rest/api/user/current")


@mcp.tool()
def get_user_by_account_id(account_id: str):
    return _request("GET", "/rest/api/user", params={"accountId": account_id})


@mcp.tool()
def search_content(cql: str, limit: int = 25, start: int = 0):
    return _request("GET", "/rest/api/content/search", params={"cql": cql, "limit": limit, "start": start})


@mcp.tool()
def get_page(page_id: str, version: Optional[int] = None):
    params = {"expand": "body.storage,version,space,ancestors"}
    if version is not None:
        params["version"] = version
    return _request("GET", f"/rest/api/content/{page_id}", params=params)


@mcp.tool()
def create_page(space_key: Optional[str], title: str, body: str, parent_id: Optional[str] = None):
    body_obj = {"storage": {"value": body, "representation": "storage"}}
    payload = {"type": "page", "title": title, "space": {"key": space_key or SPACE_KEY}, "body": {"storage": body_obj["storage"]}}
    if parent_id:
        payload["ancestors"] = [{"id": parent_id}]
    return _request("POST", "/rest/api/content", json_body=payload)


@mcp.tool()
def update_page(page_id: str, title: str, body: str, version: int):
    payload = {"id": page_id, "type": "page", "title": title, "version": {"number": version}, "body": {"storage": {"value": body, "representation": "storage"}}}
    return _request("PUT", f"/rest/api/content/{page_id}", json_body=payload)


@mcp.tool()
def delete_page(page_id: str):
    return _request("DELETE", f"/rest/api/content/{page_id}")


@mcp.tool()
def get_page_children(page_id: str, limit: int = 25):
    return _request("GET", f"/rest/api/content/{page_id}/child/page", params={"limit": limit})


@mcp.tool()
def get_page_ancestors(page_id: str):
    return _request("GET", f"/rest/api/content/{page_id}/ancestors")


@mcp.tool()
def move_page(page_id: str, position: str, target_id: Optional[str] = None):
    params = {"position": position}
    if target_id:
        params["targetId"] = target_id
    return _request("PUT", f"/rest/api/content/{page_id}/move/{position}", params=params)


@mcp.tool()
def list_labels(page_id: str):
    return _request("GET", f"/rest/api/content/{page_id}/label")


@mcp.tool()
def add_label(page_id: str, label: str):
    return _request("POST", f"/rest/api/content/{page_id}/label", json_body=[{"prefix": "global", "name": label}])


@mcp.tool()
def remove_label(page_id: str, label: str):
    return _request("DELETE", f"/rest/api/content/{page_id}/label/{label}")


@mcp.tool()
def list_attachments(page_id: str):
    return _request("GET", f"/rest/api/content/{page_id}/child/attachment")


@mcp.tool()
def upload_attachment(page_id: str, filename: str, content: str):
    files = {"file": (filename, content.encode())}
    return _request("POST", f"/rest/api/content/{page_id}/child/attachment", headers={"X-Atlassian-Token": "no-check"}, files=files)


@mcp.tool()
def get_attachment(attachment_id: str):
    return _request("GET", f"/rest/api/content/{attachment_id}")


@mcp.tool()
def create_comment(page_id: str, body: str, parent_comment_id: Optional[str] = None):
    payload = {"type": "comment", "container": {"id": page_id, "type": "page"}, "body": {"storage": {"value": body, "representation": "storage"}}}
    if parent_comment_id:
        payload["ancestors"] = [{"id": parent_comment_id}]
    return _request("POST", "/rest/api/content", json_body=payload)


@mcp.tool()
def list_comments(page_id: str, limit: int = 25):
    return _request("GET", f"/rest/api/content/{page_id}/child/comment", params={"limit": limit})


@mcp.tool()
def list_page_versions(page_id: str):
    return _request("GET", f"/rest/api/content/{page_id}/version")


@mcp.tool()
def get_page_version(page_id: str, version_number: int):
    return _request("GET", f"/rest/api/content/{page_id}/version/{version_number}")


@mcp.tool()
def restore_page_version(page_id: str, version_number: int):
    return _request("POST", f"/rest/api/content/{page_id}/version", json_body={"number": version_number})


@mcp.tool()
def get_content_property(page_id: str, key: str):
    return _request("GET", f"/rest/api/content/{page_id}/property/{key}")


@mcp.tool()
def set_content_property(page_id: str, key: str, value: Any):
    return _request("PUT", f"/rest/api/content/{page_id}/property/{key}", json_body={"key": key, "value": value})


@mcp.tool()
def create_blog_post(space_key: Optional[str], title: str, body: str, publish_date: Optional[str] = None):
    payload = {"type": "blogpost", "title": title, "space": {"key": space_key or SPACE_KEY}, "body": {"storage": {"value": body, "representation": "storage"}}}
    if publish_date:
        payload["version"] = {"when": publish_date}
    return _request("POST", "/rest/api/content", json_body=payload)


@mcp.tool()
def update_blog_post(post_id: str, title: str, body: str, version: int):
    payload = {"id": post_id, "type": "blogpost", "title": title, "version": {"number": version}, "body": {"storage": {"value": body, "representation": "storage"}}}
    return _request("PUT", f"/rest/api/content/{post_id}", json_body=payload)


@mcp.tool()
def delete_blog_post(post_id: str):
    return _request("DELETE", f"/rest/api/content/{post_id}")


if __name__ == "__main__":
    mcp.run()
