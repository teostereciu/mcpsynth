from typing import Any, Dict, Optional

from ._client import GitHubClient


def get_repo(*, owner: str, repo: str) -> Dict[str, Any]:
    """GET /repos/{owner}/{repo} - Get a repository."""
    c = GitHubClient()
    return c.request("GET", f"/repos/{owner}/{repo}")


def list_org_repos(
    *,
    org: str,
    type: Optional[str] = None,
    sort: Optional[str] = None,
    direction: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
) -> Dict[str, Any]:
    """GET /orgs/{org}/repos - List organization repositories."""
    c = GitHubClient()
    return c.request(
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
    auto_init: Optional[bool] = None,
    gitignore_template: Optional[str] = None,
    license_template: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /orgs/{org}/repos - Create an organization repository."""
    c = GitHubClient()
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
    }.items():
        if v is not None:
            payload[k] = v
    return c.request("POST", f"/orgs/{org}/repos", json=payload)


def delete_repo(*, owner: str, repo: str) -> Dict[str, Any]:
    """DELETE /repos/{owner}/{repo} - Delete a repository."""
    c = GitHubClient()
    return c.request("DELETE", f"/repos/{owner}/{repo}")


def fork_repo(
    *, owner: str, repo: str, organization: Optional[str] = None, name: Optional[str] = None
) -> Dict[str, Any]:
    """POST /repos/{owner}/{repo}/forks - Create a fork."""
    c = GitHubClient()
    payload: Dict[str, Any] = {}
    if organization is not None:
        payload["organization"] = organization
    if name is not None:
        payload["name"] = name
    return c.request("POST", f"/repos/{owner}/{repo}/forks", json=payload)
