from mcp_server import mcp
from github_client import make_request

@mcp.tool()
def create_repository(name: str, description: str = None, private: bool = False, auto_init: bool = True) -> dict:
    """Create a new repository for the authenticated user."""
    payload = {"name": name, "private": private, "auto_init": auto_init}
    if description: payload["description"] = description
    return make_request("POST", "/user/repos", json=payload)

@mcp.tool()
def fork_repository(owner: str, repo: str, organization: str = None) -> dict:
    """Create a fork of a repository."""
    payload = {}
    if organization: payload["organization"] = organization
    return make_request("POST", f"/repos/{owner}/{repo}/forks", json=payload)

@mcp.tool()
def list_branches(owner: str, repo: str, per_page: int = 30, page: int = 1) -> dict:
    """List branches in a repository."""
    return make_request("GET", f"/repos/{owner}/{repo}/branches", params={"per_page": per_page, "page": page})

@mcp.tool()
def list_commits(owner: str, repo: str, sha: str = None, per_page: int = 30, page: int = 1) -> dict:
    """List commits in a repository."""
    params = {"per_page": per_page, "page": page}
    if sha: params["sha"] = sha
    return make_request("GET", f"/repos/{owner}/{repo}/commits", params=params)

@mcp.tool()
def get_repository_content(owner: str, repo: str, path: str, ref: str = None) -> dict:
    """Get repository content (file or directory)."""
    params = {}
    if ref: params["ref"] = ref
    return make_request("GET", f"/repos/{owner}/{repo}/contents/{path}", params=params)

@mcp.tool()
def create_or_update_file(owner: str, repo: str, path: str, message: str, content: str, sha: str = None, branch: str = None) -> dict:
    """Create or update a file in a repository. Content must be base64 encoded."""
    payload = {"message": message, "content": content}
    if sha: payload["sha"] = sha
    if branch: payload["branch"] = branch
    return make_request("PUT", f"/repos/{owner}/{repo}/contents/{path}", json=payload)

@mcp.tool()
def delete_file(owner: str, repo: str, path: str, message: str, sha: str, branch: str = None) -> dict:
    """Delete a file in a repository."""
    payload = {"message": message, "sha": sha}
    if branch: payload["branch"] = branch
    return make_request("DELETE", f"/repos/{owner}/{repo}/contents/{path}", json=payload)
