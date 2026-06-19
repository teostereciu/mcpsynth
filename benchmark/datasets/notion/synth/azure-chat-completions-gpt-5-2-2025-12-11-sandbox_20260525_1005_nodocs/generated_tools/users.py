from typing import Any, Dict, Optional

from .notion_client import NotionClient


def users_list(
    *,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
    notion_version: str = "2022-06-28",
) -> Any:
    """GET /users"""
    client = NotionClient(notion_version=notion_version)
    params: Dict[str, Any] = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return client.request("GET", "/users", params=params or None)


def users_retrieve(user_id: str, *, notion_version: str = "2022-06-28") -> Any:
    """GET /users/{user_id}"""
    client = NotionClient(notion_version=notion_version)
    return client.request("GET", f"/users/{user_id}")


def users_me(*, notion_version: str = "2022-06-28") -> Any:
    """GET /users/me"""
    client = NotionClient(notion_version=notion_version)
    return client.request("GET", "/users/me")
