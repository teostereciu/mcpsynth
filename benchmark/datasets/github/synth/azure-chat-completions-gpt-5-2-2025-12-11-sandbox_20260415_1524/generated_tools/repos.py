from __future__ import annotations

from typing import Any, Dict, Optional

from .github_client import GitHubClient


def get_repo(client: GitHubClient, *, owner: str, repo: str) -> Any:
    return client.request("GET", f"/repos/{owner}/{repo}")


def list_org_repos(
    client: GitHubClient,
    *,
    org: str,
    type: Optional[str] = None,
    sort: Optional[str] = None,
    direction: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    paginate: bool = False,
) -> Any:
    params: Dict[str, Any] = {
        "type": type,
        "sort": sort,
        "direction": direction,
        "per_page": per_page,
        "page": page,
    }
    params = {k: v for k, v in params.items() if v is not None}
    return client.request("GET", f"/orgs/{org}/repos", params=params, paginate=paginate)


def list_user_repos(
    client: GitHubClient,
    *,
    username: str,
    type: Optional[str] = None,
    sort: Optional[str] = None,
    direction: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    paginate: bool = False,
) -> Any:
    params: Dict[str, Any] = {
        "type": type,
        "sort": sort,
        "direction": direction,
        "per_page": per_page,
        "page": page,
    }
    params = {k: v for k, v in params.items() if v is not None}
    return client.request("GET", f"/users/{username}/repos", params=params, paginate=paginate)


def create_org_repo(
    client: GitHubClient,
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
) -> Any:
    payload: Dict[str, Any] = {
        "name": name,
        "description": description,
        "homepage": homepage,
        "private": private,
        "visibility": visibility,
        "has_issues": has_issues,
        "has_projects": has_projects,
        "has_wiki": has_wiki,
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
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    return client.request("POST", f"/orgs/{org}/repos", json=payload)


def create_user_repo(
    client: GitHubClient,
    *,
    name: str,
    description: Optional[str] = None,
    homepage: Optional[str] = None,
    private: Optional[bool] = None,
    visibility: Optional[str] = None,
    has_issues: Optional[bool] = None,
    has_projects: Optional[bool] = None,
    has_wiki: Optional[bool] = None,
    is_template: Optional[bool] = None,
    auto_init: Optional[bool] = None,
    gitignore_template: Optional[str] = None,
    license_template: Optional[str] = None,
) -> Any:
    payload: Dict[str, Any] = {
        "name": name,
        "description": description,
        "homepage": homepage,
        "private": private,
        "visibility": visibility,
        "has_issues": has_issues,
        "has_projects": has_projects,
        "has_wiki": has_wiki,
        "is_template": is_template,
        "auto_init": auto_init,
        "gitignore_template": gitignore_template,
        "license_template": license_template,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    return client.request("POST", "/user/repos", json=payload)


def fork_repo(client: GitHubClient, *, owner: str, repo: str, organization: Optional[str] = None, name: Optional[str] = None, default_branch_only: Optional[bool] = None) -> Any:
    payload: Dict[str, Any] = {"organization": organization, "name": name, "default_branch_only": default_branch_only}
    payload = {k: v for k, v in payload.items() if v is not None}
    return client.request("POST", f"/repos/{owner}/{repo}/forks", json=payload if payload else None)


def update_repo(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    homepage: Optional[str] = None,
    private: Optional[bool] = None,
    visibility: Optional[str] = None,
    default_branch: Optional[str] = None,
    has_issues: Optional[bool] = None,
    has_projects: Optional[bool] = None,
    has_wiki: Optional[bool] = None,
    allow_squash_merge: Optional[bool] = None,
    allow_merge_commit: Optional[bool] = None,
    allow_rebase_merge: Optional[bool] = None,
    allow_auto_merge: Optional[bool] = None,
    delete_branch_on_merge: Optional[bool] = None,
) -> Any:
    payload: Dict[str, Any] = {
        "name": name,
        "description": description,
        "homepage": homepage,
        "private": private,
        "visibility": visibility,
        "default_branch": default_branch,
        "has_issues": has_issues,
        "has_projects": has_projects,
        "has_wiki": has_wiki,
        "allow_squash_merge": allow_squash_merge,
        "allow_merge_commit": allow_merge_commit,
        "allow_rebase_merge": allow_rebase_merge,
        "allow_auto_merge": allow_auto_merge,
        "delete_branch_on_merge": delete_branch_on_merge,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    return client.request("PATCH", f"/repos/{owner}/{repo}", json=payload)
