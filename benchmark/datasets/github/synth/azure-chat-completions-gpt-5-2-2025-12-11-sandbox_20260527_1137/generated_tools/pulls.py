from typing import Any, Dict, Optional

from .github_client import GitHubClient


def list_pull_requests(
    *,
    owner: str,
    repo: str,
    state: Optional[str] = None,
    head: Optional[str] = None,
    base: Optional[str] = None,
    sort: Optional[str] = None,
    direction: Optional[str] = None,
    per_page: Optional[int] = None,
    page: Optional[int] = None,
    accept: Optional[str] = None,
) -> Any:
    """GET /repos/{owner}/{repo}/pulls

    Lists pull requests in a specified repository.
    """
    client = GitHubClient()
    params: Dict[str, Any] = {
        "state": state,
        "head": head,
        "base": base,
        "sort": sort,
        "direction": direction,
        "per_page": per_page,
        "page": page,
    }
    return client.request("GET", f"/repos/{owner}/{repo}/pulls", params=params, accept=accept)
