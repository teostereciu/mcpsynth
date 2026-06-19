from typing import Any, Dict, Optional

from generated_tools.confluence_client import client


def create_blog_post(title: str, body_value: str, space_key: Optional[str] = None) -> Dict[str, Any]:
    payload = {
        "type": "blogpost",
        "title": title,
        "space": {"key": space_key or client.space_key},
        "body": {"storage": {"value": body_value, "representation": "storage"}},
    }
    return client.request("POST", "/rest/api/content", json_body=payload)


def get_blog_post(content_id: str, expand: Optional[str] = None) -> Dict[str, Any]:
    params = {"expand": expand} if expand else None
    return client.request("GET", f"/rest/api/content/{content_id}", params=params)


def update_blog_post(content_id: str, title: str, body_value: str, version_number: int) -> Dict[str, Any]:
    current = get_blog_post(content_id)
    if current.get("error"):
        return current
    payload = {
        "id": content_id,
        "type": "blogpost",
        "title": title,
        "space": current.get("space"),
        "body": {"storage": {"value": body_value, "representation": "storage"}},
        "version": {"number": version_number},
    }
    return client.request("PUT", f"/rest/api/content/{content_id}", json_body=payload)


def delete_blog_post(content_id: str) -> Dict[str, Any]:
    return client.request("DELETE", f"/rest/api/content/{content_id}")
