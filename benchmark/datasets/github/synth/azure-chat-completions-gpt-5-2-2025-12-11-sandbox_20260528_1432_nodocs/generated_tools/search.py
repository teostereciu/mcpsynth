from typing import Any, Dict, Optional

from .github_client import GitHubClient


def search_code(q: str, sort: Optional[str] = None, order: str = "desc", per_page: int = 30, page: int = 1) -> Any:
    """GET /search/code"""
    params: Dict[str, Any] = {"q": q, "order": order, "per_page": per_page, "page": page}
    if sort:
        params["sort"] = sort
    return GitHubClient().request("GET", "/search/code", params=params)


def search_issues(q: str, sort: Optional[str] = None, order: str = "desc", per_page: int = 30, page: int = 1) -> Any:
    """GET /search/issues"""
    params: Dict[str, Any] = {"q": q, "order": order, "per_page": per_page, "page": page}
    if sort:
        params["sort"] = sort
    return GitHubClient().request("GET", "/search/issues", params=params)


def search_repositories(q: str, sort: Optional[str] = None, order: str = "desc", per_page: int = 30, page: int = 1) -> Any:
    """GET /search/repositories"""
    params: Dict[str, Any] = {"q": q, "order": order, "per_page": per_page, "page": page}
    if sort:
        params["sort"] = sort
    return GitHubClient().request("GET", "/search/repositories", params=params)
