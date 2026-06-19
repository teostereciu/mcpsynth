from typing import Any, Dict, Optional

from ._client import GitHubClient


def get_branch_protection(*, owner: str, repo: str, branch: str) -> Dict[str, Any]:
    """GET /repos/{owner}/{repo}/branches/{branch}/protection - Get branch protection."""
    c = GitHubClient()
    return c.request("GET", f"/repos/{owner}/{repo}/branches/{branch}/protection")


def update_branch_protection(
    *,
    owner: str,
    repo: str,
    branch: str,
    required_status_checks: Optional[Dict[str, Any]] = None,
    enforce_admins: Optional[bool] = None,
    required_pull_request_reviews: Optional[Dict[str, Any]] = None,
    restrictions: Optional[Dict[str, Any]] = None,
    required_linear_history: Optional[bool] = None,
    allow_force_pushes: Optional[bool] = None,
    allow_deletions: Optional[bool] = None,
    required_conversation_resolution: Optional[bool] = None,
    lock_branch: Optional[bool] = None,
    allow_fork_syncing: Optional[bool] = None,
) -> Dict[str, Any]:
    """PUT /repos/{owner}/{repo}/branches/{branch}/protection - Update branch protection.

    This endpoint expects a fairly complex JSON body. Pass sub-objects as dicts.
    """
    c = GitHubClient()
    payload: Dict[str, Any] = {}
    for k, v in {
        "required_status_checks": required_status_checks,
        "enforce_admins": enforce_admins,
        "required_pull_request_reviews": required_pull_request_reviews,
        "restrictions": restrictions,
        "required_linear_history": required_linear_history,
        "allow_force_pushes": allow_force_pushes,
        "allow_deletions": allow_deletions,
        "required_conversation_resolution": required_conversation_resolution,
        "lock_branch": lock_branch,
        "allow_fork_syncing": allow_fork_syncing,
    }.items():
        if v is not None:
            payload[k] = v
    return c.request("PUT", f"/repos/{owner}/{repo}/branches/{branch}/protection", json=payload)
