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

@tool("get_branch_protection")
def get_branch_protection(owner: str, repo: str, branch: str):
    """Get branch protection for a branch."""
    url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/branches/{branch}/protection"
    resp = requests.get(url, headers=HEADERS)
    return handle_response(resp)

@tool("update_branch_protection")
def update_branch_protection(owner: str, repo: str, branch: str, protection: dict):
    """Update branch protection for a branch."""
    url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/branches/{branch}/protection"
    resp = requests.put(url, headers=HEADERS, json=protection)
    return handle_response(resp)
