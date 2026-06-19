from typing import Any, Optional

from generated_tools.github_common import compact, github_request


def list_repository_webhooks(owner: str, repo: str, per_page: int = 30, page: int = 1) -> str:
    return compact(github_request("GET", f"/repos/{owner}/{repo}/hooks", params={"per_page": per_page, "page": page}))


def get_repository_webhook(owner: str, repo: str, hook_id: int) -> str:
    return compact(github_request("GET", f"/repos/{owner}/{repo}/hooks/{hook_id}"))


def create_repository_webhook(owner: str, repo: str, config: dict[str, Any], events: Optional[list[str]] = None, active: bool = True, name: str = "web") -> str:
    return compact(github_request("POST", f"/repos/{owner}/{repo}/hooks", json_body={"name": name, "config": config, "events": events or ["push"], "active": active}))


def update_repository_webhook(owner: str, repo: str, hook_id: int, config: Optional[dict[str, Any]] = None, events: Optional[list[str]] = None, add_events: Optional[list[str]] = None, remove_events: Optional[list[str]] = None, active: Optional[bool] = None) -> str:
    return compact(github_request("PATCH", f"/repos/{owner}/{repo}/hooks/{hook_id}", json_body={"config": config, "events": events, "add_events": add_events, "remove_events": remove_events, "active": active}))


def delete_repository_webhook(owner: str, repo: str, hook_id: int) -> str:
    return compact(github_request("DELETE", f"/repos/{owner}/{repo}/hooks/{hook_id}"))
