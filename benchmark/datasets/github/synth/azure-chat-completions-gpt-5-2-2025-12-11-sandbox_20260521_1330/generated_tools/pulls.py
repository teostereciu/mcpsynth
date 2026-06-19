from typing import Any, Dict, List, Optional

from .github_client import GitHubClient


def list_pulls(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    state: Optional[str] = None,
    head: Optional[str] = None,
    base: Optional[str] = None,
    sort: Optional[str] = None,
    direction: Optional[str] = None,
    per_page: Optional[int] = None,
    page: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /repos/{owner}/{repo}/pulls"""
    return client.request(
        "GET",
        f"/repos/{owner}/{repo}/pulls",
        params={
            "state": state,
            "head": head,
            "base": base,
            "sort": sort,
            "direction": direction,
            "per_page": per_page,
            "page": page,
        },
    )


def get_pull(client: GitHubClient, *, owner: str, repo: str, pull_number: int) -> Dict[str, Any]:
    """GET /repos/{owner}/{repo}/pulls/{pull_number}"""
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
) -> Dict[str, Any]:
    """POST /repos/{owner}/{repo}/pulls"""
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
) -> Dict[str, Any]:
    """PATCH /repos/{owner}/{repo}/pulls/{pull_number}"""
    payload: Dict[str, Any] = {}
    for k, v in {
        "title": title,
        "body": body,
        "state": state,
        "base": base,
        "maintainer_can_modify": maintainer_can_modify,
    }.items():
        if v is not None:
            payload[k] = v
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
) -> Dict[str, Any]:
    """PUT /repos/{owner}/{repo}/pulls/{pull_number}/merge"""
    payload: Dict[str, Any] = {}
    for k, v in {
        "commit_title": commit_title,
        "commit_message": commit_message,
        "merge_method": merge_method,
        "sha": sha,
    }.items():
        if v is not None:
            payload[k] = v
    return client.request("PUT", f"/repos/{owner}/{repo}/pulls/{pull_number}/merge", json=payload)
