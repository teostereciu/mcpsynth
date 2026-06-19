from typing import Any, Dict, Optional

from .notion_client import NotionClient


def list_users(
    *,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
    client: Optional[NotionClient] = None,
) -> Dict[str, Any]:
    client = client or NotionClient()
    params: Dict[str, Any] = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    data, err = client.request("GET", "/users", params=params)
    return err or data  # type: ignore[return-value]


def get_user(user_id: str, *, client: Optional[NotionClient] = None) -> Dict[str, Any]:
    client = client or NotionClient()
    data, err = client.request("GET", f"/users/{user_id}")
    return err or data  # type: ignore[return-value]


def get_me(*, client: Optional[NotionClient] = None) -> Dict[str, Any]:
    client = client or NotionClient()
    data, err = client.request("GET", "/users/me")
    return err or data  # type: ignore[return-value]
