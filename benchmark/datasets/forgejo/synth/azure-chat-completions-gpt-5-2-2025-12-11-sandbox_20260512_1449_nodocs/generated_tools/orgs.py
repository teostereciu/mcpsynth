from typing import Any, Dict, Optional

from .client import request_json


def list_my_orgs(page: Optional[int] = None, limit: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {}
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    return request_json("GET", "/user/orgs", params=params if params else None)


def get_org(org: str) -> Any:
    return request_json("GET", f"/orgs/{org}")


def list_org_repos(org: str, page: Optional[int] = None, limit: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {}
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    return request_json("GET", f"/orgs/{org}/repos", params=params if params else None)
