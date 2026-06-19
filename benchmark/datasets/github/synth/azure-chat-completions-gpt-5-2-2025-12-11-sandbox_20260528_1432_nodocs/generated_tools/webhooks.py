from typing import Any, Dict, Optional

from .github_client import GitHubClient


def list_repo_webhooks(owner: str, repo: str, per_page: int = 30, page: int = 1) -> Any:
    """GET /repos/{owner}/{repo}/hooks"""
    params = {"per_page": per_page, "page": page}
    return GitHubClient().request("GET", f"/repos/{owner}/{repo}/hooks", params=params)


def get_repo_webhook(owner: str, repo: str, hook_id: int) -> Any:
    """GET /repos/{owner}/{repo}/hooks/{hook_id}"""
    return GitHubClient().request("GET", f"/repos/{owner}/{repo}/hooks/{hook_id}")


def create_repo_webhook(owner: str, repo: str, config: Dict[str, Any], events: Optional[list] = None, active: bool = True, name: str = "web") -> Any:
    """POST /repos/{owner}/{repo}/hooks"""
    payload: Dict[str, Any] = {"name": name, "active": active, "config": config}
    if events is not None:
        payload["events"] = events
    return GitHubClient().request("POST", f"/repos/{owner}/{repo}/hooks", json=payload)


def update_repo_webhook(owner: str, repo: str, hook_id: int, config: Optional[Dict[str, Any]] = None, events: Optional[list] = None, active: Optional[bool] = None, add_events: Optional[list] = None, remove_events: Optional[list] = None) -> Any:
    """PATCH /repos/{owner}/{repo}/hooks/{hook_id}"""
    payload: Dict[str, Any] = {}
    if config is not None:
        payload["config"] = config
    if events is not None:
        payload["events"] = events
    if active is not None:
        payload["active"] = active
    if add_events is not None:
        payload["add_events"] = add_events
    if remove_events is not None:
        payload["remove_events"] = remove_events
    return GitHubClient().request("PATCH", f"/repos/{owner}/{repo}/hooks/{hook_id}", json=payload)


def delete_repo_webhook(owner: str, repo: str, hook_id: int) -> Any:
    """DELETE /repos/{owner}/{repo}/hooks/{hook_id}"""
    return GitHubClient().request("DELETE", f"/repos/{owner}/{repo}/hooks/{hook_id}")


def ping_repo_webhook(owner: str, repo: str, hook_id: int) -> Any:
    """POST /repos/{owner}/{repo}/hooks/{hook_id}/pings"""
    return GitHubClient().request("POST", f"/repos/{owner}/{repo}/hooks/{hook_id}/pings")
