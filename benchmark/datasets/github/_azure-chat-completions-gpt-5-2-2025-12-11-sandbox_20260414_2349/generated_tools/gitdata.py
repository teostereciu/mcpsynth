"""Git data tools (refs/tags) and commit comparison helpers."""

from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .http import github_request, split_repo


@mcp.tool
def git_get_ref(repo: str, ref: str) -> Dict[str, Any]:
    """Get a git reference.

    `ref` should be like `heads/main` or `tags/v1.0.0`.
    """
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}
    return github_request("GET", f"/repos/{r['owner']}/{r['repo']}/git/ref/{ref}")


@mcp.tool
def git_create_ref(repo: str, ref: str, sha: str) -> Dict[str, Any]:
    """Create a git reference.

    `ref` must be fully qualified, e.g. `refs/heads/new-branch` or `refs/tags/v1.0.0`.
    """
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}
    return github_request(
        "POST",
        f"/repos/{r['owner']}/{r['repo']}/git/refs",
        json={"ref": ref, "sha": sha},
    )


@mcp.tool
def git_update_ref(repo: str, ref: str, sha: str, force: bool = False) -> Dict[str, Any]:
    """Update a git reference.

    `ref` should be like `heads/main` or `tags/v1.0.0`.
    """
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}
    return github_request(
        "PATCH",
        f"/repos/{r['owner']}/{r['repo']}/git/refs/{ref}",
        json={"sha": sha, "force": force},
    )


@mcp.tool
def repos_compare_commits(repo: str, base: str, head: str) -> Dict[str, Any]:
    """Compare two commits/refs."""
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}
    return github_request("GET", f"/repos/{r['owner']}/{r['repo']}/compare/{base}...{head}")


@mcp.tool
def repos_get_branch(repo: str, branch: str) -> Dict[str, Any]:
    """Get a branch (includes latest commit SHA)."""
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}
    return github_request("GET", f"/repos/{r['owner']}/{r['repo']}/branches/{branch}")
