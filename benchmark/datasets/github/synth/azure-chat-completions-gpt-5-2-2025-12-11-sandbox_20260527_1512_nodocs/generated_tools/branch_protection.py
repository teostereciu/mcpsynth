from typing import Any, Dict, Optional

from ._client import GitHubClient, split_repo


def get_branch_protection(repo: str, branch: str) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    return client.request("GET", f"/repos/{owner}/{name}/branches/{branch}/protection")


def update_branch_protection(repo: str, branch: str, required_status_checks: Optional[Dict[str, Any]] = None, enforce_admins: Optional[bool] = None, required_pull_request_reviews: Optional[Dict[str, Any]] = None, restrictions: Optional[Dict[str, Any]] = None, required_linear_history: Optional[bool] = None, allow_force_pushes: Optional[bool] = None, allow_deletions: Optional[bool] = None, block_creations: Optional[bool] = None, required_conversation_resolution: Optional[bool] = None, lock_branch: Optional[bool] = None, allow_fork_syncing: Optional[bool] = None) -> Any:
    """Update branch protection. GitHub requires specific preview/accept headers historically; we use vnd.github+json."""
    owner, name = split_repo(repo)
    client = GitHubClient()
    payload: Dict[str, Any] = {}
    if required_status_checks is not None:
        payload["required_status_checks"] = required_status_checks
    if enforce_admins is not None:
        payload["enforce_admins"] = enforce_admins
    if required_pull_request_reviews is not None:
        payload["required_pull_request_reviews"] = required_pull_request_reviews
    if restrictions is not None:
        payload["restrictions"] = restrictions
    if required_linear_history is not None:
        payload["required_linear_history"] = required_linear_history
    if allow_force_pushes is not None:
        payload["allow_force_pushes"] = allow_force_pushes
    if allow_deletions is not None:
        payload["allow_deletions"] = allow_deletions
    if block_creations is not None:
        payload["block_creations"] = block_creations
    if required_conversation_resolution is not None:
        payload["required_conversation_resolution"] = required_conversation_resolution
    if lock_branch is not None:
        payload["lock_branch"] = lock_branch
    if allow_fork_syncing is not None:
        payload["allow_fork_syncing"] = allow_fork_syncing
    return client.request("PUT", f"/repos/{owner}/{name}/branches/{branch}/protection", json=payload)


def delete_branch_protection(repo: str, branch: str) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    return client.request("DELETE", f"/repos/{owner}/{name}/branches/{branch}/protection", expected=(204,))
