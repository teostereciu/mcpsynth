import os
import requests
from typing import Any, Dict, List, Optional, Union
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("github-api")

# GitHub API configuration
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
GITHUB_API_BASE_URL = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com").rstrip("/")

def make_request(method: str, endpoint: str, **kwargs) -> Any:
    """Helper to make GitHub API requests."""
    url = f"{GITHUB_API_BASE_URL}{endpoint}"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    
    if "headers" in kwargs:
        headers.update(kwargs.pop("headers"))
        
    response = requests.request(method, url, headers=headers, **kwargs)
    
    try:
        response.raise_for_status()
        if response.content:
            return response.json()
        return {"status": "success"}
    except requests.exceptions.HTTPError as e:
        try:
            error_data = response.json()
            return {"error": str(e), "details": error_data}
        except Exception:
            return {"error": str(e), "details": response.text}
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def list_repository_issues(owner: str, repo: str, state: str = "open", per_page: int = 30, page: int = 1) -> Any:
    """List issues in a repository."""
    return make_request("GET", f"/repos/{owner}/{repo}/issues", params={"state": state, "per_page": per_page, "page": page})

@mcp.tool()
def create_issue(owner: str, repo: str, title: str, body: Optional[str] = None, assignees: Optional[List[str]] = None, labels: Optional[List[str]] = None) -> Any:
    """Create an issue."""
    data = {"title": title}
    if body is not None: data["body"] = body
    if assignees is not None: data["assignees"] = assignees
    if labels is not None: data["labels"] = labels
    return make_request("POST", f"/repos/{owner}/{repo}/issues", json=data)

@mcp.tool()
def get_issue(owner: str, repo: str, issue_number: int) -> Any:
    """Get an issue."""
    return make_request("GET", f"/repos/{owner}/{repo}/issues/{issue_number}")

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

if __name__ == "__main__":
    mcp.run()
