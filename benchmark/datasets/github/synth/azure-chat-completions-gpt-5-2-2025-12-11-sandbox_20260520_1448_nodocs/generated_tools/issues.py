from typing import Any, Dict, Optional

from .github_client import GitHubClient


def list_issues(owner: str, repo: str, state: str = "open", labels: Optional[str] = None, assignee: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    client = GitHubClient()
    params: Dict[str, Any] = {"state": state, "per_page": per_page, "page": page}
    if labels is not None:
        params["labels"] = labels
    if assignee is not None:
        params["assignee"] = assignee
    return client.request("GET", f"/repos/{owner}/{repo}/issues", params=params)


def get_issue(owner: str, repo: str, issue_number: int) -> Any:
    client = GitHubClient()
    return client.request("GET", f"/repos/{owner}/{repo}/issues/{issue_number}")


def create_issue(owner: str, repo: str, title: str, body: Optional[str] = None, labels: Optional[list] = None, assignees: Optional[list] = None, milestone: Optional[int] = None) -> Any:
    client = GitHubClient()
    payload: Dict[str, Any] = {"title": title}
    if body is not None:
        payload["body"] = body
    if labels is not None:
        payload["labels"] = labels
    if assignees is not None:
        payload["assignees"] = assignees
    if milestone is not None:
        payload["milestone"] = milestone
    return client.request("POST", f"/repos/{owner}/{repo}/issues", json=payload)


def update_issue(owner: str, repo: str, issue_number: int, title: Optional[str] = None, body: Optional[str] = None, state: Optional[str] = None, labels: Optional[list] = None, assignees: Optional[list] = None) -> Any:
    client = GitHubClient()
    payload: Dict[str, Any] = {}
    if title is not None:
        payload["title"] = title
    if body is not None:
        payload["body"] = body
    if state is not None:
        payload["state"] = state
    if labels is not None:
        payload["labels"] = labels
    if assignees is not None:
        payload["assignees"] = assignees
    return client.request("PATCH", f"/repos/{owner}/{repo}/issues/{issue_number}", json=payload)


def lock_issue(owner: str, repo: str, issue_number: int, lock_reason: Optional[str] = None) -> Any:
    client = GitHubClient()
    payload: Dict[str, Any] = {}
    if lock_reason is not None:
        payload["lock_reason"] = lock_reason
    return client.request("PUT", f"/repos/{owner}/{repo}/issues/{issue_number}/lock", json=payload if payload else None)


def unlock_issue(owner: str, repo: str, issue_number: int) -> Any:
    client = GitHubClient()
    return client.request("DELETE", f"/repos/{owner}/{repo}/issues/{issue_number}/lock")


def list_issue_comments(owner: str, repo: str, issue_number: int, per_page: int = 30, page: int = 1) -> Any:
    client = GitHubClient()
    return client.request("GET", f"/repos/{owner}/{repo}/issues/{issue_number}/comments", params={"per_page": per_page, "page": page})


def create_issue_comment(owner: str, repo: str, issue_number: int, body: str) -> Any:
    client = GitHubClient()
    return client.request("POST", f"/repos/{owner}/{repo}/issues/{issue_number}/comments", json={"body": body})


def update_issue_comment(owner: str, repo: str, comment_id: int, body: str) -> Any:
    client = GitHubClient()
    return client.request("PATCH", f"/repos/{owner}/{repo}/issues/comments/{comment_id}", json={"body": body})


def delete_issue_comment(owner: str, repo: str, comment_id: int) -> Any:
    client = GitHubClient()
    return client.request("DELETE", f"/repos/{owner}/{repo}/issues/comments/{comment_id}")


def add_labels(owner: str, repo: str, issue_number: int, labels: list) -> Any:
    client = GitHubClient()
    return client.request("POST", f"/repos/{owner}/{repo}/issues/{issue_number}/labels", json=labels)


def remove_label(owner: str, repo: str, issue_number: int, name: str) -> Any:
    client = GitHubClient()
    return client.request("DELETE", f"/repos/{owner}/{repo}/issues/{issue_number}/labels/{name}")
