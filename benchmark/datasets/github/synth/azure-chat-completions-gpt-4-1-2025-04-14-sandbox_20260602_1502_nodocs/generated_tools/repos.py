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

@tool("get_repo")
def get_repo(owner: str, repo: str):
    """Get a repository."""
    url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}"
    resp = requests.get(url, headers=HEADERS)
    return handle_response(resp)

@tool("create_repo")
def create_repo(name: str, description: str = None, private: bool = False, auto_init: bool = False):
    """Create a new repository for the authenticated user."""
    url = f"{GITHUB_API_BASE_URL}/user/repos"
    data = {"name": name, "private": private, "auto_init": auto_init}
    if description:
        data["description"] = description
    resp = requests.post(url, headers=HEADERS, json=data)
    return handle_response(resp)

@tool("fork_repo")
def fork_repo(owner: str, repo: str):
    """Fork a repository."""
    url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/forks"
    resp = requests.post(url, headers=HEADERS)
    return handle_response(resp)

@tool("list_branches")
def list_branches(owner: str, repo: str):
    """List branches in a repository."""
    url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/branches"
    resp = requests.get(url, headers=HEADERS)
    return handle_response(resp)

@tool("get_branch")
def get_branch(owner: str, repo: str, branch: str):
    """Get a branch in a repository."""
    url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/branches/{branch}"
    resp = requests.get(url, headers=HEADERS)
    return handle_response(resp)
