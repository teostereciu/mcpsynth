from typing import Any, Dict, List, Optional

from .github_client import GitHubClient


def list_my_issues(
    client: GitHubClient,
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
) -> Any:
    params: Dict[str, Any] = {
        "filter": filter,
        "state": state,
        "sort": sort,
        "direction": direction,
        "per_page": per_page,
        "page": page,
    }
    if labels is not None:
        params["labels"] = labels
    if since is not None:
        params["since"] = since
    if collab is not None:
        params["collab"] = collab
    if orgs is not None:
        params["orgs"] = orgs
    if owned is not None:
        params["owned"] = owned
    if pulls is not None:
        params["pulls"] = pulls
    return client.request("GET", "/issues", params=params)


def list_repo_issues(
    client: GitHubClient,
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
) -> Any:
    params: Dict[str, Any] = {
        "state": state,
        "sort": sort,
        "direction": direction,
        "per_page": per_page,
        "page": page,
    }
    if milestone is not None:
        params["milestone"] = milestone
    if assignee is not None:
        params["assignee"] = assignee
    if creator is not None:
        params["creator"] = creator
    if mentioned is not None:
        params["mentioned"] = mentioned
    if labels is not None:
        params["labels"] = labels
    if since is not None:
        params["since"] = since
    return client.request("GET", f"/repos/{owner}/{repo}/issues", params=params)


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
    payload: Dict[str, Any] = {"title": title}
    if body is not None:
        payload["body"] = body
    if assignees is not None:
        payload["assignees"] = assignees
    if milestone is not None:
        payload["milestone"] = milestone
    if labels is not None:
        payload["labels"] = labels
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
    payload: Dict[str, Any] = {}
    if title is not None:
        payload["title"] = title
    if body is not None:
        payload["body"] = body
    if state is not None:
        payload["state"] = state
    if state_reason is not None:
        payload["state_reason"] = state_reason
    if assignees is not None:
        payload["assignees"] = assignees
    if milestone is not None:
        payload["milestone"] = milestone
    if labels is not None:
        payload["labels"] = labels
    return client.request("PATCH", f"/repos/{owner}/{repo}/issues/{issue_number}", json=payload)


def lock_issue(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    issue_number: int,
    lock_reason: Optional[str] = None,
) -> Any:
    payload: Dict[str, Any] = {}
    if lock_reason is not None:
        payload["lock_reason"] = lock_reason
    return client.request("PUT", f"/repos/{owner}/{repo}/issues/{issue_number}/lock", json=payload)


def unlock_issue(client: GitHubClient, *, owner: str, repo: str, issue_number: int) -> Any:
    return client.request("DELETE", f"/repos/{owner}/{repo}/issues/{issue_number}/lock")
