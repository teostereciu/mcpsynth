"""Repository tools (get/update repo, topics, forks, branch protection, contents)."""

from __future__ import annotations

import base64
from typing import Any, Dict, List, Optional

from . import mcp
from .http import github_request, split_repo


@mcp.tool
def repos_get(repo: str) -> Dict[str, Any]:
    """Get a repository."""
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}
    return github_request("GET", f"/repos/{r['owner']}/{r['repo']}")


@mcp.tool
def repos_update(
    repo: str,
    description: Optional[str] = None,
    homepage: Optional[str] = None,
) -> Dict[str, Any]:
    """Update repository settings (description/homepage)."""
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}
    payload: Dict[str, Any] = {}
    if description is not None:
        payload["description"] = description
    if homepage is not None:
        payload["homepage"] = homepage
    return github_request("PATCH", f"/repos/{r['owner']}/{r['repo']}", json=payload)


@mcp.tool
def repos_replace_topics(repo: str, topics: List[str]) -> Dict[str, Any]:
    """Replace all repository topics."""
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}
    # Topics API requires a custom Accept header.
    return github_request(
        "PUT",
        f"/repos/{r['owner']}/{r['repo']}/topics",
        json={"names": topics},
        headers={"Accept": "application/vnd.github+json"},
    )


@mcp.tool
def repos_fork(repo: str, organization: Optional[str] = None, name: Optional[str] = None) -> Dict[str, Any]:
    """Fork a repository."""
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}
    payload: Dict[str, Any] = {}
    if organization is not None:
        payload["organization"] = organization
    if name is not None:
        payload["name"] = name
    return github_request("POST", f"/repos/{r['owner']}/{r['repo']}/forks", json=payload or None)


@mcp.tool
def branches_update_protection(
    repo: str,
    branch: str,
    required_approving_review_count: int,
    status_checks: List[str],
    enforce_admins: bool,
    required_linear_history: bool,
) -> Dict[str, Any]:
    """Configure branch protection for a branch.

    This uses the Branch Protection API.
    """
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}

    payload: Dict[str, Any] = {
        "required_status_checks": {"strict": True, "contexts": status_checks},
        "enforce_admins": enforce_admins,
        "required_pull_request_reviews": {
            "dismiss_stale_reviews": False,
            "require_code_owner_reviews": False,
            "required_approving_review_count": required_approving_review_count,
        },
        "restrictions": None,
        "required_linear_history": {"enabled": required_linear_history},
        "allow_force_pushes": {"enabled": False},
        "allow_deletions": {"enabled": False},
        "block_creations": {"enabled": False},
        "required_conversation_resolution": {"enabled": False},
        "lock_branch": {"enabled": False},
        "allow_fork_syncing": {"enabled": True},
    }

    return github_request(
        "PUT",
        f"/repos/{r['owner']}/{r['repo']}/branches/{branch}/protection",
        json=payload,
    )


@mcp.tool
def repos_get_content(repo: str, path: str, ref: Optional[str] = None) -> Dict[str, Any]:
    """Get repository content for a file or directory."""
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}
    params: Dict[str, Any] = {}
    if ref is not None:
        params["ref"] = ref
    return github_request("GET", f"/repos/{r['owner']}/{r['repo']}/contents/{path.lstrip('/')}" , params=params or None)


@mcp.tool
def repos_put_file(
    repo: str,
    path: str,
    message: str,
    content: str,
    branch: Optional[str] = None,
    sha: Optional[str] = None,
) -> Dict[str, Any]:
    """Create or update a file in a repository.

    `content` is raw text; it will be base64-encoded.
    """
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}

    payload: Dict[str, Any] = {
        "message": message,
        "content": base64.b64encode(content.encode("utf-8")).decode("ascii"),
    }
    if branch is not None:
        payload["branch"] = branch
    if sha is not None:
        payload["sha"] = sha

    return github_request(
        "PUT",
        f"/repos/{r['owner']}/{r['repo']}/contents/{path.lstrip('/')}" ,
        json=payload,
    )
