from typing import Optional

from generated_tools.github_common import compact, github_request


def list_pull_requests(owner: str, repo: str, state: str = "open", head: Optional[str] = None, base: Optional[str] = None, sort: str = "created", direction: str = "desc", per_page: int = 30, page: int = 1) -> str:
    return compact(github_request("GET", f"/repos/{owner}/{repo}/pulls", params={"state": state, "head": head, "base": base, "sort": sort, "direction": direction, "per_page": per_page, "page": page}))


def get_pull_request(owner: str, repo: str, pull_number: int) -> str:
    return compact(github_request("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}"))


def create_pull_request(owner: str, repo: str, title: str, head: str, base: str, body: Optional[str] = None, draft: bool = False, maintainer_can_modify: bool = True) -> str:
    return compact(github_request("POST", f"/repos/{owner}/{repo}/pulls", json_body={"title": title, "head": head, "base": base, "body": body, "draft": draft, "maintainer_can_modify": maintainer_can_modify}))


def update_pull_request(owner: str, repo: str, pull_number: int, title: Optional[str] = None, body: Optional[str] = None, state: Optional[str] = None, base: Optional[str] = None, maintainer_can_modify: Optional[bool] = None) -> str:
    return compact(github_request("PATCH", f"/repos/{owner}/{repo}/pulls/{pull_number}", json_body={"title": title, "body": body, "state": state, "base": base, "maintainer_can_modify": maintainer_can_modify}))


def merge_pull_request(owner: str, repo: str, pull_number: int, commit_title: Optional[str] = None, commit_message: Optional[str] = None, merge_method: str = "merge", sha: Optional[str] = None) -> str:
    return compact(github_request("PUT", f"/repos/{owner}/{repo}/pulls/{pull_number}/merge", json_body={"commit_title": commit_title, "commit_message": commit_message, "merge_method": merge_method, "sha": sha}))
