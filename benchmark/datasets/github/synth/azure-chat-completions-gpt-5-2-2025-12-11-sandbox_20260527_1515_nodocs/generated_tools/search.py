from typing import Any, Dict, Optional

from .github_client import GitHubClient


client = GitHubClient()


def search_code(q: str, *, sort: Optional[str] = None, order: str = "desc", per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    params: Dict[str, Any] = {"q": q, "order": order, "per_page": per_page, "page": page}
    if sort is not None:
        params["sort"] = sort
    return client.request("GET", "/search/code", params=params)


def search_issues_and_prs(q: str, *, sort: Optional[str] = None, order: str = "desc", per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    params: Dict[str, Any] = {"q": q, "order": order, "per_page": per_page, "page": page}
    if sort is not None:
        params["sort"] = sort
    return client.request("GET", "/search/issues", params=params)


def search_repositories(q: str, *, sort: Optional[str] = None, order: str = "desc", per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    params: Dict[str, Any] = {"q": q, "order": order, "per_page": per_page, "page": page}
    if sort is not None:
        params["sort"] = sort
    return client.request("GET", "/search/repositories", params=params)
