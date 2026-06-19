from typing import Any, Dict, Optional

from ._client import gh_request


# Docs: docs/api_issues-issues.md

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
    accept: Optional[str] = None,
) -> Any:
    """GET /issues — List issues assigned to the authenticated user."""
    return gh_request(
        "GET",
        "/issues",
        query={
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
