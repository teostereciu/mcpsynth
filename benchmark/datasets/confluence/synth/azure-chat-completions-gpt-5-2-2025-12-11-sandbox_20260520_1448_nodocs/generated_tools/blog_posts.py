import os
from typing import Any, Dict, Optional

from .http import confluence_request


def get_blog_post(blog_id: int, expand: str = "body.storage,version") -> Dict[str, Any]:
    return confluence_request("GET", f"/rest/api/content/{blog_id}", params={"expand": expand})


def create_blog_post(
    title: str,
    body: str,
    space_key: Optional[str] = None,
    representation: str = "storage",
) -> Dict[str, Any]:
    if space_key is None:
        space_key = os.environ.get("CONFLUENCE_SPACE_KEY")
    if not space_key:
        return {"error": "space_key not provided and CONFLUENCE_SPACE_KEY not set"}

    payload = {
        "type": "blogpost",
        "title": title,
        "space": {"key": space_key},
        "body": {representation: {"value": body, "representation": representation}},
    }
    return confluence_request("POST", "/rest/api/content", json=payload)


def update_blog_post(blog_id: int, title: Optional[str] = None, body: Optional[str] = None, representation: str = "storage") -> Dict[str, Any]:
    current = confluence_request("GET", f"/rest/api/content/{blog_id}", params={"expand": "version"})
    if "error" in current:
        return current
    version_number = int(current.get("version", {}).get("number", 0)) + 1
    if title is None:
        title = current.get("title")

    payload: Dict[str, Any] = {
        "id": str(blog_id),
        "type": "blogpost",
        "title": title or "",
        "version": {"number": version_number},
    }
    if body is not None:
        payload["body"] = {representation: {"value": body, "representation": representation}}
    return confluence_request("PUT", f"/rest/api/content/{blog_id}", json=payload)


def delete_blog_post(blog_id: int) -> Dict[str, Any]:
    return confluence_request("DELETE", f"/rest/api/content/{blog_id}")
