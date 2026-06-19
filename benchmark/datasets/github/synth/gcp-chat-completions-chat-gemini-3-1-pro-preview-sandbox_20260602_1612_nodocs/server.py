import os
import requests
import base64
from typing import Optional, List, Dict, Any
from fastmcp import FastMCP

mcp = FastMCP("github-mcp-server")

def get_base_url() -> str:
    return os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com").rstrip("/")

def get_headers() -> dict:
    token = os.environ.get("GITHUB_TOKEN")
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers

def make_request(method: str, path: str, **kwargs) -> Any:
    url = f"{get_base_url()}{path}"
    headers = get_headers()
    if "headers" in kwargs:
        headers.update(kwargs.pop("headers"))
    
    try:
        response = requests.request(method, url, headers=headers, **kwargs)
        response.raise_for_status()
        if response.status_code == 204:
            return {"status": "success"}
        return response.json()
    except requests.exceptions.RequestException as e:
        if hasattr(e, "response") and e.response is not None:
            try:
                return {"error": e.response.json()}
            except ValueError:
                return {"error": e.response.text}
        return {"error": str(e)}

# --- Issues ---

@mcp.tool()
def get_issue(owner: str, repo: str, issue_number: int) -> Any:
    """Get an issue."""
    return make_request("GET", f"/repos/{owner}/{repo}/issues/{issue_number}")

@mcp.tool()
def list_issues(owner: str, repo: str, state: str = "open") -> Any:
    """List issues for a repository."""
    return make_request("GET", f"/repos/{owner}/{repo}/issues", params={"state": state})

@mcp.tool()
def create_issue(owner: str, repo: str, title: str, body: Optional[str] = None, assignees: Optional[List[str]] = None, labels: Optional[List[str]] = None) -> Any:
    """Create an issue."""
    data = {"title": title}
    if body is not None: data["body"] = body
    if assignees is not None: data["assignees"] = assignees
    if labels is not None: data["labels"] = labels
    return make_request("POST", f"/repos/{owner}/{repo}/issues", json=data)

@mcp.tool()
def update_issue(owner: str, repo: str, issue_number: int, title: Optional[str] = None, body: Optional[str] = None, state: Optional[str] = None) -> Any:
    """Update an issue."""
    data = {}
    if title is not None: data["title"] = title
    if body is not None: data["body"] = body
    if state is not None: data["state"] = state
    return make_request("PATCH", f"/repos/{owner}/{repo}/issues/{issue_number}", json=data)

@mcp.tool()
def list_issue_comments(owner: str, repo: str, issue_number: int) -> Any:
    """List issue comments."""
    return make_request("GET", f"/repos/{owner}/{repo}/issues/{issue_number}/comments")

@mcp.tool()
def create_issue_comment(owner: str, repo: str, issue_number: int, body: str) -> Any:
    """Create an issue comment."""
    return make_request("POST", f"/repos/{owner}/{repo}/issues/{issue_number}/comments", json={"body": body})

# --- Pull Requests ---

@mcp.tool()
def get_pull_request(owner: str, repo: str, pull_number: int) -> Any:
    """Get a pull request."""
    return make_request("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}")

@mcp.tool()
def list_pull_requests(owner: str, repo: str, state: str = "open") -> Any:
    """List pull requests."""
    return make_request("GET", f"/repos/{owner}/{repo}/pulls", params={"state": state})

@mcp.tool()
def create_pull_request(owner: str, repo: str, title: str, head: str, base: str, body: Optional[str] = None) -> Any:
    """Create a pull request."""
    data = {"title": title, "head": head, "base": base}
    if body is not None: data["body"] = body
    return make_request("POST", f"/repos/{owner}/{repo}/pulls", json=data)

@mcp.tool()
def merge_pull_request(owner: str, repo: str, pull_number: int, commit_title: Optional[str] = None, merge_method: str = "merge") -> Any:
    """Merge a pull request."""
    data = {"merge_method": merge_method}
    if commit_title is not None: data["commit_title"] = commit_title
    return make_request("PUT", f"/repos/{owner}/{repo}/pulls/{pull_number}/merge", json=data)

@mcp.tool()
def create_pull_request_review(owner: str, repo: str, pull_number: int, event: str, body: Optional[str] = None) -> Any:
    """Create a review for a pull request."""
    data = {"event": event}
    if body is not None: data["body"] = body
    return make_request("POST", f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews", json=data)

# --- Repositories ---

@mcp.tool()
def get_repository(owner: str, repo: str) -> Any:
    """Get a repository."""
    return make_request("GET", f"/repos/{owner}/{repo}")

@mcp.tool()
def create_repository(name: str, description: Optional[str] = None, private: bool = False) -> Any:
    """Create a new repository for the authenticated user."""
    data = {"name": name, "private": private}
    if description is not None: data["description"] = description
    return make_request("POST", "/user/repos", json=data)

@mcp.tool()
def fork_repository(owner: str, repo: str, organization: Optional[str] = None) -> Any:
    """Create a fork for the authenticated user."""
    data = {}
    if organization is not None: data["organization"] = organization
    return make_request("POST", f"/repos/{owner}/{repo}/forks", json=data)

@mcp.tool()
def list_branches(owner: str, repo: str) -> Any:
    """List branches."""
    return make_request("GET", f"/repos/{owner}/{repo}/branches")

@mcp.tool()
def get_branch(owner: str, repo: str, branch: str) -> Any:
    """Get a branch."""
    return make_request("GET", f"/repos/{owner}/{repo}/branches/{branch}")

@mcp.tool()
def list_commits(owner: str, repo: str, sha: Optional[str] = None) -> Any:
    """List commits."""
    params = {}
    if sha is not None: params["sha"] = sha
    return make_request("GET", f"/repos/{owner}/{repo}/commits", params=params)

@mcp.tool()
def get_repository_content(owner: str, repo: str, path: str, ref: Optional[str] = None) -> Any:
    """Get repository content."""
    params = {}
    if ref is not None: params["ref"] = ref
    return make_request("GET", f"/repos/{owner}/{repo}/contents/{path}", params=params)

@mcp.tool()
def create_or_update_file_contents(owner: str, repo: str, path: str, message: str, content: str, sha: Optional[str] = None, branch: Optional[str] = None) -> Any:
    """Create or update file contents."""
    encoded_content = base64.b64encode(content.encode("utf-8")).decode("utf-8")
    data = {"message": message, "content": encoded_content}
    if sha is not None: data["sha"] = sha
    if branch is not None: data["branch"] = branch
    return make_request("PUT", f"/repos/{owner}/{repo}/contents/{path}", json=data)

# --- Releases ---

@mcp.tool()
def list_releases(owner: str, repo: str) -> Any:
    """List releases."""
    return make_request("GET", f"/repos/{owner}/{repo}/releases")

@mcp.tool()
def get_release(owner: str, repo: str, release_id: int) -> Any:
    """Get a release."""
    return make_request("GET", f"/repos/{owner}/{repo}/releases/{release_id}")

@mcp.tool()
def create_release(owner: str, repo: str, tag_name: str, name: Optional[str] = None, body: Optional[str] = None, draft: bool = False, prerelease: bool = False) -> Any:
    """Create a release."""
    data = {"tag_name": tag_name, "draft": draft, "prerelease": prerelease}
    if name is not None: data["name"] = name
    if body is not None: data["body"] = body
    return make_request("POST", f"/repos/{owner}/{repo}/releases", json=data)

# --- Actions ---

@mcp.tool()
def list_repository_workflows(owner: str, repo: str) -> Any:
    """List repository workflows."""
    return make_request("GET", f"/repos/{owner}/{repo}/actions/workflows")

@mcp.tool()
def list_workflow_runs(owner: str, repo: str, workflow_id: str) -> Any:
    """List workflow runs."""
    return make_request("GET", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs")

@mcp.tool()
def trigger_workflow_dispatch(owner: str, repo: str, workflow_id: str, ref: str, inputs: Optional[Dict[str, Any]] = None) -> Any:
    """Create a workflow dispatch event."""
    data = {"ref": ref}
    if inputs is not None: data["inputs"] = inputs
    return make_request("POST", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches", json=data)

# --- Code Search ---

@mcp.tool()
def search_code(q: str, sort: Optional[str] = None, order: Optional[str] = None) -> Any:
    """Search code."""
    params = {"q": q}
    if sort is not None: params["sort"] = sort
    if order is not None: params["order"] = order
    return make_request("GET", "/search/code", params=params)

@mcp.tool()
def search_issues(q: str, sort: Optional[str] = None, order: Optional[str] = None) -> Any:
    """Search issues and pull requests."""
    params = {"q": q}
    if sort is not None: params["sort"] = sort
    if order is not None: params["order"] = order
    return make_request("GET", "/search/issues", params=params)

@mcp.tool()
def search_repositories(q: str, sort: Optional[str] = None, order: Optional[str] = None) -> Any:
    """Search repositories."""
    params = {"q": q}
    if sort is not None: params["sort"] = sort
    if order is not None: params["order"] = order
    return make_request("GET", "/search/repositories", params=params)

# --- Webhooks ---

@mcp.tool()
def list_repository_webhooks(owner: str, repo: str) -> Any:
    """List repository webhooks."""
    return make_request("GET", f"/repos/{owner}/{repo}/hooks")

@mcp.tool()
def create_repository_webhook(owner: str, repo: str, config: Dict[str, Any], events: Optional[List[str]] = None, active: bool = True) -> Any:
    """Create a repository webhook."""
    data = {"config": config, "active": active}
    if events is not None: data["events"] = events
    return make_request("POST", f"/repos/{owner}/{repo}/hooks", json=data)

# --- Branch Protection ---

@mcp.tool()
def get_branch_protection(owner: str, repo: str, branch: str) -> Any:
    """Get branch protection."""
    return make_request("GET", f"/repos/{owner}/{repo}/branches/{branch}/protection")

@mcp.tool()
def update_branch_protection(owner: str, repo: str, branch: str, required_status_checks: Optional[Dict[str, Any]], enforce_admins: bool, required_pull_request_reviews: Optional[Dict[str, Any]], restrictions: Optional[Dict[str, Any]]) -> Any:
    """Update branch protection."""
    data = {
        "required_status_checks": required_status_checks,
        "enforce_admins": enforce_admins,
        "required_pull_request_reviews": required_pull_request_reviews,
        "restrictions": restrictions
    }
    return make_request("PUT", f"/repos/{owner}/{repo}/branches/{branch}/protection", json=data)

if __name__ == "__main__":
    mcp.run()
