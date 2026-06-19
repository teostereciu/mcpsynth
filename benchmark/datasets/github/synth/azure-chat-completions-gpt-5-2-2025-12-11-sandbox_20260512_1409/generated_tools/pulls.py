from typing import Any, Dict, List, Optional

from .github_client import GitHubClient


def list_pulls(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    state: str = "open",
    head: Optional[str] = None,
    base: Optional[str] = None,
    sort: str = "created",
    direction: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
) -> Any:
    params: Dict[str, Any] = {"state": state, "sort": sort, "per_page": per_page, "page": page}
    if head is not None:
        params["head"] = head
    if base is not None:
        params["base"] = base
    if direction is not None:
        params["direction"] = direction
    return client.request("GET", f"/repos/{owner}/{repo}/pulls", params=params)


def get_pull(client: GitHubClient, *, owner: str, repo: str, pull_number: int) -> Any:
    return client.request("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}")


def create_pull(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    title: str,
    head: str,
    base: str,
    body: Optional[str] = None,
    draft: Optional[bool] = None,
    maintainer_can_modify: Optional[bool] = None,
) -> Any:
    payload: Dict[str, Any] = {"title": title, "head": head, "base": base}
    if body is not None:
        payload["body"] = body
    if draft is not None:
        payload["draft"] = draft
    if maintainer_can_modify is not None:
        payload["maintainer_can_modify"] = maintainer_can_modify
    return client.request("POST", f"/repos/{owner}/{repo}/pulls", json=payload)


def update_pull(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    pull_number: int,
    title: Optional[str] = None,
    body: Optional[str] = None,
    state: Optional[str] = None,
    base: Optional[str] = None,
    maintainer_can_modify: Optional[bool] = None,
) -> Any:
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
    return client.request("PATCH", f"/repos/{owner}/{repo}/pulls/{pull_number}", json=payload)


def merge_pull(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    pull_number: int,
    commit_title: Optional[str] = None,
    commit_message: Optional[str] = None,
    merge_method: Optional[str] = None,
    sha: Optional[str] = None,
) -> Any:
    payload: Dict[str, Any] = {}
    if commit_title is not None:
        payload["commit_title"] = commit_title
    if commit_message is not None:
        payload["commit_message"] = commit_message
    if merge_method is not None:
        payload["merge_method"] = merge_method
    if sha is not None:
        payload["sha"] = sha
    return client.request("PUT", f"/repos/{owner}/{repo}/pulls/{pull_number}/merge", json=payload)


def list_pull_commits(client: GitHubClient, *, owner: str, repo: str, pull_number: int, per_page: int = 30, page: int = 1) -> Any:
    return client.request(
        "GET",
        f"/repos/{owner}/{repo}/pulls/{pull_number}/commits",
        params={"per_page": per_page, "page": page},
    )


def list_pull_files(client: GitHubClient, *, owner: str, repo: str, pull_number: int, per_page: int = 30, page: int = 1) -> Any:
    return client.request(
        "GET",
        f"/repos/{owner}/{repo}/pulls/{pull_number}/files",
        params={"per_page": per_page, "page": page},
    )


def create_pull_review(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    pull_number: int,
    body: Optional[str] = None,
    event: Optional[str] = None,
    comments: Optional[List[Dict[str, Any]]] = None,
) -> Any:
    payload: Dict[str, Any] = {}
    if body is not None:
        payload["body"] = body
    if event is not None:
        payload["event"] = event
    if comments is not None:
        payload["comments"] = comments
    return client.request("POST", f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews", json=payload)
