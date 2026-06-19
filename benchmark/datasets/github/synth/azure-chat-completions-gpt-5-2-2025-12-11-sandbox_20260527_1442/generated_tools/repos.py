from typing import Any, Dict, Optional

from ._client import gh_request


def list_org_repos(
    org: str,
    type: str = "all",
    sort: str = "created",
    direction: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
) -> Any:
    """GET /orgs/{org}/repos"""
    params: Dict[str, Any] = {
        "type": type,
        "sort": sort,
        "per_page": per_page,
        "page": page,
    }
    if direction is not None:
        params["direction"] = direction
    return gh_request("GET", f"/orgs/{org}/repos", params=params)


def create_org_repo(
    org: str,
    name: str,
    description: Optional[str] = None,
    homepage: Optional[str] = None,
    private: bool = False,
    visibility: Optional[str] = None,
    has_issues: bool = True,
    has_projects: bool = True,
    has_wiki: bool = True,
    auto_init: bool = False,
    is_template: bool = False,
) -> Any:
    """POST /orgs/{org}/repos"""
    payload: Dict[str, Any] = {
        "name": name,
        "private": private,
        "has_issues": has_issues,
        "has_projects": has_projects,
        "has_wiki": has_wiki,
        "auto_init": auto_init,
        "is_template": is_template,
    }
    if description is not None:
        payload["description"] = description
    if homepage is not None:
        payload["homepage"] = homepage
    if visibility is not None:
        payload["visibility"] = visibility
    return gh_request("POST", f"/orgs/{org}/repos", json=payload)
