from typing import Any, Dict, List, Optional
from .client import make_request

def get_branch_protection(owner: str, repo: str, branch: str) -> Any:
    """Get branch protection."""
    return make_request("GET", f"/repos/{owner}/{repo}/branches/{branch}/protection")

def update_branch_protection(owner: str, repo: str, branch: str, required_status_checks: Optional[Dict[str, Any]] = None, enforce_admins: bool = True, required_pull_request_reviews: Optional[Dict[str, Any]] = None, restrictions: Optional[Dict[str, Any]] = None) -> Any:
    """Update branch protection."""
    data = {
        "required_status_checks": required_status_checks,
        "enforce_admins": enforce_admins,
        "required_pull_request_reviews": required_pull_request_reviews,
        "restrictions": restrictions
    }
    return make_request("PUT", f"/repos/{owner}/{repo}/branches/{branch}/protection", json=data)
