from typing import Any, Dict, List, Optional

from generated_tools.github_common import clean_params, github_request


def get_authenticated_user() -> Any:
    return github_request("GET", "/user")


def list_user_repos(visibility: Optional[str] = None, affiliation: Optional[str] = None, sort: Optional[str] = None, direction: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    params = clean_params(visibility=visibility, affiliation=affiliation, sort=sort, direction=direction, per_page=per_page, page=page)
    return github_request("GET", "/user/repos", params=params)


def get_repo(owner: str, repo: str) -> Any:
    return github_request("GET", f"/repos/{owner}/{repo}")


def create_repo(name: str, description: Optional[str] = None, private: bool = False, auto_init: bool = False, gitignore_template: Optional[str] = None, license_template: Optional[str] = None, homepage: Optional[str] = None, has_issues: Optional[bool] = None, has_projects: Optional[bool] = None, has_wiki: Optional[bool] = None) -> Any:
    body = clean_params(name=name, description=description, private=private, auto_init=auto_init, gitignore_template=gitignore_template, license_template=license_template, homepage=homepage, has_issues=has_issues, has_projects=has_projects, has_wiki=has_wiki)
    return github_request("POST", "/user/repos", json_body=body)


def update_repo(owner: str, repo: str, name: Optional[str] = None, description: Optional[str] = None, homepage: Optional[str] = None, private: Optional[bool] = None, default_branch: Optional[str] = None, has_issues: Optional[bool] = None, has_projects: Optional[bool] = None, has_wiki: Optional[bool] = None, archived: Optional[bool] = None, allow_squash_merge: Optional[bool] = None, allow_merge_commit: Optional[bool] = None, allow_rebase_merge: Optional[bool] = None) -> Any:
    body = clean_params(name=name, description=description, homepage=homepage, private=private, default_branch=default_branch, has_issues=has_issues, has_projects=has_projects, has_wiki=has_wiki, archived=archived, allow_squash_merge=allow_squash_merge, allow_merge_commit=allow_merge_commit, allow_rebase_merge=allow_rebase_merge)
    return github_request("PATCH", f"/repos/{owner}/{repo}", json_body=body)


def delete_repo(owner: str, repo: str) -> Any:
    return github_request("DELETE", f"/repos/{owner}/{repo}")


def fork_repo(owner: str, repo: str, organization: Optional[str] = None, name: Optional[str] = None, default_branch_only: Optional[bool] = None) -> Any:
    body = clean_params(organization=organization, name=name, default_branch_only=default_branch_only)
    return github_request("POST", f"/repos/{owner}/{repo}/forks", json_body=body)


def list_branches(owner: str, repo: str, protected: Optional[bool] = None, per_page: int = 30, page: int = 1) -> Any:
    params = clean_params(protected=protected, per_page=per_page, page=page)
    return github_request("GET", f"/repos/{owner}/{repo}/branches", params=params)


def get_branch(owner: str, repo: str, branch: str) -> Any:
    return github_request("GET", f"/repos/{owner}/{repo}/branches/{branch}")


def list_commits(owner: str, repo: str, sha: Optional[str] = None, path: Optional[str] = None, author: Optional[str] = None, since: Optional[str] = None, until: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    params = clean_params(sha=sha, path=path, author=author, since=since, until=until, per_page=per_page, page=page)
    return github_request("GET", f"/repos/{owner}/{repo}/commits", params=params)


def get_commit(owner: str, repo: str, ref: str) -> Any:
    return github_request("GET", f"/repos/{owner}/{repo}/commits/{ref}")


def get_content(owner: str, repo: str, path: str, ref: Optional[str] = None) -> Any:
    params = clean_params(ref=ref)
    return github_request("GET", f"/repos/{owner}/{repo}/contents/{path}", params=params)


def create_or_update_file(owner: str, repo: str, path: str, message: str, content_base64: str, branch: Optional[str] = None, sha: Optional[str] = None, committer: Optional[Dict[str, str]] = None, author: Optional[Dict[str, str]] = None) -> Any:
    body = clean_params(message=message, content=content_base64, branch=branch, sha=sha, committer=committer, author=author)
    return github_request("PUT", f"/repos/{owner}/{repo}/contents/{path}", json_body=body)


def delete_file(owner: str, repo: str, path: str, message: str, sha: str, branch: Optional[str] = None, committer: Optional[Dict[str, str]] = None, author: Optional[Dict[str, str]] = None) -> Any:
    body = clean_params(message=message, sha=sha, branch=branch, committer=committer, author=author)
    return github_request("DELETE", f"/repos/{owner}/{repo}/contents/{path}", json_body=body)
