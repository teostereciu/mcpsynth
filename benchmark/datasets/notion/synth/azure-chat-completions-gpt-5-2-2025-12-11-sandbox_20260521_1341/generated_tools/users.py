from typing import Any, Dict, Optional

from .notion_client import NotionClient, omit_none


def users_list(
    *, start_cursor: Optional[str] = None, page_size: Optional[int] = None
) -> Dict[str, Any]:
    """GET /users

    Source: docs/get-users.md
    """
    params = omit_none({"start_cursor": start_cursor, "page_size": page_size})
    return NotionClient().request("GET", "/users", params=params or None)


def users_retrieve(*, user_id: str) -> Dict[str, Any]:
    """GET /users/{user_id}

    Source: docs/get-user.md
    """
    return NotionClient().request("GET", f"/users/{user_id}")


def users_me() -> Dict[str, Any]:
    """GET /users/me

    Source: docs/get-self.md
    """
    return NotionClient().request("GET", "/users/me")
