import os
import json
import base64
from typing import Any, Dict, Optional, List, Union

import requests
from mcp.server.fastmcp import FastMCP


mcp = FastMCP("confluence-cloud")


def _env(name: str, default: Optional[str] = None) -> Optional[str]:
    v = os.getenv(name)
    return v if v not in (None, "") else default


def _auth_header() -> Dict[str, str]:
    email = _env("JIRA_EMAIL")
    token = _env("JIRA_API_TOKEN")
    if not email or not token:
        return {}
    b64 = base64.b64encode(f"{email}:{token}".encode("utf-8")).decode("ascii")
    return {"Authorization": f"Basic {b64}"}


def _base_url() -> str:
    base = _env("CONFLUENCE_BASE_URL", "").rstrip("/")
    return base


def _default_space_key() -> Optional[str]:
    return _env("CONFLUENCE_SPACE_KEY")


def _request(
    method: str,
    path: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    json_body: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    files: Any = None,
    data: Any = None,
    stream: bool = False,
) -> Union[Dict[str, Any], str, List[Any]]:
    base = _base_url()
    if not base:
        return {"error": "CONFLUENCE_BASE_URL is not set"}

    url = f"{base}{path}"
    h = {
        "Accept": "application/json",
        **_auth_header(),
    }
    if headers:
        h.update(headers)

    try:
        resp = requests.request(
            method,
            url,
            params=params,
            json=json_body,
            headers=h,
            files=files,
            data=data,
            timeout=60,
            stream=stream,
        )
    except Exception as e:
        return {"error": f"Request failed: {e}"}

    # Handle non-JSON downloads
    content_type = resp.headers.get("Content-Type", "")

    if resp.status_code >= 400:
        # Try to parse JSON error
        try:
            err = resp.json()
        except Exception:
            err = {"message": resp.text}
        return {
            "error": "Confluence API error",
            "status": resp.status_code,
            "details": err,
            "url": url,
        }

    if stream:
        # Return base64 for binary content
        b = resp.content
        return {
            "content_base64": base64.b64encode(b).decode("ascii"),
            "content_type": content_type,
            "content_length": len(b),
        }

    if "application/json" in content_type or content_type.endswith("+json"):
        try:
            return resp.json()
        except Exception:
            return {"error": "Failed to parse JSON response", "text": resp.text}

    return resp.text


# ---------------------- Spaces (v2 preferred) ----------------------

@mcp.tool()
def list_spaces(limit: int = 25, cursor: Optional[str] = None) -> Any:
    """List spaces (v2)."""
    params: Dict[str, Any] = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return _request("GET", "/api/v2/spaces", params=params)


@mcp.tool()
def get_space(space_id: Optional[int] = None, space_key: Optional[str] = None) -> Any:
    """Get a space by id (v2) or by key (v1)."""
    if space_id is not None:
        return _request("GET", f"/api/v2/spaces/{space_id}")
    key = space_key or _default_space_key()
    if not key:
        return {"error": "Provide space_id or space_key (or set CONFLUENCE_SPACE_KEY)"}
    return _request("GET", f"/rest/api/space/{key}")


@mcp.tool()
def create_space(
    key: str,
    name: str,
    description_plain: Optional[str] = None,
) -> Any:
    """Create a space (v1)."""
    body: Dict[str, Any] = {"key": key, "name": name}
    if description_plain:
        body["description"] = {
            "plain": {"value": description_plain, "representation": "plain"}
        }
    return _request("POST", "/rest/api/space", json_body=body)


@mcp.tool()
def delete_space(space_key: Optional[str] = None) -> Any:
    """Delete a space by key (v1)."""
    key = space_key or _default_space_key()
    if not key:
        return {"error": "Provide space_key (or set CONFLUENCE_SPACE_KEY)"}
    return _request("DELETE", f"/rest/api/space/{key}")


# ---------------------- Pages (v2 preferred) ----------------------

@mcp.tool()
def create_page(
    title: str,
    body_storage: str,
    space_id: Optional[int] = None,
    parent_id: Optional[int] = None,
    status: str = "current",
) -> Any:
    """Create a page (v2). body_storage should be Confluence storage format."""
    if space_id is None:
        # try resolve from default space key via v1
        key = _default_space_key()
        if not key:
            return {"error": "space_id is required unless CONFLUENCE_SPACE_KEY is set"}
        sp = _request("GET", f"/rest/api/space/{key}")
        if isinstance(sp, dict) and sp.get("id"):
            try:
                space_id = int(sp["id"])
            except Exception:
                return {"error": "Failed to resolve space_id from space key", "space": sp}
        else:
            return {"error": "Failed to resolve space from CONFLUENCE_SPACE_KEY", "space": sp}

    body: Dict[str, Any] = {
        "spaceId": space_id,
        "status": status,
        "title": title,
        "body": {"representation": "storage", "value": body_storage},
    }
    if parent_id is not None:
        body["parentId"] = parent_id
    return _request("POST", "/api/v2/pages", json_body=body)


@mcp.tool()
def get_page(page_id: int, body_format: str = "storage") -> Any:
    """Get a page (v2). body_format: storage|atlas_doc_format|view."""
    params = {"body-format": body_format}
    return _request("GET", f"/api/v2/pages/{page_id}", params=params)


@mcp.tool()
def update_page(
    page_id: int,
    title: Optional[str] = None,
    body_storage: Optional[str] = None,
    version_number: Optional[int] = None,
    status: str = "current",
) -> Any:
    """Update a page (v2). Provide version_number; if omitted, it will be fetched and incremented."""
    if version_number is None:
        current = _request("GET", f"/api/v2/pages/{page_id}", params={"body-format": "storage"})
        if not isinstance(current, dict) or "version" not in current:
            return {"error": "Failed to fetch current page to determine version", "details": current}
        try:
            version_number = int(current["version"]["number"]) + 1
        except Exception:
            return {"error": "Failed to parse current version", "details": current}

    body: Dict[str, Any] = {"id": page_id, "status": status, "version": {"number": version_number}}
    if title is not None:
        body["title"] = title
    if body_storage is not None:
        body["body"] = {"representation": "storage", "value": body_storage}
    return _request("PUT", f"/api/v2/pages/{page_id}", json_body=body)


@mcp.tool()
def delete_page(page_id: int) -> Any:
    """Delete a page (v2)."""
    return _request("DELETE", f"/api/v2/pages/{page_id}")


@mcp.tool()
def get_page_children(page_id: int, limit: int = 25, cursor: Optional[str] = None) -> Any:
    """Get child pages (v2)."""
    params: Dict[str, Any] = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return _request("GET", f"/api/v2/pages/{page_id}/children", params=params)


@mcp.tool()
def get_page_ancestors(page_id: int) -> Any:
    """Get page ancestors (v1)."""
    return _request("GET", f"/rest/api/content/{page_id}", params={"expand": "ancestors"})


@mcp.tool()
def move_page(page_id: int, target_parent_id: int, position: str = "append") -> Any:
    """Move a page under a new parent (v1 content move). position: before|after|append."""
    body = {"position": position, "target": {"type": "page", "id": str(target_parent_id)}}
    return _request("POST", f"/rest/api/content/{page_id}/move", json_body=body)


# ---------------------- Blog posts (v2) ----------------------

@mcp.tool()
def create_blog_post(
    title: str,
    body_storage: str,
    space_id: Optional[int] = None,
    status: str = "current",
) -> Any:
    """Create a blog post (v2)."""
    if space_id is None:
        key = _default_space_key()
        if not key:
            return {"error": "space_id is required unless CONFLUENCE_SPACE_KEY is set"}
        sp = _request("GET", f"/rest/api/space/{key}")
        if isinstance(sp, dict) and sp.get("id"):
            space_id = int(sp["id"])
        else:
            return {"error": "Failed to resolve space", "details": sp}

    body = {
        "spaceId": space_id,
        "status": status,
        "title": title,
        "body": {"representation": "storage", "value": body_storage},
    }
    return _request("POST", "/api/v2/blogposts", json_body=body)


@mcp.tool()
def get_blog_post(blogpost_id: int, body_format: str = "storage") -> Any:
    params = {"body-format": body_format}
    return _request("GET", f"/api/v2/blogposts/{blogpost_id}", params=params)


@mcp.tool()
def update_blog_post(
    blogpost_id: int,
    title: Optional[str] = None,
    body_storage: Optional[str] = None,
    version_number: Optional[int] = None,
    status: str = "current",
) -> Any:
    if version_number is None:
        current = _request("GET", f"/api/v2/blogposts/{blogpost_id}", params={"body-format": "storage"})
        if not isinstance(current, dict) or "version" not in current:
            return {"error": "Failed to fetch current blog post to determine version", "details": current}
        version_number = int(current["version"]["number"]) + 1

    body: Dict[str, Any] = {"id": blogpost_id, "status": status, "version": {"number": version_number}}
    if title is not None:
        body["title"] = title
    if body_storage is not None:
        body["body"] = {"representation": "storage", "value": body_storage}
    return _request("PUT", f"/api/v2/blogposts/{blogpost_id}", json_body=body)


@mcp.tool()
def delete_blog_post(blogpost_id: int) -> Any:
    return _request("DELETE", f"/api/v2/blogposts/{blogpost_id}")


# ---------------------- Search (v1 CQL) ----------------------

@mcp.tool()
def search_cql(cql: str, limit: int = 25, start: int = 0, expand: Optional[str] = None) -> Any:
    """Search content using CQL (v1)."""
    params: Dict[str, Any] = {"cql": cql, "limit": limit, "start": start}
    if expand:
        params["expand"] = expand
    return _request("GET", "/rest/api/content/search", params=params)


# ---------------------- Labels (v1) ----------------------

@mcp.tool()
def list_content_labels(content_id: int, prefix: str = "global", limit: int = 200, start: int = 0) -> Any:
    """List labels on content (v1). prefix: global|my|team."""
    params = {"prefix": prefix, "limit": limit, "start": start}
    return _request("GET", f"/rest/api/content/{content_id}/label", params=params)


@mcp.tool()
def add_content_labels(content_id: int, labels: List[str], prefix: str = "global") -> Any:
    """Add labels to content (v1)."""
    body = [{"prefix": prefix, "name": name} for name in labels]
    return _request("POST", f"/rest/api/content/{content_id}/label", json_body=body)


@mcp.tool()
def remove_content_label(content_id: int, label: str) -> Any:
    """Remove a label from content (v1)."""
    return _request("DELETE", f"/rest/api/content/{content_id}/label/{label}")


# ---------------------- Attachments ----------------------

@mcp.tool()
def list_attachments(page_id: int, limit: int = 25, start: int = 0) -> Any:
    """List attachments on a page (v1)."""
    params = {"limit": limit, "start": start, "expand": "version"}
    return _request("GET", f"/rest/api/content/{page_id}/child/attachment", params=params)


@mcp.tool()
def upload_attachment(page_id: int, file_path: str, comment: Optional[str] = None) -> Any:
    """Upload an attachment to a page (v1)."""
    if not os.path.exists(file_path):
        return {"error": f"File not found: {file_path}"}
    filename = os.path.basename(file_path)
    params: Dict[str, Any] = {}
    if comment:
        params["comment"] = comment
    headers = {"X-Atlassian-Token": "no-check"}
    with open(file_path, "rb") as f:
        files = {"file": (filename, f)}
        return _request(
            "POST",
            f"/rest/api/content/{page_id}/child/attachment",
            params=params,
            headers=headers,
            files=files,
        )


@mcp.tool()
def download_attachment(attachment_id: int) -> Any:
    """Download an attachment binary by attachment content id (v1). Returns base64."""
    meta = _request("GET", f"/rest/api/content/{attachment_id}", params={"expand": "_links"})
    if not isinstance(meta, dict):
        return {"error": "Failed to fetch attachment metadata", "details": meta}
    dl = None
    try:
        dl = meta.get("_links", {}).get("download")
    except Exception:
        dl = None
    if not dl:
        return {"error": "Attachment download link not found", "details": meta}
    # download link is relative to /wiki
    return _request("GET", dl, stream=True)


# ---------------------- Comments (v2) ----------------------

@mcp.tool()
def list_page_comments(page_id: int, comment_type: str = "footer", limit: int = 25, cursor: Optional[str] = None) -> Any:
    """List comments on a page (v2). comment_type: footer|inline."""
    params: Dict[str, Any] = {"limit": limit, "type": comment_type}
    if cursor:
        params["cursor"] = cursor
    return _request("GET", f"/api/v2/pages/{page_id}/comments", params=params)


@mcp.tool()
def create_page_comment(
    page_id: int,
    body_storage: str,
    comment_type: str = "footer",
    parent_comment_id: Optional[int] = None,
) -> Any:
    """Create a footer/inline comment on a page (v2)."""
    body: Dict[str, Any] = {
        "pageId": page_id,
        "type": comment_type,
        "body": {"representation": "storage", "value": body_storage},
    }
    if parent_comment_id is not None:
        body["parentCommentId"] = parent_comment_id
    return _request("POST", "/api/v2/comments", json_body=body)


# ---------------------- Versions (v1) ----------------------

@mcp.tool()
def list_page_versions(page_id: int, limit: int = 25, start: int = 0) -> Any:
    """List versions of a page (v1)."""
    params = {"limit": limit, "start": start}
    return _request("GET", f"/rest/api/content/{page_id}/version", params=params)


@mcp.tool()
def get_page_version(page_id: int, version_number: int) -> Any:
    """Get a specific version of a page (v1)."""
    return _request("GET", f"/rest/api/content/{page_id}/version/{version_number}")


@mcp.tool()
def restore_page_version(page_id: int, version_number: int) -> Any:
    """Restore a page to a previous version (v1)."""
    return _request("POST", f"/rest/api/content/{page_id}/version/{version_number}/restore")


# ---------------------- Content properties (v1) ----------------------

@mcp.tool()
def get_content_property(content_id: int, key: str) -> Any:
    """Get a content property (v1)."""
    return _request("GET", f"/rest/api/content/{content_id}/property/{key}")


@mcp.tool()
def set_content_property(content_id: int, key: str, value: Any, version_number: Optional[int] = None) -> Any:
    """Create/update a content property (v1). If updating, provide version_number or it will be fetched and incremented."""
    if version_number is None:
        existing = _request("GET", f"/rest/api/content/{content_id}/property/{key}")
        if isinstance(existing, dict) and existing.get("version", {}).get("number"):
            version_number = int(existing["version"]["number"]) + 1
        else:
            version_number = 1

    body = {"key": key, "value": value, "version": {"number": version_number}}
    # PUT works for update; POST for create. We'll try PUT first; if 404 then POST.
    put = _request("PUT", f"/rest/api/content/{content_id}/property/{key}", json_body=body)
    if isinstance(put, dict) and put.get("error") and put.get("status") == 404:
        return _request("POST", f"/rest/api/content/{content_id}/property", json_body=body)
    return put


# ---------------------- Users ----------------------

@mcp.tool()
def get_current_user() -> Any:
    """Get current user (v1)."""
    return _request("GET", "/rest/api/user/current")


@mcp.tool()
def get_user(account_id: str) -> Any:
    """Get user by accountId (v1)."""
    return _request("GET", "/rest/api/user", params={"accountId": account_id})


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
