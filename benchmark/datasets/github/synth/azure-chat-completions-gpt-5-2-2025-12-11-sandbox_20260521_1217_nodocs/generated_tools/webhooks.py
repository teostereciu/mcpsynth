from typing import Any, Dict, Optional, List

from .http import request_json


def list_repo_webhooks(owner: str, repo: str, *, per_page: int = 30, page: int = 1) -> Any:
    return request_json("GET", f"/repos/{owner}/{repo}/hooks", params={"per_page": per_page, "page": page})


def get_repo_webhook(owner: str, repo: str, hook_id: int) -> Any:
    return request_json("GET", f"/repos/{owner}/{repo}/hooks/{hook_id}")


def create_repo_webhook(owner: str, repo: str, config: Dict[str, Any], *, events: Optional[List[str]] = None, active: bool = True, name: str = "web") -> Any:
    payload: Dict[str, Any] = {"name": name, "config": config, "active": active}
    if events is not None:
        payload["events"] = events
    return request_json("POST", f"/repos/{owner}/{repo}/hooks", json=payload)


def update_repo_webhook(owner: str, repo: str, hook_id: int, *, config: Optional[Dict[str, Any]] = None, events: Optional[List[str]] = None, active: Optional[bool] = None, add_events: Optional[List[str]] = None, remove_events: Optional[List[str]] = None) -> Any:
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
    return request_json("PATCH", f"/repos/{owner}/{repo}/hooks/{hook_id}", json=payload)


def delete_repo_webhook(owner: str, repo: str, hook_id: int) -> Any:
    return request_json("DELETE", f"/repos/{owner}/{repo}/hooks/{hook_id}")


def ping_repo_webhook(owner: str, repo: str, hook_id: int) -> Any:
    return request_json("POST", f"/repos/{owner}/{repo}/hooks/{hook_id}/pings")
