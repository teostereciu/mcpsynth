import os
import json
from typing import Any, Dict, Optional

import httpx
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

load_dotenv()

mcp = FastMCP("confluence-cloud")


def _get_base_url() -> str:
    base = os.getenv("CONFLUENCE_BASE_URL", "").strip()
    if not base:
        raise ValueError(
            "CONFLUENCE_BASE_URL is required, e.g. https://your-domain.atlassian.net"
        )
    return base.rstrip("/")


def _get_auth_headers() -> Dict[str, str]:
    # Prefer OAuth bearer token if provided.
    token = os.getenv("CONFLUENCE_API_TOKEN", "").strip()
    email = os.getenv("CONFLUENCE_EMAIL", "").strip()
    bearer = os.getenv("CONFLUENCE_BEARER_TOKEN", "").strip()

    headers = {
        "Accept": "application/json",
    }

    if bearer:
        headers["Authorization"] = f"Bearer {bearer}"
        return headers

    if token and email:
        import base64

        basic = base64.b64encode(f"{email}:{token}".encode("utf-8")).decode("utf-8")
        headers["Authorization"] = f"Basic {basic}"
        return headers

    raise ValueError(
        "Authentication not configured. Set CONFLUENCE_BEARER_TOKEN or (CONFLUENCE_EMAIL and CONFLUENCE_API_TOKEN)."
    )


async def _request(
    method: str,
    path: str,
    *,
    query: Optional[Dict[str, Any]] = None,
    json_body: Optional[Any] = None,
    headers: Optional[Dict[str, str]] = None,
    timeout_s: float = 60.0,
) -> Any:
    base = _get_base_url()
    url = f"{base}{path}"

    req_headers = _get_auth_headers()
    if headers:
        req_headers.update({k: v for k, v in headers.items() if v is not None})

    # httpx will encode list query params if provided as list values.
    async with httpx.AsyncClient(timeout=timeout_s) as client:
        resp = await client.request(
            method.upper(),
            url,
            params=query,
            json=json_body,
            headers=req_headers,
        )

    # Confluence often returns empty body for 204.
    if resp.status_code == 204:
        return {"status": 204}

    content_type = resp.headers.get("content-type", "")
    if "application/json" in content_type:
        data = resp.json()
    else:
        data = {"text": resp.text}

    if resp.is_error:
        raise RuntimeError(
            json.dumps(
                {
                    "error": True,
                    "status": resp.status_code,
                    "url": url,
                    "response": data,
                },
                ensure_ascii=False,
            )
        )

    return data


@mcp.tool()
async def confluence_request(
    method: str,
    path: str,
    query: Optional[Dict[str, Any]] = None,
    body: Optional[Any] = None,
    headers: Optional[Dict[str, str]] = None,
) -> Any:
    """Generic Confluence Cloud REST request.

    Use this when a dedicated tool is not available.

    Args:
      method: HTTP method (GET, POST, PUT, DELETE)
      path: Full path starting with /wiki/rest/api (v1) or /wiki/api/v2 (v2)
      query: Query parameters dict. Use list values for repeated params (e.g. include=[...]).
      body: JSON-serializable request body.
      headers: Additional headers.
    """
    if not path.startswith("/"):
        path = "/" + path
    return await _request(method, path, query=query, json_body=body, headers=headers)


# -------------------------
# v2: Spaces
# -------------------------

@mcp.tool()
async def confluence_v2_get_spaces(
    limit: Optional[int] = None,
    cursor: Optional[str] = None,
    keys: Optional[str] = None,
    ids: Optional[str] = None,
    type: Optional[str] = None,
    status: Optional[str] = None,
    sort: Optional[str] = None,
) -> Any:
    """GET /wiki/api/v2/spaces"""
    query: Dict[str, Any] = {}
    for k, v in {
        "limit": limit,
        "cursor": cursor,
        "keys": keys,
        "ids": ids,
        "type": type,
        "status": status,
        "sort": sort,
    }.items():
        if v is not None:
            query[k] = v
    return await _request("GET", "/wiki/api/v2/spaces", query=query)


@mcp.tool()
async def confluence_v2_post_spaces(body: Dict[str, Any]) -> Any:
    """POST /wiki/api/v2/spaces"""
    return await _request("POST", "/wiki/api/v2/spaces", json_body=body)


@mcp.tool()
async def confluence_v2_get_space_by_id(id: int) -> Any:
    """GET /wiki/api/v2/spaces/{id}"""
    return await _request("GET", f"/wiki/api/v2/spaces/{id}")


# -------------------------
# v2: Pages
# -------------------------

@mcp.tool()
async def confluence_v2_get_pages(
    limit: Optional[int] = None,
    cursor: Optional[str] = None,
    space_id: Optional[int] = None,
    title: Optional[str] = None,
    status: Optional[str] = None,
    parent_id: Optional[int] = None,
    sort: Optional[str] = None,
) -> Any:
    """GET /wiki/api/v2/pages"""
    query: Dict[str, Any] = {}
    for k, v in {
        "limit": limit,
        "cursor": cursor,
        "space-id": space_id,
        "title": title,
        "status": status,
        "parent-id": parent_id,
        "sort": sort,
    }.items():
        if v is not None:
            query[k] = v
    return await _request("GET", "/wiki/api/v2/pages", query=query)


@mcp.tool()
async def confluence_v2_post_pages(body: Dict[str, Any]) -> Any:
    """POST /wiki/api/v2/pages"""
    return await _request("POST", "/wiki/api/v2/pages", json_body=body)


@mcp.tool()
async def confluence_v2_get_page_by_id(id: int) -> Any:
    """GET /wiki/api/v2/pages/{id}"""
    return await _request("GET", f"/wiki/api/v2/pages/{id}")


# -------------------------
# v2: Blog posts
# -------------------------

@mcp.tool()
async def confluence_v2_get_blogposts(
    limit: Optional[int] = None,
    cursor: Optional[str] = None,
    space_id: Optional[int] = None,
    status: Optional[str] = None,
    sort: Optional[str] = None,
) -> Any:
    """GET /wiki/api/v2/blogposts"""
    query: Dict[str, Any] = {}
    for k, v in {
        "limit": limit,
        "cursor": cursor,
        "space-id": space_id,
        "status": status,
        "sort": sort,
    }.items():
        if v is not None:
            query[k] = v
    return await _request("GET", "/wiki/api/v2/blogposts", query=query)


@mcp.tool()
async def confluence_v2_post_blogposts(body: Dict[str, Any]) -> Any:
    """POST /wiki/api/v2/blogposts"""
    return await _request("POST", "/wiki/api/v2/blogposts", json_body=body)


# -------------------------
# v2: Attachments
# -------------------------

@mcp.tool()
async def confluence_v2_get_attachments(
    limit: Optional[int] = None,
    cursor: Optional[str] = None,
    media_type: Optional[str] = None,
    filename: Optional[str] = None,
    status: Optional[str] = None,
    sort: Optional[str] = None,
) -> Any:
    """GET /wiki/api/v2/attachments"""
    query: Dict[str, Any] = {}
    for k, v in {
        "limit": limit,
        "cursor": cursor,
        "media-type": media_type,
        "filename": filename,
        "status": status,
        "sort": sort,
    }.items():
        if v is not None:
            query[k] = v
    return await _request("GET", "/wiki/api/v2/attachments", query=query)


@mcp.tool()
async def confluence_v2_get_attachment_by_id(id: int) -> Any:
    """GET /wiki/api/v2/attachments/{id}"""
    return await _request("GET", f"/wiki/api/v2/attachments/{id}")


# -------------------------
# v2: Comments
# -------------------------

@mcp.tool()
async def confluence_v2_get_comments(
    limit: Optional[int] = None,
    cursor: Optional[str] = None,
    body_format: Optional[str] = None,
    sort: Optional[str] = None,
) -> Any:
    """GET /wiki/api/v2/comments"""
    query: Dict[str, Any] = {}
    for k, v in {
        "limit": limit,
        "cursor": cursor,
        "body-format": body_format,
        "sort": sort,
    }.items():
        if v is not None:
            query[k] = v
    return await _request("GET", "/wiki/api/v2/comments", query=query)


# -------------------------
# v1: Search
# -------------------------

@mcp.tool()
async def confluence_v1_search(
    cql: str,
    limit: Optional[int] = None,
    start: Optional[int] = None,
    expand: Optional[str] = None,
    include_archived_spaces: Optional[bool] = None,
) -> Any:
    """GET /wiki/rest/api/search (CQL search)."""
    query: Dict[str, Any] = {"cql": cql}
    if limit is not None:
        query["limit"] = limit
    if start is not None:
        query["start"] = start
    if expand is not None:
        query["expand"] = expand
    if include_archived_spaces is not None:
        query["includeArchivedSpaces"] = str(include_archived_spaces).lower()
    return await _request("GET", "/wiki/rest/api/search", query=query)


# -------------------------
# v1: Content labels
# -------------------------

@mcp.tool()
async def confluence_v1_add_labels_to_content(id: str, labels: Any) -> Any:
    """POST /wiki/rest/api/content/{id}/label"""
    return await _request(
        "POST", f"/wiki/rest/api/content/{id}/label", json_body=labels
    )


@mcp.tool()
async def confluence_v1_remove_label_from_content_query(id: str, name: str) -> Any:
    """DELETE /wiki/rest/api/content/{id}/label?name={name}"""
    return await _request(
        "DELETE", f"/wiki/rest/api/content/{id}/label", query={"name": name}
    )


@mcp.tool()
async def confluence_v1_remove_label_from_content(id: str, label: str) -> Any:
    """DELETE /wiki/rest/api/content/{id}/label/{label}"""
    return await _request("DELETE", f"/wiki/rest/api/content/{id}/label/{label}")


# -------------------------
# v1: Content versions
# -------------------------

@mcp.tool()
async def confluence_v1_restore_content_version(
    id: str,
    operation_key: str,
    params: Dict[str, Any],
    include: Optional[list[str]] = None,
) -> Any:
    """POST /wiki/rest/api/content/{id}/version"""
    query: Dict[str, Any] = {}
    if include is not None:
        query["include"] = include
    body = {"operationKey": operation_key, "params": params}
    return await _request(
        "POST", f"/wiki/rest/api/content/{id}/version", query=query, json_body=body
    )


# -------------------------
# v1: Users
# -------------------------

@mcp.tool()
async def confluence_v1_get_user(account_id: str, include: Optional[list[str]] = None) -> Any:
    """GET /wiki/rest/api/user"""
    query: Dict[str, Any] = {"accountId": account_id}
    if include is not None:
        query["include"] = include
    return await _request("GET", "/wiki/rest/api/user", query=query)


@mcp.tool()
async def confluence_v1_get_current_user(include: Optional[list[str]] = None) -> Any:
    """GET /wiki/rest/api/user/current"""
    query: Dict[str, Any] = {}
    if include is not None:
        query["include"] = include
    return await _request("GET", "/wiki/rest/api/user/current", query=query)


@mcp.tool()
async def confluence_v1_get_anonymous_user(include: Optional[list[str]] = None) -> Any:
    """GET /wiki/rest/api/user/anonymous"""
    query: Dict[str, Any] = {}
    if include is not None:
        query["include"] = include
    return await _request("GET", "/wiki/rest/api/user/anonymous", query=query)


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
