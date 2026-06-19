from typing import Any, Dict, Optional

from ._client import GitHubClient


def search_code(q: str, sort: Optional[str] = None, order: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    client = GitHubClient()
    params: Dict[str, Any] = {"q": q, "per_page": per_page, "page": page}
    if sort is not None:
        params["sort"] = sort
    if order is not None:
        params["order"] = order
    return client.request("GET", "/search/code", params=params)


def search_issues_and_prs(q: str, sort: Optional[str] = None, order: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    client = GitHubClient()
    params: Dict[str, Any] = {"q": q, "per_page": per_page, "page": page}
    if sort is not None:
        params["sort"] = sort
    if order is not None:
        params["order"] = order
    return client.request("GET", "/search/issues", params=params)


def search_repositories(q: str, sort: Optional[str] = None, order: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    client = GitHubClient()
    params: Dict[str, Any] = {"q": q, "per_page": per_page, "page": page}
    if sort is not None:
        params["sort"] = sort
    if order is not None:
        params["order"] = order
    return client.request("GET", "/search/repositories", params=params)


def search_users(q: str, sort: Optional[str] = None, order: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    client = GitHubClient()
    params: Dict[str, Any] = {"q": q, "per_page": per_page, "page": page}
    if sort is not None:
        params["sort"] = sort
    if order is not None:
        params["order"] = order
    return client.request("GET", "/search/users", params=params)
