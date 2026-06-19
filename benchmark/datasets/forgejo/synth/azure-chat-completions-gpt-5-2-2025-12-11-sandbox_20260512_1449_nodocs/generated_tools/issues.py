from typing import Any, Dict, List, Optional

from .client import request_json


def list_issues(owner: str, repo: str, state: Optional[str] = None, labels: Optional[str] = None, page: Optional[int] = None, limit: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {}
    if state is not None:
        params["state"] = state
    if labels is not None:
        params["labels"] = labels
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    return request_json("GET", f"/repos/{owner}/{repo}/issues", params=params if params else None)


def get_issue(owner: str, repo: str, index: int) -> Any:
    return request_json("GET", f"/repos/{owner}/{repo}/issues/{index}")


def create_issue(owner: str, repo: str, title: str, body: Optional[str] = None, assignees: Optional[List[str]] = None, labels: Optional[List[int]] = None) -> Any:
    payload: Dict[str, Any] = {"title": title}
    if body is not None:
        payload["body"] = body
    if assignees is not None:
        payload["assignees"] = assignees
    if labels is not None:
        payload["labels"] = labels
    return request_json("POST", f"/repos/{owner}/{repo}/issues", json=payload)


def update_issue(owner: str, repo: str, index: int, title: Optional[str] = None, body: Optional[str] = None, state: Optional[str] = None) -> Any:
    payload: Dict[str, Any] = {}
    if title is not None:
        payload["title"] = title
    if body is not None:
        payload["body"] = body
    if state is not None:
        payload["state"] = state
    return request_json("PATCH", f"/repos/{owner}/{repo}/issues/{index}", json=payload)


def close_issue(owner: str, repo: str, index: int) -> Any:
    return update_issue(owner, repo, index, state="closed")


def add_issue_labels(owner: str, repo: str, index: int, labels: List[int]) -> Any:
    payload: Dict[str, Any] = {"labels": labels}
    return request_json("POST", f"/repos/{owner}/{repo}/issues/{index}/labels", json=payload)


def create_issue_comment(owner: str, repo: str, index: int, body: str) -> Any:
    payload: Dict[str, Any] = {"body": body}
    return request_json("POST", f"/repos/{owner}/{repo}/issues/{index}/comments", json=payload)
