from typing import Any, Dict, Optional

from .github_client import GitHubClient


def get_repo(client: GitHubClient, *, owner: str, repo: str) -> Any:
    return client.request("GET", f"/repos/{owner}/{repo}")


def list_org_repos(
    client: GitHubClient,
    *,
    org: str,
    type: str = "all",
    sort: str = "created",
    direction: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
) -> Any:
    params: Dict[str, Any] = {"type": type, "sort": sort, "per_page": per_page, "page": page}
    if direction is not None:
        params["direction"] = direction
    return client.request("GET", f"/orgs/{org}/repos", params=params)


def list_user_repos(
    client: GitHubClient,
    *,
    username: str,
    type: str = "owner",
    sort: str = "full_name",
    direction: str = "asc",
    per_page: int = 30,
    page: int = 1,
) -> Any:
    return client.request(
        "GET",
        f"/users/{username}/repos",
        params={"type": type, "sort": sort, "direction": direction, "per_page": per_page, "page": page},
    )


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
) -> Any:
    payload: Dict[str, Any] = {"name": name}
    for k, v in {
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
    }.items():
        if v is not None:
            payload[k] = v
    return client.request("POST", f"/orgs/{org}/repos", json=payload)


def delete_repo(client: GitHubClient, *, owner: str, repo: str) -> Any:
    return client.request("DELETE", f"/repos/{owner}/{repo}")
