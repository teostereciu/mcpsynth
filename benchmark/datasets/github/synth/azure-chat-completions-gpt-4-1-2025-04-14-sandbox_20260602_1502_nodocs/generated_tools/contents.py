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

@tool("get_file_contents")
def get_file_contents(owner: str, repo: str, path: str, ref: str = None):
    """Get the contents of a file or directory in a repository."""
    url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/contents/{path}"
    params = {}
    if ref:
        params["ref"] = ref
    resp = requests.get(url, headers=HEADERS, params=params)
    return handle_response(resp)

@tool("update_file_contents")
def update_file_contents(owner: str, repo: str, path: str, message: str, content: str, sha: str, branch: str = None):
    """Update a file in a repository (content must be base64 encoded)."""
    url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/contents/{path}"
    data = {"message": message, "content": content, "sha": sha}
    if branch:
        data["branch"] = branch
    resp = requests.put(url, headers=HEADERS, json=data)
    return handle_response(resp)

@tool("create_file")
def create_file(owner: str, repo: str, path: str, message: str, content: str, branch: str = None):
    """Create a new file in a repository (content must be base64 encoded)."""
    url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/contents/{path}"
    data = {"message": message, "content": content}
    if branch:
        data["branch"] = branch
    resp = requests.put(url, headers=HEADERS, json=data)
    return handle_response(resp)
