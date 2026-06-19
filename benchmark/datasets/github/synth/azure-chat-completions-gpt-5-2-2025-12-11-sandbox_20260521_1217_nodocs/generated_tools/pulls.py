from typing import Any, Dict, Optional, List

from .http import request_json


def list_pull_requests(owner: str, repo: str, *, state: str = "open", head: Optional[str] = None, base: Optional[str] = None, sort: str = "created", direction: str = "desc", per_page: int = 30, page: int = 1) -> Any:
    params: Dict[str, Any] = {"state": state, "sort": sort, "direction": direction, "per_page": per_page, "page": page}
    if head:
        params["head"] = head
    if base:
        params["base"] = base
    return request_json("GET", f"/repos/{owner}/{repo}/pulls", params=params)


def get_pull_request(owner: str, repo: str, pull_number: int) -> Any:
    return request_json("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}")


def create_pull_request(owner: str, repo: str, title: str, head: str, base: str, *, body: str = "", draft: bool = False, maintainer_can_modify: bool = True) -> Any:
    payload: Dict[str, Any] = {"title": title, "head": head, "base": base, "body": body, "draft": draft, "maintainer_can_modify": maintainer_can_modify}
    return request_json("POST", f"/repos/{owner}/{repo}/pulls", json=payload)


def update_pull_request(owner: str, repo: str, pull_number: int, *, title: Optional[str] = None, body: Optional[str] = None, state: Optional[str] = None, base: Optional[str] = None, maintainer_can_modify: Optional[bool] = None) -> Any:
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
    return request_json("PATCH", f"/repos/{owner}/{repo}/pulls/{pull_number}", json=payload)


def list_pull_reviews(owner: str, repo: str, pull_number: int, *, per_page: int = 30, page: int = 1) -> Any:
    return request_json("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews", params={"per_page": per_page, "page": page})


def create_pull_review(owner: str, repo: str, pull_number: int, *, body: str = "", event: str = "COMMENT", comments: Optional[List[Dict[str, Any]]] = None) -> Any:
    payload: Dict[str, Any] = {"body": body, "event": event}
    if comments is not None:
        payload["comments"] = comments
    return request_json("POST", f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews", json=payload)


def merge_pull_request(owner: str, repo: str, pull_number: int, *, commit_title: Optional[str] = None, commit_message: Optional[str] = None, merge_method: str = "merge", sha: Optional[str] = None) -> Any:
    payload: Dict[str, Any] = {"merge_method": merge_method}
    if commit_title:
        payload["commit_title"] = commit_title
    if commit_message:
        payload["commit_message"] = commit_message
    if sha:
        payload["sha"] = sha
    return request_json("PUT", f"/repos/{owner}/{repo}/pulls/{pull_number}/merge", json=payload)


def request_reviewers(owner: str, repo: str, pull_number: int, *, reviewers: Optional[List[str]] = None, team_reviewers: Optional[List[str]] = None) -> Any:
    payload: Dict[str, Any] = {}
    if reviewers is not None:
        payload["reviewers"] = reviewers
    if team_reviewers is not None:
        payload["team_reviewers"] = team_reviewers
    return request_json("POST", f"/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers", json=payload)
