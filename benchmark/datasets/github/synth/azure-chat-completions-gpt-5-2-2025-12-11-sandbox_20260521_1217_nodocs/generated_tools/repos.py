from typing import Any, Dict, Optional

from .http import request_json


def get_repo(owner: str, repo: str) -> Any:
    return request_json("GET", f"/repos/{owner}/{repo}")


def list_user_repos(username: str, *, type: str = "owner", sort: str = "full_name", per_page: int = 30, page: int = 1) -> Any:
    params = {"type": type, "sort": sort, "per_page": per_page, "page": page}
    return request_json("GET", f"/users/{username}/repos", params=params)


def list_org_repos(org: str, *, type: str = "all", sort: str = "full_name", per_page: int = 30, page: int = 1) -> Any:
    params = {"type": type, "sort": sort, "per_page": per_page, "page": page}
    return request_json("GET", f"/orgs/{org}/repos", params=params)


def create_repo_for_authenticated_user(name: str, *, description: str = "", private: bool = False, auto_init: bool = True) -> Any:
    body: Dict[str, Any] = {"name": name, "description": description, "private": private, "auto_init": auto_init}
    return request_json("POST", "/user/repos", json=body)


def fork_repo(owner: str, repo: str, *, organization: Optional[str] = None, name: Optional[str] = None, default_branch_only: bool = False) -> Any:
    body: Dict[str, Any] = {"default_branch_only": default_branch_only}
    if organization:
        body["organization"] = organization
    if name:
        body["name"] = name
    return request_json("POST", f"/repos/{owner}/{repo}/forks", json=body)


def list_branches(owner: str, repo: str, *, protected: Optional[bool] = None, per_page: int = 30, page: int = 1) -> Any:
    params: Dict[str, Any] = {"per_page": per_page, "page": page}
    if protected is not None:
        params["protected"] = protected
    return request_json("GET", f"/repos/{owner}/{repo}/branches", params=params)


def get_branch(owner: str, repo: str, branch: str) -> Any:
    return request_json("GET", f"/repos/{owner}/{repo}/branches/{branch}")


def get_commit(owner: str, repo: str, ref: str) -> Any:
    return request_json("GET", f"/repos/{owner}/{repo}/commits/{ref}")


def list_commits(owner: str, repo: str, *, sha: Optional[str] = None, path: Optional[str] = None, author: Optional[str] = None, since: Optional[str] = None, until: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
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
    return request_json("GET", f"/repos/{owner}/{repo}/commits", params=params)


def get_content(owner: str, repo: str, path: str, *, ref: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    if ref:
        params["ref"] = ref
    return request_json("GET", f"/repos/{owner}/{repo}/contents/{path.lstrip('/')}" , params=params)


def create_or_update_file(owner: str, repo: str, path: str, message: str, content_base64: str, *, branch: Optional[str] = None, sha: Optional[str] = None, committer: Optional[Dict[str, str]] = None, author: Optional[Dict[str, str]] = None) -> Any:
    body: Dict[str, Any] = {"message": message, "content": content_base64}
    if branch:
        body["branch"] = branch
    if sha:
        body["sha"] = sha
    if committer:
        body["committer"] = committer
    if author:
        body["author"] = author
    return request_json("PUT", f"/repos/{owner}/{repo}/contents/{path.lstrip('/')}" , json=body)


def delete_file(owner: str, repo: str, path: str, message: str, sha: str, *, branch: Optional[str] = None, committer: Optional[Dict[str, str]] = None, author: Optional[Dict[str, str]] = None) -> Any:
    body: Dict[str, Any] = {"message": message, "sha": sha}
    if branch:
        body["branch"] = branch
    if committer:
        body["committer"] = committer
    if author:
        body["author"] = author
    return request_json("DELETE", f"/repos/{owner}/{repo}/contents/{path.lstrip('/')}" , json=body)


def get_branch_protection(owner: str, repo: str, branch: str) -> Any:
    return request_json("GET", f"/repos/{owner}/{repo}/branches/{branch}/protection")


def update_branch_protection(owner: str, repo: str, branch: str, protection: Dict[str, Any]) -> Any:
    return request_json("PUT", f"/repos/{owner}/{repo}/branches/{branch}/protection", json=protection)


def delete_branch_protection(owner: str, repo: str, branch: str) -> Any:
    return request_json("DELETE", f"/repos/{owner}/{repo}/branches/{branch}/protection")
