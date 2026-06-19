from typing import Any, Dict, Optional

from .http_client import GitHubClient, ok_or_error


def list_pull_requests(
    *,
    owner: str,
    repo: str,
    state: Optional[str] = None,
    head: Optional[str] = None,
    base: Optional[str] = None,
    sort: Optional[str] = None,
    direction: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    accept: Optional[str] = None,
) -> Any:
    """GET /repos/{owner}/{repo}/pulls - Lists pull requests in a specified repository."""
    client = GitHubClient()
    params: Dict[str, Any] = {"per_page": per_page, "page": page}
    for k, v in {
        "state": state,
        "head": head,
        "base": base,
        "sort": sort,
        "direction": direction,
    }.items():
        if v is not None:
            params[k] = v

    status, data, headers = client.request(
        "GET", f"/repos/{owner}/{repo}/pulls", params=params, accept=accept
    )
    return ok_or_error(status, data, headers)
