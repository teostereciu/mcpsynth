from mcp_server import mcp
from github_client import make_request

@mcp.tool()
def list_repository_webhooks(owner: str, repo: str, per_page: int = 30, page: int = 1) -> dict:
    """List repository webhooks."""
    return make_request("GET", f"/repos/{owner}/{repo}/hooks", params={"per_page": per_page, "page": page})

@mcp.tool()
def create_repository_webhook(owner: str, repo: str, url: str, content_type: str = "json", secret: str = None, events: list[str] = None, active: bool = True) -> dict:
    """Create a repository webhook."""
    config = {"url": url, "content_type": content_type}
    if secret: config["secret"] = secret
    payload = {"name": "web", "config": config, "active": active}
    if events: payload["events"] = events
    return make_request("POST", f"/repos/{owner}/{repo}/hooks", json=payload)
