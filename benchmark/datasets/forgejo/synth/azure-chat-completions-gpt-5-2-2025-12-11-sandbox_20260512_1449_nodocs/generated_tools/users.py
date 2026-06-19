from typing import Any, Dict, Optional

from .client import request_json


def get_authenticated_user() -> Any:
    return request_json("GET", "/user")


def get_user(username: str) -> Any:
    return request_json("GET", f"/users/{username}")


def search_users(q: str, limit: Optional[int] = None, page: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {"q": q}
    if limit is not None:
        params["limit"] = limit
    if page is not None:
        params["page"] = page
    return request_json("GET", "/users/search", params=params)
