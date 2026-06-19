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
    required_linear_history: Optional[Dict[str, Any]] = None,
    allow_force_pushes: Optional[Dict[str, Any]] = None,
    allow_deletions: Optional[Dict[str, Any]] = None,
    block_creations: Optional[Dict[str, Any]] = None,
    required_conversation_resolution: Optional[Dict[str, Any]] = None,
    lock_branch: Optional[Dict[str, Any]] = None,
    allow_fork_syncing: Optional[Dict[str, Any]] = None,
) -> Any:
    # GitHub expects many of these keys to be present; callers can pass explicit None to disable.
    payload: Dict[str, Any] = {
        "required_status_checks": required_status_checks,
        "enforce_admins": enforce_admins,
        "required_pull_request_reviews": required_pull_request_reviews,
        "restrictions": restrictions,
        "required_linear_history": required_linear_history,
        "allow_force_pushes": allow_force_pushes,
        "allow_deletions": allow_deletions,
        "block_creations": block_creations,
        "required_conversation_resolution": required_conversation_resolution,
        "lock_branch": lock_branch,
        "allow_fork_syncing": allow_fork_syncing,
    }
    return client.request("PUT", f"/repos/{owner}/{repo}/branches/{branch}/protection", json=payload)


def delete_branch_protection(client: GitHubClient, *, owner: str, repo: str, branch: str) -> Any:
    return client.request("DELETE", f"/repos/{owner}/{repo}/branches/{branch}/protection")
