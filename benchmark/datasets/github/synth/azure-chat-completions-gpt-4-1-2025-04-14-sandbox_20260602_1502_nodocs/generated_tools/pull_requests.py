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

@tool("list_pull_requests")
def list_pull_requests(owner: str, repo: str, state: str = "open"): 
    """List pull requests for a repository."""
    url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/pulls"
    params = {"state": state}
    resp = requests.get(url, headers=HEADERS, params=params)
    return handle_response(resp)

@tool("create_pull_request")
def create_pull_request(owner: str, repo: str, title: str, head: str, base: str, body: str = None):
    """Create a new pull request."""
    url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/pulls"
    data = {"title": title, "head": head, "base": base}
    if body:
        data["body"] = body
    resp = requests.post(url, headers=HEADERS, json=data)
    return handle_response(resp)

@tool("get_pull_request")
def get_pull_request(owner: str, repo: str, pull_number: int):
    """Get a single pull request."""
    url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/pulls/{pull_number}"
    resp = requests.get(url, headers=HEADERS)
    return handle_response(resp)

@tool("merge_pull_request")
def merge_pull_request(owner: str, repo: str, pull_number: int, commit_title: str = None, commit_message: str = None, merge_method: str = "merge"):
    """Merge a pull request."""
    url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/pulls/{pull_number}/merge"
    data = {"merge_method": merge_method}
    if commit_title:
        data["commit_title"] = commit_title
    if commit_message:
        data["commit_message"] = commit_message
    resp = requests.put(url, headers=HEADERS, json=data)
    return handle_response(resp)
