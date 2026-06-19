from typing import Any, Dict, Optional

from .notion_client import NotionClient


client = NotionClient()


def search(body: Dict[str, Any]) -> Any:
    return client.request("POST", "/search", json=body)


def list_users(start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    params = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return client.request("GET", "/users", params=params or None)


def retrieve_user(user_id: str) -> Any:
    return client.request("GET", f"/users/{user_id}")


def get_me() -> Any:
    return client.request("GET", "/users/me")


def list_comments(block_id: Optional[str] = None, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    params = {}
    if block_id is not None:
        params["block_id"] = block_id
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return client.request("GET", "/comments", params=params or None)


def create_comment(body: Dict[str, Any]) -> Any:
    return client.request("POST", "/comments", json=body)
