from typing import Any, Dict, List, Optional

from ._client import GitHubClient


def list_repo_webhooks(*, owner: str, repo: str, per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    """GET /repos/{owner}/{repo}/hooks - List repository webhooks."""
    c = GitHubClient()
    return c.request(
        "GET", f"/repos/{owner}/{repo}/hooks", params={"per_page": per_page, "page": page}
    )


def get_repo_webhook(*, owner: str, repo: str, hook_id: int) -> Dict[str, Any]:
    """GET /repos/{owner}/{repo}/hooks/{hook_id} - Get a repository webhook."""
    c = GitHubClient()
    return c.request("GET", f"/repos/{owner}/{repo}/hooks/{hook_id}")


def create_repo_webhook(
    *,
    owner: str,
    repo: str,
    url: str,
    content_type: str = "json",
    secret: Optional[str] = None,
    insecure_ssl: str = "0",
    events: Optional[List[str]] = None,
    active: bool = True,
) -> Dict[str, Any]:
    """POST /repos/{owner}/{repo}/hooks - Create a repository webhook."""
    c = GitHubClient()
    payload: Dict[str, Any] = {
        "name": "web",
        "active": active,
        "events": events or ["push"],
        "config": {
            "url": url,
            "content_type": content_type,
            "insecure_ssl": insecure_ssl,
        },
    }
    if secret is not None:
        payload["config"]["secret"] = secret
    return c.request("POST", f"/repos/{owner}/{repo}/hooks", json=payload)


def update_repo_webhook(
    *,
    owner: str,
    repo: str,
    hook_id: int,
    config: Optional[Dict[str, Any]] = None,
    events: Optional[List[str]] = None,
    add_events: Optional[List[str]] = None,
    remove_events: Optional[List[str]] = None,
    active: Optional[bool] = None,
) -> Dict[str, Any]:
    """PATCH /repos/{owner}/{repo}/hooks/{hook_id} - Update a repository webhook."""
    c = GitHubClient()
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
    return c.request("PATCH", f"/repos/{owner}/{repo}/hooks/{hook_id}", json=payload)


def delete_repo_webhook(*, owner: str, repo: str, hook_id: int) -> Dict[str, Any]:
    """DELETE /repos/{owner}/{repo}/hooks/{hook_id} - Delete a repository webhook."""
    c = GitHubClient()
    return c.request("DELETE", f"/repos/{owner}/{repo}/hooks/{hook_id}")
