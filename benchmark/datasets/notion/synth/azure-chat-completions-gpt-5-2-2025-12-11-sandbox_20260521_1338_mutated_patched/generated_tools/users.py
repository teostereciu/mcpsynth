from typing import Any, Dict, Optional

from .notion_client import request_json


def users_list(*, page_cursor: Optional[str] = None, results_per_page: Optional[int] = None) -> Dict[str, Any]:
    """GET /v1/users

    Doc: docs/get-users.md
    """
    params: Dict[str, Any] = {}
    if page_cursor is not None:
        params["start_cursor"] = page_cursor
    if results_per_page is not None:
        params["page_size"] = results_per_page
    return request_json("GET", "/users", params=params)


def users_retrieve(user_id: str) -> Dict[str, Any]:
    """GET /v1/users/{user_id}

    Doc: docs/get-user.md
    """
    return request_json("GET", f"/users/{user_id}")


def users_me() -> Dict[str, Any]:
    """GET /v1/users/me

    Doc: docs/get-self.md
    """
    return request_json("GET", "/users/me")
