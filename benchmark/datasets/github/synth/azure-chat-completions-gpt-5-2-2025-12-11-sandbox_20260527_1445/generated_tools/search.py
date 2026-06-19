from typing import Any, Optional

from ._client import gh_request


def search_code(
    *,
    q: str,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    per_page: Optional[int] = None,
    page: Optional[int] = None,
    text_match: bool = False,
) -> Any:
    extra_headers = None
    if text_match:
        extra_headers = {"Accept": "application/vnd.github.text-match+json"}
    return gh_request(
        "GET",
        "/search/code",
        params={"q": q, "sort": sort, "order": order, "per_page": per_page, "page": page},
        extra_headers=extra_headers,
    )


def search_issues_and_prs(
    *,
    q: str,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    per_page: Optional[int] = None,
    page: Optional[int] = None,
    text_match: bool = False,
) -> Any:
    extra_headers = None
    if text_match:
        extra_headers = {"Accept": "application/vnd.github.text-match+json"}
    return gh_request(
        "GET",
        "/search/issues",
        params={"q": q, "sort": sort, "order": order, "per_page": per_page, "page": page},
        extra_headers=extra_headers,
    )


def search_repositories(
    *,
    q: str,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    per_page: Optional[int] = None,
    page: Optional[int] = None,
) -> Any:
    return gh_request(
        "GET",
        "/search/repositories",
        params={"q": q, "sort": sort, "order": order, "per_page": per_page, "page": page},
    )
