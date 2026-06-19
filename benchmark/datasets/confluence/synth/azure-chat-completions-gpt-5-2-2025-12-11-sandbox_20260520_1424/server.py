import os
import json
import re
from typing import Any, Dict, Optional

import httpx
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

load_dotenv()

mcp = FastMCP("confluence-cloud")


def _env(name: str, default: Optional[str] = None) -> Optional[str]:
    v = os.getenv(name)
    return v if v not in (None, "") else default


def _get_base_url() -> str:
    # Expect full site base, e.g. https://your-domain.atlassian.net
    base = _env("CONFLUENCE_BASE_URL") or _env("ATLASSIAN_BASE_URL")
    if not base:
        raise ValueError(
            "Missing CONFLUENCE_BASE_URL (e.g. https://your-domain.atlassian.net)"
        )
    return base.rstrip("/")


def _get_auth_headers() -> Dict[str, str]:
    # Prefer OAuth bearer token
    token = _env("CONFLUENCE_API_TOKEN") or _env("ATLASSIAN_API_TOKEN")
    email = _env("CONFLUENCE_EMAIL") or _env("ATLASSIAN_EMAIL")
    bearer = _env("CONFLUENCE_BEARER_TOKEN") or _env("ATLASSIAN_BEARER_TOKEN")

    headers: Dict[str, str] = {
        "Accept": "application/json",
        "User-Agent": "mcp-confluence-cloud/1.0",
    }

    if bearer:
        headers["Authorization"] = f"Bearer {bearer}"
        return headers

    if token and email:
        import base64

        basic = base64.b64encode(f"{email}:{token}".encode("utf-8")).decode("ascii")
        headers["Authorization"] = f"Basic {basic}"
        return headers

    raise ValueError(
        "Missing auth. Set CONFLUENCE_BEARER_TOKEN (OAuth) OR CONFLUENCE_EMAIL + CONFLUENCE_API_TOKEN (API token)."
    )


def _normalize_path(path: str) -> str:
    if not path:
        raise ValueError("path is required")
    if not path.startswith("/"):
        path = "/" + path
    # Allow callers to pass full /wiki/... paths; otherwise assume /wiki prefix.
    if not path.startswith("/wiki/"):
        path = "/wiki" + path
    return path


def _coerce_query_params(params: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    if not params:
        return {}
    out: Dict[str, Any] = {}
    for k, v in params.items():
        if v is None:
            continue
        # httpx supports list values for repeated query params
        out[k] = v
    return out


async def _request(
    method: str,
    path: str,
    query: Optional[Dict[str, Any]] = None,
    json_body: Any = None,
    headers: Optional[Dict[str, str]] = None,
    timeout_s: float = 60.0,
) -> Dict[str, Any]:
    base = _get_base_url()
    url = base + _normalize_path(path)

    req_headers = _get_auth_headers()
    if headers:
        req_headers.update({k: v for k, v in headers.items() if v is not None})

    async with httpx.AsyncClient(timeout=timeout_s) as client:
        resp = await client.request(
            method.upper(),
            url,
            params=_coerce_query_params(query),
            json=json_body,
            headers=req_headers,
        )

    content_type = resp.headers.get("content-type", "")
    is_json = "application/json" in content_type

    if resp.status_code >= 400:
        detail: Any
        if is_json:
            try:
                detail = resp.json()
            except Exception:
                detail = resp.text
        else:
            detail = resp.text
        raise RuntimeError(
            json.dumps(
                {
                    "error": "Confluence API request failed",
                    "status": resp.status_code,
                    "method": method.upper(),
                    "url": url,
                    "detail": detail,
                },
                ensure_ascii=False,
            )
        )

    if resp.status_code == 204:
        return {"status": 204, "headers": dict(resp.headers), "data": None}

    if is_json:
        return {"status": resp.status_code, "headers": dict(resp.headers), "data": resp.json()}

    return {"status": resp.status_code, "headers": dict(resp.headers), "data": resp.text}


@mcp.tool()
async def confluence_request(
    method: str,
    path: str,
    query: Optional[Dict[str, Any]] = None,
    json_body: Any = None,
    headers: Optional[Dict[str, str]] = None,
    timeout_s: float = 60.0,
) -> Dict[str, Any]:
    """Generic Confluence Cloud REST request.

    - Base URL: CONFLUENCE_BASE_URL (e.g. https://your-domain.atlassian.net)
    - Path: either full '/wiki/rest/api/...' or '/api/v2/...' etc. If it doesn't start with '/wiki/', '/wiki' is prepended.

    Authentication:
    - OAuth: CONFLUENCE_BEARER_TOKEN
    - OR API token: CONFLUENCE_EMAIL + CONFLUENCE_API_TOKEN

    Returns: {status, headers, data}
    """
    return await _request(method, path, query=query, json_body=json_body, headers=headers, timeout_s=timeout_s)


# High-level convenience tools (cover common real-world tasks)

@mcp.tool()
async def confluence_search_cql(
    cql: str,
    limit: int = 25,
    start: int = 0,
    expand: Optional[str] = None,
) -> Dict[str, Any]:
    """Search Confluence using CQL (v1).

    Endpoint: GET /wiki/rest/api/search
    Query params: cql, limit, start, expand
    """
    q: Dict[str, Any] = {"cql": cql, "limit": limit, "start": start}
    if expand:
        q["expand"] = expand
    return await _request("GET", "/wiki/rest/api/search", query=q)


@mcp.tool()
async def confluence_get_spaces_v2(
    limit: int = 25,
    cursor: Optional[str] = None,
    keys: Optional[list[str]] = None,
    ids: Optional[list[int]] = None,
    type: Optional[str] = None,
    status: Optional[list[str]] = None,
) -> Dict[str, Any]:
    """List spaces (v2).

    Endpoint: GET /wiki/api/v2/spaces
    """
    q: Dict[str, Any] = {"limit": limit}
    if cursor:
        q["cursor"] = cursor
    if keys:
        q["keys"] = keys
    if ids:
        q["id"] = ids
    if type:
        q["type"] = type
    if status:
        q["status"] = status
    return await _request("GET", "/wiki/api/v2/spaces", query=q)


@mcp.tool()
async def confluence_get_pages_v2(
    limit: int = 25,
    cursor: Optional[str] = None,
    space_id: Optional[list[int]] = None,
    title: Optional[str] = None,
    status: Optional[list[str]] = None,
    body_format: Optional[str] = None,
    sort: Optional[str] = None,
) -> Dict[str, Any]:
    """List pages (v2).

    Endpoint: GET /wiki/api/v2/pages
    """
    q: Dict[str, Any] = {"limit": limit}
    if cursor:
        q["cursor"] = cursor
    if space_id:
        q["space-id"] = space_id
    if title:
        q["title"] = title
    if status:
        q["status"] = status
    if body_format:
        q["body-format"] = body_format
    if sort:
        q["sort"] = sort
    return await _request("GET", "/wiki/api/v2/pages", query=q)


@mcp.tool()
async def confluence_get_page_by_id_v2(
    id: int,
    body_format: Optional[str] = None,
    get_draft: Optional[bool] = None,
    status: Optional[list[str]] = None,
    version: Optional[int] = None,
    include_labels: Optional[bool] = None,
    include_properties: Optional[bool] = None,
    include_operations: Optional[bool] = None,
    include_likes: Optional[bool] = None,
    include_versions: Optional[bool] = None,
) -> Dict[str, Any]:
    """Get a page by id (v2).

    Endpoint: GET /wiki/api/v2/pages/{id}
    """
    q: Dict[str, Any] = {}
    if body_format is not None:
        q["body-format"] = body_format
    if get_draft is not None:
        q["get-draft"] = get_draft
    if status is not None:
        q["status"] = status
    if version is not None:
        q["version"] = version
    if include_labels is not None:
        q["include-labels"] = include_labels
    if include_properties is not None:
        q["include-properties"] = include_properties
    if include_operations is not None:
        q["include-operations"] = include_operations
    if include_likes is not None:
        q["include-likes"] = include_likes
    if include_versions is not None:
        q["include-versions"] = include_versions
    return await _request("GET", f"/wiki/api/v2/pages/{id}", query=q)


@mcp.tool()
async def confluence_create_page_v2(
    spaceId: str,
    title: str,
    body: Dict[str, Any],
    status: str = "current",
    parentId: Optional[str] = None,
) -> Dict[str, Any]:
    """Create a page (v2).

    Endpoint: POST /wiki/api/v2/pages

    body should be like: {"representation":"storage","value":"<p>..</p>"}
    """
    payload: Dict[str, Any] = {"spaceId": spaceId, "status": status, "title": title, "body": body}
    if parentId:
        payload["parentId"] = parentId
    return await _request("POST", "/wiki/api/v2/pages", json_body=payload)


@mcp.tool()
async def confluence_update_page_v2(
    id: int,
    title: str,
    body: Dict[str, Any],
    version_number: int,
    version_message: Optional[str] = None,
    status: str = "current",
    spaceId: Optional[str] = None,
) -> Dict[str, Any]:
    """Update a page (v2).

    Endpoint: PUT /wiki/api/v2/pages/{id}

    Confluence requires incrementing version.number.
    """
    payload: Dict[str, Any] = {
        "id": str(id),
        "status": status,
        "title": title,
        "body": body,
        "version": {"number": version_number, **({"message": version_message} if version_message else {})},
    }
    if spaceId:
        payload["spaceId"] = spaceId
    return await _request("PUT", f"/wiki/api/v2/pages/{id}", json_body=payload)


@mcp.tool()
async def confluence_delete_page_v2(id: int, purge: Optional[bool] = None, draft: Optional[bool] = None) -> Dict[str, Any]:
    """Delete a page (v2).

    Endpoint: DELETE /wiki/api/v2/pages/{id}
    Query params: purge, draft
    """
    q: Dict[str, Any] = {}
    if purge is not None:
        q["purge"] = purge
    if draft is not None:
        q["draft"] = draft
    return await _request("DELETE", f"/wiki/api/v2/pages/{id}", query=q)


@mcp.tool()
async def confluence_get_labels_v2(
    limit: int = 25,
    cursor: Optional[str] = None,
    prefix: Optional[list[str]] = None,
    label_id: Optional[list[int]] = None,
    sort: Optional[str] = None,
) -> Dict[str, Any]:
    """Get labels (v2).

    Endpoint: GET /wiki/api/v2/labels
    """
    q: Dict[str, Any] = {"limit": limit}
    if cursor:
        q["cursor"] = cursor
    if prefix:
        q["prefix"] = prefix
    if label_id:
        q["label-id"] = label_id
    if sort:
        q["sort"] = sort
    return await _request("GET", "/wiki/api/v2/labels", query=q)


@mcp.tool()
async def confluence_get_user_v1(accountId: str, expand: Optional[list[str]] = None) -> Dict[str, Any]:
    """Get a user (v1).

    Endpoint: GET /wiki/rest/api/user?accountId=...
    """
    q: Dict[str, Any] = {"accountId": accountId}
    if expand:
        q["expand"] = expand
    return await _request("GET", "/wiki/rest/api/user", query=q)


@mcp.tool()
async def confluence_get_current_user_v1(expand: Optional[list[str]] = None) -> Dict[str, Any]:
    """Get current user (v1).

    Endpoint: GET /wiki/rest/api/user/current
    """
    q: Dict[str, Any] = {}
    if expand:
        q["expand"] = expand
    return await _request("GET", "/wiki/rest/api/user/current", query=q)


def _strip_html(html: str) -> str:
    # Very small helper for agents; not a full HTML parser.
    html = re.sub(r"<script[\s\S]*?</script>", "", html, flags=re.I)
    html = re.sub(r"<style[\s\S]*?</style>", "", html, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", html)
    text = re.sub(r"\s+", " ", text).strip()
    return text


@mcp.tool()
async def confluence_extract_page_text_v2(id: int) -> Dict[str, Any]:
    """Fetch a page (v2) with body-format=storage and return a best-effort plain-text extraction."""
    res = await confluence_get_page_by_id_v2(id=id, body_format="storage")
    data = res.get("data") or {}
    storage = (((data.get("body") or {}).get("storage") or {}).get("value"))
    if not isinstance(storage, str):
        return {"pageId": id, "text": "", "note": "No storage body found", "raw": data}
    return {"pageId": id, "text": _strip_html(storage)}


if __name__ == "__main__":
    mcp.run()
