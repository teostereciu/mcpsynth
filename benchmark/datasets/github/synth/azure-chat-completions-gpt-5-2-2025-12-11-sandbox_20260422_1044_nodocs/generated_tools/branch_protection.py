from typing import Any, Dict, Optional

from .github_client import GitHubClient, parse_owner_repo


def get_branch_protection(owner_repo: str, branch: str) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return GitHubClient().request("GET", f"/repos/{owner}/{repo}/branches/{branch}/protection")


def update_branch_protection(owner_repo: str, branch: str, protection: Dict[str, Any]) -> Dict[str, Any]:
    """Update branch protection.

    protection should match GitHub's Branch Protection schema.
    """
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    # GitHub requires a preview accept for some fields historically; v3 json accept works for most.
    return GitHubClient().request("PUT", f"/repos/{owner}/{repo}/branches/{branch}/protection", json=protection)


def delete_branch_protection(owner_repo: str, branch: str) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return GitHubClient().request("DELETE", f"/repos/{owner}/{repo}/branches/{branch}/protection")
