"""Repository webhook tools."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from . import mcp
from .http import github_request, split_repo


@mcp.tool
def webhooks_list(repo: str, per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    """List repository webhooks."""
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}
    return github_request(
        "GET",
        f"/repos/{r['owner']}/{r['repo']}/hooks",
        params={"per_page": per_page, "page": page},
    )


@mcp.tool
def webhooks_create(
    repo: str,
    url: str,
    events: Optional[List[str]] = None,
    content_type: str = "json",
    active: bool = True,
    secret: Optional[str] = None,
    insecure_ssl: str = "0",
) -> Dict[str, Any]:
    """Create a repository webhook."""
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}

    config: Dict[str, Any] = {"url": url, "content_type": content_type, "insecure_ssl": insecure_ssl}
    if secret is not None:
        config["secret"] = secret

    payload: Dict[str, Any] = {"name": "web", "active": active, "config": config}
    if events is not None:
        payload["events"] = events

    return github_request("POST", f"/repos/{r['owner']}/{r['repo']}/hooks", json=payload)


@mcp.tool
def webhooks_ping(repo: str, hook_id: int) -> Dict[str, Any]:
    """Ping a repository webhook."""
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}
    return github_request("POST", f"/repos/{r['owner']}/{r['repo']}/hooks/{hook_id}/pings")


@mcp.tool
def webhooks_update(
    repo: str,
    hook_id: int,
    add_events: Optional[List[str]] = None,
    remove_events: Optional[List[str]] = None,
    events: Optional[List[str]] = None,
    active: Optional[bool] = None,
    config: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Update a repository webhook."""
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}

    payload: Dict[str, Any] = {}
    if add_events is not None:
        payload["add_events"] = add_events
    if remove_events is not None:
        payload["remove_events"] = remove_events
    if events is not None:
        payload["events"] = events
    if active is not None:
        payload["active"] = active
    if config is not None:
        payload["config"] = config

    return github_request("PATCH", f"/repos/{r['owner']}/{r['repo']}/hooks/{hook_id}", json=payload)


@mcp.tool
def webhooks_delete(repo: str, hook_id: int) -> Dict[str, Any]:
    """Delete a repository webhook."""
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}
    return github_request("DELETE", f"/repos/{r['owner']}/{r['repo']}/hooks/{hook_id}")
