from typing import Any, Dict, Optional

from ._client import get_client


def search_code(q: str, sort: Optional[str] = None, order: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    """GET /search/code"""
    return get_client().request(
        "GET",
        "/search/code",
        params={"q": q, "sort": sort, "order": order, "per_page": per_page, "page": page},
    )


def search_issues_and_pull_requests(
    q: str,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
) -> Any:
    """GET /search/issues"""
    return get_client().request(
        "GET",
        "/search/issues",
        params={"q": q, "sort": sort, "order": order, "per_page": per_page, "page": page},
    )


def search_repositories(
    q: str,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
) -> Any:
    """GET /search/repositories"""
    return get_client().request(
        "GET",
        "/search/repositories",
        params={"q": q, "sort": sort, "order": order, "per_page": per_page, "page": page},
    )


def search_users(
    q: str,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
) -> Any:
    """GET /search/users"""
    return get_client().request(
        "GET",
        "/search/users",
        params={"q": q, "sort": sort, "order": order, "per_page": per_page, "page": page},
    )


def search_commits(
    q: str,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    text_match: bool = False,
) -> Any:
    """GET /search/commits"""
    headers: Dict[str, str] = {}
    if text_match:
        headers["Accept"] = "application/vnd.github.text-match+json"
    return get_client().request(
        "GET",
        "/search/commits",
        params={"q": q, "sort": sort, "order": order, "per_page": per_page, "page": page},
        headers=headers or None,
    )
