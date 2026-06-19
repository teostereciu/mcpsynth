from typing import Any, Dict, Optional

from .http_client import request_json, parse_owner_repo


# docs/api_repos-repos.md

def list_org_repos(
    *,
    org: str,
    type: Optional[str] = None,
    sort: Optional[str] = None,
    direction: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    accept: Optional[str] = None,
) -> Any:
    return request_json(
        "GET",
        f"/orgs/{org}/repos",
        accept=accept,
        params={
            "type": type,
            "sort": sort,
            "direction": direction,
            "per_page": per_page,
            "page": page,
        },
    )


# docs/api_repos-repos.md

def get_repo(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    accept: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo is required (or set GITHUB_TEST_REPO)"}
    return request_json("GET", f"/repos/{o}/{r}", accept=accept)


# docs/api_repos-repos.md

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
    accept: Optional[str] = None,
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
    }.items():
        if v is not None:
            payload[k] = v

    return request_json("POST", f"/orgs/{org}/repos", accept=accept, json=payload)


# docs/api_repos-repos.md

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
    has_issues: Optional[bool] = None,
    has_projects: Optional[bool] = None,
    has_wiki: Optional[bool] = None,
    is_template: Optional[bool] = None,
    default_branch: Optional[str] = None,
    allow_squash_merge: Optional[bool] = None,
    allow_merge_commit: Optional[bool] = None,
    allow_rebase_merge: Optional[bool] = None,
    allow_auto_merge: Optional[bool] = None,
    delete_branch_on_merge: Optional[bool] = None,
    accept: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo is required (or set GITHUB_TEST_REPO)"}

    payload: Dict[str, Any] = {}
    for k, v in {
        "name": name,
        "description": description,
        "homepage": homepage,
        "private": private,
        "visibility": visibility,
        "has_issues": has_issues,
        "has_projects": has_projects,
        "has_wiki": has_wiki,
        "is_template": is_template,
        "default_branch": default_branch,
        "allow_squash_merge": allow_squash_merge,
        "allow_merge_commit": allow_merge_commit,
        "allow_rebase_merge": allow_rebase_merge,
        "allow_auto_merge": allow_auto_merge,
        "delete_branch_on_merge": delete_branch_on_merge,
    }.items():
        if v is not None:
            payload[k] = v

    return request_json("PATCH", f"/repos/{o}/{r}", accept=accept, json=payload)
