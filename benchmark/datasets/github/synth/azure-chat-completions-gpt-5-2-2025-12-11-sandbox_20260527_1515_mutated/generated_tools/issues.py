from typing import Any, Dict, Optional

from ._client import gh_request


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
    """GET /issues

    List issues assigned to the authenticated user.
    """
    params: Dict[str, Any] = {}
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
        "per_page": per_page,
        "page": page,
    }.items():
        if v is not None:
            params[k] = v
    return gh_request("GET", "/issues", params=params or None, accept=accept)
