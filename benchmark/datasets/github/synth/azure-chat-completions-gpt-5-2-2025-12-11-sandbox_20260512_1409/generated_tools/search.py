from typing import Any, Dict, Optional

from .github_client import GitHubClient


def search_code(
    client: GitHubClient,
    *,
    q: str,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    text_match: bool = False,
) -> Any:
    params: Dict[str, Any] = {"q": q, "per_page": per_page, "page": page}
    if sort is not None:
        params["sort"] = sort
    if order is not None:
        params["order"] = order

    accept = "application/vnd.github.text-match+json" if text_match else None
    return client.request("GET", "/search/code", params=params, accept=accept)


def search_issues_and_prs(
    client: GitHubClient,
    *,
    q: str,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    text_match: bool = False,
) -> Any:
    params: Dict[str, Any] = {"q": q, "per_page": per_page, "page": page}
    if sort is not None:
        params["sort"] = sort
    if order is not None:
        params["order"] = order
    accept = "application/vnd.github.text-match+json" if text_match else None
    return client.request("GET", "/search/issues", params=params, accept=accept)


def search_repositories(
    client: GitHubClient,
    *,
    q: str,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
) -> Any:
    params: Dict[str, Any] = {"q": q, "per_page": per_page, "page": page}
    if sort is not None:
        params["sort"] = sort
    if order is not None:
        params["order"] = order
    return client.request("GET", "/search/repositories", params=params)
