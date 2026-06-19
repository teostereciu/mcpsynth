from typing import Any, Dict, List, Optional
from .client import make_request

def list_issues(owner: str, repo: str, state: str = "open", per_page: int = 30, page: int = 1) -> Any:
    """List issues in a repository."""
    return make_request("GET", f"/repos/{owner}/{repo}/issues", params={"state": state, "per_page": per_page, "page": page})

def get_issue(owner: str, repo: str, issue_number: int) -> Any:
    """Get an issue."""
    return make_request("GET", f"/repos/{owner}/{repo}/issues/{issue_number}")

def create_issue(owner: str, repo: str, title: str, body: Optional[str] = None, assignees: Optional[List[str]] = None, labels: Optional[List[str]] = None) -> Any:
    """Create an issue."""
    data = {"title": title}
    if body is not None: data["body"] = body
    if assignees is not None: data["assignees"] = assignees
    if labels is not None: data["labels"] = labels
    return make_request("POST", f"/repos/{owner}/{repo}/issues", json=data)

def update_issue(owner: str, repo: str, issue_number: int, title: Optional[str] = None, body: Optional[str] = None, state: Optional[str] = None) -> Any:
    """Update an issue."""
    data = {}
    if title is not None: data["title"] = title
    if body is not None: data["body"] = body
    if state is not None: data["state"] = state
    return make_request("PATCH", f"/repos/{owner}/{repo}/issues/{issue_number}", json=data)

def list_issue_comments(owner: str, repo: str, issue_number: int) -> Any:
    """List issue comments."""
    return make_request("GET", f"/repos/{owner}/{repo}/issues/{issue_number}/comments")

def create_issue_comment(owner: str, repo: str, issue_number: int, body: str) -> Any:
    """Create an issue comment."""
    return make_request("POST", f"/repos/{owner}/{repo}/issues/{issue_number}/comments", json={"body": body})

def add_issue_labels(owner: str, repo: str, issue_number: int, labels: List[str]) -> Any:
    """Add labels to an issue."""
    return make_request("POST", f"/repos/{owner}/{repo}/issues/{issue_number}/labels", json={"labels": labels})

def remove_issue_label(owner: str, repo: str, issue_number: int, name: str) -> Any:
    """Remove a label from an issue."""
    return make_request("DELETE", f"/repos/{owner}/{repo}/issues/{issue_number}/labels/{name}")

def add_issue_assignees(owner: str, repo: str, issue_number: int, assignees: List[str]) -> Any:
    """Add assignees to an issue."""
    return make_request("POST", f"/repos/{owner}/{repo}/issues/{issue_number}/assignees", json={"assignees": assignees})

def remove_issue_assignees(owner: str, repo: str, issue_number: int, assignees: List[str]) -> Any:
    """Remove assignees from an issue."""
    return make_request("DELETE", f"/repos/{owner}/{repo}/issues/{issue_number}/assignees", json={"assignees": assignees})
