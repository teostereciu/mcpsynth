from typing import Any, Dict, Optional

from .github_client import GitHubClient


def search_code(
    client: GitHubClient,
    *,
    q: str,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    per_page: Optional[int] = None,
    page: Optional[int] = None,
    text_match: bool = False,
) -> Dict[str, Any]:
    """GET /search/code"""
    accept = "application/vnd.github.text-match+json" if text_match else None
    return client.request(
        "GET",
        "/search/code",
        params={"q": q, "sort": sort, "order": order, "per_page": per_page, "page": page},
        accept=accept,
    )


def search_issues_and_prs(
    client: GitHubClient,
    *,
    q: str,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    per_page: Optional[int] = None,
    page: Optional[int] = None,
    text_match: bool = False,
) -> Dict[str, Any]:
    """GET /search/issues"""
    accept = "application/vnd.github.text-match+json" if text_match else None
    return client.request(
        "GET",
        "/search/issues",
        params={"q": q, "sort": sort, "order": order, "per_page": per_page, "page": page},
        accept=accept,
    )


def search_repositories(
    client: GitHubClient,
    *,
    q: str,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    per_page: Optional[int] = None,
    page: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /search/repositories"""
    return client.request(
        "GET",
        "/search/repositories",
        params={"q": q, "sort": sort, "order": order, "per_page": per_page, "page": page},
    )
