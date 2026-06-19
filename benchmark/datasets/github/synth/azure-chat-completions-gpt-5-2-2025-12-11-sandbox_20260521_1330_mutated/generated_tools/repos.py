from typing import Any, Dict, Optional

from ._client import get_client


def get_repository(owner: str, repo: str) -> Any:
    """GET /repos/{owner}/{repo}"""
    return get_client().request("GET", f"/repos/{owner}/{repo}")


def list_org_repositories(
    org: str,
    type: str = "all",
    sort: str = "created",
    direction: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
) -> Any:
    """GET /orgs/{org}/repos"""
    return get_client().request(
        "GET",
        f"/orgs/{org}/repos",
        params={"type": type, "sort": sort, "direction": direction, "per_page": per_page, "page": page},
    )


def create_org_repository(
    org: str,
    name: str,
    description: Optional[str] = None,
    homepage: Optional[str] = None,
    private: bool = False,
    visibility: Optional[str] = None,
    has_issues: bool = True,
    has_projects: Optional[bool] = True,
    has_wiki: bool = True,
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
) -> Any:
    """POST /orgs/{org}/repos"""
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
    return get_client().request("POST", f"/orgs/{org}/repos", json=payload, expected=(201,))


def create_user_repository(
    name: str,
    description: Optional[str] = None,
    homepage: Optional[str] = None,
    private: bool = False,
    visibility: Optional[str] = None,
    has_issues: bool = True,
    has_projects: Optional[bool] = True,
    has_wiki: bool = True,
    is_template: bool = False,
    auto_init: bool = False,
    gitignore_template: Optional[str] = None,
    license_template: Optional[str] = None,
) -> Any:
    """POST /user/repos"""
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
    return get_client().request("POST", "/user/repos", json=payload, expected=(201,))


def update_repository(
    owner: str,
    repo: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    homepage: Optional[str] = None,
    private: Optional[bool] = None,
    visibility: Optional[str] = None,
    has_issues: Optional[bool] = None,
    has_projects: Optional[bool] = None,
    has_wiki: Optional[bool] = None,
    default_branch: Optional[str] = None,
    allow_squash_merge: Optional[bool] = None,
    allow_merge_commit: Optional[bool] = None,
    allow_rebase_merge: Optional[bool] = None,
    allow_auto_merge: Optional[bool] = None,
    delete_branch_on_merge: Optional[bool] = None,
) -> Any:
    """PATCH /repos/{owner}/{repo}"""
    payload: Dict[str, Any] = {
        "name": name,
        "description": description,
        "homepage": homepage,
        "private": private,
        "visibility": visibility,
        "has_issues": has_issues,
        "has_projects": has_projects,
        "has_wiki": has_wiki,
        "default_branch": default_branch,
        "allow_squash_merge": allow_squash_merge,
        "allow_merge_commit": allow_merge_commit,
        "allow_rebase_merge": allow_rebase_merge,
        "allow_auto_merge": allow_auto_merge,
        "delete_branch_on_merge": delete_branch_on_merge,
    }
    return get_client().request("PATCH", f"/repos/{owner}/{repo}", json=payload)


def delete_repository(owner: str, repo: str) -> Any:
    """DELETE /repos/{owner}/{repo}"""
    return get_client().request("DELETE", f"/repos/{owner}/{repo}", expected=(204,))


def fork_repository(owner: str, repo: str, organization: Optional[str] = None, name: Optional[str] = None) -> Any:
    """POST /repos/{owner}/{repo}/forks"""
    payload: Dict[str, Any] = {"organization": organization, "name": name}
    return get_client().request("POST", f"/repos/{owner}/{repo}/forks", json=payload, expected=(202, 201))
