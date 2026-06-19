from typing import Any, Dict, Optional

from ._client import GitHubClient


def list_pulls(
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
) -> Dict[str, Any]:
    """GET /repos/{owner}/{repo}/pulls - List pull requests."""
    c = GitHubClient()
    return c.request(
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


def create_pull(
    *,
    owner: str,
    repo: str,
    title: str,
    head: str,
    base: str,
    body: Optional[str] = None,
    draft: Optional[bool] = None,
    maintainer_can_modify: Optional[bool] = None,
) -> Dict[str, Any]:
    """POST /repos/{owner}/{repo}/pulls - Create a pull request."""
    c = GitHubClient()
    payload: Dict[str, Any] = {"title": title, "head": head, "base": base}
    if body is not None:
        payload["body"] = body
    if draft is not None:
        payload["draft"] = draft
    if maintainer_can_modify is not None:
        payload["maintainer_can_modify"] = maintainer_can_modify
    return c.request("POST", f"/repos/{owner}/{repo}/pulls", json=payload)


def get_pull(*, owner: str, repo: str, pull_number: int) -> Dict[str, Any]:
    """GET /repos/{owner}/{repo}/pulls/{pull_number} - Get a pull request."""
    c = GitHubClient()
    return c.request("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}")


def update_pull(
    *,
    owner: str,
    repo: str,
    pull_number: int,
    title: Optional[str] = None,
    body: Optional[str] = None,
    state: Optional[str] = None,
    base: Optional[str] = None,
    maintainer_can_modify: Optional[bool] = None,
) -> Dict[str, Any]:
    """PATCH /repos/{owner}/{repo}/pulls/{pull_number} - Update a pull request."""
    c = GitHubClient()
    payload: Dict[str, Any] = {}
    for k, v in {
        "title": title,
        "body": body,
        "state": state,
        "base": base,
        "maintainer_can_modify": maintainer_can_modify,
    }.items():
        if v is not None:
            payload[k] = v
    return c.request("PATCH", f"/repos/{owner}/{repo}/pulls/{pull_number}", json=payload)


def list_pull_commits(
    *, owner: str, repo: str, pull_number: int, per_page: int = 30, page: int = 1
) -> Dict[str, Any]:
    """GET /repos/{owner}/{repo}/pulls/{pull_number}/commits - List commits on a pull request."""
    c = GitHubClient()
    return c.request(
        "GET",
        f"/repos/{owner}/{repo}/pulls/{pull_number}/commits",
        params={"per_page": per_page, "page": page},
    )


def list_pull_files(
    *, owner: str, repo: str, pull_number: int, per_page: int = 30, page: int = 1
) -> Dict[str, Any]:
    """GET /repos/{owner}/{repo}/pulls/{pull_number}/files - List pull request files."""
    c = GitHubClient()
    return c.request(
        "GET",
        f"/repos/{owner}/{repo}/pulls/{pull_number}/files",
        params={"per_page": per_page, "page": page},
    )


def merge_pull(
    *,
    owner: str,
    repo: str,
    pull_number: int,
    commit_title: Optional[str] = None,
    commit_message: Optional[str] = None,
    sha: Optional[str] = None,
    merge_method: Optional[str] = None,
) -> Dict[str, Any]:
    """PUT /repos/{owner}/{repo}/pulls/{pull_number}/merge - Merge a pull request."""
    c = GitHubClient()
    payload: Dict[str, Any] = {}
    for k, v in {
        "commit_title": commit_title,
        "commit_message": commit_message,
        "sha": sha,
        "merge_method": merge_method,
    }.items():
        if v is not None:
            payload[k] = v
    return c.request("PUT", f"/repos/{owner}/{repo}/pulls/{pull_number}/merge", json=payload)


def update_pull_branch(
    *, owner: str, repo: str, pull_number: int, expected_head_sha: Optional[str] = None
) -> Dict[str, Any]:
    """PUT /repos/{owner}/{repo}/pulls/{pull_number}/update-branch - Update a pull request branch."""
    c = GitHubClient()
    payload: Dict[str, Any] = {}
    if expected_head_sha is not None:
        payload["expected_head_sha"] = expected_head_sha
    return c.request(
        "PUT", f"/repos/{owner}/{repo}/pulls/{pull_number}/update-branch", json=payload
    )
