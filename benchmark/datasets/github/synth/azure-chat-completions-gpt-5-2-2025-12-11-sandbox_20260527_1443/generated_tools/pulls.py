from typing import Any, Dict, Optional

from ._client import request_json


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
    """GET /repos/{owner}/{repo}/pulls"""
    params: Dict[str, Any] = {
        "state": state,
        "head": head,
        "base": base,
        "sort": sort,
        "direction": direction,
        "per_page": per_page,
        "page": page,
    }
    return request_json("GET", f"/repos/{owner}/{repo}/pulls", params=params, accept=accept)
