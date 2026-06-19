from mcp_server import mcp
from github_client import make_request

@mcp.tool()
def get_branch_protection(owner: str, repo: str, branch: str) -> dict:
    """Get branch protection."""
    return make_request("GET", f"/repos/{owner}/{repo}/branches/{branch}/protection")

@mcp.tool()
def update_branch_protection(owner: str, repo: str, branch: str, required_status_checks: dict = None, enforce_admins: bool = None, required_pull_request_reviews: dict = None, restrictions: dict = None) -> dict:
    """Update branch protection."""
    payload = {
        "required_status_checks": required_status_checks,
        "enforce_admins": enforce_admins,
        "required_pull_request_reviews": required_pull_request_reviews,
        "restrictions": restrictions
    }
    return make_request("PUT", f"/repos/{owner}/{repo}/branches/{branch}/protection", json=payload)
