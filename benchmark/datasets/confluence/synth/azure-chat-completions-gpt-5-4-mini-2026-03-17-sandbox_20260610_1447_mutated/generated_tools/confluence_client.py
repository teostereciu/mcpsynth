import base64
import json
import os
from typing import Any, Dict, Optional
from urllib.parse import urlencode

import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("confluence-cloud")


def _base_url() -> str:
    return os.environ["CONFLUENCE_BASE_URL"].rstrip("/")


def _auth_headers() -> Dict[str, str]:
    email = os.environ.get("JIRA_EMAIL", "")
    token = os.environ.get("JIRA_API_TOKEN", "")
    if email and token:
        raw = f"{email}:{token}".encode()
        return {"Authorization": f"Basic {base64.b64encode(raw).decode()}"}
    return {}


def _request(method: str, path: str, *, params: Optional[Dict[str, Any]] = None, json_body: Any = None) -> Any:
    url = f"{_base_url()}{path}"
    headers = {"Accept": "application/json", **_auth_headers()}
    if json_body is not None:
        headers["Content-Type"] = "application/json"
    with httpx.Client(timeout=60.0) as client:
        resp = client.request(method, url, params=params, json=json_body, headers=headers)
        if resp.status_code == 204:
            return {"status_code": resp.status_code, "ok": True}
        try:
            data = resp.json()
        except Exception:
            data = resp.text
        return {"status_code": resp.status_code, "ok": resp.is_success, "data": data}


def _query(**kwargs: Any) -> Dict[str, Any]:
    return {k.replace("_", "-"): v for k, v in kwargs.items() if v is not None}


@mcp.tool()
def confluence_get_pages(space_id: Optional[str] = None, title: Optional[str] = None, cursor: Optional[str] = None, max_results: Optional[int] = None) -> Any:
    return _request("GET", "/api/v2/pages", params=_query(space_id=space_id, title=title, cursor=cursor, max_results=max_results))


@mcp.tool()
def confluence_get_page(page_id: str, include_labels: Optional[bool] = None, include_properties: Optional[bool] = None, include_operations: Optional[bool] = None, include_likes: Optional[bool] = None, include_versions: Optional[bool] = None) -> Any:
    return _request("GET", f"/api/v2/pages/{page_id}", params=_query(include_labels=include_labels, include_properties=include_properties, include_operations=include_operations, include_likes=include_likes, include_versions=include_versions))


@mcp.tool()
def confluence_create_page(space_id: str, title: str, body: Dict[str, Any], parent_id: Optional[str] = None, content_status: Optional[str] = None, subtype: Optional[str] = None) -> Any:
    payload = {"spaceId": space_id, "title": title, "body": body}
    if parent_id is not None:
        payload["parentId"] = parent_id
    if content_status is not None:
        payload["content_status"] = content_status
    if subtype is not None:
        payload["subtype"] = subtype
    return _request("POST", "/api/v2/pages", json_body=payload)


@mcp.tool()
def confluence_update_page(page_id: str, title: str, body: Dict[str, Any], version: Dict[str, Any], content_status: str, space_id: Optional[str] = None, parent_id: Optional[str] = None, owner_id: Optional[str] = None) -> Any:
    payload = {"id": str(page_id), "title": title, "body": body, "version": version, "content_status": content_status}
    if space_id is not None:
        payload["spaceId"] = space_id
    if parent_id is not None:
        payload["parentId"] = parent_id
    if owner_id is not None:
        payload["ownerId"] = owner_id
    return _request("PUT", f"/api/v2/pages/{page_id}", json_body=payload)


@mcp.tool()
def confluence_delete_page(page_id: str, purge: Optional[bool] = None, draft: Optional[bool] = None) -> Any:
    return _request("DELETE", f"/api/v2/pages/{page_id}", params=_query(purge=purge, draft=draft))


@mcp.tool()
def confluence_get_spaces(ids: Optional[list[int]] = None, keys: Optional[list[str]] = None, cursor: Optional[str] = None, max_results: Optional[int] = None) -> Any:
    return _request("GET", "/api/v2/spaces", params=_query(ids=ids, keys=keys, cursor=cursor, max_results=max_results))


@mcp.tool()
def confluence_create_space(name: str, key: Optional[str] = None, alias: Optional[str] = None, description: Optional[Dict[str, Any]] = None, create_private_space: Optional[bool] = None, template_key: Optional[str] = None) -> Any:
    payload: Dict[str, Any] = {"name": name}
    if key is not None:
        payload["key"] = key
    if alias is not None:
        payload["alias"] = alias
    if description is not None:
        payload["description"] = description
    if create_private_space is not None:
        payload["createPrivateSpace"] = create_private_space
    if template_key is not None:
        payload["templateKey"] = template_key
    return _request("POST", "/api/v2/spaces", json_body=payload)


@mcp.tool()
def confluence_get_space(space_id: str, include_icon: Optional[bool] = None, include_operations: Optional[bool] = None, include_properties: Optional[bool] = None, include_permissions: Optional[bool] = None, include_role_assignments: Optional[bool] = None, include_labels: Optional[bool] = None) -> Any:
    return _request("GET", f"/api/v2/spaces/{space_id}", params=_query(include_icon=include_icon, include_operations=include_operations, include_properties=include_properties, include_permissions=include_permissions, include_role_assignments=include_role_assignments, include_labels=include_labels))


@mcp.tool()
def confluence_get_blogposts(space_id: Optional[str] = None, title: Optional[str] = None, cursor: Optional[str] = None, max_results: Optional[int] = None) -> Any:
    return _request("GET", "/api/v2/blogposts", params=_query(space_id=space_id, title=title, cursor=cursor, max_results=max_results))


@mcp.tool()
def confluence_create_blogpost(space_id: str, title: str, body: Dict[str, Any], content_status: Optional[str] = None, created_at: Optional[str] = None, private: Optional[bool] = None) -> Any:
    payload: Dict[str, Any] = {"spaceId": space_id, "title": title, "body": body}
    if content_status is not None:
        payload["content_status"] = content_status
    if created_at is not None:
        payload["createdAt"] = created_at
    return _request("POST", "/api/v2/blogposts", params=_query(private=private), json_body=payload)


@mcp.tool()
def confluence_get_blogpost(blogpost_id: str, include_labels: Optional[bool] = None, include_properties: Optional[bool] = None, include_operations: Optional[bool] = None, include_likes: Optional[bool] = None, include_versions: Optional[bool] = None) -> Any:
    return _request("GET", f"/api/v2/blogposts/{blogpost_id}", params=_query(include_labels=include_labels, include_properties=include_properties, include_operations=include_operations, include_likes=include_likes, include_versions=include_versions))


@mcp.tool()
def confluence_get_labels(label_id: Optional[str] = None) -> Any:
    return _request("GET", "/api/v2/labels", params=_query(id=label_id))


@mcp.tool()
def confluence_get_pages_for_label(label_id: str, space_id: Optional[list[int]] = None, cursor: Optional[str] = None, max_results: Optional[int] = None) -> Any:
    return _request("GET", f"/api/v2/labels/{label_id}/pages", params=_query(space_id=space_id, cursor=cursor, max_results=max_results))


@mcp.tool()
def confluence_get_blogposts_for_label(label_id: str, space_id: Optional[list[int]] = None, cursor: Optional[str] = None, max_results: Optional[int] = None) -> Any:
    return _request("GET", f"/api/v2/labels/{label_id}/blogposts", params=_query(space_id=space_id, cursor=cursor, max_results=max_results))


@mcp.tool()
def confluence_get_attachments(page_id: Optional[str] = None, blogpost_id: Optional[str] = None, cursor: Optional[str] = None, max_results: Optional[int] = None) -> Any:
    if page_id:
        return _request("GET", f"/api/v2/pages/{page_id}/attachments", params=_query(cursor=cursor, max_results=max_results))
    if blogpost_id:
        return _request("GET", f"/api/v2/blogposts/{blogpost_id}/attachments", params=_query(cursor=cursor, max_results=max_results))
    return _request("GET", "/api/v2/attachments", params=_query(cursor=cursor, max_results=max_results))
