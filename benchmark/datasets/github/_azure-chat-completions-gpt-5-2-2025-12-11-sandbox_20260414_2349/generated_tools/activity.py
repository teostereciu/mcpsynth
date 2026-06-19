"""User activity tools (starring)."""

from __future__ import annotations

from typing import Any, Dict

from . import mcp
from .http import github_request, split_repo


@mcp.tool
def activity_star_repo(repo: str) -> Dict[str, Any]:
    """Star a repository for the authenticated user."""
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}
    # GitHub expects empty body.
    return github_request("PUT", f"/user/starred/{r['owner']}/{r['repo']}")


@mcp.tool
def activity_unstar_repo(repo: str) -> Dict[str, Any]:
    """Unstar a repository for the authenticated user."""
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}
    return github_request("DELETE", f"/user/starred/{r['owner']}/{r['repo']}")
