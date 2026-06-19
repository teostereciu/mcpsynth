from typing import Any, Dict, Optional

from ._client import GitHubClient


def list_my_issues(
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
) -> Dict[str, Any]:
    """GET /issues - List issues assigned to the authenticated user."""
    c = GitHubClient()
    return c.request(
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
    )


def list_repo_issues(
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
) -> Dict[str, Any]:
    """GET /repos/{owner}/{repo}/issues - List repository issues."""
    c = GitHubClient()
    return c.request(
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
    )


def create_issue(
    *,
    owner: str,
    repo: str,
    title: str,
    body: Optional[str] = None,
    assignees: Optional[list[str]] = None,
    milestone: Optional[int] = None,
    labels: Optional[list[str]] = None,
) -> Dict[str, Any]:
    """POST /repos/{owner}/{repo}/issues - Create an issue."""
    c = GitHubClient()
    payload: Dict[str, Any] = {"title": title}
    if body is not None:
        payload["body"] = body
    if assignees is not None:
        payload["assignees"] = assignees
    if milestone is not None:
        payload["milestone"] = milestone
    if labels is not None:
        payload["labels"] = labels
    return c.request("POST", f"/repos/{owner}/{repo}/issues", json=payload)


def get_issue(*, owner: str, repo: str, issue_number: int) -> Dict[str, Any]:
    """GET /repos/{owner}/{repo}/issues/{issue_number} - Get an issue."""
    c = GitHubClient()
    return c.request("GET", f"/repos/{owner}/{repo}/issues/{issue_number}")


def update_issue(
    *,
    owner: str,
    repo: str,
    issue_number: int,
    title: Optional[str] = None,
    body: Optional[str] = None,
    state: Optional[str] = None,
    state_reason: Optional[str] = None,
    assignees: Optional[list[str]] = None,
    milestone: Optional[int] = None,
    labels: Optional[list[str]] = None,
) -> Dict[str, Any]:
    """PATCH /repos/{owner}/{repo}/issues/{issue_number} - Update an issue."""
    c = GitHubClient()
    payload: Dict[str, Any] = {}
    for k, v in {
        "title": title,
        "body": body,
        "state": state,
        "state_reason": state_reason,
        "assignees": assignees,
        "milestone": milestone,
        "labels": labels,
    }.items():
        if v is not None:
            payload[k] = v
    return c.request("PATCH", f"/repos/{owner}/{repo}/issues/{issue_number}", json=payload)
