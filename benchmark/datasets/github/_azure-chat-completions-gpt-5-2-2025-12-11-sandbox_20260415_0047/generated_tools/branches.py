from __future__ import annotations

from typing import Any, Dict, List

from . import mcp
from .http import GitHubClient, split_repo


@mcp.tool()
def branches_update_protection(
    repo: str,
    branch: str,
    required_approving_review_count: int,
    required_status_check_contexts: List[str],
    enforce_admins: bool,
    required_linear_history: bool,
) -> Dict[str, Any]:
    """Update branch protection with common settings used in CI workflows."""
    try:
        owner, r = split_repo(repo)
        client = GitHubClient.from_env()
        json_body: Dict[str, Any] = {
            "required_status_checks": {"strict": True, "contexts": required_status_check_contexts},
            "enforce_admins": enforce_admins,
            "required_pull_request_reviews": {
                "dismiss_stale_reviews": False,
                "require_code_owner_reviews": False,
                "required_approving_review_count": required_approving_review_count,
            },
            "restrictions": None,
            "required_linear_history": {"enabled": required_linear_history},
        }
        status, payload = client.request("PUT", f"/repos/{owner}/{r}/branches/{branch}/protection", json_body=json_body)
        return client.ok_or_error(status, payload)  # type: ignore[return-value]
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def branches_get_protection(repo: str, branch: str) -> Any:
    """Get branch protection."""
    try:
        owner, r = split_repo(repo)
        client = GitHubClient.from_env()
        status, payload = client.request("GET", f"/repos/{owner}/{r}/branches/{branch}/protection")
        return client.ok_or_error(status, payload)
    except Exception as e:
        return {"error": str(e)}
