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

@tool("list_releases")
def list_releases(owner: str, repo: str):
    """List releases for a repository."""
    url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/releases"
    resp = requests.get(url, headers=HEADERS)
    return handle_response(resp)

@tool("create_release")
def create_release(owner: str, repo: str, tag_name: str, name: str = None, body: str = None, draft: bool = False, prerelease: bool = False):
    """Create a new release."""
    url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/releases"
    data = {"tag_name": tag_name, "draft": draft, "prerelease": prerelease}
    if name:
        data["name"] = name
    if body:
        data["body"] = body
    resp = requests.post(url, headers=HEADERS, json=data)
    return handle_response(resp)

@tool("get_release")
def get_release(owner: str, repo: str, release_id: int):
    """Get a single release."""
    url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/releases/{release_id}"
    resp = requests.get(url, headers=HEADERS)
    return handle_response(resp)
