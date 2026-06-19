"""Label management tools."""

from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .http import github_request, split_repo


@mcp.tool
def labels_create(repo: str, name: str, color: str, description: Optional[str] = None) -> Dict[str, Any]:
    """Create a label."""
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}
    payload: Dict[str, Any] = {"name": name, "color": color}
    if description is not None:
        payload["description"] = description
    return github_request("POST", f"/repos/{r['owner']}/{r['repo']}/labels", json=payload)


@mcp.tool
def labels_update(repo: str, name: str, new_name: Optional[str] = None, color: Optional[str] = None, description: Optional[str] = None) -> Dict[str, Any]:
    """Update a label."""
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}
    payload: Dict[str, Any] = {}
    if new_name is not None:
        payload["new_name"] = new_name
    if color is not None:
        payload["color"] = color
    if description is not None:
        payload["description"] = description
    return github_request("PATCH", f"/repos/{r['owner']}/{r['repo']}/labels/{name}", json=payload)


@mcp.tool
def labels_delete(repo: str, name: str) -> Dict[str, Any]:
    """Delete a label."""
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}
    return github_request("DELETE", f"/repos/{r['owner']}/{r['repo']}/labels/{name}")
