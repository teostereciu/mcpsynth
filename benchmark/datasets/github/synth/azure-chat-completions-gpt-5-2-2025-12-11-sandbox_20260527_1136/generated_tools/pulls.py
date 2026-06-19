from typing import Any, Dict, Optional

from .http_client import GitHubClient


def list_pull_requests(
    owner: str,
    repo: str,
    *,
    state: str = "open",
    head: Optional[str] = None,
    base: Optional[str] = None,
    sort: str = "created",
    direction: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
) -> Dict[str, Any]:
    """GET /repos/{owner}/{repo}/pulls"""
    return GitHubClient().request(
        "GET",
        f"/repos/{owner}/{repo}/pulls",
        params={
            "state": state,
            "head": head,
            "base": base,
            "sort": sort,
            "direction": direction,
            "per_page": per_page,
            "page": page,
        },
    )
