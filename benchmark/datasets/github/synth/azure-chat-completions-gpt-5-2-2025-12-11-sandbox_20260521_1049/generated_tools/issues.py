from typing import Any, Dict, List, Optional

from .http_client import request_json


def list_my_issues(
    *,
    filter: str = "assigned",
    state: str = "open",
    labels: Optional[str] = None,
    sort: str = "created",
    direction: str = "desc",
    since: Optional[str] = None,
    collab: Optional[bool] = None,
    orgs: Optional[bool] = None,
    owned: Optional[bool] = None,
    pulls: Optional[bool] = None,
    per_page: int = 30,
    page: int = 1,
    accept: str = "application/vnd.github+json",
) -> Any:
    """GET /issues - List issues assigned to the authenticated user."""
    status, data, _ = request_json(
        "GET",
        "/issues",
        params={
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
        },
        accept=accept,
    )
    return data


def list_repo_issues(
    *,
    owner: str,
    repo: str,
    milestone: Optional[str] = None,
    state: str = "open",
    assignee: Optional[str] = None,
    creator: Optional[str] = None,
    mentioned: Optional[str] = None,
    labels: Optional[str] = None,
    sort: str = "created",
    direction: str = "desc",
    since: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    accept: str = "application/vnd.github+json",
) -> Any:
    """GET /repos/{owner}/{repo}/issues - List repository issues."""
    status, data, _ = request_json(
        "GET",
        f"/repos/{owner}/{repo}/issues",
        params={
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
        },
        accept=accept,
    )
    return data


def create_issue(
    *,
    owner: str,
    repo: str,
    title: str,
    body: Optional[str] = None,
    assignees: Optional[List[str]] = None,
    milestone: Optional[int] = None,
    labels: Optional[List[str]] = None,
    accept: str = "application/vnd.github+json",
) -> Any:
    """POST /repos/{owner}/{repo}/issues - Create an issue."""
    status, data, _ = request_json(
        "POST",
        f"/repos/{owner}/{repo}/issues",
        json_body={
            "title": title,
            "body": body,
            "assignees": assignees,
            "milestone": milestone,
            "labels": labels,
        },
        accept=accept,
    )
    return data


def get_issue(
    *,
    owner: str,
    repo: str,
    issue_number: int,
    accept: str = "application/vnd.github+json",
) -> Any:
    """GET /repos/{owner}/{repo}/issues/{issue_number} - Get an issue."""
    status, data, _ = request_json(
        "GET",
        f"/repos/{owner}/{repo}/issues/{issue_number}",
        accept=accept,
    )
    return data


def update_issue(
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
    accept: str = "application/vnd.github+json",
) -> Any:
    """PATCH /repos/{owner}/{repo}/issues/{issue_number} - Update an issue."""
    status, data, _ = request_json(
        "PATCH",
        f"/repos/{owner}/{repo}/issues/{issue_number}",
        json_body={
            "title": title,
            "body": body,
            "state": state,
            "state_reason": state_reason,
            "assignees": assignees,
            "milestone": milestone,
            "labels": labels,
        },
        accept=accept,
    )
    return data
