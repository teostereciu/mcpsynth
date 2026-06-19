from typing import Any, Dict, Optional

from ._client import request_json, split_owner_repo


def get_repo_content(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    path: str = "",
    ref: Optional[str] = None,
    accept: Optional[str] = None,
) -> Any:
    """GET /repos/{owner}/{repo}/contents/{path}

    Gets the contents of a file or directory in a repository.
    """
    if owner is None or repo is None:
        parts = split_owner_repo(owner_repo)
        owner = owner or parts["owner"]
        repo = repo or parts["repo"]

    params: Dict[str, Any] = {}
    if ref is not None:
        params["ref"] = ref

    # GitHub allows omitting path to list root; keep URL correct.
    if path:
        api_path = f"/repos/{owner}/{repo}/contents/{path}"
    else:
        api_path = f"/repos/{owner}/{repo}/contents"

    return request_json("GET", api_path, params=params or None, accept=accept)


def create_or_update_file_contents(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    path: str,
    message: str,
    content_base64: str,
    sha: Optional[str] = None,
    branch: Optional[str] = None,
    committer: Optional[Dict[str, Any]] = None,
    author: Optional[Dict[str, Any]] = None,
    accept: Optional[str] = None,
) -> Any:
    """PUT /repos/{owner}/{repo}/contents/{path}

    Creates a new file or replaces an existing file in a repository.
    """
    if owner is None or repo is None:
        parts = split_owner_repo(owner_repo)
        owner = owner or parts["owner"]
        repo = repo or parts["repo"]

    payload: Dict[str, Any] = {"message": message, "content": content_base64}
    if sha is not None:
        payload["sha"] = sha
    if branch is not None:
        payload["branch"] = branch
    if committer is not None:
        payload["committer"] = committer
    if author is not None:
        payload["author"] = author

    return request_json("PUT", f"/repos/{owner}/{repo}/contents/{path}", json=payload, accept=accept)


def delete_file(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    path: str,
    message: str,
    sha: str,
    branch: Optional[str] = None,
    committer: Optional[Dict[str, Any]] = None,
    author: Optional[Dict[str, Any]] = None,
    accept: Optional[str] = None,
) -> Any:
    """DELETE /repos/{owner}/{repo}/contents/{path}

    Deletes a file in a repository.
    """
    if owner is None or repo is None:
        parts = split_owner_repo(owner_repo)
        owner = owner or parts["owner"]
        repo = repo or parts["repo"]

    payload: Dict[str, Any] = {"message": message, "sha": sha}
    if branch is not None:
        payload["branch"] = branch
    if committer is not None:
        payload["committer"] = committer
    if author is not None:
        payload["author"] = author

    return request_json("DELETE", f"/repos/{owner}/{repo}/contents/{path}", json=payload, accept=accept)


def list_org_repos(
    *,
    org: str,
    type: str = "all",
    sort: str = "created",
    direction: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    accept: Optional[str] = None,
) -> Any:
    """GET /orgs/{org}/repos

    Lists repositories for the specified organization.
    """
    params: Dict[str, Any] = {"type": type, "sort": sort, "per_page": per_page, "page": page}
    if direction is not None:
        params["direction"] = direction
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
    accept: Optional[str] = None,
) -> Any:
    """POST /orgs/{org}/repos

    Creates a new repository in the specified organization.
    """
    payload: Dict[str, Any] = {
        "name": name,
        "private": private,
        "has_issues": has_issues,
        "has_projects": has_projects,
        "has_wiki": has_wiki,
        "has_downloads": has_downloads,
        "is_template": is_template,
        "auto_init": auto_init,
        "allow_squash_merge": allow_squash_merge,
        "allow_merge_commit": allow_merge_commit,
        "allow_rebase_merge": allow_rebase_merge,
        "allow_auto_merge": allow_auto_merge,
        "delete_branch_on_merge": delete_branch_on_merge,
    }
    for k, v in {
        "description": description,
        "homepage": homepage,
        "visibility": visibility,
        "team_id": team_id,
        "gitignore_template": gitignore_template,
        "license_template": license_template,
        "squash_merge_commit_title": squash_merge_commit_title,
        "squash_merge_commit_message": squash_merge_commit_message,
        "merge_commit_title": merge_commit_title,
        "merge_commit_message": merge_commit_message,
        "custom_properties": custom_properties,
    }.items():
        if v is not None:
            payload[k] = v

    return request_json("POST", f"/orgs/{org}/repos", json=payload, accept=accept)
