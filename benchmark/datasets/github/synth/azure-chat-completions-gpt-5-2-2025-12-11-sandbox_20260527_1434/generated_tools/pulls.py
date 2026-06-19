from typing import Any, Dict, Optional

from .http_client import request_json


def list_pull_requests(
    *,
    owner: str,
    repo: str,
    state: str = "open",
    head: Optional[str] = None,
    base: Optional[str] = None,
    sort: str = "created",
    direction: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    accept: str = "application/vnd.github+json",
) -> Any:
    """GET /repos/{owner}/{repo}/pulls

    Lists pull requests in a specified repository.
    """
    params: Dict[str, Any] = {"state": state, "sort": sort, "per_page": per_page, "page": page}
    if head is not None:
        params["head"] = head
    if base is not None:
        params["base"] = base
    if direction is not None:
        params["direction"] = direction

    return request_json("GET", f"/repos/{owner}/{repo}/pulls", params=params, accept=accept)
