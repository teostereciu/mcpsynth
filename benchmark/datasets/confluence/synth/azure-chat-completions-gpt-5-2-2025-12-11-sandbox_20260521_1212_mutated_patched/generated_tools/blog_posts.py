from typing import Any, Dict, Optional

from .http_client import ConfluenceClient


def list_blog_posts(
    space_id: Optional[int] = None,
    title: Optional[str] = None,
    content_status: Optional[list[str]] = None,
    cursor: Optional[str] = None,
    max_results: int = 25,
    body_format: Optional[str] = None,
    sort: Optional[str] = None,
    ids: Optional[list[int]] = None,
) -> Dict[str, Any]:
    """GET /api/v2/blogposts"""
    client = ConfluenceClient()
    params: Dict[str, Any] = {"limit": max_results}
    if space_id is not None:
        params["space-id"] = [space_id]
    if title is not None:
        params["title"] = title
    if content_status is not None:
        params["status"] = content_status
    if cursor is not None:
        params["cursor"] = cursor
    if body_format is not None:
        params["body-format"] = body_format
    if sort is not None:
        params["sort"] = sort
    if ids is not None:
        params["id"] = ids
    return client.request("GET", "/api/v2/blogposts", params=params)


def get_blog_post(blog_post_id: int, body_format: Optional[str] = None, get_draft: Optional[bool] = None) -> Dict[str, Any]:
    """GET /api/v2/blogposts/{id}"""
    client = ConfluenceClient()
    params: Dict[str, Any] = {}
    if body_format is not None:
        params["body-format"] = body_format
    if get_draft is not None:
        params["get-draft"] = get_draft
    return client.request("GET", f"/api/v2/blogposts/{blog_post_id}", params=params)


def create_blog_post(
    space_id: str,
    title: str,
    body_value: str,
    content_status: str = "current",
    private: Optional[bool] = None,
    created_at: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /api/v2/blogposts"""
    client = ConfluenceClient()
    params: Dict[str, Any] = {}
    if private is not None:
        params["private"] = private
    payload: Dict[str, Any] = {
        "spaceId": space_id,
        "status": content_status,
        "title": title,
        "body": {"representation": "storage", "value": body_value},
    }
    if created_at is not None:
        payload["createdAt"] = created_at
    return client.request("POST", "/api/v2/blogposts", params=params, json=payload)


def update_blog_post(
    blog_post_id: int,
    space_id: str,
    title: str,
    body_value: str,
    version_number: int,
    version_message: Optional[str] = None,
    content_status: str = "current",
    created_at: Optional[str] = None,
) -> Dict[str, Any]:
    """PUT /api/v2/blogposts/{id}"""
    client = ConfluenceClient()
    payload: Dict[str, Any] = {
        "id": str(blog_post_id),
        "status": content_status,
        "title": title,
        "spaceId": space_id,
        "body": {"representation": "storage", "value": body_value},
        "version": {"number": version_number},
    }
    if version_message is not None:
        payload["version"]["message"] = version_message
    if created_at is not None:
        payload["createdAt"] = created_at
    return client.request("PUT", f"/api/v2/blogposts/{blog_post_id}", json=payload)


def delete_blog_post(blog_post_id: int, purge: Optional[bool] = None, draft: Optional[bool] = None) -> Dict[str, Any]:
    """DEL /api/v2/blogposts/{id}"""
    client = ConfluenceClient()
    params: Dict[str, Any] = {}
    if purge is not None:
        params["purge"] = purge
    if draft is not None:
        params["draft"] = draft
    return client.request("DELETE", f"/api/v2/blogposts/{blog_post_id}", params=params)
