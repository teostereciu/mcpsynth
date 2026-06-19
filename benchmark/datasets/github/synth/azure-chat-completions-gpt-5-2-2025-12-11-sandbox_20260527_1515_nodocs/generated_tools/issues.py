from typing import Any, Dict, Optional

from .github_client import GitHubClient


client = GitHubClient()


def list_issues(owner: str, repo: str, *, state: str = "open", labels: Optional[str] = None, assignee: Optional[str] = None, per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    params: Dict[str, Any] = {"state": state, "per_page": per_page, "page": page}
    if labels is not None:
        params["labels"] = labels
    if assignee is not None:
        params["assignee"] = assignee
    return client.request("GET", f"/repos/{owner}/{repo}/issues", params=params)


def get_issue(owner: str, repo: str, issue_number: int) -> Dict[str, Any]:
    return client.request("GET", f"/repos/{owner}/{repo}/issues/{issue_number}")


def create_issue(owner: str, repo: str, title: str, *, body: Optional[str] = None, assignees: Optional[list[str]] = None, labels: Optional[list[str]] = None) -> Dict[str, Any]:
    payload: Dict[str, Any] = {"title": title}
    if body is not None:
        payload["body"] = body
    if assignees is not None:
        payload["assignees"] = assignees
    if labels is not None:
        payload["labels"] = labels
    return client.request("POST", f"/repos/{owner}/{repo}/issues", json=payload)


def update_issue(owner: str, repo: str, issue_number: int, *, title: Optional[str] = None, body: Optional[str] = None, state: Optional[str] = None, assignees: Optional[list[str]] = None, labels: Optional[list[str]] = None) -> Dict[str, Any]:
    payload: Dict[str, Any] = {}
    if title is not None:
        payload["title"] = title
    if body is not None:
        payload["body"] = body
    if state is not None:
        payload["state"] = state
    if assignees is not None:
        payload["assignees"] = assignees
    if labels is not None:
        payload["labels"] = labels
    return client.request("PATCH", f"/repos/{owner}/{repo}/issues/{issue_number}", json=payload)


def lock_issue(owner: str, repo: str, issue_number: int, *, lock_reason: Optional[str] = None) -> Dict[str, Any]:
    payload: Dict[str, Any] = {}
    if lock_reason is not None:
        payload["lock_reason"] = lock_reason
    return client.request("PUT", f"/repos/{owner}/{repo}/issues/{issue_number}/lock", json=payload)


def unlock_issue(owner: str, repo: str, issue_number: int) -> Dict[str, Any]:
    return client.request("DELETE", f"/repos/{owner}/{repo}/issues/{issue_number}/lock")


def list_issue_comments(owner: str, repo: str, issue_number: int, *, per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    return client.request(
        "GET",
        f"/repos/{owner}/{repo}/issues/{issue_number}/comments",
        params={"per_page": per_page, "page": page},
    )


def create_issue_comment(owner: str, repo: str, issue_number: int, body: str) -> Dict[str, Any]:
    return client.request("POST", f"/repos/{owner}/{repo}/issues/{issue_number}/comments", json={"body": body})


def update_issue_comment(owner: str, repo: str, comment_id: int, body: str) -> Dict[str, Any]:
    return client.request("PATCH", f"/repos/{owner}/{repo}/issues/comments/{comment_id}", json={"body": body})


def delete_issue_comment(owner: str, repo: str, comment_id: int) -> Dict[str, Any]:
    return client.request("DELETE", f"/repos/{owner}/{repo}/issues/comments/{comment_id}")


def add_labels(owner: str, repo: str, issue_number: int, labels: list[str]) -> Dict[str, Any]:
    return client.request("POST", f"/repos/{owner}/{repo}/issues/{issue_number}/labels", json=labels)


def remove_label(owner: str, repo: str, issue_number: int, name: str) -> Dict[str, Any]:
    return client.request("DELETE", f"/repos/{owner}/{repo}/issues/{issue_number}/labels/{name}")


def list_labels(owner: str, repo: str, *, per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    return client.request("GET", f"/repos/{owner}/{repo}/labels", params={"per_page": per_page, "page": page})


def create_label(owner: str, repo: str, name: str, color: str, *, description: Optional[str] = None) -> Dict[str, Any]:
    payload: Dict[str, Any] = {"name": name, "color": color}
    if description is not None:
        payload["description"] = description
    return client.request("POST", f"/repos/{owner}/{repo}/labels", json=payload)


def update_label(owner: str, repo: str, name: str, *, new_name: Optional[str] = None, color: Optional[str] = None, description: Optional[str] = None) -> Dict[str, Any]:
    payload: Dict[str, Any] = {}
    if new_name is not None:
        payload["new_name"] = new_name
    if color is not None:
        payload["color"] = color
    if description is not None:
        payload["description"] = description
    return client.request("PATCH", f"/repos/{owner}/{repo}/labels/{name}", json=payload)


def delete_label(owner: str, repo: str, name: str) -> Dict[str, Any]:
    return client.request("DELETE", f"/repos/{owner}/{repo}/labels/{name}")
