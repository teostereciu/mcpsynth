from __future__ import annotations

from typing import Any, Dict, List, Optional

from . import mcp
from .http import GitHubClient, split_repo


@mcp.tool()
def pulls_create(
    repo: str,
    title: str,
    head: str,
    base: str,
    body: Optional[str] = None,
    draft: bool = False,
) -> Dict[str, Any]:
    """Create a pull request."""
    try:
        owner, name = split_repo(repo)
        client = GitHubClient.from_env()
        status, payload = client.request(
            "POST",
            f"/repos/{owner}/{name}/pulls",
            json_body={"title": title, "head": head, "base": base, "body": body, "draft": draft},
        )
        return client.ok_or_error(status, payload)  # type: ignore[return-value]
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def pulls_get(repo: str, pull_number: int) -> Dict[str, Any]:
    """Get a pull request."""
    try:
        owner, name = split_repo(repo)
        client = GitHubClient.from_env()
        status, payload = client.request("GET", f"/repos/{owner}/{name}/pulls/{pull_number}")
        return client.ok_or_error(status, payload)  # type: ignore[return-value]
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def pulls_merge(
    repo: str,
    pull_number: int,
    merge_method: str = "merge",
    commit_title: Optional[str] = None,
    commit_message: Optional[str] = None,
) -> Dict[str, Any]:
    """Merge a pull request."""
    try:
        owner, name = split_repo(repo)
        client = GitHubClient.from_env()
        json_body = {k: v for k, v in {"merge_method": merge_method, "commit_title": commit_title, "commit_message": commit_message}.items() if v is not None}
        status, payload = client.request("PUT", f"/repos/{owner}/{name}/pulls/{pull_number}/merge", json_body=json_body)
        return client.ok_or_error(status, payload)  # type: ignore[return-value]
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def pulls_create_review(
    repo: str,
    pull_number: int,
    event: Optional[str] = None,
    body: Optional[str] = None,
    comments: Optional[List[Dict[str, Any]]] = None,
    commit_id: Optional[str] = None,
) -> Dict[str, Any]:
    """Create a pull request review (optionally with inline comments).

    Note: GitHub supports either `position` (diff position) or `line`/`side` style.
    This tool passes through whatever you provide in each comment object.
    """
    try:
        owner, name = split_repo(repo)
        client = GitHubClient.from_env()
        json_body: Dict[str, Any] = {}
        if commit_id is not None:
            json_body["commit_id"] = commit_id
        if body is not None:
            json_body["body"] = body
        if event is not None:
            json_body["event"] = event
        if comments is not None:
            json_body["comments"] = comments
        status, payload = client.request("POST", f"/repos/{owner}/{name}/pulls/{pull_number}/reviews", json_body=json_body)
        return client.ok_or_error(status, payload)  # type: ignore[return-value]
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def pulls_create_review_comment(
    repo: str,
    pull_number: int,
    body: str,
    commit_id: str,
    path: str,
    line: int,
    side: str = "RIGHT",
) -> Dict[str, Any]:
    """Create a single pull request review comment using line/side API."""
    try:
        owner, name = split_repo(repo)
        client = GitHubClient.from_env()
        status, payload = client.request(
            "POST",
            f"/repos/{owner}/{name}/pulls/{pull_number}/comments",
            json_body={"body": body, "commit_id": commit_id, "path": path, "line": line, "side": side},
        )
        return client.ok_or_error(status, payload)  # type: ignore[return-value]
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def pulls_reply_review_comment(repo: str, pull_number: int, comment_id: int, body: str) -> Dict[str, Any]:
    """Reply to a pull request review comment thread."""
    try:
        owner, name = split_repo(repo)
        client = GitHubClient.from_env()
        status, payload = client.request(
            "POST",
            f"/repos/{owner}/{name}/pulls/{pull_number}/comments/{comment_id}/replies",
            json_body={"body": body},
        )
        return client.ok_or_error(status, payload)  # type: ignore[return-value]
    except Exception as e:
        return {"error": str(e)}
