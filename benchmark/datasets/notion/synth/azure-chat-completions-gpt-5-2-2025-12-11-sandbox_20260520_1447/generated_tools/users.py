from typing import Any, Dict, Optional

from .notion_client import NotionClient


def users_retrieve(user_id: str) -> Dict[str, Any]:
    """GET /v1/users/{user_id}

    Doc: docs/get-user.md
    """
    client = NotionClient()
    return client.request("GET", f"/users/{user_id}")


def users_me() -> Dict[str, Any]:
    """GET /v1/users/me

    Doc: docs/get-self.md
    """
    client = NotionClient()
    return client.request("GET", "/users/me")


def users_list(*, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Dict[str, Any]:
    """GET /v1/users

    Doc: docs/get-users.md
    """
    params: Dict[str, Any] = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    client = NotionClient()
    return client.request("GET", "/users", params=params or None)
