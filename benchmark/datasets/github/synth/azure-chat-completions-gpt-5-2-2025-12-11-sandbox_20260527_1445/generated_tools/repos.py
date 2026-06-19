from typing import Any, Dict, Optional

from ._client import gh_request, parse_owner_repo


def get_repo(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo required (or set GITHUB_TEST_REPO)"}
    return gh_request("GET", f"/repos/{o}/{r}")


def list_org_repos(
    *,
    org: str,
    type: Optional[str] = None,
    sort: Optional[str] = None,
    direction: Optional[str] = None,
    per_page: Optional[int] = None,
    page: Optional[int] = None,
) -> Any:
    return gh_request(
        "GET",
        f"/orgs/{org}/repos",
        params={
            "type": type,
            "sort": sort,
            "direction": direction,
            "per_page": per_page,
            "page": page,
        },
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
    }.items():
        if v is not None:
            payload[k] = v
    return gh_request("POST", f"/orgs/{org}/repos", json=payload)


def create_user_repo(
    *,
    name: str,
    description: Optional[str] = None,
    homepage: Optional[str] = None,
    private: Optional[bool] = None,
    has_issues: Optional[bool] = None,
    has_projects: Optional[bool] = None,
    has_wiki: Optional[bool] = None,
    auto_init: Optional[bool] = None,
) -> Any:
    payload: Dict[str, Any] = {"name": name}
    for k, v in {
        "description": description,
        "homepage": homepage,
        "private": private,
        "has_issues": has_issues,
        "has_projects": has_projects,
        "has_wiki": has_wiki,
        "auto_init": auto_init,
    }.items():
        if v is not None:
            payload[k] = v
    return gh_request("POST", "/user/repos", json=payload)


def fork_repo(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    organization: Optional[str] = None,
    name: Optional[str] = None,
    default_branch_only: Optional[bool] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo required (or set GITHUB_TEST_REPO)"}
    payload: Dict[str, Any] = {}
    for k, v in {
        "organization": organization,
        "name": name,
        "default_branch_only": default_branch_only,
    }.items():
        if v is not None:
            payload[k] = v
    return gh_request("POST", f"/repos/{o}/{r}/forks", json=payload or None)


def list_forks(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    sort: Optional[str] = None,
    per_page: Optional[int] = None,
    page: Optional[int] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo required (or set GITHUB_TEST_REPO)"}
    return gh_request(
        "GET",
        f"/repos/{o}/{r}/forks",
        params={"sort": sort, "per_page": per_page, "page": page},
    )
