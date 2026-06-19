from typing import Any, List, Optional

from generated_tools.github_common import clean_params, github_request


def get_branch_protection(owner: str, repo: str, branch: str) -> Any:
    return github_request("GET", f"/repos/{owner}/{repo}/branches/{branch}/protection")


def update_branch_protection(owner: str, repo: str, branch: str, required_status_checks: Optional[dict] = None, enforce_admins: Optional[bool] = None, required_pull_request_reviews: Optional[dict] = None, restrictions: Optional[dict] = None, required_linear_history: Optional[bool] = None, allow_force_pushes: Optional[bool] = None, allow_deletions: Optional[bool] = None, block_creations: Optional[bool] = None, required_conversation_resolution: Optional[bool] = None, lock_branch: Optional[bool] = None, allow_fork_syncing: Optional[bool] = None) -> Any:
    payload = clean_params(required_status_checks=required_status_checks, enforce_admins=enforce_admins, required_pull_request_reviews=required_pull_request_reviews, restrictions=restrictions, required_linear_history=required_linear_history, allow_force_pushes=allow_force_pushes, allow_deletions=allow_deletions, block_creations=block_creations, required_conversation_resolution=required_conversation_resolution, lock_branch=lock_branch, allow_fork_syncing=allow_fork_syncing)
    return github_request("PUT", f"/repos/{owner}/{repo}/branches/{branch}/protection", json_body=payload)


def delete_branch_protection(owner: str, repo: str, branch: str) -> Any:
    return github_request("DELETE", f"/repos/{owner}/{repo}/branches/{branch}/protection")
