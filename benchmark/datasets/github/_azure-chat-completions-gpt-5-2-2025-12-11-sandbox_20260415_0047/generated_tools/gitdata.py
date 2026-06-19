from __future__ import annotations

import base64
from typing import Any, Dict, Optional

from . import mcp
from .http import GitHubClient, split_repo


@mcp.tool()
def git_get_ref(repo: str, ref: str) -> Dict[str, Any]:
    """Get a git ref (e.g. heads/main, tags/v1.0.0)."""
    try:
        owner, r = split_repo(repo)
        client = GitHubClient.from_env()
        status, payload = client.request("GET", f"/repos/{owner}/{r}/git/ref/{ref}")
        return client.ok_or_error(status, payload)  # type: ignore[return-value]
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def git_create_ref(repo: str, ref: str, sha: str) -> Dict[str, Any]:
    """Create a git ref (ref must be fully qualified like refs/heads/x or refs/tags/y)."""
    try:
        owner, r = split_repo(repo)
        client = GitHubClient.from_env()
        status, payload = client.request("POST", f"/repos/{owner}/{r}/git/refs", json_body={"ref": ref, "sha": sha})
        return client.ok_or_error(status, payload)  # type: ignore[return-value]
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def git_update_ref(repo: str, ref: str, sha: str, force: bool = False) -> Dict[str, Any]:
    """Update a git ref (ref is like heads/branch or tags/tagname)."""
    try:
        owner, r = split_repo(repo)
        client = GitHubClient.from_env()
        status, payload = client.request(
            "PATCH",
            f"/repos/{owner}/{r}/git/refs/{ref}",
            json_body={"sha": sha, "force": force},
        )
        return client.ok_or_error(status, payload)  # type: ignore[return-value]
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def repos_get_content(repo: str, path: str, ref: Optional[str] = None) -> Any:
    """Get repository content metadata (and base64 content for files)."""
    try:
        owner, r = split_repo(repo)
        client = GitHubClient.from_env()
        params: Dict[str, Any] = {}
        if ref is not None:
            params["ref"] = ref
        status, payload = client.request("GET", f"/repos/{owner}/{r}/contents/{path.lstrip('/')}" , params=params)
        return client.ok_or_error(status, payload)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def repos_put_content(
    repo: str,
    path: str,
    message: str,
    content_utf8: str,
    branch: Optional[str] = None,
    sha: Optional[str] = None,
) -> Dict[str, Any]:
    """Create or update a file via the Contents API."""
    try:
        owner, r = split_repo(repo)
        client = GitHubClient.from_env()
        content_b64 = base64.b64encode(content_utf8.encode("utf-8")).decode("ascii")
        json_body: Dict[str, Any] = {"message": message, "content": content_b64}
        if branch is not None:
            json_body["branch"] = branch
        if sha is not None:
            json_body["sha"] = sha
        status, payload = client.request("PUT", f"/repos/{owner}/{r}/contents/{path.lstrip('/')}" , json_body=json_body)
        return client.ok_or_error(status, payload)  # type: ignore[return-value]
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def repos_list_commits(repo: str, sha: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    """List commits for a repository (optionally starting from a branch/SHA)."""
    try:
        owner, r = split_repo(repo)
        client = GitHubClient.from_env()
        params: Dict[str, Any] = {"per_page": per_page, "page": page}
        if sha is not None:
            params["sha"] = sha
        status, payload = client.request("GET", f"/repos/{owner}/{r}/commits", params=params)
        return client.ok_or_error(status, payload)
    except Exception as e:
        return {"error": str(e)}
