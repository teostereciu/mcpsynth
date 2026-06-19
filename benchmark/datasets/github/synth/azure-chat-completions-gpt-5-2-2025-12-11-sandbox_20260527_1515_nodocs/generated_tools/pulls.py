from typing import Any, Dict, Optional

from .github_client import GitHubClient


client = GitHubClient()


def list_pulls(owner: str, repo: str, *, state: str = "open", base: Optional[str] = None, head: Optional[str] = None, per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    params: Dict[str, Any] = {"state": state, "per_page": per_page, "page": page}
    if base is not None:
        params["base"] = base
    if head is not None:
        params["head"] = head
    return client.request("GET", f"/repos/{owner}/{repo}/pulls", params=params)


def get_pull(owner: str, repo: str, pull_number: int) -> Dict[str, Any]:
    return client.request("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}")


def create_pull(owner: str, repo: str, title: str, head: str, base: str, *, body: Optional[str] = None, draft: bool = False) -> Dict[str, Any]:
    payload: Dict[str, Any] = {"title": title, "head": head, "base": base, "draft": draft}
    if body is not None:
        payload["body"] = body
    return client.request("POST", f"/repos/{owner}/{repo}/pulls", json=payload)


def update_pull(owner: str, repo: str, pull_number: int, *, title: Optional[str] = None, body: Optional[str] = None, state: Optional[str] = None, base: Optional[str] = None) -> Dict[str, Any]:
    payload: Dict[str, Any] = {}
    if title is not None:
        payload["title"] = title
    if body is not None:
        payload["body"] = body
    if state is not None:
        payload["state"] = state
    if base is not None:
        payload["base"] = base
    return client.request("PATCH", f"/repos/{owner}/{repo}/pulls/{pull_number}", json=payload)


def create_pull_review(owner: str, repo: str, pull_number: int, *, body: Optional[str] = None, event: str = "COMMENT", comments: Optional[list[dict]] = None) -> Dict[str, Any]:
    payload: Dict[str, Any] = {"event": event}
    if body is not None:
        payload["body"] = body
    if comments is not None:
        payload["comments"] = comments
    return client.request("POST", f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews", json=payload)


def merge_pull(owner: str, repo: str, pull_number: int, *, commit_title: Optional[str] = None, commit_message: Optional[str] = None, merge_method: str = "merge", sha: Optional[str] = None) -> Dict[str, Any]:
    payload: Dict[str, Any] = {"merge_method": merge_method}
    if commit_title is not None:
        payload["commit_title"] = commit_title
    if commit_message is not None:
        payload["commit_message"] = commit_message
    if sha is not None:
        payload["sha"] = sha
    return client.request("PUT", f"/repos/{owner}/{repo}/pulls/{pull_number}/merge", json=payload)


def list_pull_files(owner: str, repo: str, pull_number: int, *, per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    return client.request(
        "GET",
        f"/repos/{owner}/{repo}/pulls/{pull_number}/files",
        params={"per_page": per_page, "page": page},
    )


def list_pull_comments(owner: str, repo: str, pull_number: int, *, per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    return client.request(
        "GET",
        f"/repos/{owner}/{repo}/pulls/{pull_number}/comments",
        params={"per_page": per_page, "page": page},
    )
