from typing import Any, Dict, Optional

from ._client import GitHubClient, split_repo


def list_repo_webhooks(repo: str, per_page: int = 30, page: int = 1) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    return client.request("GET", f"/repos/{owner}/{name}/hooks", params={"per_page": per_page, "page": page})


def get_repo_webhook(repo: str, hook_id: int) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    return client.request("GET", f"/repos/{owner}/{name}/hooks/{hook_id}")


def create_repo_webhook(repo: str, config: Dict[str, Any], events: Optional[list] = None, active: bool = True, name: str = "web") -> Any:
    owner, rname = split_repo(repo)
    client = GitHubClient()
    payload: Dict[str, Any] = {"name": name, "active": active, "config": config}
    if events is not None:
        payload["events"] = events
    return client.request("POST", f"/repos/{owner}/{rname}/hooks", json=payload, expected=(201,))


def update_repo_webhook(repo: str, hook_id: int, config: Optional[Dict[str, Any]] = None, events: Optional[list] = None, active: Optional[bool] = None, name: Optional[str] = None) -> Any:
    owner, rname = split_repo(repo)
    client = GitHubClient()
    payload: Dict[str, Any] = {}
    if config is not None:
        payload["config"] = config
    if events is not None:
        payload["events"] = events
    if active is not None:
        payload["active"] = active
    if name is not None:
        payload["name"] = name
    return client.request("PATCH", f"/repos/{owner}/{rname}/hooks/{hook_id}", json=payload)


def delete_repo_webhook(repo: str, hook_id: int) -> Any:
    owner, rname = split_repo(repo)
    client = GitHubClient()
    return client.request("DELETE", f"/repos/{owner}/{rname}/hooks/{hook_id}", expected=(204,))


def ping_repo_webhook(repo: str, hook_id: int) -> Any:
    owner, rname = split_repo(repo)
    client = GitHubClient()
    return client.request("POST", f"/repos/{owner}/{rname}/hooks/{hook_id}/pings", expected=(204,))
