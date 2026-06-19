from typing import Any, Dict, Optional

from generated_tools.common import notion_request


def search(query: Optional[str] = None, filter: Optional[Dict[str, Any]] = None, sort: Optional[Dict[str, Any]] = None, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    body: Dict[str, Any] = {}
    if query is not None:
        body["query"] = query
    if filter is not None:
        body["filter"] = filter
    if sort is not None:
        body["sort"] = sort
    if start_cursor is not None:
        body["start_cursor"] = start_cursor
    if page_size is not None:
        body["page_size"] = page_size
    return notion_request("POST", "/search", json_body=body)


def list_users(start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    params = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return notion_request("GET", "/users", params=params or None)


def get_user(user_id: str) -> Any:
    return notion_request("GET", f"/users/{user_id}")


def get_self() -> Any:
    return notion_request("GET", "/users/me")
