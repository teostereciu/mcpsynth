from typing import Any, Dict, Optional

from .github_client import GitHubClient


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
    accept: str = "application/vnd.github+json",
    client: Optional[GitHubClient] = None,
) -> Any:
    """GET /issues — List issues assigned to the authenticated user."""
    c = client or GitHubClient()
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
    return c.request("GET", "/issues", params=params, accept=accept)
