from typing import Any, Dict, Optional

from ._client import request_json, split_owner_repo


def list_pull_requests(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    state: str = "open",
    head: Optional[str] = None,
    base: Optional[str] = None,
    sort: str = "created",
    direction: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    accept: Optional[str] = None,
) -> Any:
    """GET /repos/{owner}/{repo}/pulls

    Lists pull requests in a specified repository.
    """
    if owner is None or repo is None:
        parts = split_owner_repo(owner_repo)
        owner = owner or parts["owner"]
        repo = repo or parts["repo"]

    params: Dict[str, Any] = {"state": state, "sort": sort, "per_page": per_page, "page": page}
    if head is not None:
        params["head"] = head
    if base is not None:
        params["base"] = base
    if direction is not None:
        params["direction"] = direction

    return request_json("GET", f"/repos/{owner}/{repo}/pulls", params=params, accept=accept)
