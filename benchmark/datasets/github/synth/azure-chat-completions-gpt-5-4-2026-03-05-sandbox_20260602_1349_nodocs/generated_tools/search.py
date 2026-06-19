from typing import Any, Optional

from generated_tools.github_common import clean_params, github_request


def search_code(q: str, sort: Optional[str] = None, order: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    return github_request("GET", "/search/code", params=clean_params(q=q, sort=sort, order=order, per_page=per_page, page=page))


def search_issues_and_pull_requests(q: str, sort: Optional[str] = None, order: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    return github_request("GET", "/search/issues", params=clean_params(q=q, sort=sort, order=order, per_page=per_page, page=page))


def search_repositories(q: str, sort: Optional[str] = None, order: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    return github_request("GET", "/search/repositories", params=clean_params(q=q, sort=sort, order=order, per_page=per_page, page=page))
