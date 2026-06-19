from typing import Any, Dict, Optional

from ._client import GitHubClient


def search_code(
    *,
    q: str,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    text_match: bool = False,
) -> Dict[str, Any]:
    """GET /search/code - Search code."""
    c = GitHubClient()
    headers = {"Accept": "application/vnd.github.text-match+json"} if text_match else None
    return c.request(
        "GET",
        "/search/code",
        params={"q": q, "sort": sort, "order": order, "per_page": per_page, "page": page},
        headers=headers,
    )


def search_issues(
    *,
    q: str,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    text_match: bool = False,
) -> Dict[str, Any]:
    """GET /search/issues - Search issues and pull requests."""
    c = GitHubClient()
    headers = {"Accept": "application/vnd.github.text-match+json"} if text_match else None
    return c.request(
        "GET",
        "/search/issues",
        params={"q": q, "sort": sort, "order": order, "per_page": per_page, "page": page},
        headers=headers,
    )


def search_repositories(
    *,
    q: str,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    text_match: bool = False,
) -> Dict[str, Any]:
    """GET /search/repositories - Search repositories."""
    c = GitHubClient()
    headers = {"Accept": "application/vnd.github.text-match+json"} if text_match else None
    return c.request(
        "GET",
        "/search/repositories",
        params={"q": q, "sort": sort, "order": order, "per_page": per_page, "page": page},
        headers=headers,
    )
