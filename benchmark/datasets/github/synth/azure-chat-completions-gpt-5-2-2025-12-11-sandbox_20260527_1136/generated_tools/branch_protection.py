from typing import Any, Dict, Optional

from .http_client import request_json, parse_owner_repo


# docs/api_branches-branch-protection.md

def get_branch_protection(
    *,
    branch: str,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    accept: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo is required (or set GITHUB_TEST_REPO)"}
    return request_json(
        "GET",
        f"/repos/{o}/{r}/branches/{branch}/protection",
        accept=accept,
    )


# docs/api_branches-branch-protection.md

def update_branch_protection(
    *,
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
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    accept: Optional[str] = None,
) -> Any:
    """Update branch protection.

    The GitHub API requires several top-level keys; pass them as dicts or None.
    """
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo is required (or set GITHUB_TEST_REPO)"}

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
        f"/repos/{o}/{r}/branches/{branch}/protection",
        accept=accept,
        json=payload,
    )


# docs/api_branches-branch-protection.md

def delete_branch_protection(
    *,
    branch: str,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    accept: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo is required (or set GITHUB_TEST_REPO)"}
    return request_json(
        "DELETE",
        f"/repos/{o}/{r}/branches/{branch}/protection",
        accept=accept,
    )
