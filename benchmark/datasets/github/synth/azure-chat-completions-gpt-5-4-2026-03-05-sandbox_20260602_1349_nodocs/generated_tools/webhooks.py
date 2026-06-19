from typing import Any, List, Optional

from generated_tools.github_common import clean_params, github_request


def list_repo_webhooks(owner: str, repo: str, per_page: int = 30, page: int = 1) -> Any:
    return github_request("GET", f"/repos/{owner}/{repo}/hooks", params=clean_params(per_page=per_page, page=page))


def get_repo_webhook(owner: str, repo: str, hook_id: int) -> Any:
    return github_request("GET", f"/repos/{owner}/{repo}/hooks/{hook_id}")


def create_repo_webhook(owner: str, repo: str, url: str, events: Optional[List[str]] = None, active: bool = True, content_type: str = "json", secret: Optional[str] = None, insecure_ssl: Optional[str] = None) -> Any:
    config = clean_params(url=url, content_type=content_type, secret=secret, insecure_ssl=insecure_ssl)
    payload = clean_params(name="web", active=active, events=events, config=config)
    return github_request("POST", f"/repos/{owner}/{repo}/hooks", json_body=payload)


def update_repo_webhook(owner: str, repo: str, hook_id: int, url: Optional[str] = None, events: Optional[List[str]] = None, add_events: Optional[List[str]] = None, remove_events: Optional[List[str]] = None, active: Optional[bool] = None, content_type: Optional[str] = None, secret: Optional[str] = None, insecure_ssl: Optional[str] = None) -> Any:
    config = clean_params(url=url, content_type=content_type, secret=secret, insecure_ssl=insecure_ssl)
    payload = clean_params(config=config if config else None, events=events, add_events=add_events, remove_events=remove_events, active=active)
    return github_request("PATCH", f"/repos/{owner}/{repo}/hooks/{hook_id}", json_body=payload)


def delete_repo_webhook(owner: str, repo: str, hook_id: int) -> Any:
    return github_request("DELETE", f"/repos/{owner}/{repo}/hooks/{hook_id}")


def ping_repo_webhook(owner: str, repo: str, hook_id: int) -> Any:
    return github_request("POST", f"/repos/{owner}/{repo}/hooks/{hook_id}/pings")
