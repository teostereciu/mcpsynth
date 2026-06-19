from mcp_server import mcp
from github_client import make_request

@mcp.tool()
def list_releases(owner: str, repo: str, per_page: int = 30, page: int = 1) -> dict:
    """List releases in a repository."""
    return make_request("GET", f"/repos/{owner}/{repo}/releases", params={"per_page": per_page, "page": page})

@mcp.tool()
def create_release(owner: str, repo: str, tag_name: str, name: str = None, body: str = None, draft: bool = False, prerelease: bool = False) -> dict:
    """Create a release in a repository."""
    payload = {"tag_name": tag_name, "draft": draft, "prerelease": prerelease}
    if name: payload["name"] = name
    if body: payload["body"] = body
    return make_request("POST", f"/repos/{owner}/{repo}/releases", json=payload)

@mcp.tool()
def get_release(owner: str, repo: str, release_id: int) -> dict:
    """Get a release in a repository."""
    return make_request("GET", f"/repos/{owner}/{repo}/releases/{release_id}")
