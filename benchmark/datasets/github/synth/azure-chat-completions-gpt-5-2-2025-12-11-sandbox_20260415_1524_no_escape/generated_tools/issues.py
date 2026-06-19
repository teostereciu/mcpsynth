from __future__ import annotations

from typing import Any, Dict, List, Optional

from .github_client import GitHubClient


def list_my_issues(
    client: GitHubClient,
    *,
    filter: Optional[str] = None,
    state: Optional[str] = None,
    labels: Optional[str] = None,
    sort: Optional[str] = None,
    direction: Optional[str] = None,
    since: Optional[str] = None,
    collab: Optional[bool] = None,
    orgs: Optional[bool] = None,
    owned: Optional[bool] = None,
    pulls: Optional[bool] = None,
    per_page: int = 30,
    page: int = 1,
    paginate: bool = False,
) -> Any:
    params: Dict[str, Any] = {
        "filter": filter,
        "state": state,
        "labels": labels,
        "sort": sort,
        "direction": direction,
        "since": since,
        "collab": collab,
        "orgs": orgs,
        "owned": owned,
        "pulls": pulls,
        "per_page": per_page,
        "page": page,
    }
    params = {k: v for k, v in params.items() if v is not None}
    return client.request("GET", "/issues", params=params, paginate=paginate)


def list_repo_issues(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    milestone: Optional[str] = None,
    state: Optional[str] = None,
    assignee: Optional[str] = None,
    creator: Optional[str] = None,
    mentioned: Optional[str] = None,
    labels: Optional[str] = None,
    sort: Optional[str] = None,
    direction: Optional[str] = None,
    since: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    paginate: bool = False,
) -> Any:
    params: Dict[str, Any] = {
        "milestone": milestone,
        "state": state,
        "assignee": assignee,
        "creator": creator,
        "mentioned": mentioned,
        "labels": labels,
        "sort": sort,
        "direction": direction,
        "since": since,
        "per_page": per_page,
        "page": page,
    }
    params = {k: v for k, v in params.items() if v is not None}
    return client.request("GET", f"/repos/{owner}/{repo}/issues", params=params, paginate=paginate)


def get_issue(client: GitHubClient, *, owner: str, repo: str, issue_number: int) -> Any:
    return client.request("GET", f"/repos/{owner}/{repo}/issues/{issue_number}")


def create_issue(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    title: str,
    body: Optional[str] = None,
    assignees: Optional[List[str]] = None,
    milestone: Optional[int] = None,
    labels: Optional[List[str]] = None,
) -> Any:
    payload: Dict[str, Any] = {"title": title, "body": body, "assignees": assignees, "milestone": milestone, "labels": labels}
    payload = {k: v for k, v in payload.items() if v is not None}
    return client.request("POST", f"/repos/{owner}/{repo}/issues", json=payload)


def update_issue(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    issue_number: int,
    title: Optional[str] = None,
    body: Optional[str] = None,
    state: Optional[str] = None,
    state_reason: Optional[str] = None,
    assignees: Optional[List[str]] = None,
    milestone: Optional[int] = None,
    labels: Optional[List[str]] = None,
) -> Any:
    payload: Dict[str, Any] = {
        "title": title,
        "body": body,
        "state": state,
        "state_reason": state_reason,
        "assignees": assignees,
        "milestone": milestone,
        "labels": labels,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    return client.request("PATCH", f"/repos/{owner}/{repo}/issues/{issue_number}", json=payload)


def lock_issue(client: GitHubClient, *, owner: str, repo: str, issue_number: int, lock_reason: Optional[str] = None) -> Any:
    payload = {"lock_reason": lock_reason} if lock_reason else None
    return client.request("PUT", f"/repos/{owner}/{repo}/issues/{issue_number}/lock", json=payload)


def unlock_issue(client: GitHubClient, *, owner: str, repo: str, issue_number: int) -> Any:
    return client.request("DELETE", f"/repos/{owner}/{repo}/issues/{issue_number}/lock")


def add_assignees(client: GitHubClient, *, owner: str, repo: str, issue_number: int, assignees: List[str]) -> Any:
    return client.request("POST", f"/repos/{owner}/{repo}/issues/{issue_number}/assignees", json={"assignees": assignees})


def remove_assignees(client: GitHubClient, *, owner: str, repo: str, issue_number: int, assignees: List[str]) -> Any:
    return client.request("DELETE", f"/repos/{owner}/{repo}/issues/{issue_number}/assignees", json={"assignees": assignees})
