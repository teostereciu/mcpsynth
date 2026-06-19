from typing import Any, Dict
from .notion_client import NotionClient

client = NotionClient()


def get_self() -> Dict[str, Any]:
    return client.request("GET", "/users/me")


def get_user(user_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/users/{user_id}")


def get_users(start_cursor: Any = None, page_size: Any = None) -> Dict[str, Any]:
    params = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return client.request("GET", "/users", params=params or None)
