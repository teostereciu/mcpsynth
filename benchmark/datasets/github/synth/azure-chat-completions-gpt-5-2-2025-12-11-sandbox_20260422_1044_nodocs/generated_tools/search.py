from typing import Any, Dict, Optional

from .github_client import GitHubClient


def search_code(q: str, sort: Optional[str] = None, order: Optional[str] = None, per_page: int = 100, page: int = 1) -> Dict[str, Any]:
    params: Dict[str, Any] = {"q": q, "per_page": per_page, "page": page}
    if sort is not None:
        params["sort"] = sort
    if order is not None:
        params["order"] = order
    return GitHubClient().request("GET", "/search/code", params=params)


def search_issues(q: str, sort: Optional[str] = None, order: Optional[str] = None, per_page: int = 100, page: int = 1) -> Dict[str, Any]:
    params: Dict[str, Any] = {"q": q, "per_page": per_page, "page": page}
    if sort is not None:
        params["sort"] = sort
    if order is not None:
        params["order"] = order
    return GitHubClient().request("GET", "/search/issues", params=params)


def search_repositories(q: str, sort: Optional[str] = None, order: Optional[str] = None, per_page: int = 100, page: int = 1) -> Dict[str, Any]:
    params: Dict[str, Any] = {"q": q, "per_page": per_page, "page": page}
    if sort is not None:
        params["sort"] = sort
    if order is not None:
        params["order"] = order
    return GitHubClient().request("GET", "/search/repositories", params=params)


def search_users(q: str, sort: Optional[str] = None, order: Optional[str] = None, per_page: int = 100, page: int = 1) -> Dict[str, Any]:
    params: Dict[str, Any] = {"q": q, "per_page": per_page, "page": page}
    if sort is not None:
        params["sort"] = sort
    if order is not None:
        params["order"] = order
    return GitHubClient().request("GET", "/search/users", params=params)
