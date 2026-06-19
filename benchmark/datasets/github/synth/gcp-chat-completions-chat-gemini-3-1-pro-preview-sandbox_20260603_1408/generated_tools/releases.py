from typing import Any, Dict, List, Optional
from .client import make_request

def list_releases(owner: str, repo: str) -> Any:
    """List releases."""
    return make_request("GET", f"/repos/{owner}/{repo}/releases")

def create_release(owner: str, repo: str, tag_name: str, name: Optional[str] = None, body: Optional[str] = None, draft: bool = False, prerelease: bool = False) -> Any:
    """Create a release."""
    data = {"tag_name": tag_name, "draft": draft, "prerelease": prerelease}
    if name is not None: data["name"] = name
    if body is not None: data["body"] = body
    return make_request("POST", f"/repos/{owner}/{repo}/releases", json=data)
