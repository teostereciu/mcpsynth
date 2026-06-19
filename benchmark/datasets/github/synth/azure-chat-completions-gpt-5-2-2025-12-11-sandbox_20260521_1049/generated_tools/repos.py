from typing import Any, Dict, Optional

from .http_client import request_json


def get_repo(*, owner: str, repo: str, accept: str = "application/vnd.github+json") -> Any:
    """GET /repos/{owner}/{repo} - Get a repository."""
    _, data, _ = request_json("GET", f"/repos/{owner}/{repo}", accept=accept)
    return data


def list_org_repos(
    *,
    org: str,
    type: str = "all",
    sort: str = "created",
    direction: str = "desc",
    per_page: int = 30,
    page: int = 1,
    accept: str = "application/vnd.github+json",
) -> Any:
    """GET /orgs/{org}/repos - List organization repositories."""
    _, data, _ = request_json(
        "GET",
        f"/orgs/{org}/repos",
        params={
            "type": type,
            "sort": sort,
            "direction": direction,
            "per_page": per_page,
            "page": page,
        },
        accept=accept,
    )
    return data


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
    auto_init: bool = False,
    is_template: bool = False,
    delete_branch_on_merge: Optional[bool] = None,
    allow_squash_merge: Optional[bool] = None,
    allow_merge_commit: Optional[bool] = None,
    allow_rebase_merge: Optional[bool] = None,
    allow_auto_merge: Optional[bool] = None,
    accept: str = "application/vnd.github+json",
) -> Any:
    """POST /orgs/{org}/repos - Create an organization repository."""
    _, data, _ = request_json(
        "POST",
        f"/orgs/{org}/repos",
        json_body={
            "name": name,
            "description": description,
            "homepage": homepage,
            "private": private,
            "visibility": visibility,
            "has_issues": has_issues,
            "has_projects": has_projects,
            "has_wiki": has_wiki,
            "auto_init": auto_init,
            "is_template": is_template,
            "delete_branch_on_merge": delete_branch_on_merge,
            "allow_squash_merge": allow_squash_merge,
            "allow_merge_commit": allow_merge_commit,
            "allow_rebase_merge": allow_rebase_merge,
            "allow_auto_merge": allow_auto_merge,
        },
        accept=accept,
    )
    return data


def update_repo(
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
    is_template: Optional[bool] = None,
    archived: Optional[bool] = None,
    allow_squash_merge: Optional[bool] = None,
    allow_merge_commit: Optional[bool] = None,
    allow_rebase_merge: Optional[bool] = None,
    allow_auto_merge: Optional[bool] = None,
    delete_branch_on_merge: Optional[bool] = None,
    accept: str = "application/vnd.github+json",
) -> Any:
    """PATCH /repos/{owner}/{repo} - Update a repository."""
    _, data, _ = request_json(
        "PATCH",
        f"/repos/{owner}/{repo}",
        json_body={
            "name": name,
            "description": description,
            "homepage": homepage,
            "private": private,
            "visibility": visibility,
            "default_branch": default_branch,
            "has_issues": has_issues,
            "has_projects": has_projects,
            "has_wiki": has_wiki,
            "is_template": is_template,
            "archived": archived,
            "allow_squash_merge": allow_squash_merge,
            "allow_merge_commit": allow_merge_commit,
            "allow_rebase_merge": allow_rebase_merge,
            "allow_auto_merge": allow_auto_merge,
            "delete_branch_on_merge": delete_branch_on_merge,
        },
        accept=accept,
    )
    return data


def delete_repo(*, owner: str, repo: str, accept: str = "application/vnd.github+json") -> Any:
    """DELETE /repos/{owner}/{repo} - Delete a repository."""
    _, data, _ = request_json("DELETE", f"/repos/{owner}/{repo}", accept=accept)
    return {"deleted": True} if data is None else data
