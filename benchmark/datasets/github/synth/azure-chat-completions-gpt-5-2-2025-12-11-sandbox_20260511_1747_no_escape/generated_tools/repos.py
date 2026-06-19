from typing import Any, Dict, List, Optional, Union

from .http_client import GitHubClient, parse_owner_repo


def get_repo(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """GET /repos/{owner}/{repo}"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    return client.request("GET", f"/repos/{o}/{r}", accept=accept)


def list_org_repos(
    *,
    org: str,
    type: str = "all",
    sort: str = "created",
    direction: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """GET /orgs/{org}/repos"""
    client = GitHubClient()
    params: Dict[str, Any] = {"type": type, "sort": sort, "per_page": per_page, "page": page}
    if direction is not None:
        params["direction"] = direction
    return client.request("GET", f"/orgs/{org}/repos", params=params, accept=accept)


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
    auto_init: Optional[bool] = None,
    gitignore_template: Optional[str] = None,
    license_template: Optional[str] = None,
    is_template: Optional[bool] = None,
    delete_branch_on_merge: Optional[bool] = None,
    allow_squash_merge: Optional[bool] = None,
    allow_merge_commit: Optional[bool] = None,
    allow_rebase_merge: Optional[bool] = None,
    allow_auto_merge: Optional[bool] = None,
    squash_merge_commit_title: Optional[str] = None,
    squash_merge_commit_message: Optional[str] = None,
    merge_commit_title: Optional[str] = None,
    merge_commit_message: Optional[str] = None,
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """POST /orgs/{org}/repos"""
    client = GitHubClient()
    payload: Dict[str, Any] = {"name": name}
    for k, v in {
        "description": description,
        "homepage": homepage,
        "private": private,
        "visibility": visibility,
        "has_issues": has_issues,
        "has_projects": has_projects,
        "has_wiki": has_wiki,
        "auto_init": auto_init,
        "gitignore_template": gitignore_template,
        "license_template": license_template,
        "is_template": is_template,
        "delete_branch_on_merge": delete_branch_on_merge,
        "allow_squash_merge": allow_squash_merge,
        "allow_merge_commit": allow_merge_commit,
        "allow_rebase_merge": allow_rebase_merge,
        "allow_auto_merge": allow_auto_merge,
        "squash_merge_commit_title": squash_merge_commit_title,
        "squash_merge_commit_message": squash_merge_commit_message,
        "merge_commit_title": merge_commit_title,
        "merge_commit_message": merge_commit_message,
    }.items():
        if v is not None:
            payload[k] = v
    return client.request("POST", f"/orgs/{org}/repos", json=payload, accept=accept)


def update_repo(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
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
    delete_branch_on_merge: Optional[bool] = None,
    allow_squash_merge: Optional[bool] = None,
    allow_merge_commit: Optional[bool] = None,
    allow_rebase_merge: Optional[bool] = None,
    allow_auto_merge: Optional[bool] = None,
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """PATCH /repos/{owner}/{repo}"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    payload: Dict[str, Any] = {}
    for k, v in {
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
        "delete_branch_on_merge": delete_branch_on_merge,
        "allow_squash_merge": allow_squash_merge,
        "allow_merge_commit": allow_merge_commit,
        "allow_rebase_merge": allow_rebase_merge,
        "allow_auto_merge": allow_auto_merge,
    }.items():
        if v is not None:
            payload[k] = v
    return client.request("PATCH", f"/repos/{o}/{r}", json=payload, accept=accept)


def delete_repo(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """DELETE /repos/{owner}/{repo}"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    return client.request("DELETE", f"/repos/{o}/{r}", accept=accept)


def fork_repo(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    organization: Optional[str] = None,
    name: Optional[str] = None,
    default_branch_only: Optional[bool] = None,
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """POST /repos/{owner}/{repo}/forks"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    payload: Dict[str, Any] = {}
    if organization is not None:
        payload["organization"] = organization
    if name is not None:
        payload["name"] = name
    if default_branch_only is not None:
        payload["default_branch_only"] = default_branch_only
    return client.request("POST", f"/repos/{o}/{r}/forks", json=payload or None, accept=accept)
