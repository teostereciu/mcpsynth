"""Issue-related tools (issues, comments, labels, milestones, dependencies/sub-issues)."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from . import mcp
from .http import github_request, split_repo


@mcp.tool
def issues_create(repo: str, title: str, body: Optional[str] = None, labels: Optional[List[str]] = None) -> Dict[str, Any]:
    """Create an issue in a repository."""
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}
    payload: Dict[str, Any] = {"title": title}
    if body is not None:
        payload["body"] = body
    if labels is not None:
        payload["labels"] = labels
    return github_request("POST", f"/repos/{r['owner']}/{r['repo']}/issues", json=payload)


@mcp.tool
def issues_update(
    repo: str,
    issue_number: int,
    title: Optional[str] = None,
    body: Optional[str] = None,
    state: Optional[str] = None,
    labels: Optional[List[str]] = None,
    milestone: Optional[int] = None,
) -> Dict[str, Any]:
    """Update an issue (title/body/state/labels/milestone)."""
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}
    payload: Dict[str, Any] = {}
    if title is not None:
        payload["title"] = title
    if body is not None:
        payload["body"] = body
    if state is not None:
        payload["state"] = state
    if labels is not None:
        payload["labels"] = labels
    if milestone is not None:
        payload["milestone"] = milestone
    return github_request("PATCH", f"/repos/{r['owner']}/{r['repo']}/issues/{issue_number}", json=payload)


@mcp.tool
def issues_add_labels(repo: str, issue_number: int, labels: List[str]) -> Dict[str, Any]:
    """Add labels to an issue."""
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}
    return github_request(
        "POST",
        f"/repos/{r['owner']}/{r['repo']}/issues/{issue_number}/labels",
        json={"labels": labels},
    )


@mcp.tool
def issues_remove_label(repo: str, issue_number: int, name: str) -> Dict[str, Any]:
    """Remove a label from an issue."""
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}
    return github_request(
        "DELETE",
        f"/repos/{r['owner']}/{r['repo']}/issues/{issue_number}/labels/{name}",
    )


@mcp.tool
def issues_create_comment(repo: str, issue_number: int, body: str) -> Dict[str, Any]:
    """Create an issue comment."""
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}
    return github_request(
        "POST",
        f"/repos/{r['owner']}/{r['repo']}/issues/{issue_number}/comments",
        json={"body": body},
    )


@mcp.tool
def issues_list_for_repo(
    repo: str,
    state: str = "open",
    labels: Optional[List[str]] = None,
    per_page: int = 30,
    page: int = 1,
) -> Dict[str, Any]:
    """List issues for a repository."""
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}
    params: Dict[str, Any] = {"state": state, "per_page": per_page, "page": page}
    if labels:
        params["labels"] = ",".join(labels)
    return github_request("GET", f"/repos/{r['owner']}/{r['repo']}/issues", params=params)


@mcp.tool
def milestones_list(repo: str, state: str = "open", per_page: int = 100, page: int = 1) -> Dict[str, Any]:
    """List milestones for a repository."""
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}
    return github_request(
        "GET",
        f"/repos/{r['owner']}/{r['repo']}/milestones",
        params={"state": state, "per_page": per_page, "page": page},
    )


@mcp.tool
def milestones_create(repo: str, title: str, description: Optional[str] = None) -> Dict[str, Any]:
    """Create a milestone."""
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}
    payload: Dict[str, Any] = {"title": title}
    if description is not None:
        payload["description"] = description
    return github_request("POST", f"/repos/{r['owner']}/{r['repo']}/milestones", json=payload)


@mcp.tool
def issues_add_sub_issue(repo: str, issue_number: int, sub_issue_id: int) -> Dict[str, Any]:
    """Add a sub-issue to an issue (issue dependencies/sub-issues)."""
    try:
        r = split_repo(repo)
    except ValueError as e:
        return {"error": str(e)}
    return github_request(
        "POST",
        f"/repos/{r['owner']}/{r['repo']}/issues/{issue_number}/sub_issues",
        json={"sub_issue_id": sub_issue_id},
    )
