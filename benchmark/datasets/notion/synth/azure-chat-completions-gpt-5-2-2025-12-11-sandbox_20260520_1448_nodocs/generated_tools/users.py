from typing import Any, Dict, Optional

from notion_client import NotionClient


def users_list(*, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    """GET /users"""
    client = NotionClient()
    params: Dict[str, Any] = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return client.request("GET", "/users", params=params or None)


def users_retrieve(user_id: str) -> Any:
    """GET /users/{user_id}"""
    client = NotionClient()
    return client.request("GET", f"/users/{user_id}")


def users_me() -> Any:
    """GET /users/me"""
    client = NotionClient()
    return client.request("GET", "/users/me")
