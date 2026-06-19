from typing import Any, Dict, Optional

from ._client import request_json, split_owner_repo


def get_branch_protection(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    branch: str,
    accept: Optional[str] = None,
) -> Any:
    """GET /repos/{owner}/{repo}/branches/{branch}/protection

    Get branch protection.
    """
    if owner is None or repo is None:
        parts = split_owner_repo(owner_repo)
        owner = owner or parts["owner"]
        repo = repo or parts["repo"]

    return request_json(
        "GET",
        f"/repos/{owner}/{repo}/branches/{branch}/protection",
        accept=accept,
    )


def update_branch_protection(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    branch: str,
    required_status_checks: Any,
    enforce_admins: Any,
    required_pull_request_reviews: Any,
    restrictions: Any,
    required_linear_history: Optional[Dict[str, Any]] = None,
    allow_force_pushes: Optional[Dict[str, Any]] = None,
    allow_deletions: Optional[Dict[str, Any]] = None,
    block_creations: Optional[bool] = None,
    required_conversation_resolution: Optional[Dict[str, Any]] = None,
    lock_branch: Optional[Dict[str, Any]] = None,
    allow_fork_syncing: Optional[Dict[str, Any]] = None,
    accept: Optional[str] = None,
) -> Any:
    """PUT /repos/{owner}/{repo}/branches/{branch}/protection

    Update branch protection.

    Note: This endpoint has a complex schema; pass objects matching GitHub's docs.
    """
    if owner is None or repo is None:
        parts = split_owner_repo(owner_repo)
        owner = owner or parts["owner"]
        repo = repo or parts["repo"]

    payload: Dict[str, Any] = {
        "required_status_checks": required_status_checks,
        "enforce_admins": enforce_admins,
        "required_pull_request_reviews": required_pull_request_reviews,
        "restrictions": restrictions,
    }
    for k, v in {
        "required_linear_history": required_linear_history,
        "allow_force_pushes": allow_force_pushes,
        "allow_deletions": allow_deletions,
        "block_creations": block_creations,
        "required_conversation_resolution": required_conversation_resolution,
        "lock_branch": lock_branch,
        "allow_fork_syncing": allow_fork_syncing,
    }.items():
        if v is not None:
            payload[k] = v

    return request_json(
        "PUT",
        f"/repos/{owner}/{repo}/branches/{branch}/protection",
        json=payload,
        accept=accept,
    )
