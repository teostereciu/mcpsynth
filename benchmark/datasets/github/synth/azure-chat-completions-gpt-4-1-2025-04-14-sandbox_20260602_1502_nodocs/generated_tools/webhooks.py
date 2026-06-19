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

@tool("list_repo_webhooks")
def list_repo_webhooks(owner: str, repo: str):
    """List webhooks for a repository."""
    url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/hooks"
    resp = requests.get(url, headers=HEADERS)
    return handle_response(resp)

@tool("create_repo_webhook")
def create_repo_webhook(owner: str, repo: str, config: dict, events: list = None, active: bool = True):
    """Create a webhook for a repository."""
    url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/hooks"
    data = {"config": config, "active": active}
    if events:
        data["events"] = events
    resp = requests.post(url, headers=HEADERS, json=data)
    return handle_response(resp)
