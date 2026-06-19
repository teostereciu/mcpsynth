from typing import Any, Dict, Optional

from .github_client import request_json


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

    return request_json("GET", "/issues", params=params, accept=accept)
