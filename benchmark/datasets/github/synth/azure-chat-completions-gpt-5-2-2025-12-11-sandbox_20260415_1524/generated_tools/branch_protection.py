from __future__ import annotations

from typing import Any, Dict, Optional

from .github_client import GitHubClient


def get_branch_protection(client: GitHubClient, *, owner: str, repo: str, branch: str) -> Any:
    return client.request("GET", f"/repos/{owner}/{repo}/branches/{branch}/protection")


def update_branch_protection(
    client: GitHubClient,
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
) -> Any:
    payload: Dict[str, Any] = {
        "required_status_checks": required_status_checks,
        "enforce_admins": enforce_admins,
        "required_pull_request_reviews": required_pull_request_reviews,
        "restrictions": restrictions,
        "required_linear_history": {"enabled": required_linear_history} if required_linear_history is not None else None,
        "allow_force_pushes": {"enabled": allow_force_pushes} if allow_force_pushes is not None else None,
        "allow_deletions": {"enabled": allow_deletions} if allow_deletions is not None else None,
        "block_creations": {"enabled": block_creations} if block_creations is not None else None,
        "required_conversation_resolution": {"enabled": required_conversation_resolution} if required_conversation_resolution is not None else None,
        "lock_branch": {"enabled": lock_branch} if lock_branch is not None else None,
        "allow_fork_syncing": {"enabled": allow_fork_syncing} if allow_fork_syncing is not None else None,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    return client.request("PUT", f"/repos/{owner}/{repo}/branches/{branch}/protection", json=payload)


def delete_branch_protection(client: GitHubClient, *, owner: str, repo: str, branch: str) -> Any:
    return client.request("DELETE", f"/repos/{owner}/{repo}/branches/{branch}/protection")
