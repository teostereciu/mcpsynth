from typing import Any, Dict, Optional

from ._client import gh_request


def search_code(q: str, *, sort: Optional[str] = None, order: str = "desc", per_page: int = 30, page: int = 1) -> Any:
    params: Dict[str, Any] = {"q": q, "order": order, "per_page": per_page, "page": page}
    if sort:
        params["sort"] = sort
    return gh_request("GET", "/search/code", params=params)


def search_issues(q: str, *, sort: Optional[str] = None, order: str = "desc", per_page: int = 30, page: int = 1) -> Any:
    params: Dict[str, Any] = {"q": q, "order": order, "per_page": per_page, "page": page}
    if sort:
        params["sort"] = sort
    return gh_request("GET", "/search/issues", params=params)


def search_repositories(q: str, *, sort: Optional[str] = None, order: str = "desc", per_page: int = 30, page: int = 1) -> Any:
    params: Dict[str, Any] = {"q": q, "order": order, "per_page": per_page, "page": page}
    if sort:
        params["sort"] = sort
    return gh_request("GET", "/search/repositories", params=params)
