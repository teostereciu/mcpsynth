from mcp_server import mcp
from github_client import make_request

@mcp.tool()
def list_issues(owner: str, repo: str, state: str = "open", per_page: int = 30, page: int = 1) -> dict:
    """List issues in a repository."""
    return make_request("GET", f"/repos/{owner}/{repo}/issues", params={"state": state, "per_page": per_page, "page": page})

@mcp.tool()
def create_issue(owner: str, repo: str, title: str, body: str = None, assignees: list[str] = None, labels: list[str] = None) -> dict:
    """Create an issue in a repository."""
    payload = {"title": title}
    if body: payload["body"] = body
    if assignees: payload["assignees"] = assignees
    if labels: payload["labels"] = labels
    return make_request("POST", f"/repos/{owner}/{repo}/issues", json=payload)

@mcp.tool()
def get_issue(owner: str, repo: str, issue_number: int) -> dict:
    """Get an issue in a repository."""
    return make_request("GET", f"/repos/{owner}/{repo}/issues/{issue_number}")

@mcp.tool()
def update_issue(owner: str, repo: str, issue_number: int, title: str = None, body: str = None, state: str = None) -> dict:
    """Update an issue in a repository."""
    payload = {}
    if title: payload["title"] = title
    if body: payload["body"] = body
    if state: payload["state"] = state
    return make_request("PATCH", f"/repos/{owner}/{repo}/issues/{issue_number}", json=payload)

@mcp.tool()
def add_issue_labels(owner: str, repo: str, issue_number: int, labels: list[str]) -> dict:
    """Add labels to an issue."""
    return make_request("POST", f"/repos/{owner}/{repo}/issues/{issue_number}/labels", json={"labels": labels})

@mcp.tool()
def add_issue_assignees(owner: str, repo: str, issue_number: int, assignees: list[str]) -> dict:
    """Add assignees to an issue."""
    return make_request("POST", f"/repos/{owner}/{repo}/issues/{issue_number}/assignees", json={"assignees": assignees})

@mcp.tool()
def list_issue_comments(owner: str, repo: str, issue_number: int) -> dict:
    """List comments on an issue."""
    return make_request("GET", f"/repos/{owner}/{repo}/issues/{issue_number}/comments")

@mcp.tool()
def create_issue_comment(owner: str, repo: str, issue_number: int, body: str) -> dict:
    """Create a comment on an issue."""
    return make_request("POST", f"/repos/{owner}/{repo}/issues/{issue_number}/comments", json={"body": body})
