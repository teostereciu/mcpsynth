from typing import Any, Dict, List, Optional
from .client import make_request

def list_pull_requests(owner: str, repo: str, state: str = "open", per_page: int = 30, page: int = 1) -> Any:
    """List pull requests."""
    return make_request("GET", f"/repos/{owner}/{repo}/pulls", params={"state": state, "per_page": per_page, "page": page})

def get_pull_request(owner: str, repo: str, pull_number: int) -> Any:
    """Get a pull request."""
    return make_request("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}")

def create_pull_request(owner: str, repo: str, title: str, head: str, base: str, body: Optional[str] = None) -> Any:
    """Create a pull request."""
    data = {"title": title, "head": head, "base": base}
    if body is not None: data["body"] = body
    return make_request("POST", f"/repos/{owner}/{repo}/pulls", json=data)

def update_pull_request(owner: str, repo: str, pull_number: int, title: Optional[str] = None, body: Optional[str] = None, state: Optional[str] = None) -> Any:
    """Update a pull request."""
    data = {}
    if title is not None: data["title"] = title
    if body is not None: data["body"] = body
    if state is not None: data["state"] = state
    return make_request("PATCH", f"/repos/{owner}/{repo}/pulls/{pull_number}", json=data)

def merge_pull_request(owner: str, repo: str, pull_number: int, commit_title: Optional[str] = None, merge_method: str = "merge") -> Any:
    """Merge a pull request."""
    data = {"merge_method": merge_method}
    if commit_title is not None: data["commit_title"] = commit_title
    return make_request("PUT", f"/repos/{owner}/{repo}/pulls/{pull_number}/merge", json=data)

def create_pull_request_review(owner: str, repo: str, pull_number: int, event: str, body: Optional[str] = None) -> Any:
    """Create a review for a pull request."""
    data = {"event": event}
    if body is not None: data["body"] = body
    return make_request("POST", f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews", json=data)
