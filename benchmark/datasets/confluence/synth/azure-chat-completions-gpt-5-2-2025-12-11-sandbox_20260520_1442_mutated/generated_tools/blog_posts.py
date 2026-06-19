from typing import Any, Dict, Optional

from .http_client import ConfluenceClient, ok_or_error


def list_blog_posts(*, space_ids: Optional[list[int]] = None, cursor: Optional[str] = None, max_results: int = 25) -> Dict[str, Any]:
    """GET /api/v2/blogposts"""
    c = ConfluenceClient()
    params: Dict[str, Any] = {"max_results": max_results}
    if space_ids:
        params["space-id"] = space_ids
    if cursor:
        params["cursor"] = cursor
    status, body, headers = c.request("GET", "/api/v2/blogposts", params=params)
    return ok_or_error(status, body, headers)


def get_blog_post(blogpost_id: int) -> Dict[str, Any]:
    """GET /api/v2/blogposts/{id}"""
    c = ConfluenceClient()
    status, body, headers = c.request("GET", f"/api/v2/blogposts/{blogpost_id}")
    return ok_or_error(status, body, headers)


def create_blog_post(
    *,
    space_id: str,
    title: str,
    body_storage_value: str,
    content_status: str = "current",
    private: Optional[bool] = None,
) -> Dict[str, Any]:
    """POST /api/v2/blogposts"""
    c = ConfluenceClient()
    params: Dict[str, Any] = {}
    if private is not None:
        params["private"] = str(private).lower()
    payload: Dict[str, Any] = {
        "spaceId": space_id,
        "content_status": content_status,
        "title": title,
        "body": {"representation": "storage", "value": body_storage_value},
    }
    status, body, headers = c.request("POST", "/api/v2/blogposts", params=params, json_body=payload)
    return ok_or_error(status, body, headers)


def update_blog_post(
    blogpost_id: int,
    *,
    space_id: str,
    title: str,
    body_storage_value: str,
    version_number: int,
    version_message: Optional[str] = None,
    content_status: str = "current",
) -> Dict[str, Any]:
    """PUT /api/v2/blogposts/{id}"""
    c = ConfluenceClient()
    payload: Dict[str, Any] = {
        "id": str(blogpost_id),
        "content_status": content_status,
        "title": title,
        "spaceId": space_id,
        "body": {"representation": "storage", "value": body_storage_value},
        "version": {"number": version_number},
    }
    if version_message:
        payload["version"]["message"] = version_message
    status, body, headers = c.request("PUT", f"/api/v2/blogposts/{blogpost_id}", json_body=payload)
    return ok_or_error(status, body, headers)


def delete_blog_post(blogpost_id: int, *, purge: bool = False, draft: bool = False) -> Dict[str, Any]:
    """DELETE /api/v2/blogposts/{id}"""
    c = ConfluenceClient()
    params = {"purge": str(purge).lower(), "draft": str(draft).lower()}
    status, body, headers = c.request("DELETE", f"/api/v2/blogposts/{blogpost_id}", params=params)
    return ok_or_error(status, body, headers)
