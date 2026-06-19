"""GitHub Branches and Branch Protection tools."""
import os
import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com")
TOKEN = os.environ.get("GITHUB_TOKEN", "")

HEADERS = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}
if TOKEN:
    HEADERS["Authorization"] = f"Bearer {TOKEN}"


def _get(path, params=None):
    try:
        r = requests.get(f"{BASE_URL}{path}", headers=HEADERS, params=params, timeout=30)
        if r.status_code == 204:
            return {"status": "no_content"}
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def _post(path, json=None):
    try:
        r = requests.post(f"{BASE_URL}{path}", headers=HEADERS, json=json, timeout=30)
        if r.status_code == 204:
            return {"status": "no_content"}
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def _put(path, json=None):
    try:
        r = requests.put(f"{BASE_URL}{path}", headers=HEADERS, json=json, timeout=30)
        if r.status_code == 204:
            return {"status": "no_content"}
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def _delete(path, json=None):
    try:
        r = requests.delete(f"{BASE_URL}{path}", headers=HEADERS, json=json, timeout=30)
        if r.status_code == 204:
            return {"status": "no_content"}
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def register_branches_tools(mcp: FastMCP):

    @mcp.tool()
    def list_branches(owner: str, repo: str, protected: bool = None,
                      per_page: int = 30, page: int = 1) -> dict:
        """List branches for a repository."""
        params = {"per_page": per_page, "page": page}
        if protected is not None:
            params["protected"] = protected
        return _get(f"/repos/{owner}/{repo}/branches", params)

    @mcp.tool()
    def get_branch(owner: str, repo: str, branch: str) -> dict:
        """Get a specific branch."""
        return _get(f"/repos/{owner}/{repo}/branches/{branch}")

    @mcp.tool()
    def rename_branch(owner: str, repo: str, branch: str, new_name: str) -> dict:
        """Rename a branch in a repository."""
        return _post(f"/repos/{owner}/{repo}/branches/{branch}/rename", {"new_name": new_name})

    @mcp.tool()
    def sync_fork_branch(owner: str, repo: str, branch: str) -> dict:
        """Sync a fork branch with the upstream repository."""
        return _post(f"/repos/{owner}/{repo}/merge-upstream", {"branch": branch})

    @mcp.tool()
    def merge_branch(owner: str, repo: str, base: str, head: str,
                     commit_message: str = None) -> dict:
        """Merge a branch into another branch."""
        payload = {"base": base, "head": head}
        if commit_message:
            payload["commit_message"] = commit_message
        return _post(f"/repos/{owner}/{repo}/merges", payload)

    # --- Git Refs (create branches) ---

    @mcp.tool()
    def list_git_refs(owner: str, repo: str, ref: str = None) -> dict:
        """List git references (branches, tags) for a repository."""
        path = f"/repos/{owner}/{repo}/git/refs"
        if ref:
            path += f"/{ref}"
        return _get(path)

    @mcp.tool()
    def create_git_ref(owner: str, repo: str, ref: str, sha: str) -> dict:
        """Create a git reference (e.g., a new branch). ref must be fully qualified like refs/heads/branch-name."""
        return _post(f"/repos/{owner}/{repo}/git/refs", {"ref": ref, "sha": sha})

    @mcp.tool()
    def update_git_ref(owner: str, repo: str, ref: str, sha: str, force: bool = False) -> dict:
        """Update a git reference to point to a new SHA."""
        try:
            r = requests.patch(f"{BASE_URL}/repos/{owner}/{repo}/git/refs/{ref}",
                               headers=HEADERS, json={"sha": sha, "force": force}, timeout=30)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def delete_git_ref(owner: str, repo: str, ref: str) -> dict:
        """Delete a git reference (e.g., delete a branch via refs/heads/branch-name)."""
        return _delete(f"/repos/{owner}/{repo}/git/refs/{ref}")

    # --- Branch Protection ---

    @mcp.tool()
    def get_branch_protection(owner: str, repo: str, branch: str) -> dict:
        """Get branch protection settings for a branch."""
        return _get(f"/repos/{owner}/{repo}/branches/{branch}/protection")

    @mcp.tool()
    def update_branch_protection(owner: str, repo: str, branch: str,
                                 required_status_checks: dict = None,
                                 enforce_admins: bool = None,
                                 required_pull_request_reviews: dict = None,
                                 restrictions: dict = None,
                                 required_linear_history: bool = False,
                                 allow_force_pushes: bool = False,
                                 allow_deletions: bool = False,
                                 required_conversation_resolution: bool = False) -> dict:
        """Update branch protection rules for a branch."""
        payload = {
            "required_status_checks": required_status_checks,
            "enforce_admins": enforce_admins,
            "required_pull_request_reviews": required_pull_request_reviews,
            "restrictions": restrictions,
            "required_linear_history": required_linear_history,
            "allow_force_pushes": allow_force_pushes,
            "allow_deletions": allow_deletions,
            "required_conversation_resolution": required_conversation_resolution,
        }
        return _put(f"/repos/{owner}/{repo}/branches/{branch}/protection", payload)

    @mcp.tool()
    def delete_branch_protection(owner: str, repo: str, branch: str) -> dict:
        """Delete branch protection rules for a branch."""
        return _delete(f"/repos/{owner}/{repo}/branches/{branch}/protection")
