from typing import Any, Dict, Optional

from .github_client import GitHubClient


def list_pull_requests(owner: str, repo: str, state: str = "open", base: Optional[str] = None, head: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    client = GitHubClient()
    params: Dict[str, Any] = {"state": state, "per_page": per_page, "page": page}
    if base is not None:
        params["base"] = base
    if head is not None:
        params["head"] = head
    return client.request("GET", f"/repos/{owner}/{repo}/pulls", params=params)


def get_pull_request(owner: str, repo: str, pull_number: int) -> Any:
    client = GitHubClient()
    return client.request("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}")


def create_pull_request(owner: str, repo: str, title: str, head: str, base: str, body: Optional[str] = None, draft: bool = False) -> Any:
    client = GitHubClient()
    payload: Dict[str, Any] = {"title": title, "head": head, "base": base, "draft": draft}
    if body is not None:
        payload["body"] = body
    return client.request("POST", f"/repos/{owner}/{repo}/pulls", json=payload)


def update_pull_request(owner: str, repo: str, pull_number: int, title: Optional[str] = None, body: Optional[str] = None, state: Optional[str] = None) -> Any:
    client = GitHubClient()
    payload: Dict[str, Any] = {}
    if title is not None:
        payload["title"] = title
    if body is not None:
        payload["body"] = body
    if state is not None:
        payload["state"] = state
    return client.request("PATCH", f"/repos/{owner}/{repo}/pulls/{pull_number}", json=payload)


def list_pull_reviews(owner: str, repo: str, pull_number: int, per_page: int = 30, page: int = 1) -> Any:
    client = GitHubClient()
    return client.request("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews", params={"per_page": per_page, "page": page})


def create_pull_review(owner: str, repo: str, pull_number: int, body: str, event: str = "COMMENT", comments: Optional[list] = None, commit_id: Optional[str] = None) -> Any:
    client = GitHubClient()
    payload: Dict[str, Any] = {"body": body, "event": event}
    if comments is not None:
        payload["comments"] = comments
    if commit_id is not None:
        payload["commit_id"] = commit_id
    return client.request("POST", f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews", json=payload)


def merge_pull_request(owner: str, repo: str, pull_number: int, commit_title: Optional[str] = None, commit_message: Optional[str] = None, merge_method: str = "merge") -> Any:
    client = GitHubClient()
    payload: Dict[str, Any] = {"merge_method": merge_method}
    if commit_title is not None:
        payload["commit_title"] = commit_title
    if commit_message is not None:
        payload["commit_message"] = commit_message
    return client.request("PUT", f"/repos/{owner}/{repo}/pulls/{pull_number}/merge", json=payload)
