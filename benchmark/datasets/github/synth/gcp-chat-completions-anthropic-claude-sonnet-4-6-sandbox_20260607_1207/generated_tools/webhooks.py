"""GitHub Repository Webhooks and Forks tools."""
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


def _patch(path, json=None):
    try:
        r = requests.patch(f"{BASE_URL}{path}", headers=HEADERS, json=json, timeout=30)
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


def register_webhooks_tools(mcp: FastMCP):

    # --- Repository Webhooks ---

    @mcp.tool()
    def list_repo_webhooks(owner: str, repo: str, per_page: int = 30, page: int = 1) -> dict:
        """List webhooks for a repository."""
        return _get(f"/repos/{owner}/{repo}/hooks", {"per_page": per_page, "page": page})

    @mcp.tool()
    def create_repo_webhook(owner: str, repo: str, url: str, events: list = None,
                            content_type: str = "json", secret: str = None,
                            active: bool = True) -> dict:
        """Create a webhook for a repository."""
        config = {"url": url, "content_type": content_type}
        if secret:
            config["secret"] = secret
        payload = {"name": "web", "active": active, "config": config,
                   "events": events or ["push"]}
        return _post(f"/repos/{owner}/{repo}/hooks", payload)

    @mcp.tool()
    def get_repo_webhook(owner: str, repo: str, hook_id: int) -> dict:
        """Get a specific repository webhook by ID."""
        return _get(f"/repos/{owner}/{repo}/hooks/{hook_id}")

    @mcp.tool()
    def update_repo_webhook(owner: str, repo: str, hook_id: int, url: str = None,
                            events: list = None, add_events: list = None,
                            remove_events: list = None, active: bool = None,
                            content_type: str = None, secret: str = None) -> dict:
        """Update a repository webhook."""
        payload = {}
        config = {}
        if url:
            config["url"] = url
        if content_type:
            config["content_type"] = content_type
        if secret:
            config["secret"] = secret
        if config:
            payload["config"] = config
        if events is not None:
            payload["events"] = events
        if add_events:
            payload["add_events"] = add_events
        if remove_events:
            payload["remove_events"] = remove_events
        if active is not None:
            payload["active"] = active
        return _patch(f"/repos/{owner}/{repo}/hooks/{hook_id}", payload)

    @mcp.tool()
    def delete_repo_webhook(owner: str, repo: str, hook_id: int) -> dict:
        """Delete a repository webhook."""
        return _delete(f"/repos/{owner}/{repo}/hooks/{hook_id}")

    @mcp.tool()
    def ping_repo_webhook(owner: str, repo: str, hook_id: int) -> dict:
        """Ping a repository webhook to test it."""
        return _post(f"/repos/{owner}/{repo}/hooks/{hook_id}/pings")

    @mcp.tool()
    def test_push_repo_webhook(owner: str, repo: str, hook_id: int) -> dict:
        """Test a push webhook by triggering a fake push event."""
        return _post(f"/repos/{owner}/{repo}/hooks/{hook_id}/tests")

    # --- Forks ---

    @mcp.tool()
    def list_forks(owner: str, repo: str, sort: str = "newest",
                   per_page: int = 30, page: int = 1) -> dict:
        """List forks of a repository."""
        return _get(f"/repos/{owner}/{repo}/forks",
                    {"sort": sort, "per_page": per_page, "page": page})

    @mcp.tool()
    def create_fork(owner: str, repo: str, organization: str = None,
                    name: str = None, default_branch_only: bool = False) -> dict:
        """Fork a repository for the authenticated user or into an organization."""
        payload = {"default_branch_only": default_branch_only}
        if organization:
            payload["organization"] = organization
        if name:
            payload["name"] = name
        return _post(f"/repos/{owner}/{repo}/forks", payload)
