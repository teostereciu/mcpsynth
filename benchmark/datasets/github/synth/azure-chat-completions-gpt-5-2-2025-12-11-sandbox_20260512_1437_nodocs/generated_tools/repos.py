from typing import Any, Dict, Optional

from ._client import gh_request


def get_repo(owner: str, repo: str) -> Any:
    return gh_request("GET", f"/repos/{owner}/{repo}")


def list_user_repos(username: str, *, type: str = "owner", sort: str = "full_name", per_page: int = 30, page: int = 1) -> Any:
    return gh_request("GET", f"/users/{username}/repos", params={"type": type, "sort": sort, "per_page": per_page, "page": page})


def list_org_repos(org: str, *, type: str = "all", per_page: int = 30, page: int = 1) -> Any:
    return gh_request("GET", f"/orgs/{org}/repos", params={"type": type, "per_page": per_page, "page": page})


def create_repo(name: str, *, description: str = "", private: bool = False, auto_init: bool = True, has_issues: bool = True, has_projects: bool = True, has_wiki: bool = True) -> Any:
    body: Dict[str, Any] = {
        "name": name,
        "description": description,
        "private": private,
        "auto_init": auto_init,
        "has_issues": has_issues,
        "has_projects": has_projects,
        "has_wiki": has_wiki,
    }
    return gh_request("POST", "/user/repos", json=body)


def fork_repo(owner: str, repo: str, *, organization: Optional[str] = None, name: Optional[str] = None, default_branch_only: bool = False) -> Any:
    body: Dict[str, Any] = {"default_branch_only": default_branch_only}
    if organization:
        body["organization"] = organization
    if name:
        body["name"] = name
    return gh_request("POST", f"/repos/{owner}/{repo}/forks", json=body)


def list_branches(owner: str, repo: str, *, protected: Optional[bool] = None, per_page: int = 30, page: int = 1) -> Any:
    params: Dict[str, Any] = {"per_page": per_page, "page": page}
    if protected is not None:
        params["protected"] = str(protected).lower()
    return gh_request("GET", f"/repos/{owner}/{repo}/branches", params=params)


def get_branch(owner: str, repo: str, branch: str) -> Any:
    return gh_request("GET", f"/repos/{owner}/{repo}/branches/{branch}")


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
    return gh_request("GET", f"/repos/{owner}/{repo}/commits", params=params)


def get_commit(owner: str, repo: str, ref: str) -> Any:
    return gh_request("GET", f"/repos/{owner}/{repo}/commits/{ref}")


def get_content(owner: str, repo: str, path: str, *, ref: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    if ref:
        params["ref"] = ref
    return gh_request("GET", f"/repos/{owner}/{repo}/contents/{path.lstrip('/')}" , params=params)


def create_or_update_file(owner: str, repo: str, path: str, message: str, content_base64: str, *, branch: Optional[str] = None, sha: Optional[str] = None, committer_name: Optional[str] = None, committer_email: Optional[str] = None, author_name: Optional[str] = None, author_email: Optional[str] = None) -> Any:
    body: Dict[str, Any] = {"message": message, "content": content_base64}
    if branch:
        body["branch"] = branch
    if sha:
        body["sha"] = sha
    if committer_name and committer_email:
        body["committer"] = {"name": committer_name, "email": committer_email}
    if author_name and author_email:
        body["author"] = {"name": author_name, "email": author_email}
    return gh_request("PUT", f"/repos/{owner}/{repo}/contents/{path.lstrip('/')}" , json=body)


def delete_file(owner: str, repo: str, path: str, message: str, sha: str, *, branch: Optional[str] = None) -> Any:
    body: Dict[str, Any] = {"message": message, "sha": sha}
    if branch:
        body["branch"] = branch
    return gh_request("DELETE", f"/repos/{owner}/{repo}/contents/{path.lstrip('/')}" , json=body)
