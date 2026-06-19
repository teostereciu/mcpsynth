import os
import requests
from fastmcp import tool

GITHUB_API_BASE_URL = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}

def handle_response(resp):
    try:
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": resp.status_code, "body": resp.text}

@tool("list_issues")
def list_issues(owner: str, repo: str, state: str = "open", labels: str = None, assignee: str = None):
    """List issues for a repository."""
    url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/issues"
    params = {"state": state}
    if labels:
        params["labels"] = labels
    if assignee:
        params["assignee"] = assignee
    resp = requests.get(url, headers=HEADERS, params=params)
    return handle_response(resp)

@tool("create_issue")
def create_issue(owner: str, repo: str, title: str, body: str = None, labels: list = None, assignees: list = None):
    """Create a new issue in a repository."""
    url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/issues"
    data = {"title": title}
    if body:
        data["body"] = body
    if labels:
        data["labels"] = labels
    if assignees:
        data["assignees"] = assignees
    resp = requests.post(url, headers=HEADERS, json=data)
    return handle_response(resp)

@tool("get_issue")
def get_issue(owner: str, repo: str, issue_number: int):
    """Get a single issue."""
    url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/issues/{issue_number}"
    resp = requests.get(url, headers=HEADERS)
    return handle_response(resp)

@tool("update_issue")
def update_issue(owner: str, repo: str, issue_number: int, title: str = None, body: str = None, state: str = None, labels: list = None, assignees: list = None):
    """Update an issue."""
    url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/issues/{issue_number}"
    data = {}
    if title:
        data["title"] = title
    if body:
        data["body"] = body
    if state:
        data["state"] = state
    if labels:
        data["labels"] = labels
    if assignees:
        data["assignees"] = assignees
    resp = requests.patch(url, headers=HEADERS, json=data)
    return handle_response(resp)

@tool("close_issue")
def close_issue(owner: str, repo: str, issue_number: int):
    """Close an issue."""
    url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/issues/{issue_number}"
    data = {"state": "closed"}
    resp = requests.patch(url, headers=HEADERS, json=data)
    return handle_response(resp)
