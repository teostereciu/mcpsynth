from typing import Any, Dict, Optional

from .http_client import request


def repo_pulls_list(owner: str, repo: str, *, state: Optional[str] = None, page: Optional[int] = None, limit: Optional[int] = None) -> Any:
    # Forgejo: GET /repos/{owner}/{repo}/pulls
    params: Dict[str, Any] = {}
    if state is not None:
        params["state"] = state
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    return request("GET", f"/repos/{owner}/{repo}/pulls", params=params or None)


def repo_pull_get(owner: str, repo: str, index: int) -> Any:
    # Forgejo: GET /repos/{owner}/{repo}/pulls/{index}
    return request("GET", f"/repos/{owner}/{repo}/pulls/{index}")


def repo_pull_create(owner: str, repo: str, body: Dict[str, Any]) -> Any:
    # Forgejo: POST /repos/{owner}/{repo}/pulls
    return request("POST", f"/repos/{owner}/{repo}/pulls", json=body)


def repo_pull_merge(owner: str, repo: str, index: int, body: Optional[Dict[str, Any]] = None) -> Any:
    # Forgejo: POST /repos/{owner}/{repo}/pulls/{index}/merge
    return request("POST", f"/repos/{owner}/{repo}/pulls/{index}/merge", json=body or {})
