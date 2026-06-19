from typing import Any, Dict, Optional

from ._client import get_client


def list_pull_requests(
    owner: str,
    repo: str,
    state: str = "open",
    head: Optional[str] = None,
    base: Optional[str] = None,
    sort: str = "created",
    direction: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
) -> Any:
    """GET /repos/{owner}/{repo}/pulls"""
    return get_client().request(
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


def get_pull_request(owner: str, repo: str, pull_number: int) -> Any:
    """GET /repos/{owner}/{repo}/pulls/{pull_number}"""
    return get_client().request("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}")


def create_pull_request(
    owner: str,
    repo: str,
    title: str,
    head: str,
    base: str,
    body: Optional[str] = None,
    draft: Optional[bool] = None,
    maintainer_can_modify: Optional[bool] = None,
) -> Any:
    """POST /repos/{owner}/{repo}/pulls"""
    payload: Dict[str, Any] = {
        "title": title,
        "head": head,
        "base": base,
        "body": body,
        "draft": draft,
        "maintainer_can_modify": maintainer_can_modify,
    }
    return get_client().request("POST", f"/repos/{owner}/{repo}/pulls", json=payload, expected=(201,))


def update_pull_request(
    owner: str,
    repo: str,
    pull_number: int,
    title: Optional[str] = None,
    body: Optional[str] = None,
    state: Optional[str] = None,
    base: Optional[str] = None,
    maintainer_can_modify: Optional[bool] = None,
) -> Any:
    """PATCH /repos/{owner}/{repo}/pulls/{pull_number}"""
    payload: Dict[str, Any] = {
        "title": title,
        "body": body,
        "state": state,
        "base": base,
        "maintainer_can_modify": maintainer_can_modify,
    }
    return get_client().request("PATCH", f"/repos/{owner}/{repo}/pulls/{pull_number}", json=payload)


def merge_pull_request(
    owner: str,
    repo: str,
    pull_number: int,
    commit_title: Optional[str] = None,
    commit_message: Optional[str] = None,
    merge_method: Optional[str] = None,
    sha: Optional[str] = None,
) -> Any:
    """PUT /repos/{owner}/{repo}/pulls/{pull_number}/merge"""
    payload: Dict[str, Any] = {
        "commit_title": commit_title,
        "commit_message": commit_message,
        "merge_method": merge_method,
        "sha": sha,
    }
    return get_client().request(
        "PUT",
        f"/repos/{owner}/{repo}/pulls/{pull_number}/merge",
        json=payload,
        expected=(200, 201, 204),
    )
