from typing import Any, Dict, Optional

from .http_client import request


def orgs_list(*, page: Optional[int] = None, limit: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {}
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    return request("GET", "/orgs", params=params or None)


def org_get(org: str) -> Any:
    return request("GET", f"/orgs/{org}")


def org_repos_list(org: str, *, page: Optional[int] = None, limit: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {}
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    return request("GET", f"/orgs/{org}/repos", params=params or None)
