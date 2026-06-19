from typing import Any, Dict, List, Optional, Union
from github_client import client

def get_branch_protection(owner: str, repo: str, branch: str) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Get branch protection.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - branch: The name of the branch.
    """
    return client.request("GET", f"/repos/{owner}/{repo}/branches/{branch}/protection")

def update_branch_protection(
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
    allow_fork_syncing: Optional[bool] = None
) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Update branch protection.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - branch: The name of the branch.
    - required_status_checks: Require status checks to pass before merging.
    - enforce_admins: Enforce all configured restrictions for administrators.
    - required_pull_request_reviews: Require pull request reviews before merging.
    - restrictions: Restrict who can push to the branch.
    - required_linear_history: Enforce a linear commit history.
    - allow_force_pushes: Permit force pushes for all users with push access.
    - allow_deletions: Allow users with push access to delete matching branches.
    - block_creations: If set to true, the restrictions of this protection rule will also apply to creations.
    - required_conversation_resolution: Requires all conversations on code to be resolved before a pull request can be merged.
    - lock_branch: Whether to set the branch as read-only.
    - allow_fork_syncing: Whether to allow fork syncing.
    """
    # Note: GitHub API requires certain fields to be present or structured in a specific way.
    # We construct the payload based on provided parameters.
    data = {}
    if required_status_checks is not None:
        data["required_status_checks"] = required_status_checks
    else:
        data["required_status_checks"] = None

    if enforce_admins is not None:
        data["enforce_admins"] = enforce_admins
    else:
        data["enforce_admins"] = None

    if required_pull_request_reviews is not None:
        data["required_pull_request_reviews"] = required_pull_request_reviews
    else:
        data["required_pull_request_reviews"] = None

    if restrictions is not None:
        data["restrictions"] = restrictions
    else:
        data["restrictions"] = None

    if required_linear_history is not None: data["required_linear_history"] = required_linear_history
    if allow_force_pushes is not None: data["allow_force_pushes"] = allow_force_pushes
    if allow_deletions is not None: data["allow_deletions"] = allow_deletions
    if block_creations is not None: data["block_creations"] = block_creations
    if required_conversation_resolution is not None: data["required_conversation_resolution"] = required_conversation_resolution
    if lock_branch is not None: data["lock_branch"] = lock_branch
    if allow_fork_syncing is not None: data["allow_fork_syncing"] = allow_fork_syncing

    return client.request("PUT", f"/repos/{owner}/{repo}/branches/{branch}/protection", json_data=data)

def delete_branch_protection(owner: str, repo: str, branch: str) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Delete branch protection.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - branch: The name of the branch.
    """
    return client.request("DELETE", f"/repos/{owner}/{repo}/branches/{branch}/protection")
