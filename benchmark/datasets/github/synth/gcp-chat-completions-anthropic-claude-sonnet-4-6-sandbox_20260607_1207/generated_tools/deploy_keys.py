"""GitHub Deploy Keys tools."""
import os
import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com")
TOKEN = os.environ.get("GITHUB_TOKEN", "")

HEADERS = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}
if TOKEN:
    HEADERS["Authorization"] = f"Bearer {TOKEN}"


def _get(path, params=None):
    try:
        r = requests.get(f"{BASE_URL}{path}", headers=HEADERS, params=params, timeout=30)
        if r.status_code == 204:
            return {"status": "no_content"}
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def _post(path, json=None):
    try:
        r = requests.post(f"{BASE_URL}{path}", headers=HEADERS, json=json, timeout=30)
        if r.status_code == 204:
            return {"status": "no_content"}
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def _delete(path):
    try:
        r = requests.delete(f"{BASE_URL}{path}", headers=HEADERS, timeout=30)
        if r.status_code == 204:
            return {"status": "no_content"}
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def register_deploy_keys_tools(mcp: FastMCP):

    @mcp.tool()
    def list_deploy_keys(owner: str, repo: str, per_page: int = 30, page: int = 1) -> dict:
        """List deploy keys for a repository."""
        return _get(f"/repos/{owner}/{repo}/keys", {"per_page": per_page, "page": page})

    @mcp.tool()
    def create_deploy_key(owner: str, repo: str, key: str, title: str = None,
                          read_only: bool = True) -> dict:
        """Create a deploy key for a repository."""
        payload = {"key": key, "read_only": read_only}
        if title:
            payload["title"] = title
        return _post(f"/repos/{owner}/{repo}/keys", payload)

    @mcp.tool()
    def get_deploy_key(owner: str, repo: str, key_id: int) -> dict:
        """Get a deploy key by ID."""
        return _get(f"/repos/{owner}/{repo}/keys/{key_id}")

    @mcp.tool()
    def delete_deploy_key(owner: str, repo: str, key_id: int) -> dict:
        """Delete a deploy key."""
        return _delete(f"/repos/{owner}/{repo}/keys/{key_id}")
