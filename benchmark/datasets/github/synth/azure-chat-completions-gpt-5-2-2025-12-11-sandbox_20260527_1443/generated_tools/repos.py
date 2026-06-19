from typing import Any, Dict, Optional

from ._client import request_json


def list_org_repos(
    *,
    org: str,
    type: str = "all",
    sort: str = "created",
    direction: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    accept: str = "application/vnd.github+json",
) -> Any:
    """GET /orgs/{org}/repos"""
    params: Dict[str, Any] = {
        "type": type,
        "sort": sort,
        "direction": direction,
        "per_page": per_page,
        "page": page,
    }
    return request_json("GET", f"/orgs/{org}/repos", params=params, accept=accept)


def create_org_repo(
    *,
    org: str,
    name: str,
    description: Optional[str] = None,
    homepage: Optional[str] = None,
    private: bool = False,
    visibility: Optional[str] = None,
    has_issues: bool = True,
    has_projects: bool = True,
    has_wiki: bool = True,
    has_downloads: bool = True,
    is_template: bool = False,
    team_id: Optional[int] = None,
    auto_init: bool = False,
    gitignore_template: Optional[str] = None,
    license_template: Optional[str] = None,
    allow_squash_merge: bool = True,
    allow_merge_commit: bool = True,
    allow_rebase_merge: bool = True,
    allow_auto_merge: bool = False,
    delete_branch_on_merge: bool = False,
    squash_merge_commit_title: Optional[str] = None,
    squash_merge_commit_message: Optional[str] = None,
    merge_commit_title: Optional[str] = None,
    merge_commit_message: Optional[str] = None,
    custom_properties: Optional[Dict[str, Any]] = None,
    accept: str = "application/vnd.github+json",
) -> Any:
    """POST /orgs/{org}/repos"""
    body: Dict[str, Any] = {
        "name": name,
        "description": description,
        "homepage": homepage,
        "private": private,
        "visibility": visibility,
        "has_issues": has_issues,
        "has_projects": has_projects,
        "has_wiki": has_wiki,
        "has_downloads": has_downloads,
        "is_template": is_template,
        "team_id": team_id,
        "auto_init": auto_init,
        "gitignore_template": gitignore_template,
        "license_template": license_template,
        "allow_squash_merge": allow_squash_merge,
        "allow_merge_commit": allow_merge_commit,
        "allow_rebase_merge": allow_rebase_merge,
        "allow_auto_merge": allow_auto_merge,
        "delete_branch_on_merge": delete_branch_on_merge,
        "squash_merge_commit_title": squash_merge_commit_title,
        "squash_merge_commit_message": squash_merge_commit_message,
        "merge_commit_title": merge_commit_title,
        "merge_commit_message": merge_commit_message,
        "custom_properties": custom_properties,
    }
    return request_json("POST", f"/orgs/{org}/repos", json=body, accept=accept)
