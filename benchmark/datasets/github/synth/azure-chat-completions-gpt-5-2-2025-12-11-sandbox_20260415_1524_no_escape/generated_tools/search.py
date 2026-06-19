from __future__ import annotations

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
    params: Dict[str, Any] = {"q": q, "sort": sort, "order": order, "per_page": per_page, "page": page}
    params = {k: v for k, v in params.items() if v is not None}
    headers = {"Accept": "application/vnd.github.text-match+json"} if text_match else None
    return client.request("GET", "/search/code", params=params, headers=headers)


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
    params: Dict[str, Any] = {"q": q, "sort": sort, "order": order, "per_page": per_page, "page": page}
    params = {k: v for k, v in params.items() if v is not None}
    headers = {"Accept": "application/vnd.github.text-match+json"} if text_match else None
    return client.request("GET", "/search/issues", params=params, headers=headers)


def search_repositories(
    client: GitHubClient,
    *,
    q: str,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    text_match: bool = False,
) -> Any:
    params: Dict[str, Any] = {"q": q, "sort": sort, "order": order, "per_page": per_page, "page": page}
    params = {k: v for k, v in params.items() if v is not None}
    headers = {"Accept": "application/vnd.github.text-match+json"} if text_match else None
    return client.request("GET", "/search/repositories", params=params, headers=headers)


def search_users(
    client: GitHubClient,
    *,
    q: str,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    text_match: bool = False,
) -> Any:
    params: Dict[str, Any] = {"q": q, "sort": sort, "order": order, "per_page": per_page, "page": page}
    params = {k: v for k, v in params.items() if v is not None}
    headers = {"Accept": "application/vnd.github.text-match+json"} if text_match else None
    return client.request("GET", "/search/users", params=params, headers=headers)
