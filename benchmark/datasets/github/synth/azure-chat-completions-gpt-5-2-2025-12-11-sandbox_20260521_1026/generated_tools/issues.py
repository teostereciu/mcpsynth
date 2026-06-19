from typing import Any, Dict, Optional

from .http_client import GitHubClient, ok_or_error


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
    accept: Optional[str] = None,
) -> Any:
    """GET /issues - List issues assigned to the authenticated user."""
    client = GitHubClient()
    params: Dict[str, Any] = {
        "per_page": per_page,
        "page": page,
    }
    for k, v in {
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
    }.items():
        if v is not None:
            params[k] = v

    status, data, headers = client.request("GET", "/issues", params=params, accept=accept)
    return ok_or_error(status, data, headers)


def list_org_issues_assigned_to_me(
    *,
    org: str,
    filter: Optional[str] = None,
    state: Optional[str] = None,
    labels: Optional[str] = None,
    sort: Optional[str] = None,
    direction: Optional[str] = None,
    since: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    accept: Optional[str] = None,
) -> Any:
    """GET /orgs/{org}/issues - List organization issues assigned to the authenticated user."""
    client = GitHubClient()
    params: Dict[str, Any] = {"per_page": per_page, "page": page}
    for k, v in {
        "filter": filter,
        "state": state,
        "labels": labels,
        "sort": sort,
        "direction": direction,
        "since": since,
    }.items():
        if v is not None:
            params[k] = v

    status, data, headers = client.request("GET", f"/orgs/{org}/issues", params=params, accept=accept)
    return ok_or_error(status, data, headers)
