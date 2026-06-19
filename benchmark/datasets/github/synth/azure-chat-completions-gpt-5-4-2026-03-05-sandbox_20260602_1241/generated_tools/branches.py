from typing import Any

from generated_tools.github_common import compact, github_request


def get_branch_protection(owner: str, repo: str, branch: str) -> str:
    return compact(github_request("GET", f"/repos/{owner}/{repo}/branches/{branch}/protection"))


def update_branch_protection(owner: str, repo: str, branch: str, required_status_checks: dict[str, Any] | None, enforce_admins: bool | None, required_pull_request_reviews: dict[str, Any] | None, restrictions: dict[str, Any] | None, required_linear_history: bool | None = None, allow_force_pushes: bool | None = None, allow_deletions: bool | None = None, block_creations: bool | None = None, required_conversation_resolution: bool | None = None, lock_branch: bool | None = None, allow_fork_syncing: bool | None = None) -> str:
    return compact(github_request("PUT", f"/repos/{owner}/{repo}/branches/{branch}/protection", json_body={"required_status_checks": required_status_checks, "enforce_admins": enforce_admins, "required_pull_request_reviews": required_pull_request_reviews, "restrictions": restrictions, "required_linear_history": required_linear_history, "allow_force_pushes": allow_force_pushes, "allow_deletions": allow_deletions, "block_creations": block_creations, "required_conversation_resolution": required_conversation_resolution, "lock_branch": lock_branch, "allow_fork_syncing": allow_fork_syncing}))


def delete_branch_protection(owner: str, repo: str, branch: str) -> str:
    return compact(github_request("DELETE", f"/repos/{owner}/{repo}/branches/{branch}/protection"))
