import os
from typing import Any, Dict, Optional

from .http import confluence_request


# Prefer v2 for pages where possible


def list_pages(space_id: Optional[int] = None, limit: int = 25, cursor: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if space_id is not None:
        params["space-id"] = space_id
    if cursor:
        params["cursor"] = cursor
    return confluence_request("GET", "/api/v2/pages", params=params)


def get_page(page_id: int, body_format: str = "storage") -> Dict[str, Any]:
    params = {"body-format": body_format}
    return confluence_request("GET", f"/api/v2/pages/{page_id}", params=params)


def create_page(
    title: str,
    space_id: Optional[int] = None,
    parent_id: Optional[int] = None,
    body: str = "",
    body_representation: str = "storage",
    status: str = "current",
) -> Dict[str, Any]:
    if space_id is None:
        # fallback to v1 using space key
        space_key = os.environ.get("CONFLUENCE_SPACE_KEY")
        if not space_key:
            return {"error": "space_id not provided and CONFLUENCE_SPACE_KEY not set"}
        payload = {
            "type": "page",
            "title": title,
            "space": {"key": space_key},
            "body": {body_representation: {"value": body, "representation": body_representation}},
        }
        if parent_id is not None:
            payload["ancestors"] = [{"id": str(parent_id)}]
        return confluence_request("POST", "/rest/api/content", json=payload)

    payload: Dict[str, Any] = {
        "spaceId": space_id,
        "status": status,
        "title": title,
        "body": {"representation": body_representation, "value": body},
    }
    if parent_id is not None:
        payload["parentId"] = parent_id
    return confluence_request("POST", "/api/v2/pages", json=payload)


def update_page(
    page_id: int,
    title: Optional[str] = None,
    body: Optional[str] = None,
    body_representation: str = "storage",
    version_number: Optional[int] = None,
) -> Dict[str, Any]:
    # v2 update requires version; use v1 to simplify by fetching current version if not provided
    if version_number is None:
        current = confluence_request("GET", f"/rest/api/content/{page_id}", params={"expand": "version"})
        if "error" in current:
            return current
        version_number = int(current.get("version", {}).get("number", 0)) + 1
        if title is None:
            title = current.get("title")

    payload: Dict[str, Any] = {
        "id": str(page_id),
        "type": "page",
        "title": title or "",
        "version": {"number": version_number},
    }
    if body is not None:
        payload["body"] = {body_representation: {"value": body, "representation": body_representation}}
    return confluence_request("PUT", f"/rest/api/content/{page_id}", json=payload)


def delete_page(page_id: int) -> Dict[str, Any]:
    return confluence_request("DELETE", f"/api/v2/pages/{page_id}")


def get_page_children(page_id: int, limit: int = 25, cursor: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return confluence_request("GET", f"/api/v2/pages/{page_id}/children", params=params)


def get_page_ancestors(page_id: int) -> Dict[str, Any]:
    return confluence_request("GET", f"/api/v2/pages/{page_id}/ancestors")


def move_page(page_id: int, target_parent_id: int, position: str = "append") -> Dict[str, Any]:
    # v1 move endpoint
    payload = {"position": position, "targetId": str(target_parent_id)}
    return confluence_request("PUT", f"/rest/api/content/{page_id}/move", json=payload)
