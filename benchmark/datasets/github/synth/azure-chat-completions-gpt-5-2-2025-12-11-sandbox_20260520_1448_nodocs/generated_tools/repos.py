import base64
from typing import Any, Dict, Optional

from .github_client import GitHubClient


def get_repository(owner: str, repo: str) -> Any:
    client = GitHubClient()
    return client.request("GET", f"/repos/{owner}/{repo}")


def create_repository(name: str, description: Optional[str] = None, private: bool = False, auto_init: bool = True) -> Any:
    client = GitHubClient()
    payload: Dict[str, Any] = {"name": name, "private": private, "auto_init": auto_init}
    if description is not None:
        payload["description"] = description
    return client.request("POST", "/user/repos", json=payload)


def fork_repository(owner: str, repo: str, organization: Optional[str] = None) -> Any:
    client = GitHubClient()
    payload: Dict[str, Any] = {}
    if organization is not None:
        payload["organization"] = organization
    return client.request("POST", f"/repos/{owner}/{repo}/forks", json=payload if payload else None)


def list_branches(owner: str, repo: str, protected: Optional[bool] = None, per_page: int = 30, page: int = 1) -> Any:
    client = GitHubClient()
    params: Dict[str, Any] = {"per_page": per_page, "page": page}
    if protected is not None:
        params["protected"] = str(protected).lower()
    return client.request("GET", f"/repos/{owner}/{repo}/branches", params=params)


def get_branch(owner: str, repo: str, branch: str) -> Any:
    client = GitHubClient()
    return client.request("GET", f"/repos/{owner}/{repo}/branches/{branch}")


def list_commits(owner: str, repo: str, sha: Optional[str] = None, path: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    client = GitHubClient()
    params: Dict[str, Any] = {"per_page": per_page, "page": page}
    if sha is not None:
        params["sha"] = sha
    if path is not None:
        params["path"] = path
    return client.request("GET", f"/repos/{owner}/{repo}/commits", params=params)


def get_commit(owner: str, repo: str, ref: str) -> Any:
    client = GitHubClient()
    return client.request("GET", f"/repos/{owner}/{repo}/commits/{ref}")


def get_content(owner: str, repo: str, path: str, ref: Optional[str] = None) -> Any:
    client = GitHubClient()
    params: Dict[str, Any] = {}
    if ref is not None:
        params["ref"] = ref
    return client.request("GET", f"/repos/{owner}/{repo}/contents/{path}", params=params if params else None)


def put_content(owner: str, repo: str, path: str, message: str, content: str, branch: Optional[str] = None, sha: Optional[str] = None) -> Any:
    client = GitHubClient()
    b64 = base64.b64encode(content.encode("utf-8")).decode("utf-8")
    payload: Dict[str, Any] = {"message": message, "content": b64}
    if branch is not None:
        payload["branch"] = branch
    if sha is not None:
        payload["sha"] = sha
    return client.request("PUT", f"/repos/{owner}/{repo}/contents/{path}", json=payload)


def delete_content(owner: str, repo: str, path: str, message: str, sha: str, branch: Optional[str] = None) -> Any:
    client = GitHubClient()
    payload: Dict[str, Any] = {"message": message, "sha": sha}
    if branch is not None:
        payload["branch"] = branch
    return client.request("DELETE", f"/repos/{owner}/{repo}/contents/{path}", json=payload)


def get_branch_protection(owner: str, repo: str, branch: str) -> Any:
    client = GitHubClient()
    return client.request("GET", f"/repos/{owner}/{repo}/branches/{branch}/protection")


def update_branch_protection(owner: str, repo: str, branch: str, protection: Dict[str, Any]) -> Any:
    client = GitHubClient()
    return client.request("PUT", f"/repos/{owner}/{repo}/branches/{branch}/protection", json=protection)
