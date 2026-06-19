"""GitHub Branches and Branch Protection tools."""

from typing import Any, Optional
from generated_tools.github_client import github_get, github_post, github_patch, github_put, github_delete


def list_branches(owner: str, repo: str, protected: Optional[bool] = None,
                  per_page: int = 30, page: int = 1) -> Any:
    """List branches for a repository.

    Args:
        owner: Repository owner
        repo: Repository name
        protected: Filter by protected status
        per_page: Results per page (max 100)
        page: Page number
    """
    params = {"per_page": per_page, "page": page}
    if protected is not None:
        params["protected"] = str(protected).lower()
    return github_get(f"/repos/{owner}/{repo}/branches", params)


def get_branch(owner: str, repo: str, branch: str) -> Any:
    """Get a branch.

    Args:
        owner: Repository owner
        repo: Repository name
        branch: Branch name
    """
    return github_get(f"/repos/{owner}/{repo}/branches/{branch}")


def rename_branch(owner: str, repo: str, branch: str, new_name: str) -> Any:
    """Rename a branch.

    Args:
        owner: Repository owner
        repo: Repository name
        branch: Current branch name
        new_name: New branch name
    """
    return github_post(f"/repos/{owner}/{repo}/branches/{branch}/rename", {"new_name": new_name})


def sync_fork_branch(owner: str, repo: str, branch: str) -> Any:
    """Sync a fork branch with the upstream repository.

    Args:
        owner: Repository owner
        repo: Repository name
        branch: Branch name to sync
    """
    return github_post(f"/repos/{owner}/{repo}/merge-upstream", {"branch": branch})


def merge_branch(owner: str, repo: str, base: str, head: str,
                 commit_message: Optional[str] = None) -> Any:
    """Merge a branch.

    Args:
        owner: Repository owner
        repo: Repository name
        base: Branch to merge into
        head: Branch to merge from (branch name or SHA)
        commit_message: Commit message for the merge
    """
    data = {"base": base, "head": head}
    if commit_message:
        data["commit_message"] = commit_message
    return github_post(f"/repos/{owner}/{repo}/merges", data)


def get_branch_protection(owner: str, repo: str, branch: str) -> Any:
    """Get branch protection rules.

    Args:
        owner: Repository owner
        repo: Repository name
        branch: Branch name
    """
    return github_get(f"/repos/{owner}/{repo}/branches/{branch}/protection")


def update_branch_protection(owner: str, repo: str, branch: str,
                             required_status_checks: Optional[dict] = None,
                             enforce_admins: bool = False,
                             required_pull_request_reviews: Optional[dict] = None,
                             restrictions: Optional[dict] = None,
                             required_linear_history: bool = False,
                             allow_force_pushes: bool = False,
                             allow_deletions: bool = False,
                             required_conversation_resolution: bool = False) -> Any:
    """Update branch protection rules.

    Args:
        owner: Repository owner
        repo: Repository name
        branch: Branch name
        required_status_checks: Status check config (dict with strict, contexts keys) or null
        enforce_admins: Enforce for admins
        required_pull_request_reviews: PR review config or null
        restrictions: Push restriction config (dict with users, teams, apps) or null
        required_linear_history: Require linear history
        allow_force_pushes: Allow force pushes
        allow_deletions: Allow deletions
        required_conversation_resolution: Require conversation resolution
    """
    data = {
        "enforce_admins": enforce_admins,
        "required_linear_history": required_linear_history,
        "allow_force_pushes": allow_force_pushes,
        "allow_deletions": allow_deletions,
        "required_conversation_resolution": required_conversation_resolution,
        "required_status_checks": required_status_checks,
        "required_pull_request_reviews": required_pull_request_reviews,
        "restrictions": restrictions,
    }
    return github_put(f"/repos/{owner}/{repo}/branches/{branch}/protection", data)


def delete_branch_protection(owner: str, repo: str, branch: str) -> Any:
    """Delete branch protection rules.

    Args:
        owner: Repository owner
        repo: Repository name
        branch: Branch name
    """
    return github_delete(f"/repos/{owner}/{repo}/branches/{branch}/protection")
