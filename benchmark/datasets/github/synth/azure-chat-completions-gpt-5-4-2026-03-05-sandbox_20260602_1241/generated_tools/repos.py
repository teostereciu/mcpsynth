from typing import Any, Optional

from generated_tools.github_common import compact, github_request


def get_repository(owner: str, repo: str) -> str:
    return compact(github_request("GET", f"/repos/{owner}/{repo}"))


def list_org_repositories(org: str, type: str = "all", sort: str = "created", direction: str = "desc", per_page: int = 30, page: int = 1) -> str:
    return compact(github_request("GET", f"/orgs/{org}/repos", params={"type": type, "sort": sort, "direction": direction, "per_page": per_page, "page": page}))


def create_org_repository(org: str, name: str, description: Optional[str] = None, homepage: Optional[str] = None, private: bool = False, visibility: Optional[str] = None, has_issues: bool = True, has_projects: bool = True, has_wiki: bool = True, auto_init: bool = False) -> str:
    return compact(github_request("POST", f"/orgs/{org}/repos", json_body={"name": name, "description": description, "homepage": homepage, "private": private, "visibility": visibility, "has_issues": has_issues, "has_projects": has_projects, "has_wiki": has_wiki, "auto_init": auto_init}))


def get_repository_content(owner: str, repo: str, path: str, ref: Optional[str] = None, accept: str = "application/vnd.github.object+json") -> str:
    return compact(github_request("GET", f"/repos/{owner}/{repo}/contents/{path}", params={"ref": ref}, accept=accept))


def create_or_update_file(owner: str, repo: str, path: str, message: str, content_base64: str, sha: Optional[str] = None, branch: Optional[str] = None, committer: Optional[dict[str, Any]] = None, author: Optional[dict[str, Any]] = None) -> str:
    return compact(github_request("PUT", f"/repos/{owner}/{repo}/contents/{path}", json_body={"message": message, "content": content_base64, "sha": sha, "branch": branch, "committer": committer, "author": author}))


def delete_file(owner: str, repo: str, path: str, message: str, sha: str, branch: Optional[str] = None, committer: Optional[dict[str, Any]] = None, author: Optional[dict[str, Any]] = None) -> str:
    return compact(github_request("DELETE", f"/repos/{owner}/{repo}/contents/{path}", json_body={"message": message, "sha": sha, "branch": branch, "committer": committer, "author": author}))
