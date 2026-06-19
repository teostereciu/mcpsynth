from typing import Any, Dict, Optional

from ._client import gh_request, parse_owner_repo


def list_repo_webhooks(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    per_page: Optional[int] = None,
    page: Optional[int] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo required (or set GITHUB_TEST_REPO)"}
    return gh_request("GET", f"/repos/{o}/{r}/hooks", params={"per_page": per_page, "page": page})


def get_repo_webhook(
    *,
    hook_id: int,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo required (or set GITHUB_TEST_REPO)"}
    return gh_request("GET", f"/repos/{o}/{r}/hooks/{hook_id}")


def create_repo_webhook(
    *,
    config: Dict[str, Any],
    events: Optional[list[str]] = None,
    active: Optional[bool] = None,
    name: str = "web",
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo required (or set GITHUB_TEST_REPO)"}
    payload: Dict[str, Any] = {"name": name, "config": config}
    if events is not None:
        payload["events"] = events
    if active is not None:
        payload["active"] = active
    return gh_request("POST", f"/repos/{o}/{r}/hooks", json=payload)


def update_repo_webhook(
    *,
    hook_id: int,
    config: Optional[Dict[str, Any]] = None,
    events: Optional[list[str]] = None,
    add_events: Optional[list[str]] = None,
    remove_events: Optional[list[str]] = None,
    active: Optional[bool] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo required (or set GITHUB_TEST_REPO)"}
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
    return gh_request("PATCH", f"/repos/{o}/{r}/hooks/{hook_id}", json=payload)


def delete_repo_webhook(
    *,
    hook_id: int,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo required (or set GITHUB_TEST_REPO)"}
    return gh_request("DELETE", f"/repos/{o}/{r}/hooks/{hook_id}")


def ping_repo_webhook(
    *,
    hook_id: int,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo required (or set GITHUB_TEST_REPO)"}
    return gh_request("POST", f"/repos/{o}/{r}/hooks/{hook_id}/pings")
