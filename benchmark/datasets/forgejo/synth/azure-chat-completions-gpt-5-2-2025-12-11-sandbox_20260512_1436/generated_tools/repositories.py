from typing import Any, Dict, Optional

from .http_client import request


def repo_get(owner: str, repo: str) -> Any:
    return request("GET", f"/repos/{owner}/{repo}")


def repo_delete(owner: str, repo: str) -> Any:
    return request("DELETE", f"/repos/{owner}/{repo}")


def repo_search(
    q: str,
    *,
    topic: Optional[bool] = None,
    includeDesc: Optional[bool] = None,
    uid: Optional[int] = None,
    priority_owner_id: Optional[int] = None,
    team_id: Optional[int] = None,
    starredBy: Optional[int] = None,
    private: Optional[bool] = None,
    is_private: Optional[bool] = None,
    template: Optional[bool] = None,
    archived: Optional[bool] = None,
    mode: Optional[str] = None,
    exclusive: Optional[bool] = None,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    page: Optional[int] = None,
    limit: Optional[int] = None,
) -> Any:
    params: Dict[str, Any] = {"q": q}
    for k, v in {
        "topic": topic,
        "includeDesc": includeDesc,
        "uid": uid,
        "priority_owner_id": priority_owner_id,
        "team_id": team_id,
        "starredBy": starredBy,
        "private": private,
        "is_private": is_private,
        "template": template,
        "archived": archived,
        "mode": mode,
        "exclusive": exclusive,
        "sort": sort,
        "order": order,
        "page": page,
        "limit": limit,
    }.items():
        if v is not None:
            params[k] = v
    return request("GET", "/repos/search", params=params)


def repo_migrate(body: Dict[str, Any]) -> Any:
    return request("POST", "/repos/migrate", json=body)


def repo_edit(owner: str, repo: str, body: Dict[str, Any]) -> Any:
    return request("PATCH", f"/repos/{owner}/{repo}", json=body)


# Coverage expectations helpers

def repo_fork(owner: str, repo: str, body: Optional[Dict[str, Any]] = None) -> Any:
    # Not present in provided docs snapshot; endpoint exists in Forgejo: POST /repos/{owner}/{repo}/forks
    return request("POST", f"/repos/{owner}/{repo}/forks", json=body or {})


def user_repos_list(username: str, *, page: Optional[int] = None, limit: Optional[int] = None) -> Any:
    # Forgejo: GET /users/{username}/repos
    params: Dict[str, Any] = {}
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    return request("GET", f"/users/{username}/repos", params=params or None)


def org_repos_list(org: str, *, page: Optional[int] = None, limit: Optional[int] = None) -> Any:
    # Forgejo: GET /orgs/{org}/repos
    params: Dict[str, Any] = {}
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    return request("GET", f"/orgs/{org}/repos", params=params or None)


def repo_create_for_authenticated_user(body: Dict[str, Any]) -> Any:
    # Forgejo: POST /user/repos
    return request("POST", "/user/repos", json=body)


def repo_branches_list(owner: str, repo: str, *, page: Optional[int] = None, limit: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {}
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    return request("GET", f"/repos/{owner}/{repo}/branches", params=params or None)


def repo_branch_get(owner: str, repo: str, branch: str) -> Any:
    return request("GET", f"/repos/{owner}/{repo}/branches/{branch}")


def repo_branch_create(owner: str, repo: str, body: Dict[str, Any]) -> Any:
    return request("POST", f"/repos/{owner}/{repo}/branches", json=body)


def repo_commits_list(owner: str, repo: str, *, sha: Optional[str] = None, path: Optional[str] = None, page: Optional[int] = None, limit: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {}
    if sha is not None:
        params["sha"] = sha
    if path is not None:
        params["path"] = path
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    return request("GET", f"/repos/{owner}/{repo}/commits", params=params or None)


def repo_commit_get(owner: str, repo: str, sha: str) -> Any:
    # Forgejo: GET /repos/{owner}/{repo}/git/commits/{sha} or /commits/{sha}
    return request("GET", f"/repos/{owner}/{repo}/git/commits/{sha}")


def repo_releases_list(owner: str, repo: str, *, page: Optional[int] = None, limit: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {}
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    return request("GET", f"/repos/{owner}/{repo}/releases", params=params or None)


def repo_release_get(owner: str, repo: str, release_id: int) -> Any:
    return request("GET", f"/repos/{owner}/{repo}/releases/{release_id}")


def repo_release_create(owner: str, repo: str, body: Dict[str, Any]) -> Any:
    return request("POST", f"/repos/{owner}/{repo}/releases", json=body)
