from typing import Any, Dict, List, Optional

from ._client import request_json, split_owner_repo


def list_repo_webhooks(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    accept: Optional[str] = None,
) -> Any:
    """GET /repos/{owner}/{repo}/hooks

    Lists webhooks for a repository.
    """
    if owner is None or repo is None:
        parts = split_owner_repo(owner_repo)
        owner = owner or parts["owner"]
        repo = repo or parts["repo"]

    params: Dict[str, Any] = {"per_page": per_page, "page": page}
    return request_json("GET", f"/repos/{owner}/{repo}/hooks", params=params, accept=accept)


def create_repo_webhook(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    config: Dict[str, Any],
    events: Optional[List[str]] = None,
    active: bool = True,
    name: str = "web",
    accept: Optional[str] = None,
) -> Any:
    """POST /repos/{owner}/{repo}/hooks

    Create a repository webhook.
    """
    if owner is None or repo is None:
        parts = split_owner_repo(owner_repo)
        owner = owner or parts["owner"]
        repo = repo or parts["repo"]

    payload: Dict[str, Any] = {"name": name, "active": active, "config": config}
    if events is not None:
        payload["events"] = events

    return request_json("POST", f"/repos/{owner}/{repo}/hooks", json=payload, accept=accept)


def get_repo_webhook(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    hook_id: int,
    accept: Optional[str] = None,
) -> Any:
    """GET /repos/{owner}/{repo}/hooks/{hook_id}

    Get a repository webhook.
    """
    if owner is None or repo is None:
        parts = split_owner_repo(owner_repo)
        owner = owner or parts["owner"]
        repo = repo or parts["repo"]

    return request_json("GET", f"/repos/{owner}/{repo}/hooks/{hook_id}", accept=accept)


def update_repo_webhook(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    hook_id: int,
    config: Optional[Dict[str, Any]] = None,
    events: Optional[List[str]] = None,
    add_events: Optional[List[str]] = None,
    remove_events: Optional[List[str]] = None,
    active: Optional[bool] = None,
    accept: Optional[str] = None,
) -> Any:
    """PATCH /repos/{owner}/{repo}/hooks/{hook_id}

    Update a repository webhook.
    """
    if owner is None or repo is None:
        parts = split_owner_repo(owner_repo)
        owner = owner or parts["owner"]
        repo = repo or parts["repo"]

    payload: Dict[str, Any] = {}
    for k, v in {
        "config": config,
        "events": events,
        "add_events": add_events,
        "remove_events": remove_events,
        "active": active,
    }.items():
        if v is not None:
            payload[k] = v

    return request_json("PATCH", f"/repos/{owner}/{repo}/hooks/{hook_id}", json=payload, accept=accept)
