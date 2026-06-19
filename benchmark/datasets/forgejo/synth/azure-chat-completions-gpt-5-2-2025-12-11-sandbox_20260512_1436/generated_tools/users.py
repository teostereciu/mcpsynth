from typing import Any, Dict, Optional

from .http_client import request


def user_me() -> Any:
    return request("GET", "/user")


def user_get(username: str) -> Any:
    return request("GET", f"/users/{username}")


def users_search(q: str, *, uid: Optional[int] = None, sort: Optional[str] = None, page: Optional[int] = None, limit: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {"q": q}
    if uid is not None:
        params["uid"] = uid
    if sort is not None:
        params["sort"] = sort
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    return request("GET", "/users/search", params=params)


def user_repos_list(username: str, *, page: Optional[int] = None, limit: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {}
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    return request("GET", f"/users/{username}/repos", params=params or None)


def my_repos_list(*, page: Optional[int] = None, limit: Optional[int] = None, order_by: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    if order_by is not None:
        params["order_by"] = order_by
    return request("GET", "/user/repos", params=params or None)
