from typing import Any, Optional

from ._client import gh_request


# Docs: docs/api_pulls-pulls.md

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
    """GET /repos/{owner}/{repo}/pulls — List pull requests."""
    return gh_request(
        "GET",
        "/repos/{owner}/{repo}/pulls",
        path_params={"owner": owner, "repo": repo},
        query={
            "state": state,
            "head": head,
            "base": base,
            "sort": sort,
            "direction": direction,
            "per_page": per_page,
            "page": page,
        },
        accept=accept,
    )
