from typing import Any, Dict, List, Optional

from .github_client import GitHubClient


def list_repo_issues(owner: str, repo: str, state: str = "open", labels: Optional[str] = None, assignee: Optional[str] = None, creator: Optional[str] = None, mentioned: Optional[str] = None, since: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    """GET /repos/{owner}/{repo}/issues"""
    params: Dict[str, Any] = {"state": state, "per_page": per_page, "page": page}
    if labels:
        params["labels"] = labels
    if assignee:
        params["assignee"] = assignee
    if creator:
        params["creator"] = creator
    if mentioned:
        params["mentioned"] = mentioned
    if since:
        params["since"] = since
    return GitHubClient().request("GET", f"/repos/{owner}/{repo}/issues", params=params)


def get_issue(owner: str, repo: str, issue_number: int) -> Any:
    """GET /repos/{owner}/{repo}/issues/{issue_number}"""
    return GitHubClient().request("GET", f"/repos/{owner}/{repo}/issues/{issue_number}")


def create_issue(owner: str, repo: str, title: str, body: str = "", assignees: Optional[List[str]] = None, labels: Optional[List[str]] = None, milestone: Optional[int] = None) -> Any:
    """POST /repos/{owner}/{repo}/issues"""
    payload: Dict[str, Any] = {"title": title, "body": body}
    if assignees is not None:
        payload["assignees"] = assignees
    if labels is not None:
        payload["labels"] = labels
    if milestone is not None:
        payload["milestone"] = milestone
    return GitHubClient().request("POST", f"/repos/{owner}/{repo}/issues", json=payload)


def update_issue(owner: str, repo: str, issue_number: int, title: Optional[str] = None, body: Optional[str] = None, state: Optional[str] = None, assignees: Optional[List[str]] = None, labels: Optional[List[str]] = None, milestone: Optional[int] = None) -> Any:
    """PATCH /repos/{owner}/{repo}/issues/{issue_number}"""
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
    if milestone is not None:
        payload["milestone"] = milestone
    return GitHubClient().request("PATCH", f"/repos/{owner}/{repo}/issues/{issue_number}", json=payload)


def lock_issue(owner: str, repo: str, issue_number: int, lock_reason: Optional[str] = None) -> Any:
    """PUT /repos/{owner}/{repo}/issues/{issue_number}/lock"""
    payload: Dict[str, Any] = {}
    if lock_reason:
        payload["lock_reason"] = lock_reason
    return GitHubClient().request("PUT", f"/repos/{owner}/{repo}/issues/{issue_number}/lock", json=payload)


def unlock_issue(owner: str, repo: str, issue_number: int) -> Any:
    """DELETE /repos/{owner}/{repo}/issues/{issue_number}/lock"""
    return GitHubClient().request("DELETE", f"/repos/{owner}/{repo}/issues/{issue_number}/lock")


def list_issue_comments(owner: str, repo: str, issue_number: int, per_page: int = 30, page: int = 1) -> Any:
    """GET /repos/{owner}/{repo}/issues/{issue_number}/comments"""
    params = {"per_page": per_page, "page": page}
    return GitHubClient().request("GET", f"/repos/{owner}/{repo}/issues/{issue_number}/comments", params=params)


def create_issue_comment(owner: str, repo: str, issue_number: int, body: str) -> Any:
    """POST /repos/{owner}/{repo}/issues/{issue_number}/comments"""
    return GitHubClient().request("POST", f"/repos/{owner}/{repo}/issues/{issue_number}/comments", json={"body": body})


def update_issue_comment(owner: str, repo: str, comment_id: int, body: str) -> Any:
    """PATCH /repos/{owner}/{repo}/issues/comments/{comment_id}"""
    return GitHubClient().request("PATCH", f"/repos/{owner}/{repo}/issues/comments/{comment_id}", json={"body": body})


def delete_issue_comment(owner: str, repo: str, comment_id: int) -> Any:
    """DELETE /repos/{owner}/{repo}/issues/comments/{comment_id}"""
    return GitHubClient().request("DELETE", f"/repos/{owner}/{repo}/issues/comments/{comment_id}")


def add_labels(owner: str, repo: str, issue_number: int, labels: List[str]) -> Any:
    """POST /repos/{owner}/{repo}/issues/{issue_number}/labels"""
    return GitHubClient().request("POST", f"/repos/{owner}/{repo}/issues/{issue_number}/labels", json={"labels": labels})


def set_labels(owner: str, repo: str, issue_number: int, labels: List[str]) -> Any:
    """PUT /repos/{owner}/{repo}/issues/{issue_number}/labels"""
    return GitHubClient().request("PUT", f"/repos/{owner}/{repo}/issues/{issue_number}/labels", json={"labels": labels})


def remove_label(owner: str, repo: str, issue_number: int, name: str) -> Any:
    """DELETE /repos/{owner}/{repo}/issues/{issue_number}/labels/{name}"""
    return GitHubClient().request("DELETE", f"/repos/{owner}/{repo}/issues/{issue_number}/labels/{name}")


def list_labels(owner: str, repo: str, per_page: int = 30, page: int = 1) -> Any:
    """GET /repos/{owner}/{repo}/labels"""
    params = {"per_page": per_page, "page": page}
    return GitHubClient().request("GET", f"/repos/{owner}/{repo}/labels", params=params)


def create_label(owner: str, repo: str, name: str, color: str, description: str = "") -> Any:
    """POST /repos/{owner}/{repo}/labels"""
    payload: Dict[str, Any] = {"name": name, "color": color}
    if description:
        payload["description"] = description
    return GitHubClient().request("POST", f"/repos/{owner}/{repo}/labels", json=payload)


def update_label(owner: str, repo: str, name: str, new_name: Optional[str] = None, color: Optional[str] = None, description: Optional[str] = None) -> Any:
    """PATCH /repos/{owner}/{repo}/labels/{name}"""
    payload: Dict[str, Any] = {}
    if new_name is not None:
        payload["new_name"] = new_name
    if color is not None:
        payload["color"] = color
    if description is not None:
        payload["description"] = description
    return GitHubClient().request("PATCH", f"/repos/{owner}/{repo}/labels/{name}", json=payload)


def delete_label(owner: str, repo: str, name: str) -> Any:
    """DELETE /repos/{owner}/{repo}/labels/{name}"""
    return GitHubClient().request("DELETE", f"/repos/{owner}/{repo}/labels/{name}")


def add_assignees(owner: str, repo: str, issue_number: int, assignees: List[str]) -> Any:
    """POST /repos/{owner}/{repo}/issues/{issue_number}/assignees"""
    return GitHubClient().request("POST", f"/repos/{owner}/{repo}/issues/{issue_number}/assignees", json={"assignees": assignees})


def remove_assignees(owner: str, repo: str, issue_number: int, assignees: List[str]) -> Any:
    """DELETE /repos/{owner}/{repo}/issues/{issue_number}/assignees"""
    return GitHubClient().request("DELETE", f"/repos/{owner}/{repo}/issues/{issue_number}/assignees", json={"assignees": assignees})
