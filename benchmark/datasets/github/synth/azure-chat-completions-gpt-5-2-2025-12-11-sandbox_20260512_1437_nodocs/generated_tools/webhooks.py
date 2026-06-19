from typing import Any, Dict, List, Optional

from ._client import gh_request


def list_repo_webhooks(owner: str, repo: str, *, per_page: int = 30, page: int = 1) -> Any:
    return gh_request("GET", f"/repos/{owner}/{repo}/hooks", params={"per_page": per_page, "page": page})


def get_repo_webhook(owner: str, repo: str, hook_id: int) -> Any:
    return gh_request("GET", f"/repos/{owner}/{repo}/hooks/{hook_id}")


def create_repo_webhook(owner: str, repo: str, config: Dict[str, Any], *, events: Optional[List[str]] = None, active: bool = True, name: str = "web") -> Any:
    payload: Dict[str, Any] = {"name": name, "active": active, "config": config}
    if events is not None:
        payload["events"] = events
    return gh_request("POST", f"/repos/{owner}/{repo}/hooks", json=payload)


def update_repo_webhook(owner: str, repo: str, hook_id: int, *, config: Optional[Dict[str, Any]] = None, events: Optional[List[str]] = None, active: Optional[bool] = None, name: Optional[str] = None) -> Any:
    payload: Dict[str, Any] = {}
    if config is not None:
        payload["config"] = config
    if events is not None:
        payload["events"] = events
    if active is not None:
        payload["active"] = active
    if name is not None:
        payload["name"] = name
    return gh_request("PATCH", f"/repos/{owner}/{repo}/hooks/{hook_id}", json=payload)


def delete_repo_webhook(owner: str, repo: str, hook_id: int) -> Any:
    return gh_request("DELETE", f"/repos/{owner}/{repo}/hooks/{hook_id}")


def ping_repo_webhook(owner: str, repo: str, hook_id: int) -> Any:
    return gh_request("POST", f"/repos/{owner}/{repo}/hooks/{hook_id}/pings")


def test_repo_webhook(owner: str, repo: str, hook_id: int) -> Any:
    return gh_request("POST", f"/repos/{owner}/{repo}/hooks/{hook_id}/tests")
