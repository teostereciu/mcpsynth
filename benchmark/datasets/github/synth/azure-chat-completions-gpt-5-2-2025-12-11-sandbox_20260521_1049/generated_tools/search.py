from typing import Any, Optional

from .http_client import request_json


def search_code(
    *,
    q: str,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    accept: str = "application/vnd.github+json",
) -> Any:
    """GET /search/code - Search code."""
    _, data, _ = request_json(
        "GET",
        "/search/code",
        params={"q": q, "sort": sort, "order": order, "per_page": per_page, "page": page},
        accept=accept,
    )
    return data


def search_issues_and_prs(
    *,
    q: str,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    accept: str = "application/vnd.github+json",
) -> Any:
    """GET /search/issues - Search issues and pull requests."""
    _, data, _ = request_json(
        "GET",
        "/search/issues",
        params={"q": q, "sort": sort, "order": order, "per_page": per_page, "page": page},
        accept=accept,
    )
    return data


def search_repositories(
    *,
    q: str,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    accept: str = "application/vnd.github+json",
) -> Any:
    """GET /search/repositories - Search repositories."""
    _, data, _ = request_json(
        "GET",
        "/search/repositories",
        params={"q": q, "sort": sort, "order": order, "per_page": per_page, "page": page},
        accept=accept,
    )
    return data
