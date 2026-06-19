from typing import Any, Dict, Optional

from .http_client import request


def issues_search_accessible(
    *,
    state: Optional[str] = None,
    labels: Optional[str] = None,
    milestones: Optional[str] = None,
    q: Optional[str] = None,
    priority_repo_id: Optional[int] = None,
    type: Optional[str] = None,
    since: Optional[str] = None,
    before: Optional[str] = None,
    assigned: Optional[bool] = None,
    created: Optional[bool] = None,
    mentioned: Optional[bool] = None,
    review_requested: Optional[bool] = None,
    reviewed: Optional[bool] = None,
    owner: Optional[str] = None,
    team: Optional[str] = None,
    page: Optional[int] = None,
    limit: Optional[int] = None,
    sort: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {}
    for k, v in {
        "state": state,
        "labels": labels,
        "milestones": milestones,
        "q": q,
        "priority_repo_id": priority_repo_id,
        "type": type,
        "since": since,
        "before": before,
        "assigned": assigned,
        "created": created,
        "mentioned": mentioned,
        "review_requested": review_requested,
        "reviewed": reviewed,
        "owner": owner,
        "team": team,
        "page": page,
        "limit": limit,
        "sort": sort,
    }.items():
        if v is not None:
            params[k] = v
    return request("GET", "/repos/issues/search", params=params or None)


def repo_issues_list(
    owner: str,
    repo: str,
    *,
    state: Optional[str] = None,
    labels: Optional[str] = None,
    q: Optional[str] = None,
    type: Optional[str] = None,
    milestones: Optional[str] = None,
    since: Optional[str] = None,
    before: Optional[str] = None,
    created_by: Optional[str] = None,
    assigned_by: Optional[str] = None,
    mentioned_by: Optional[str] = None,
    page: Optional[int] = None,
    limit: Optional[int] = None,
    sort: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {}
    for k, v in {
        "state": state,
        "labels": labels,
        "q": q,
        "type": type,
        "milestones": milestones,
        "since": since,
        "before": before,
        "created_by": created_by,
        "assigned_by": assigned_by,
        "mentioned_by": mentioned_by,
        "page": page,
        "limit": limit,
        "sort": sort,
    }.items():
        if v is not None:
            params[k] = v
    return request("GET", f"/repos/{owner}/{repo}/issues", params=params or None)


def repo_issue_get(owner: str, repo: str, index: int) -> Any:
    return request("GET", f"/repos/{owner}/{repo}/issues/{index}")


def repo_issue_create(owner: str, repo: str, body: Dict[str, Any]) -> Any:
    return request("POST", f"/repos/{owner}/{repo}/issues", json=body)


def repo_issue_update(owner: str, repo: str, index: int, body: Dict[str, Any]) -> Any:
    return request("PATCH", f"/repos/{owner}/{repo}/issues/{index}", json=body)


def repo_issue_close(owner: str, repo: str, index: int) -> Any:
    # Forgejo: PATCH issue with state=closed
    return repo_issue_update(owner, repo, index, {"state": "closed"})


def repo_issue_labels_add(owner: str, repo: str, index: int, body: Dict[str, Any]) -> Any:
    return request("POST", f"/repos/{owner}/{repo}/issues/{index}/labels", json=body)


def repo_issue_comment_add(owner: str, repo: str, index: int, body: Dict[str, Any]) -> Any:
    return request("POST", f"/repos/{owner}/{repo}/issues/{index}/comments", json=body)


def repo_issue_comments_list(owner: str, repo: str, index: int, *, since: Optional[str] = None, before: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    if since is not None:
        params["since"] = since
    if before is not None:
        params["before"] = before
    return request("GET", f"/repos/{owner}/{repo}/issues/{index}/comments", params=params or None)
