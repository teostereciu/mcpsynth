from __future__ import annotations

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
    per_page: int = 30,
    page: int = 1,
    paginate: bool = False,
) -> Any:
    params: Dict[str, Any] = {
        "state": state,
        "head": head,
        "base": base,
        "sort": sort,
        "direction": direction,
        "per_page": per_page,
        "page": page,
    }
    params = {k: v for k, v in params.items() if v is not None}
    return client.request("GET", f"/repos/{owner}/{repo}/pulls", params=params, paginate=paginate)


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
    maintainer_can_modify: Optional[bool] = None,
    draft: Optional[bool] = None,
) -> Any:
    payload: Dict[str, Any] = {
        "title": title,
        "head": head,
        "base": base,
        "body": body,
        "maintainer_can_modify": maintainer_can_modify,
        "draft": draft,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
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
    payload: Dict[str, Any] = {
        "title": title,
        "body": body,
        "state": state,
        "base": base,
        "maintainer_can_modify": maintainer_can_modify,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    return client.request("PATCH", f"/repos/{owner}/{repo}/pulls/{pull_number}", json=payload)


def merge_pull(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    pull_number: int,
    commit_title: Optional[str] = None,
    commit_message: Optional[str] = None,
    sha: Optional[str] = None,
    merge_method: Optional[str] = None,
) -> Any:
    payload: Dict[str, Any] = {
        "commit_title": commit_title,
        "commit_message": commit_message,
        "sha": sha,
        "merge_method": merge_method,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    return client.request("PUT", f"/repos/{owner}/{repo}/pulls/{pull_number}/merge", json=payload)


def request_reviewers(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    pull_number: int,
    reviewers: Optional[List[str]] = None,
    team_reviewers: Optional[List[str]] = None,
) -> Any:
    payload: Dict[str, Any] = {"reviewers": reviewers, "team_reviewers": team_reviewers}
    payload = {k: v for k, v in payload.items() if v is not None}
    return client.request("POST", f"/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers", json=payload)


def remove_requested_reviewers(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    pull_number: int,
    reviewers: Optional[List[str]] = None,
    team_reviewers: Optional[List[str]] = None,
) -> Any:
    payload: Dict[str, Any] = {"reviewers": reviewers, "team_reviewers": team_reviewers}
    payload = {k: v for k, v in payload.items() if v is not None}
    return client.request("DELETE", f"/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers", json=payload)
