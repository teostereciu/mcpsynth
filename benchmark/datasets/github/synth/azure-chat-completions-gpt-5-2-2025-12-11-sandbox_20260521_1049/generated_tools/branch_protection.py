from typing import Any, Dict, Optional

from .http_client import request_json


def get_branch_protection(
    *,
    owner: str,
    repo: str,
    branch: str,
    accept: str = "application/vnd.github+json",
) -> Any:
    """GET /repos/{owner}/{repo}/branches/{branch}/protection - Get branch protection."""
    _, data, _ = request_json(
        "GET",
        f"/repos/{owner}/{repo}/branches/{branch}/protection",
        accept=accept,
    )
    return data


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
    block_creations: Optional[bool] = None,
    required_conversation_resolution: Optional[bool] = None,
    lock_branch: Optional[bool] = None,
    allow_fork_syncing: Optional[bool] = None,
    accept: str = "application/vnd.github+json",
) -> Any:
    """PUT /repos/{owner}/{repo}/branches/{branch}/protection - Update branch protection."""
    _, data, _ = request_json(
        "PUT",
        f"/repos/{owner}/{repo}/branches/{branch}/protection",
        json_body={
            "required_status_checks": required_status_checks,
            "enforce_admins": enforce_admins,
            "required_pull_request_reviews": required_pull_request_reviews,
            "restrictions": restrictions,
            "required_linear_history": {"enabled": required_linear_history}
            if required_linear_history is not None
            else None,
            "allow_force_pushes": {"enabled": allow_force_pushes} if allow_force_pushes is not None else None,
            "allow_deletions": {"enabled": allow_deletions} if allow_deletions is not None else None,
            "block_creations": {"enabled": block_creations} if block_creations is not None else None,
            "required_conversation_resolution": {"enabled": required_conversation_resolution}
            if required_conversation_resolution is not None
            else None,
            "lock_branch": {"enabled": lock_branch} if lock_branch is not None else None,
            "allow_fork_syncing": {"enabled": allow_fork_syncing} if allow_fork_syncing is not None else None,
        },
        accept=accept,
    )
    return data


def delete_branch_protection(
    *,
    owner: str,
    repo: str,
    branch: str,
    accept: str = "application/vnd.github+json",
) -> Any:
    """DELETE /repos/{owner}/{repo}/branches/{branch}/protection - Delete branch protection."""
    _, data, _ = request_json(
        "DELETE",
        f"/repos/{owner}/{repo}/branches/{branch}/protection",
        accept=accept,
    )
    return {"deleted": True} if data is None else data
