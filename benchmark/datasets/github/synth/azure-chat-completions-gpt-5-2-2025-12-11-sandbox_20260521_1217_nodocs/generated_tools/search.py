from typing import Any, Dict, Optional

from .http import request_json


def search_code(q: str, *, sort: Optional[str] = None, order: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    params: Dict[str, Any] = {"q": q, "per_page": per_page, "page": page}
    if sort:
        params["sort"] = sort
    if order:
        params["order"] = order
    return request_json("GET", "/search/code", params=params)


def search_issues_and_prs(q: str, *, sort: Optional[str] = None, order: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    params: Dict[str, Any] = {"q": q, "per_page": per_page, "page": page}
    if sort:
        params["sort"] = sort
    if order:
        params["order"] = order
    return request_json("GET", "/search/issues", params=params)


def search_repositories(q: str, *, sort: Optional[str] = None, order: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    params: Dict[str, Any] = {"q": q, "per_page": per_page, "page": page}
    if sort:
        params["sort"] = sort
    if order:
        params["order"] = order
    return request_json("GET", "/search/repositories", params=params)
