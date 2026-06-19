from typing import Any, Dict, List, Optional

from ._client import gh_request


def list_pulls(owner: str, repo: str, *, state: str = "open", head: Optional[str] = None, base: Optional[str] = None, sort: str = "created", direction: str = "desc", per_page: int = 30, page: int = 1) -> Any:
    params: Dict[str, Any] = {"state": state, "sort": sort, "direction": direction, "per_page": per_page, "page": page}
    if head:
        params["head"] = head
    if base:
        params["base"] = base
    return gh_request("GET", f"/repos/{owner}/{repo}/pulls", params=params)


def get_pull(owner: str, repo: str, pull_number: int) -> Any:
    return gh_request("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}")


def create_pull(owner: str, repo: str, title: str, head: str, base: str, *, body: str = "", draft: bool = False, maintainer_can_modify: bool = True) -> Any:
    payload: Dict[str, Any] = {"title": title, "head": head, "base": base, "body": body, "draft": draft, "maintainer_can_modify": maintainer_can_modify}
    return gh_request("POST", f"/repos/{owner}/{repo}/pulls", json=payload)


def update_pull(owner: str, repo: str, pull_number: int, *, title: Optional[str] = None, body: Optional[str] = None, state: Optional[str] = None, base: Optional[str] = None, maintainer_can_modify: Optional[bool] = None) -> Any:
    payload: Dict[str, Any] = {}
    if title is not None:
        payload["title"] = title
    if body is not None:
        payload["body"] = body
    if state is not None:
        payload["state"] = state
    if base is not None:
        payload["base"] = base
    if maintainer_can_modify is not None:
        payload["maintainer_can_modify"] = maintainer_can_modify
    return gh_request("PATCH", f"/repos/{owner}/{repo}/pulls/{pull_number}", json=payload)


def list_pull_reviews(owner: str, repo: str, pull_number: int, *, per_page: int = 30, page: int = 1) -> Any:
    return gh_request("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews", params={"per_page": per_page, "page": page})


def create_pull_review(owner: str, repo: str, pull_number: int, event: str, *, body: str = "", comments: Optional[List[Dict[str, Any]]] = None, commit_id: Optional[str] = None) -> Any:
    payload: Dict[str, Any] = {"event": event}
    if body:
        payload["body"] = body
    if comments is not None:
        payload["comments"] = comments
    if commit_id is not None:
        payload["commit_id"] = commit_id
    return gh_request("POST", f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews", json=payload)


def merge_pull(owner: str, repo: str, pull_number: int, *, commit_title: Optional[str] = None, commit_message: Optional[str] = None, merge_method: str = "merge", sha: Optional[str] = None) -> Any:
    payload: Dict[str, Any] = {"merge_method": merge_method}
    if commit_title is not None:
        payload["commit_title"] = commit_title
    if commit_message is not None:
        payload["commit_message"] = commit_message
    if sha is not None:
        payload["sha"] = sha
    return gh_request("PUT", f"/repos/{owner}/{repo}/pulls/{pull_number}/merge", json=payload)


def list_pull_comments(owner: str, repo: str, pull_number: int, *, per_page: int = 30, page: int = 1) -> Any:
    return gh_request("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}/comments", params={"per_page": per_page, "page": page})


def create_pull_comment(owner: str, repo: str, pull_number: int, body: str, commit_id: str, path: str, position: int) -> Any:
    payload = {"body": body, "commit_id": commit_id, "path": path, "position": position}
    return gh_request("POST", f"/repos/{owner}/{repo}/pulls/{pull_number}/comments", json=payload)
