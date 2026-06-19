from typing import Any, Dict, Optional

from .client import ConfluenceClient


def v2_get_page(page_id: str, *, body_format: str = "storage") -> Any:
    """GET /api/v2/pages/{id}"""
    c = ConfluenceClient()
    return c.request("GET", f"/api/v2/pages/{page_id}", params={"body-format": body_format})


def v2_create_page(
    *,
    space_id: str,
    title: str,
    parent_id: Optional[str] = None,
    body: str = "",
    body_format: str = "storage",
    status: str = "current",
) -> Any:
    """POST /api/v2/pages"""
    c = ConfluenceClient()
    payload: Dict[str, Any] = {
        "spaceId": space_id,
        "status": status,
        "title": title,
        "body": {"representation": body_format, "value": body},
    }
    if parent_id:
        payload["parentId"] = parent_id
    return c.request("POST", "/api/v2/pages", json=payload, expected=(200, 201))


def v2_update_page(
    page_id: str,
    *,
    title: Optional[str] = None,
    body: Optional[str] = None,
    body_format: str = "storage",
    status: str = "current",
    version_number: Optional[int] = None,
) -> Any:
    """PUT /api/v2/pages/{id}"""
    c = ConfluenceClient()
    payload: Dict[str, Any] = {"id": page_id, "status": status}
    if title is not None:
        payload["title"] = title
    if body is not None:
        payload["body"] = {"representation": body_format, "value": body}
    if version_number is not None:
        payload["version"] = {"number": version_number}
    return c.request("PUT", f"/api/v2/pages/{page_id}", json=payload)


def v2_delete_page(page_id: str, *, purge: bool = False) -> Any:
    """DELETE /api/v2/pages/{id}"""
    c = ConfluenceClient()
    return c.request("DELETE", f"/api/v2/pages/{page_id}", params={"purge": str(purge).lower()}, expected=(204,))


def v2_get_page_children(page_id: str, *, limit: int = 25, cursor: Optional[str] = None) -> Any:
    """GET /api/v2/pages/{id}/children"""
    c = ConfluenceClient()
    params: Dict[str, Any] = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return c.request("GET", f"/api/v2/pages/{page_id}/children", params=params)


def v1_get_page_ancestors(page_id: str) -> Any:
    """GET /rest/api/content/{id}?expand=ancestors"""
    c = ConfluenceClient()
    return c.request(
        "GET",
        f"/rest/api/content/{page_id}",
        params={"expand": "ancestors"},
    )


def v1_move_page(page_id: str, *, target_parent_id: str, position: str = "append") -> Any:
    """PUT /rest/api/content/{id}/move/{position}"""
    c = ConfluenceClient()
    return c.request(
        "PUT",
        f"/rest/api/content/{page_id}/move/{position}",
        json={"target": {"type": "page", "id": str(target_parent_id)}},
    )
