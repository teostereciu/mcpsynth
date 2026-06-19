from typing import Any, Dict, List, Optional

from .http_client import request_json


def list_pull_requests(
    *,
    owner: str,
    repo: str,
    state: str = "open",
    head: Optional[str] = None,
    base: Optional[str] = None,
    sort: str = "created",
    direction: str = "desc",
    per_page: int = 30,
    page: int = 1,
    accept: str = "application/vnd.github+json",
) -> Any:
    """GET /repos/{owner}/{repo}/pulls - List pull requests."""
    _, data, _ = request_json(
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
        accept=accept,
    )
    return data


def create_pull_request(
    *,
    owner: str,
    repo: str,
    title: str,
    head: str,
    base: str,
    body: Optional[str] = None,
    draft: Optional[bool] = None,
    maintainer_can_modify: Optional[bool] = None,
    accept: str = "application/vnd.github+json",
) -> Any:
    """POST /repos/{owner}/{repo}/pulls - Create a pull request."""
    _, data, _ = request_json(
        "POST",
        f"/repos/{owner}/{repo}/pulls",
        json_body={
            "title": title,
            "head": head,
            "base": base,
            "body": body,
            "draft": draft,
            "maintainer_can_modify": maintainer_can_modify,
        },
        accept=accept,
    )
    return data


def get_pull_request(
    *,
    owner: str,
    repo: str,
    pull_number: int,
    accept: str = "application/vnd.github+json",
) -> Any:
    """GET /repos/{owner}/{repo}/pulls/{pull_number} - Get a pull request."""
    _, data, _ = request_json(
        "GET",
        f"/repos/{owner}/{repo}/pulls/{pull_number}",
        accept=accept,
    )
    return data


def update_pull_request(
    *,
    owner: str,
    repo: str,
    pull_number: int,
    title: Optional[str] = None,
    body: Optional[str] = None,
    state: Optional[str] = None,
    base: Optional[str] = None,
    maintainer_can_modify: Optional[bool] = None,
    accept: str = "application/vnd.github+json",
) -> Any:
    """PATCH /repos/{owner}/{repo}/pulls/{pull_number} - Update a pull request."""
    _, data, _ = request_json(
        "PATCH",
        f"/repos/{owner}/{repo}/pulls/{pull_number}",
        json_body={
            "title": title,
            "body": body,
            "state": state,
            "base": base,
            "maintainer_can_modify": maintainer_can_modify,
        },
        accept=accept,
    )
    return data


def merge_pull_request(
    *,
    owner: str,
    repo: str,
    pull_number: int,
    commit_title: Optional[str] = None,
    commit_message: Optional[str] = None,
    merge_method: Optional[str] = None,
    sha: Optional[str] = None,
    accept: str = "application/vnd.github+json",
) -> Any:
    """PUT /repos/{owner}/{repo}/pulls/{pull_number}/merge - Merge a pull request."""
    _, data, _ = request_json(
        "PUT",
        f"/repos/{owner}/{repo}/pulls/{pull_number}/merge",
        json_body={
            "commit_title": commit_title,
            "commit_message": commit_message,
            "merge_method": merge_method,
            "sha": sha,
        },
        accept=accept,
    )
    return data
