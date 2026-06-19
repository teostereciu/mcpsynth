from typing import Any, Dict, Optional

from .client import ConfluenceClient


def v1_create_blog_post(
    *,
    space_key: str,
    title: str,
    body: str,
    body_format: str = "storage",
    status: str = "current",
) -> Any:
    """POST /rest/api/content"""
    c = ConfluenceClient()
    payload: Dict[str, Any] = {
        "type": "blogpost",
        "title": title,
        "space": {"key": space_key},
        "status": status,
        "body": {body_format: {"value": body, "representation": body_format}},
    }
    return c.request("POST", "/rest/api/content", json=payload, expected=(200, 201))


def v1_get_blog_post(content_id: str, *, expand: str = "body.storage,version") -> Any:
    """GET /rest/api/content/{id}"""
    c = ConfluenceClient()
    return c.request("GET", f"/rest/api/content/{content_id}", params={"expand": expand})


def v1_update_blog_post(
    content_id: str,
    *,
    title: Optional[str] = None,
    body: Optional[str] = None,
    body_format: str = "storage",
    version_number: int,
) -> Any:
    """PUT /rest/api/content/{id}"""
    c = ConfluenceClient()
    payload: Dict[str, Any] = {
        "id": str(content_id),
        "type": "blogpost",
        "version": {"number": version_number},
    }
    if title is not None:
        payload["title"] = title
    if body is not None:
        payload["body"] = {body_format: {"value": body, "representation": body_format}}
    return c.request("PUT", f"/rest/api/content/{content_id}", json=payload)


def v1_delete_blog_post(content_id: str) -> Any:
    """DELETE /rest/api/content/{id}"""
    c = ConfluenceClient()
    return c.request("DELETE", f"/rest/api/content/{content_id}", expected=(204,))
