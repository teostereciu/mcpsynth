from typing import Any, Dict, Optional

from .http_client import request_json


# Source doc: docs/api_repos-repos.md


def list_org_repos(
    *,
    org: str,
    type: Optional[str] = None,
    sort: Optional[str] = None,
    direction: Optional[str] = None,
    per_page: Optional[int] = None,
    page: Optional[int] = None,
    accept: Optional[str] = None,
) -> Any:
    return request_json(
        "GET",
        "/orgs/{org}/repos",
        path_params={"org": org},
        query={
            "type": type,
            "sort": sort,
            "direction": direction,
            "per_page": per_page,
            "page": page,
        },
        accept=accept,
    )


def create_org_repo(
    *,
    org: str,
    name: str,
    description: Optional[str] = None,
    homepage: Optional[str] = None,
    private: Optional[bool] = None,
    visibility: Optional[str] = None,
    has_issues: Optional[bool] = None,
    has_projects: Optional[bool] = None,
    has_wiki: Optional[bool] = None,
    has_downloads: Optional[bool] = None,
    is_template: Optional[bool] = None,
    team_id: Optional[int] = None,
    auto_init: Optional[bool] = None,
    gitignore_template: Optional[str] = None,
    license_template: Optional[str] = None,
    allow_squash_merge: Optional[bool] = None,
    allow_merge_commit: Optional[bool] = None,
    allow_rebase_merge: Optional[bool] = None,
    allow_auto_merge: Optional[bool] = None,
    delete_branch_on_merge: Optional[bool] = None,
    squash_merge_commit_title: Optional[str] = None,
    squash_merge_commit_message: Optional[str] = None,
    merge_commit_title: Optional[str] = None,
    merge_commit_message: Optional[str] = None,
    custom_properties: Optional[Dict[str, Any]] = None,
    accept: Optional[str] = None,
) -> Any:
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
    return request_json(
        "POST",
        "/orgs/{org}/repos",
        path_params={"org": org},
        body={k: v for k, v in body.items() if v is not None},
        accept=accept,
    )
