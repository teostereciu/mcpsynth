from typing import Any, Dict, Optional

from .http_client import request_json


def users_me() -> Dict[str, Any]:
    """GET /users/me"""
    return request_json("GET", "/users/me")


def users_list(*, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Dict[str, Any]:
    """GET /users"""
    params: Dict[str, Any] = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return request_json("GET", "/users", params=params or None)


def users_retrieve(user_id: str) -> Dict[str, Any]:
    """GET /users/{user_id}"""
    return request_json("GET", f"/users/{user_id}")
