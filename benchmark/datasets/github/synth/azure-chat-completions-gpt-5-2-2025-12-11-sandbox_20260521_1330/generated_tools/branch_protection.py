from typing import Any, Dict, Optional

from .github_client import GitHubClient


def get_branch_protection(client: GitHubClient, *, owner: str, repo: str, branch: str) -> Dict[str, Any]:
    """GET /repos/{owner}/{repo}/branches/{branch}/protection"""
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
) -> Dict[str, Any]:
    """PUT /repos/{owner}/{repo}/branches/{branch}/protection"""
    payload: Dict[str, Any] = {
        "required_status_checks": required_status_checks,
        "enforce_admins": enforce_admins,
        "required_pull_request_reviews": required_pull_request_reviews,
        "restrictions": restrictions,
    }
    # Optional newer fields
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

    return client.request("PUT", f"/repos/{owner}/{repo}/branches/{branch}/protection", json=payload)


def delete_branch_protection(client: GitHubClient, *, owner: str, repo: str, branch: str) -> Dict[str, Any]:
    """DELETE /repos/{owner}/{repo}/branches/{branch}/protection"""
    return client.request("DELETE", f"/repos/{owner}/{repo}/branches/{branch}/protection")
