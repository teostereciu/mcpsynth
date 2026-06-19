from typing import Any, Dict, List, Optional, Union

from .http_client import GitHubClient


def search_code(
    *,
    q: str,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    text_match: bool = False,
) -> Union[Dict[str, Any], List[Any], str]:
    """GET /search/code"""
    client = GitHubClient()
    params: Dict[str, Any] = {"q": q, "per_page": per_page, "page": page}
    if sort is not None:
        params["sort"] = sort
    if order is not None:
        params["order"] = order
    accept = "application/vnd.github.text-match+json" if text_match else "application/vnd.github+json"
    return client.request("GET", "/search/code", params=params, accept=accept)


def search_issues_and_prs(
    *,
    q: str,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    text_match: bool = False,
) -> Union[Dict[str, Any], List[Any], str]:
    """GET /search/issues"""
    client = GitHubClient()
    params: Dict[str, Any] = {"q": q, "per_page": per_page, "page": page}
    if sort is not None:
        params["sort"] = sort
    if order is not None:
        params["order"] = order
    accept = "application/vnd.github.text-match+json" if text_match else "application/vnd.github+json"
    return client.request("GET", "/search/issues", params=params, accept=accept)


def search_repositories(
    *,
    q: str,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    text_match: bool = False,
) -> Union[Dict[str, Any], List[Any], str]:
    """GET /search/repositories"""
    client = GitHubClient()
    params: Dict[str, Any] = {"q": q, "per_page": per_page, "page": page}
    if sort is not None:
        params["sort"] = sort
    if order is not None:
        params["order"] = order
    accept = "application/vnd.github.text-match+json" if text_match else "application/vnd.github+json"
    return client.request("GET", "/search/repositories", params=params, accept=accept)
