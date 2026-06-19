from typing import Any, Dict, List, Optional
from .client import make_request

def list_repository_webhooks(owner: str, repo: str) -> Any:
    """List repository webhooks."""
    return make_request("GET", f"/repos/{owner}/{repo}/hooks")

def create_repository_webhook(owner: str, repo: str, config_url: str, config_content_type: str = "json", events: List[str] = ["push"], active: bool = True) -> Any:
    """Create a repository webhook."""
    data = {
        "name": "web",
        "active": active,
        "events": events,
        "config": {
            "url": config_url,
            "content_type": config_content_type
        }
    }
    return make_request("POST", f"/repos/{owner}/{repo}/hooks", json=data)
