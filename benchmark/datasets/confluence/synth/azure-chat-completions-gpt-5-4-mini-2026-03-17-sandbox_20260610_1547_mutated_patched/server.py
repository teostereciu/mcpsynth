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
    if not BASE_URL or not EMAIL or not TOKEN:
        return {"error": "Missing required environment variables"}
    try:
        resp = requests.request(
            method,
            f"{BASE_URL}{path}",
            headers=_auth_headers(),
            params=params,
            json=json_body,
            timeout=30,
        )
        if resp.status_code >= 400:
            try:
                return {"error": resp.json()}
            except Exception:
                return {"error": resp.text or f"HTTP {resp.status_code}"}
        if resp.status_code == 204:
            return {"ok": True}
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


@mcp.tool()
def list_spaces(ids: Optional[str] = None, keys: Optional[str] = None, type: Optional[str] = None, content_status: Optional[str] = None, labels: Optional[str] = None, sort: Optional[str] = None, include_icon: Optional[bool] = None, max_results: Optional[int] = None, cursor: Optional[str] = None) -> Any:
    params = {k: v for k, v in {"ids": ids, "keys": keys, "type": type, "status": content_status, "labels": labels, "sort": sort, "include-icon": include_icon, "limit": max_results, "cursor": cursor}.items() if v is not None}
    return _request("GET", "/api/v2/spaces", params=params)


@mcp.tool()
def get_space(id: str, include_icon: Optional[bool] = None, include_operations: Optional[bool] = None, include_properties: Optional[bool] = None, include_permissions: Optional[bool] = None, include_role_assignments: Optional[bool] = None, include_labels: Optional[bool] = None) -> Any:
    params = {k: v for k, v in {"include-icon": include_icon, "include-operations": include_operations, "include-properties": include_properties, "include-permissions": include_permissions, "include-role-assignments": include_role_assignments, "include-labels": include_labels}.items() if v is not None}
    return _request("GET", f"/api/v2/spaces/{id}", params=params)


@mcp.tool()
def create_space(name: str, key: Optional[str] = None, alias: Optional[str] = None, description: Optional[dict] = None, roleAssignments: Optional[list] = None, copySpaceAccessConfiguration: Optional[int] = None, createPrivateSpace: Optional[bool] = None, templateKey: Optional[str] = None) -> Any:
    body = {"name": name}
    for k, v in {"key": key, "alias": alias, "description": description, "roleAssignments": roleAssignments, "copySpaceAccessConfiguration": copySpaceAccessConfiguration, "createPrivateSpace": createPrivateSpace, "templateKey": templateKey}.items():
        if v is not None:
            body[k] = v
    return _request("POST", "/api/v2/spaces", json_body=body)


@mcp.tool()
def list_pages(id: Optional[str] = None, space_id: Optional[str] = None, sort: Optional[str] = None, content_status: Optional[str] = None, title: Optional[str] = None, body_format: Optional[str] = None, subtype: Optional[str] = None, cursor: Optional[str] = None, max_results: Optional[int] = None, label_id: Optional[str] = None) -> Any:
    params = {k: v for k, v in {"id": id, "space-id": space_id, "sort": sort, "status": content_status, "title": title, "body-format": body_format, "subtype": subtype, "cursor": cursor, "limit": max_results}.items() if v is not None}
    if label_id is not None:
        return _request("GET", f"/api/v2/labels/{label_id}/pages", params=params)
    return _request("GET", "/api/v2/pages", params=params)


@mcp.tool()
def get_page(id: str, body_format: Optional[str] = None, get_draft: Optional[bool] = None, content_status: Optional[str] = None, version: Optional[int] = None, include_labels: Optional[bool] = None, include_properties: Optional[bool] = None, include_operations: Optional[bool] = None, include_likes: Optional[bool] = None, include_versions: Optional[bool] = None, include_version: Optional[bool] = None) -> Any:
    params = {k: v for k, v in {"body-format": body_format, "get-draft": get_draft, "status": content_status, "version": version, "include-labels": include_labels, "include-properties": include_properties, "include-operations": include_operations, "include-likes": include_likes, "include-versions": include_versions, "include-version": include_version}.items() if v is not None}
    return _request("GET", f"/api/v2/pages/{id}", params=params)


@mcp.tool()
def create_page(spaceId: Optional[str] = None, title: Optional[str] = None, body: Optional[dict] = None, parentId: Optional[str] = None, content_status: Optional[str] = None, subtype: Optional[str] = None, embedded: Optional[bool] = None, private: Optional[bool] = None, root_level: Optional[bool] = None) -> Any:
    body_json = {k: v for k, v in {"spaceId": spaceId or SPACE_KEY, "title": title, "body": body, "parentId": parentId, "status": content_status, "subtype": subtype}.items() if v is not None}
    params = {k: v for k, v in {"embedded": embedded, "private": private, "root-level": root_level}.items() if v is not None}
    return _request("POST", "/api/v2/pages", params=params, json_body=body_json)


@mcp.tool()
def update_page(id: str, content_status: str, title: str, body: dict, version: dict, spaceId: Optional[str] = None, parentId: Optional[str] = None, ownerId: Optional[str] = None) -> Any:
    body_json = {"id": id, "status": content_status, "title": title, "body": body, "version": version}
    for k, v in {"spaceId": spaceId, "parentId": parentId, "ownerId": ownerId}.items():
        if v is not None:
            body_json[k] = v
    return _request("PUT", f"/api/v2/pages/{id}", json_body=body_json)


@mcp.tool()
def delete_page(id: str, purge: Optional[bool] = None, draft: Optional[bool] = None) -> Any:
    params = {k: v for k, v in {"purge": purge, "draft": draft}.items() if v is not None}
    return _request("DELETE", f"/api/v2/pages/{id}", params=params)


@mcp.tool()
def update_page_title(id: str, content_status: str, title: str) -> Any:
    return _request("PUT", f"/api/v2/pages/{id}/title", json_body={"status": content_status, "title": title})


@mcp.tool()
def list_attachments(id: Optional[str] = None, sort: Optional[str] = None, cursor: Optional[str] = None, content_status: Optional[str] = None, mediaType: Optional[str] = None, filename: Optional[str] = None, max_results: Optional[int] = None, container_type: Optional[str] = None) -> Any:
    params = {k: v for k, v in {"sort": sort, "cursor": cursor, "status": content_status, "mediaType": mediaType, "filename": filename, "limit": max_results}.items() if v is not None}
    if container_type == "blogpost":
        return _request("GET", f"/api/v2/blogposts/{id}/attachments", params=params)
    if container_type == "custom-content":
        return _request("GET", f"/api/v2/custom-content/{id}/attachments", params=params)
    if container_type == "label":
        return _request("GET", f"/api/v2/labels/{id}/attachments", params=params)
    if id is not None:
        return _request("GET", f"/api/v2/pages/{id}/attachments", params=params)
    return _request("GET", "/api/v2/attachments", params=params)


@mcp.tool()
def get_attachment(id: str, version: Optional[int] = None, include_labels: Optional[bool] = None, include_properties: Optional[bool] = None, include_operations: Optional[bool] = None, include_versions: Optional[bool] = None, include_version: Optional[bool] = None, include_collaborators: Optional[bool] = None) -> Any:
    params = {k: v for k, v in {"version": version, "include-labels": include_labels, "include-properties": include_properties, "include-operations": include_operations, "include-versions": include_versions, "include-version": include_version, "include-collaborators": include_collaborators}.items() if v is not None}
    return _request("GET", f"/api/v2/attachments/{id}", params=params)


@mcp.tool()
def delete_attachment(id: str, purge: Optional[bool] = None) -> Any:
    params = {k: v for k, v in {"purge": purge}.items() if v is not None}
    return _request("DELETE", f"/api/v2/attachments/{id}", params=params)


if __name__ == "__main__":
    mcp.run()
