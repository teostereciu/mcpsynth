from __future__ import annotations

from typing import Any, Dict

from . import mcp
from .http import GitHubClient, split_repo


@mcp.tool()
def activity_star_repo(repo: str) -> Dict[str, Any]:
    """Star a repository for the authenticated user."""
    try:
        owner, r = split_repo(repo)
        client = GitHubClient.from_env()
        status, payload = client.request("PUT", f"/user/starred/{owner}/{r}", headers={"Content-Length": "0"})
        return client.ok_or_error(status, payload)  # type: ignore[return-value]
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def activity_check_starred(repo: str) -> Dict[str, Any]:
    """Check if a repository is starred by the authenticated user."""
    try:
        owner, r = split_repo(repo)
        client = GitHubClient.from_env()
        status, payload = client.request("GET", f"/user/starred/{owner}/{r}")
        if status == 204:
            return {"starred": True}
        if status == 404:
            return {"starred": False}
        return client.ok_or_error(status, payload)  # type: ignore[return-value]
    except Exception as e:
        return {"error": str(e)}
