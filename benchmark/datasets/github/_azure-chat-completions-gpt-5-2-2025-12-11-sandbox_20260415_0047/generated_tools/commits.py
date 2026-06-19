from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .http import GitHubClient, split_repo


@mcp.tool()
def commits_create_status(
    repo: str,
    sha: str,
    state: str,
    context: str,
    description: Optional[str] = None,
    target_url: Optional[str] = None,
) -> Dict[str, Any]:
    """Create a commit status for a SHA."""
    try:
        owner, r = split_repo(repo)
        client = GitHubClient.from_env()
        json_body: Dict[str, Any] = {"state": state, "context": context}
        if description is not None:
            json_body["description"] = description
        if target_url is not None:
            json_body["target_url"] = target_url
        status, payload = client.request("POST", f"/repos/{owner}/{r}/statuses/{sha}", json_body=json_body)
        return client.ok_or_error(status, payload)  # type: ignore[return-value]
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def commits_get_combined_status(repo: str, ref: str) -> Any:
    """Get combined status for a ref (sha/branch/tag)."""
    try:
        owner, r = split_repo(repo)
        client = GitHubClient.from_env()
        status, payload = client.request("GET", f"/repos/{owner}/{r}/commits/{ref}/status")
        return client.ok_or_error(status, payload)
    except Exception as e:
        return {"error": str(e)}
