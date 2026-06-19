from typing import Any, Optional

from .http_client import request_json


# docs/api_search-search.md

def search_code(
    *,
    q: str,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    accept: Optional[str] = None,
) -> Any:
    return request_json(
        "GET",
        "/search/code",
        accept=accept,
        params={"q": q, "sort": sort, "order": order, "per_page": per_page, "page": page},
    )


# docs/api_search-search.md

def search_issues_and_pull_requests(
    *,
    q: str,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    accept: Optional[str] = None,
) -> Any:
    return request_json(
        "GET",
        "/search/issues",
        accept=accept,
        params={"q": q, "sort": sort, "order": order, "per_page": per_page, "page": page},
    )


# docs/api_search-search.md

def search_repositories(
    *,
    q: str,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    accept: Optional[str] = None,
) -> Any:
    return request_json(
        "GET",
        "/search/repositories",
        accept=accept,
        params={"q": q, "sort": sort, "order": order, "per_page": per_page, "page": page},
    )
