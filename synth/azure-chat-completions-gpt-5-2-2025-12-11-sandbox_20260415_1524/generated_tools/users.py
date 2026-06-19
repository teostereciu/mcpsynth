from typing import Any, Dict, Optional

from ._client import request_json


def users_list(*, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return request_json("GET", "/users", params=params or None)


def users_retrieve(user_id: str) -> Any:
    return request_json("GET", f"/users/{user_id}")


def users_me() -> Any:
    return request_json("GET", "/users/me")
