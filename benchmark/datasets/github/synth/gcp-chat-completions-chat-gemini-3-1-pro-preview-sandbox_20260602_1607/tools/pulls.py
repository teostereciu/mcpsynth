from mcp_server import mcp
from github_client import make_request

@mcp.tool()
def list_pull_requests(owner: str, repo: str, state: str = "open", per_page: int = 30, page: int = 1) -> dict:
    """List pull requests in a repository."""
    return make_request("GET", f"/repos/{owner}/{repo}/pulls", params={"state": state, "per_page": per_page, "page": page})

@mcp.tool()
def create_pull_request(owner: str, repo: str, title: str, head: str, base: str, body: str = None, draft: bool = False) -> dict:
    """Create a pull request in a repository."""
    payload = {"title": title, "head": head, "base": base, "draft": draft}
    if body: payload["body"] = body
    return make_request("POST", f"/repos/{owner}/{repo}/pulls", json=payload)

@mcp.tool()
def get_pull_request(owner: str, repo: str, pull_number: int) -> dict:
    """Get a pull request in a repository."""
    return make_request("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}")

@mcp.tool()
def merge_pull_request(owner: str, repo: str, pull_number: int, commit_title: str = None, commit_message: str = None, merge_method: str = "merge") -> dict:
    """Merge a pull request."""
    payload = {"merge_method": merge_method}
    if commit_title: payload["commit_title"] = commit_title
    if commit_message: payload["commit_message"] = commit_message
    return make_request("PUT", f"/repos/{owner}/{repo}/pulls/{pull_number}/merge", json=payload)

@mcp.tool()
def create_pull_request_review(owner: str, repo: str, pull_number: int, event: str, body: str = None) -> dict:
    """Create a review for a pull request. Event can be APPROVE, REQUEST_CHANGES, or COMMENT."""
    payload = {"event": event}
    if body: payload["body"] = body
    return make_request("POST", f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews", json=payload)

@mcp.tool()
def request_reviewers(owner: str, repo: str, pull_number: int, reviewers: list[str]) -> dict:
    """Request reviewers for a pull request."""
    return make_request("POST", f"/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers", json={"reviewers": reviewers})
