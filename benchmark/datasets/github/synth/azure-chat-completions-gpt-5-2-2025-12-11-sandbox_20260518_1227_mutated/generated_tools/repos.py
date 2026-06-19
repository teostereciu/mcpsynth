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


def create_org_repo(
    client: GitHubClient,
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
    is_template: bool = False,
    auto_init: bool = False,
) -> Any:
    payload: Dict[str, Any] = {
        "name": name,
        "private": private,
        "has_issues": has_issues,
        "has_projects": has_projects,
        "has_wiki": has_wiki,
        "is_template": is_template,
        "auto_init": auto_init,
    }
    if description is not None:
        payload["description"] = description
    if homepage is not None:
        payload["homepage"] = homepage
    if visibility is not None:
        payload["visibility"] = visibility

    return client.request("POST", f"/orgs/{org}/repos", json=payload)


def update_repo(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    homepage: Optional[str] = None,
    private: Optional[bool] = None,
    default_branch: Optional[str] = None,
    has_issues: Optional[bool] = None,
    has_projects: Optional[bool] = None,
    has_wiki: Optional[bool] = None,
    archived: Optional[bool] = None,
) -> Any:
    payload: Dict[str, Any] = {}
    if name is not None:
        payload["name"] = name
    if description is not None:
        payload["description"] = description
    if homepage is not None:
        payload["homepage"] = homepage
    if private is not None:
        payload["private"] = private
    if default_branch is not None:
        payload["default_branch"] = default_branch
    if has_issues is not None:
        payload["has_issues"] = has_issues
    if has_projects is not None:
        payload["has_projects"] = has_projects
    if has_wiki is not None:
        payload["has_wiki"] = has_wiki
    if archived is not None:
        payload["archived"] = archived

    return client.request("PATCH", f"/repos/{owner}/{repo}", json=payload)
