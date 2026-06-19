from typing import Any, Dict, Optional

from .github_client import GitHubClient


def list_repo_webhooks(owner: str, repo: str, per_page: int = 30, page: int = 1) -> Any:
    client = GitHubClient()
    return client.request("GET", f"/repos/{owner}/{repo}/hooks", params={"per_page": per_page, "page": page})


def get_repo_webhook(owner: str, repo: str, hook_id: int) -> Any:
    client = GitHubClient()
    return client.request("GET", f"/repos/{owner}/{repo}/hooks/{hook_id}")


def create_repo_webhook(owner: str, repo: str, config: Dict[str, Any], events: Optional[list] = None, active: bool = True, name: str = "web") -> Any:
    client = GitHubClient()
    payload: Dict[str, Any] = {"name": name, "active": active, "config": config}
    if events is not None:
        payload["events"] = events
    return client.request("POST", f"/repos/{owner}/{repo}/hooks", json=payload)


def update_repo_webhook(owner: str, repo: str, hook_id: int, config: Optional[Dict[str, Any]] = None, events: Optional[list] = None, active: Optional[bool] = None) -> Any:
    client = GitHubClient()
    payload: Dict[str, Any] = {}
    if config is not None:
        payload["config"] = config
    if events is not None:
        payload["events"] = events
    if active is not None:
        payload["active"] = active
    return client.request("PATCH", f"/repos/{owner}/{repo}/hooks/{hook_id}", json=payload)


def delete_repo_webhook(owner: str, repo: str, hook_id: int) -> Any:
    client = GitHubClient()
    return client.request("DELETE", f"/repos/{owner}/{repo}/hooks/{hook_id}")


def ping_repo_webhook(owner: str, repo: str, hook_id: int) -> Any:
    client = GitHubClient()
    return client.request("POST", f"/repos/{owner}/{repo}/hooks/{hook_id}/pings")
