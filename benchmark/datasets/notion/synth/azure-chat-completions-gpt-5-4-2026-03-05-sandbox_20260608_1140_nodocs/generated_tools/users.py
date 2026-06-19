from typing import Any, Dict, Optional

from generated_tools.notion_client import client


def list_users(start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return client.request("GET", "/users", params=params or None)


def retrieve_user(user_id: str) -> Any:
    return client.request("GET", f"/users/{user_id}")


def retrieve_bot_user() -> Any:
    return client.request("GET", "/users/me")
