from typing import Any, Dict, Optional

from .client import notion_request


def list_users(
    *,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
    show_child_attributes: Optional[bool] = None,
) -> Dict[str, Any]:
    """GET /v1/users"""
    params: Dict[str, Any] = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    if show_child_attributes is not None:
        params["show_child_attributes"] = str(show_child_attributes).lower()
    return notion_request("GET", "/users", params=params or None)


def retrieve_user(user_id: str) -> Dict[str, Any]:
    """GET /v1/users/{user_id}"""
    return notion_request("GET", f"/users/{user_id}")


def retrieve_me() -> Dict[str, Any]:
    """GET /v1/users/me"""
    return notion_request("GET", "/users/me")
