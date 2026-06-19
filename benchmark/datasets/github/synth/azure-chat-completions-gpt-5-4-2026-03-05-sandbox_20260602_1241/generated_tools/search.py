from typing import Optional

from generated_tools.github_common import compact, github_request


def search_repositories(q: str, sort: Optional[str] = None, order: str = "desc", per_page: int = 30, page: int = 1) -> str:
    return compact(github_request("GET", "/search/repositories", params={"q": q, "sort": sort, "order": order, "per_page": per_page, "page": page}))


def search_code(q: str, sort: Optional[str] = None, order: str = "desc", per_page: int = 30, page: int = 1) -> str:
    return compact(github_request("GET", "/search/code", params={"q": q, "sort": sort, "order": order, "per_page": per_page, "page": page}))


def search_issues_and_pull_requests(q: str, sort: Optional[str] = None, order: str = "desc", per_page: int = 30, page: int = 1) -> str:
    return compact(github_request("GET", "/search/issues", params={"q": q, "sort": sort, "order": order, "per_page": per_page, "page": page}))


def search_users(q: str, sort: Optional[str] = None, order: str = "desc", per_page: int = 30, page: int = 1) -> str:
    return compact(github_request("GET", "/search/users", params={"q": q, "sort": sort, "order": order, "per_page": per_page, "page": page}))
