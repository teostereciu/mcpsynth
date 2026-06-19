from typing import Any, Dict, Optional

from generated_tools.pages import _request


def get_self() -> Any:
    return _request("GET", "/users/me")


def get_user(user_id: str) -> Any:
    return _request("GET", f"/users/{user_id}")


def list_users(start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {}
    if start_cursor is not None:
        params["start_cursor"] = start_cursor
    if page_size is not None:
        params["page_size"] = page_size
    return _request("GET", "/users", params=params or None)


def search(query: Optional[str] = None, query_filter: Optional[Dict[str, Any]] = None, sort: Optional[Dict[str, Any]] = None, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    body: Dict[str, Any] = {}
    if query is not None:
        body["query"] = query
    if query_filter is not None:
        body["filter"] = query_filter
    if sort is not None:
        body["sort"] = sort
    if start_cursor is not None:
        body["start_cursor"] = start_cursor
    if page_size is not None:
        body["page_size"] = page_size
    return _request("POST", "/search", json_body=body)
