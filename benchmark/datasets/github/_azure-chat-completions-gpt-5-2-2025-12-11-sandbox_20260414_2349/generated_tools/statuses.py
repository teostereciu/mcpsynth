"""Commit status tools."""

from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .http import github_request, split_repo


@mcp.tool
def commits_create_status(
    repo: str,
    sha: str,
    state: str,
    context: str,
    description: Optional[str] = None,
    target_url: Optional[str] = None,
) -> Dict[str, Any]:
    """Create a commit status."""
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}

    payload: Dict[str, Any] = {"state": state, "context": context}
    if description is not None:
        payload["description"] = description
    if target_url is not None:
        payload["target_url"] = target_url

    return github_request(
        "POST",
        f"/repos/{r['owner']}/{r['repo']}/statuses/{sha}",
        json=payload,
    )
