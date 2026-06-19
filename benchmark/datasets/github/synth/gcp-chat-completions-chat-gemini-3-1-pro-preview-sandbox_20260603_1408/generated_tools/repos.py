from typing import Any, Dict, List, Optional
from .client import make_request

def get_repository(owner: str, repo: str) -> Any:
    """Get a repository."""
    return make_request("GET", f"/repos/{owner}/{repo}")

def create_repository(name: str, description: Optional[str] = None, private: bool = False) -> Any:
    """Create a repository for the authenticated user."""
    data = {"name": name, "private": private}
    if description is not None: data["description"] = description
    return make_request("POST", "/user/repos", json=data)

def update_repository(owner: str, repo: str, description: Optional[str] = None, private: Optional[bool] = None) -> Any:
    """Update a repository."""
    data = {}
    if description is not None: data["description"] = description
    if private is not None: data["private"] = private
    return make_request("PATCH", f"/repos/{owner}/{repo}", json=data)

def delete_repository(owner: str, repo: str) -> Any:
    """Delete a repository."""
    return make_request("DELETE", f"/repos/{owner}/{repo}")

def create_fork(owner: str, repo: str) -> Any:
    """Create a fork."""
    return make_request("POST", f"/repos/{owner}/{repo}/forks")

def list_branches(owner: str, repo: str) -> Any:
    """List branches."""
    return make_request("GET", f"/repos/{owner}/{repo}/branches")

def list_commits(owner: str, repo: str, sha: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    """List commits."""
    params = {"per_page": per_page, "page": page}
    if sha is not None: params["sha"] = sha
    return make_request("GET", f"/repos/{owner}/{repo}/commits", params=params)

def get_repository_content(owner: str, repo: str, path: str, ref: Optional[str] = None) -> Any:
    """Get repository content."""
    params = {}
    if ref is not None: params["ref"] = ref
    return make_request("GET", f"/repos/{owner}/{repo}/contents/{path}", params=params)

def create_or_update_file_contents(owner: str, repo: str, path: str, message: str, content: str, sha: Optional[str] = None, branch: Optional[str] = None) -> Any:
    """Create or update file contents."""
    import base64
    encoded_content = base64.b64encode(content.encode("utf-8")).decode("utf-8")
    data = {"message": message, "content": encoded_content}
    if sha is not None: data["sha"] = sha
    if branch is not None: data["branch"] = branch
    return make_request("PUT", f"/repos/{owner}/{repo}/contents/{path}", json=data)

def delete_file(owner: str, repo: str, path: str, message: str, sha: str, branch: Optional[str] = None) -> Any:
    """Delete a file."""
    data = {"message": message, "sha": sha}
    if branch is not None: data["branch"] = branch
    return make_request("DELETE", f"/repos/{owner}/{repo}/contents/{path}", json=data)
