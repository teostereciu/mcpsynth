from typing import Any, Dict, Optional

from .github_client import GitHubClient, parse_owner_repo


def list_repo_webhooks(owner_repo: str, per_page: int = 100, max_pages: int = 5) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return GitHubClient().paginate(f"/repos/{owner}/{repo}/hooks", per_page=per_page, max_pages=max_pages)


def get_repo_webhook(owner_repo: str, hook_id: int) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return GitHubClient().request("GET", f"/repos/{owner}/{repo}/hooks/{hook_id}")


def create_repo_webhook(
    owner_repo: str,
    config: Dict[str, Any],
    events: Optional[list] = None,
    active: bool = True,
    name: str = "web",
) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    payload: Dict[str, Any] = {"name": name, "active": active, "config": config}
    if events is not None:
        payload["events"] = events
    return GitHubClient().request("POST", f"/repos/{owner}/{repo}/hooks", json=payload)


def update_repo_webhook(owner_repo: str, hook_id: int, config: Optional[Dict[str, Any]] = None, events: Optional[list] = None, active: Optional[bool] = None, name: Optional[str] = None) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    payload: Dict[str, Any] = {}
    if config is not None:
        payload["config"] = config
    if events is not None:
        payload["events"] = events
    if active is not None:
        payload["active"] = active
    if name is not None:
        payload["name"] = name
    return GitHubClient().request("PATCH", f"/repos/{owner}/{repo}/hooks/{hook_id}", json=payload)


def delete_repo_webhook(owner_repo: str, hook_id: int) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return GitHubClient().request("DELETE", f"/repos/{owner}/{repo}/hooks/{hook_id}")


def ping_repo_webhook(owner_repo: str, hook_id: int) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return GitHubClient().request("POST", f"/repos/{owner}/{repo}/hooks/{hook_id}/pings")
