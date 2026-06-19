from typing import Any, Dict, List, Optional, Union

from .http_client import GitHubClient, parse_owner_repo


def get_branch_protection(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    branch: str,
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """GET /repos/{owner}/{repo}/branches/{branch}/protection"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    return client.request("GET", f"/repos/{o}/{r}/branches/{branch}/protection", accept=accept)


def update_branch_protection(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    branch: str,
    required_status_checks: Optional[Dict[str, Any]] = None,
    enforce_admins: Optional[Union[bool, None]] = None,
    required_pull_request_reviews: Optional[Dict[str, Any]] = None,
    restrictions: Optional[Dict[str, Any]] = None,
    required_linear_history: Optional[Union[bool, None]] = None,
    allow_force_pushes: Optional[Union[bool, None]] = None,
    allow_deletions: Optional[Union[bool, None]] = None,
    block_creations: Optional[Union[bool, None]] = None,
    required_conversation_resolution: Optional[Union[bool, None]] = None,
    lock_branch: Optional[Union[bool, None]] = None,
    allow_fork_syncing: Optional[Union[bool, None]] = None,
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """PUT /repos/{owner}/{repo}/branches/{branch}/protection"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
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
            payload[k] = {"enabled": v} if isinstance(v, bool) else v

    return client.request("PUT", f"/repos/{o}/{r}/branches/{branch}/protection", json=payload, accept=accept)


def delete_branch_protection(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    branch: str,
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """DELETE /repos/{owner}/{repo}/branches/{branch}/protection"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    return client.request("DELETE", f"/repos/{o}/{r}/branches/{branch}/protection", accept=accept)
