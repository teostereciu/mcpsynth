from typing import Any, Dict, List, Optional, Union

from .http_client import GitHubClient, parse_owner_repo


def list_repo_webhooks(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """GET /repos/{owner}/{repo}/hooks"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    params = {"per_page": per_page, "page": page}
    return client.request("GET", f"/repos/{o}/{r}/hooks", params=params, accept=accept)


def get_repo_webhook(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    hook_id: int,
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """GET /repos/{owner}/{repo}/hooks/{hook_id}"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    return client.request("GET", f"/repos/{o}/{r}/hooks/{hook_id}", accept=accept)


def create_repo_webhook(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    config: Dict[str, Any],
    events: Optional[List[str]] = None,
    active: Optional[bool] = True,
    name: str = "web",
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """POST /repos/{owner}/{repo}/hooks"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    payload: Dict[str, Any] = {"name": name, "config": config}
    if events is not None:
        payload["events"] = events
    if active is not None:
        payload["active"] = active
    return client.request("POST", f"/repos/{o}/{r}/hooks", json=payload, accept=accept)


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
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """PATCH /repos/{owner}/{repo}/hooks/{hook_id}"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
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
    return client.request("PATCH", f"/repos/{o}/{r}/hooks/{hook_id}", json=payload, accept=accept)


def delete_repo_webhook(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    hook_id: int,
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """DELETE /repos/{owner}/{repo}/hooks/{hook_id}"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    return client.request("DELETE", f"/repos/{o}/{r}/hooks/{hook_id}", accept=accept)


def ping_repo_webhook(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    hook_id: int,
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """POST /repos/{owner}/{repo}/hooks/{hook_id}/pings"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    return client.request("POST", f"/repos/{o}/{r}/hooks/{hook_id}/pings", accept=accept)
