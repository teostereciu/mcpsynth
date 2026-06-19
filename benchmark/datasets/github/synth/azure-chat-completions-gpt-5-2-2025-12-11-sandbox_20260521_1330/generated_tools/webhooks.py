from typing import Any, Dict, List, Optional

from .github_client import GitHubClient


def list_repo_webhooks(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    per_page: Optional[int] = None,
    page: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /repos/{owner}/{repo}/hooks"""
    return client.request(
        "GET",
        f"/repos/{owner}/{repo}/hooks",
        params={"per_page": per_page, "page": page},
    )


def get_repo_webhook(client: GitHubClient, *, owner: str, repo: str, hook_id: int) -> Dict[str, Any]:
    """GET /repos/{owner}/{repo}/hooks/{hook_id}"""
    return client.request("GET", f"/repos/{owner}/{repo}/hooks/{hook_id}")


def create_repo_webhook(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    config: Dict[str, Any],
    events: Optional[List[str]] = None,
    active: Optional[bool] = None,
    name: str = "web",
) -> Dict[str, Any]:
    """POST /repos/{owner}/{repo}/hooks"""
    payload: Dict[str, Any] = {"name": name, "config": config}
    if events is not None:
        payload["events"] = events
    if active is not None:
        payload["active"] = active
    return client.request("POST", f"/repos/{owner}/{repo}/hooks", json=payload)


def update_repo_webhook(
    client: GitHubClient,
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
    """PATCH /repos/{owner}/{repo}/hooks/{hook_id}"""
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
    return client.request("PATCH", f"/repos/{owner}/{repo}/hooks/{hook_id}", json=payload)


def delete_repo_webhook(client: GitHubClient, *, owner: str, repo: str, hook_id: int) -> Dict[str, Any]:
    """DELETE /repos/{owner}/{repo}/hooks/{hook_id}"""
    return client.request("DELETE", f"/repos/{owner}/{repo}/hooks/{hook_id}")


def ping_repo_webhook(client: GitHubClient, *, owner: str, repo: str, hook_id: int) -> Dict[str, Any]:
    """POST /repos/{owner}/{repo}/hooks/{hook_id}/pings"""
    return client.request("POST", f"/repos/{owner}/{repo}/hooks/{hook_id}/pings")


def test_repo_webhook(client: GitHubClient, *, owner: str, repo: str, hook_id: int) -> Dict[str, Any]:
    """POST /repos/{owner}/{repo}/hooks/{hook_id}/tests"""
    return client.request("POST", f"/repos/{owner}/{repo}/hooks/{hook_id}/tests")
