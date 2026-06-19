"""Pull request tools (create PRs, reviews, merge, reviewers, review comments)."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from . import mcp
from .http import github_request, split_repo


@mcp.tool
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
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}
    payload: Dict[str, Any] = {"title": title, "head": head, "base": base, "draft": draft}
    if body is not None:
        payload["body"] = body
    return github_request("POST", f"/repos/{r['owner']}/{r['repo']}/pulls", json=payload)


@mcp.tool
def pulls_get(repo: str, pull_number: int) -> Dict[str, Any]:
    """Get a pull request."""
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}
    return github_request("GET", f"/repos/{r['owner']}/{r['repo']}/pulls/{pull_number}")


@mcp.tool
def pulls_merge(
    repo: str,
    pull_number: int,
    merge_method: str = "merge",
    commit_title: Optional[str] = None,
    commit_message: Optional[str] = None,
) -> Dict[str, Any]:
    """Merge a pull request."""
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}
    payload: Dict[str, Any] = {"merge_method": merge_method}
    if commit_title is not None:
        payload["commit_title"] = commit_title
    if commit_message is not None:
        payload["commit_message"] = commit_message
    return github_request("PUT", f"/repos/{r['owner']}/{r['repo']}/pulls/{pull_number}/merge", json=payload)


@mcp.tool
def pulls_request_reviewers(repo: str, pull_number: int, reviewers: Optional[List[str]] = None, team_reviewers: Optional[List[str]] = None) -> Dict[str, Any]:
    """Request reviewers for a pull request."""
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}
    payload: Dict[str, Any] = {}
    if reviewers is not None:
        payload["reviewers"] = reviewers
    if team_reviewers is not None:
        payload["team_reviewers"] = team_reviewers
    return github_request("POST", f"/repos/{r['owner']}/{r['repo']}/pulls/{pull_number}/requested_reviewers", json=payload)


@mcp.tool
def pulls_create_review(
    repo: str,
    pull_number: int,
    event: Optional[str] = None,
    body: Optional[str] = None,
    commit_id: Optional[str] = None,
    comments: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    """Create a pull request review (optionally with inline comments).

    Note: GitHub expects diff positions for inline comments. If you only have line numbers,
    consider using `pulls_create_review_comment` with `line`/`side`.
    """
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}
    payload: Dict[str, Any] = {}
    if commit_id is not None:
        payload["commit_id"] = commit_id
    if body is not None:
        payload["body"] = body
    if event is not None:
        payload["event"] = event
    if comments is not None:
        payload["comments"] = comments
    return github_request("POST", f"/repos/{r['owner']}/{r['repo']}/pulls/{pull_number}/reviews", json=payload)


@mcp.tool
def pulls_list_review_comments(repo: str, pull_number: int, per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    """List review comments on a pull request."""
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}
    return github_request(
        "GET",
        f"/repos/{r['owner']}/{r['repo']}/pulls/{pull_number}/comments",
        params={"per_page": per_page, "page": page},
    )


@mcp.tool
def pulls_create_review_comment(
    repo: str,
    pull_number: int,
    body: str,
    commit_id: str,
    path: str,
    line: Optional[int] = None,
    side: Optional[str] = None,
    start_line: Optional[int] = None,
    start_side: Optional[str] = None,
    in_reply_to: Optional[int] = None,
) -> Dict[str, Any]:
    """Create a single review comment on a pull request.

    Uses the Pulls Review Comments API.
    """
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}

    payload: Dict[str, Any] = {"body": body, "commit_id": commit_id, "path": path}
    if in_reply_to is not None:
        payload["in_reply_to"] = in_reply_to
    else:
        if line is not None:
            payload["line"] = line
        if side is not None:
            payload["side"] = side
        if start_line is not None:
            payload["start_line"] = start_line
        if start_side is not None:
            payload["start_side"] = start_side

    return github_request(
        "POST",
        f"/repos/{r['owner']}/{r['repo']}/pulls/{pull_number}/comments",
        json=payload,
    )
