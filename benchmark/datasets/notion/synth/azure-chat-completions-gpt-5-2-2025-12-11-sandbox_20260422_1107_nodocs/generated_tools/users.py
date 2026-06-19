from typing import Any, Dict, Optional

from .notion_client import NotionClient


def users_list(*, start_cursor: Optional[str] = None, page_size: Optional[int] = None,
               notion_version: str = "2022-06-28", api_key: Optional[str] = None) -> Dict[str, Any]:
    """GET /users"""
    params: Dict[str, Any] = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    client = NotionClient(api_key=api_key, notion_version=notion_version)
    return client.request("GET", "/users", params=params)


def users_retrieve(user_id: str, *, notion_version: str = "2022-06-28", api_key: Optional[str] = None) -> Dict[str, Any]:
    """GET /users/{user_id}"""
    client = NotionClient(api_key=api_key, notion_version=notion_version)
    return client.request("GET", f"/users/{user_id}")


def users_me(*, notion_version: str = "2022-06-28", api_key: Optional[str] = None) -> Dict[str, Any]:
    """GET /users/me"""
    client = NotionClient(api_key=api_key, notion_version=notion_version)
    return client.request("GET", "/users/me")
