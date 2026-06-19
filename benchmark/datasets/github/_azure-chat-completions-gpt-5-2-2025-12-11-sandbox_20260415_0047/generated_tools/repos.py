from __future__ import annotations

from typing import Any, Dict, List, Optional

from . import mcp
from .http import GitHubClient, split_repo


@mcp.tool()
def repos_get(repo: str) -> Dict[str, Any]:
    """Get a repository."""
    try:
        owner, r = split_repo(repo)
        client = GitHubClient.from_env()
        status, payload = client.request("GET", f"/repos/{owner}/{r}")
        return client.ok_or_error(status, payload)  # type: ignore[return-value]
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def repos_update(
    repo: str,
    description: Optional[str] = None,
    homepage: Optional[str] = None,
    private: Optional[bool] = None,
) -> Dict[str, Any]:
    """Update repository settings."""
    try:
        owner, r = split_repo(repo)
        client = GitHubClient.from_env()
        json_body = {k: v for k, v in {"description": description, "homepage": homepage, "private": private}.items() if v is not None}
        status, payload = client.request("PATCH", f"/repos/{owner}/{r}", json_body=json_body)
        return client.ok_or_error(status, payload)  # type: ignore[return-value]
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def repos_replace_topics(repo: str, topics: List[str]) -> Dict[str, Any]:
    """Replace repository topics."""
    try:
        owner, r = split_repo(repo)
        client = GitHubClient.from_env()
        status, payload = client.request(
            "PUT",
            f"/repos/{owner}/{r}/topics",
            json_body={"names": topics},
            headers={"Accept": "application/vnd.github+json"},
        )
        return client.ok_or_error(status, payload)  # type: ignore[return-value]
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def repos_compare_commits(repo: str, base: str, head: str) -> Any:
    """Compare two commits."""
    try:
        owner, r = split_repo(repo)
        client = GitHubClient.from_env()
        status, payload = client.request("GET", f"/repos/{owner}/{r}/compare/{base}...{head}")
        return client.ok_or_error(status, payload)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def repos_fork(repo: str, organization: Optional[str] = None, name: Optional[str] = None, default_branch_only: Optional[bool] = None) -> Dict[str, Any]:
    """Fork a repository."""
    try:
        owner, r = split_repo(repo)
        client = GitHubClient.from_env()
        json_body = {k: v for k, v in {"organization": organization, "name": name, "default_branch_only": default_branch_only}.items() if v is not None}
        status, payload = client.request("POST", f"/repos/{owner}/{r}/forks", json_body=json_body)
        return client.ok_or_error(status, payload)  # type: ignore[return-value]
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def repos_create_webhook(
    repo: str,
    url: str,
    events: List[str],
    content_type: str = "json",
    secret: Optional[str] = None,
    insecure_ssl: str = "0",
    active: bool = True,
) -> Dict[str, Any]:
    """Create a repository webhook."""
    try:
        owner, r = split_repo(repo)
        client = GitHubClient.from_env()
        config: Dict[str, Any] = {"url": url, "content_type": content_type, "insecure_ssl": insecure_ssl}
        if secret is not None:
            config["secret"] = secret
        status, payload = client.request(
            "POST",
            f"/repos/{owner}/{r}/hooks",
            json_body={"name": "web", "active": active, "events": events, "config": config},
        )
        return client.ok_or_error(status, payload)  # type: ignore[return-value]
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def repos_list_webhooks(repo: str, per_page: int = 30, page: int = 1) -> Any:
    """List repository webhooks."""
    try:
        owner, r = split_repo(repo)
        client = GitHubClient.from_env()
        status, payload = client.request("GET", f"/repos/{owner}/{r}/hooks", params={"per_page": per_page, "page": page})
        return client.ok_or_error(status, payload)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def repos_ping_webhook(repo: str, hook_id: int) -> Dict[str, Any]:
    """Ping a repository webhook."""
    try:
        owner, r = split_repo(repo)
        client = GitHubClient.from_env()
        status, payload = client.request("POST", f"/repos/{owner}/{r}/hooks/{hook_id}/pings")
        return client.ok_or_error(status, payload)  # type: ignore[return-value]
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def repos_update_webhook(repo: str, hook_id: int, events: Optional[List[str]] = None, active: Optional[bool] = None, config: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Update a repository webhook."""
    try:
        owner, r = split_repo(repo)
        client = GitHubClient.from_env()
        json_body: Dict[str, Any] = {}
        if events is not None:
            json_body["events"] = events
        if active is not None:
            json_body["active"] = active
        if config is not None:
            json_body["config"] = config
        status, payload = client.request("PATCH", f"/repos/{owner}/{r}/hooks/{hook_id}", json_body=json_body)
        return client.ok_or_error(status, payload)  # type: ignore[return-value]
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def repos_delete_webhook(repo: str, hook_id: int) -> Dict[str, Any]:
    """Delete a repository webhook."""
    try:
        owner, r = split_repo(repo)
        client = GitHubClient.from_env()
        status, payload = client.request("DELETE", f"/repos/{owner}/{r}/hooks/{hook_id}")
        return client.ok_or_error(status, payload)  # type: ignore[return-value]
    except Exception as e:
        return {"error": str(e)}
