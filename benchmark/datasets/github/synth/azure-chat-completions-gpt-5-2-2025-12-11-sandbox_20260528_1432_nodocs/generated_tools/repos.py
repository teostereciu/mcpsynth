from typing import Any, Dict, Optional

from .github_client import GitHubClient


def get_repo(owner: str, repo: str) -> Any:
    """GET /repos/{owner}/{repo}"""
    return GitHubClient().request("GET", f"/repos/{owner}/{repo}")


def list_user_repos(username: str, type: str = "owner", sort: str = "full_name", direction: str = "asc", per_page: int = 30, page: int = 1) -> Any:
    """GET /users/{username}/repos"""
    params = {"type": type, "sort": sort, "direction": direction, "per_page": per_page, "page": page}
    return GitHubClient().request("GET", f"/users/{username}/repos", params=params)


def list_org_repos(org: str, type: str = "all", sort: str = "full_name", direction: str = "asc", per_page: int = 30, page: int = 1) -> Any:
    """GET /orgs/{org}/repos"""
    params = {"type": type, "sort": sort, "direction": direction, "per_page": per_page, "page": page}
    return GitHubClient().request("GET", f"/orgs/{org}/repos", params=params)


def create_repo(name: str, description: str = "", private: bool = False, auto_init: bool = True, has_issues: bool = True, has_projects: bool = True, has_wiki: bool = True) -> Any:
    """POST /user/repos"""
    body: Dict[str, Any] = {
        "name": name,
        "description": description,
        "private": private,
        "auto_init": auto_init,
        "has_issues": has_issues,
        "has_projects": has_projects,
        "has_wiki": has_wiki,
    }
    return GitHubClient().request("POST", "/user/repos", json=body)


def fork_repo(owner: str, repo: str, organization: Optional[str] = None, default_branch_only: bool = False, name: Optional[str] = None) -> Any:
    """POST /repos/{owner}/{repo}/forks"""
    body: Dict[str, Any] = {"default_branch_only": default_branch_only}
    if organization:
        body["organization"] = organization
    if name:
        body["name"] = name
    return GitHubClient().request("POST", f"/repos/{owner}/{repo}/forks", json=body)


def list_branches(owner: str, repo: str, protected: Optional[bool] = None, per_page: int = 30, page: int = 1) -> Any:
    """GET /repos/{owner}/{repo}/branches"""
    params: Dict[str, Any] = {"per_page": per_page, "page": page}
    if protected is not None:
        params["protected"] = str(protected).lower()
    return GitHubClient().request("GET", f"/repos/{owner}/{repo}/branches", params=params)


def get_branch(owner: str, repo: str, branch: str) -> Any:
    """GET /repos/{owner}/{repo}/branches/{branch}"""
    return GitHubClient().request("GET", f"/repos/{owner}/{repo}/branches/{branch}")


def update_branch_protection(
    owner: str,
    repo: str,
    branch: str,
    required_status_checks: Optional[Dict[str, Any]] = None,
    enforce_admins: Optional[bool] = None,
    required_pull_request_reviews: Optional[Dict[str, Any]] = None,
    restrictions: Optional[Dict[str, Any]] = None,
    required_linear_history: Optional[bool] = None,
    allow_force_pushes: Optional[bool] = None,
    allow_deletions: Optional[bool] = None,
    block_creations: Optional[bool] = None,
    required_conversation_resolution: Optional[bool] = None,
    lock_branch: Optional[bool] = None,
    allow_fork_syncing: Optional[bool] = None,
) -> Any:
    """PUT /repos/{owner}/{repo}/branches/{branch}/protection"""
    body: Dict[str, Any] = {
        "required_status_checks": required_status_checks,
        "enforce_admins": enforce_admins,
        "required_pull_request_reviews": required_pull_request_reviews,
        "restrictions": restrictions,
        "required_linear_history": required_linear_history,
        "allow_force_pushes": allow_force_pushes,
        "allow_deletions": allow_deletions,
        "block_creations": block_creations,
        "required_conversation_resolution": required_conversation_resolution,
        "lock_branch": lock_branch,
        "allow_fork_syncing": allow_fork_syncing,
    }
    # GitHub expects explicit nulls for some fields; keep as-is.
    return GitHubClient().request("PUT", f"/repos/{owner}/{repo}/branches/{branch}/protection", json=body)


def delete_branch_protection(owner: str, repo: str, branch: str) -> Any:
    """DELETE /repos/{owner}/{repo}/branches/{branch}/protection"""
    return GitHubClient().request("DELETE", f"/repos/{owner}/{repo}/branches/{branch}/protection")


def get_commit(owner: str, repo: str, ref: str) -> Any:
    """GET /repos/{owner}/{repo}/commits/{ref}"""
    return GitHubClient().request("GET", f"/repos/{owner}/{repo}/commits/{ref}")


def list_commits(owner: str, repo: str, sha: Optional[str] = None, path: Optional[str] = None, author: Optional[str] = None, since: Optional[str] = None, until: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    """GET /repos/{owner}/{repo}/commits"""
    params: Dict[str, Any] = {"per_page": per_page, "page": page}
    if sha:
        params["sha"] = sha
    if path:
        params["path"] = path
    if author:
        params["author"] = author
    if since:
        params["since"] = since
    if until:
        params["until"] = until
    return GitHubClient().request("GET", f"/repos/{owner}/{repo}/commits", params=params)


def get_content(owner: str, repo: str, path: str, ref: Optional[str] = None) -> Any:
    """GET /repos/{owner}/{repo}/contents/{path}"""
    params: Dict[str, Any] = {}
    if ref:
        params["ref"] = ref
    return GitHubClient().request("GET", f"/repos/{owner}/{repo}/contents/{path}", params=params)


def create_or_update_file(
    owner: str,
    repo: str,
    path: str,
    message: str,
    content_b64: str,
    branch: Optional[str] = None,
    sha: Optional[str] = None,
    committer: Optional[Dict[str, str]] = None,
    author: Optional[Dict[str, str]] = None,
) -> Any:
    """PUT /repos/{owner}/{repo}/contents/{path}"""
    body: Dict[str, Any] = {"message": message, "content": content_b64}
    if branch:
        body["branch"] = branch
    if sha:
        body["sha"] = sha
    if committer:
        body["committer"] = committer
    if author:
        body["author"] = author
    return GitHubClient().request("PUT", f"/repos/{owner}/{repo}/contents/{path}", json=body)


def delete_file(owner: str, repo: str, path: str, message: str, sha: str, branch: Optional[str] = None, committer: Optional[Dict[str, str]] = None, author: Optional[Dict[str, str]] = None) -> Any:
    """DELETE /repos/{owner}/{repo}/contents/{path}"""
    body: Dict[str, Any] = {"message": message, "sha": sha}
    if branch:
        body["branch"] = branch
    if committer:
        body["committer"] = committer
    if author:
        body["author"] = author
    return GitHubClient().request("DELETE", f"/repos/{owner}/{repo}/contents/{path}", json=body)
