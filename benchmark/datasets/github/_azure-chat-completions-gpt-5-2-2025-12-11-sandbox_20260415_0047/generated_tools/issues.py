from __future__ import annotations

from typing import Any, Dict, List, Optional

from . import mcp
from .http import GitHubClient, split_repo


@mcp.tool()
def issues_create(repo: str, title: str, body: Optional[str] = None, labels: Optional[List[str]] = None) -> Dict[str, Any]:
    """Create an issue in a repository."""
    try:
        owner, name = split_repo(repo)
        client = GitHubClient.from_env()
        status, payload = client.request(
            "POST",
            f"/repos/{owner}/{name}/issues",
            json_body={k: v for k, v in {"title": title, "body": body, "labels": labels}.items() if v is not None},
        )
        return client.ok_or_error(status, payload)  # type: ignore[return-value]
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
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
        owner, name = split_repo(repo)
        client = GitHubClient.from_env()
        json_body = {k: v for k, v in {"title": title, "body": body, "state": state, "labels": labels, "milestone": milestone}.items() if v is not None}
        status, payload = client.request("PATCH", f"/repos/{owner}/{name}/issues/{issue_number}", json_body=json_body)
        return client.ok_or_error(status, payload)  # type: ignore[return-value]
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def issues_add_comment(repo: str, issue_number: int, body: str) -> Dict[str, Any]:
    """Add a comment to an issue."""
    try:
        owner, name = split_repo(repo)
        client = GitHubClient.from_env()
        status, payload = client.request(
            "POST",
            f"/repos/{owner}/{name}/issues/{issue_number}/comments",
            json_body={"body": body},
        )
        return client.ok_or_error(status, payload)  # type: ignore[return-value]
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def issues_list(repo: str, state: str = "open", labels: Optional[List[str]] = None, per_page: int = 30, page: int = 1) -> Any:
    """List issues for a repository."""
    try:
        owner, name = split_repo(repo)
        client = GitHubClient.from_env()
        params: Dict[str, Any] = {"state": state, "per_page": per_page, "page": page}
        if labels:
            params["labels"] = ",".join(labels)
        status, payload = client.request("GET", f"/repos/{owner}/{name}/issues", params=params)
        return client.ok_or_error(status, payload)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def issues_remove_label(repo: str, issue_number: int, label: str) -> Dict[str, Any]:
    """Remove a label from an issue."""
    try:
        owner, name = split_repo(repo)
        client = GitHubClient.from_env()
        status, payload = client.request("DELETE", f"/repos/{owner}/{name}/issues/{issue_number}/labels/{label}")
        return client.ok_or_error(status, payload)  # type: ignore[return-value]
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def milestones_list(repo: str, state: str = "open", per_page: int = 100, page: int = 1) -> Any:
    """List milestones for a repository."""
    try:
        owner, name = split_repo(repo)
        client = GitHubClient.from_env()
        status, payload = client.request(
            "GET",
            f"/repos/{owner}/{name}/milestones",
            params={"state": state, "per_page": per_page, "page": page},
        )
        return client.ok_or_error(status, payload)
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def labels_create(repo: str, name: str, color: str, description: str | None = None) -> Dict[str, Any]:
    """Create a label in a repository."""
    try:
        owner, r = split_repo(repo)
        client = GitHubClient.from_env()
        json_body: Dict[str, Any] = {"name": name, "color": color}
        if description is not None:
            json_body["description"] = description
        status, payload = client.request("POST", f"/repos/{owner}/{r}/labels", json_body=json_body)
        return client.ok_or_error(status, payload)  # type: ignore[return-value]
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def labels_update(repo: str, name: str, new_name: str | None = None, color: str | None = None, description: str | None = None) -> Dict[str, Any]:
    """Update a label."""
    try:
        owner, r = split_repo(repo)
        client = GitHubClient.from_env()
        json_body: Dict[str, Any] = {}
        if new_name is not None:
            json_body["new_name"] = new_name
        if color is not None:
            json_body["color"] = color
        if description is not None:
            json_body["description"] = description
        status, payload = client.request("PATCH", f"/repos/{owner}/{r}/labels/{name}", json_body=json_body)
        return client.ok_or_error(status, payload)  # type: ignore[return-value]
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def labels_delete(repo: str, name: str) -> Dict[str, Any]:
    """Delete a label."""
    try:
        owner, r = split_repo(repo)
        client = GitHubClient.from_env()
        status, payload = client.request("DELETE", f"/repos/{owner}/{r}/labels/{name}")
        return client.ok_or_error(status, payload)  # type: ignore[return-value]
    except Exception as e:
        return {"error": str(e)}
