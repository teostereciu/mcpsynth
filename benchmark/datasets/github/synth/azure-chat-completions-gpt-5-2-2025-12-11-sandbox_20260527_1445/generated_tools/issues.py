from typing import Any, Dict, Optional

from ._client import gh_request, parse_owner_repo


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
    per_page: Optional[int] = None,
    page: Optional[int] = None,
) -> Any:
    return gh_request(
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
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    milestone: Optional[str] = None,
    state: Optional[str] = None,
    assignee: Optional[str] = None,
    creator: Optional[str] = None,
    mentioned: Optional[str] = None,
    labels: Optional[str] = None,
    sort: Optional[str] = None,
    direction: Optional[str] = None,
    since: Optional[str] = None,
    per_page: Optional[int] = None,
    page: Optional[int] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo required (or set GITHUB_TEST_REPO)"}
    return gh_request(
        "GET",
        f"/repos/{o}/{r}/issues",
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


def get_issue(
    *,
    issue_number: int,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo required (or set GITHUB_TEST_REPO)"}
    return gh_request("GET", f"/repos/{o}/{r}/issues/{issue_number}")


def create_issue(
    *,
    title: str,
    body: Optional[str] = None,
    assignees: Optional[list[str]] = None,
    milestone: Optional[int] = None,
    labels: Optional[list[str]] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo required (or set GITHUB_TEST_REPO)"}
    payload: Dict[str, Any] = {"title": title}
    if body is not None:
        payload["body"] = body
    if assignees is not None:
        payload["assignees"] = assignees
    if milestone is not None:
        payload["milestone"] = milestone
    if labels is not None:
        payload["labels"] = labels
    return gh_request("POST", f"/repos/{o}/{r}/issues", json=payload)


def update_issue(
    *,
    issue_number: int,
    title: Optional[str] = None,
    body: Optional[str] = None,
    state: Optional[str] = None,
    state_reason: Optional[str] = None,
    assignees: Optional[list[str]] = None,
    milestone: Optional[int] = None,
    labels: Optional[list[str]] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo required (or set GITHUB_TEST_REPO)"}
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
    return gh_request("PATCH", f"/repos/{o}/{r}/issues/{issue_number}", json=payload)


def lock_issue(
    *,
    issue_number: int,
    lock_reason: Optional[str] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo required (or set GITHUB_TEST_REPO)"}
    payload: Dict[str, Any] = {}
    if lock_reason is not None:
        payload["lock_reason"] = lock_reason
    return gh_request("PUT", f"/repos/{o}/{r}/issues/{issue_number}/lock", json=payload or None)


def unlock_issue(
    *,
    issue_number: int,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo required (or set GITHUB_TEST_REPO)"}
    return gh_request("DELETE", f"/repos/{o}/{r}/issues/{issue_number}/lock")
