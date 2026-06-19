import os
import requests
from typing import Any, Dict, Optional

from mcp.server.fastmcp import FastMCP

BASE_URL = "https://api.clockify.me/api/v1"


def _headers() -> Dict[str, str]:
    api_key = os.getenv("CLOCKIFY_API_KEY")
    return {
        "X-Api-Key": api_key or "",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }


def _request(method: str, path: str, *, params: Optional[Dict[str, Any]] = None, json: Any = None) -> Any:
    api_key = os.getenv("CLOCKIFY_API_KEY")
    if not api_key:
        return {"error": "CLOCKIFY_API_KEY environment variable is not set"}

    url = f"{BASE_URL}{path}"
    try:
        resp = requests.request(method, url, headers=_headers(), params=params, json=json, timeout=30)
    except Exception as e:
        return {"error": f"Request failed: {e}"}

    if resp.status_code >= 400:
        try:
            data = resp.json()
        except Exception:
            data = resp.text
        return {"error": f"HTTP {resp.status_code}", "details": data, "url": url}

    if resp.status_code == 204:
        return {"ok": True}

    try:
        return resp.json()
    except Exception:
        return resp.text


mcp = FastMCP("clockify")


# Workspaces
@mcp.tool()
def list_workspaces() -> Any:
    """List workspaces accessible by the API key."""
    return _request("GET", "/workspaces")


@mcp.tool()
def get_workspace(workspace_id: str) -> Any:
    """Get workspace details."""
    return _request("GET", f"/workspaces/{workspace_id}")


# Users
@mcp.tool()
def get_current_user() -> Any:
    """Get current user (me)."""
    return _request("GET", "/user")


@mcp.tool()
def list_workspace_users(workspace_id: str, page: Optional[int] = None, page_size: Optional[int] = None) -> Any:
    """List users in a workspace."""
    params: Dict[str, Any] = {}
    if page is not None:
        params["page"] = page
    if page_size is not None:
        params["page-size"] = page_size
    return _request("GET", f"/workspaces/{workspace_id}/users", params=params or None)


# Projects
@mcp.tool()
def list_projects(
    workspace_id: str,
    name: Optional[str] = None,
    archived: Optional[bool] = None,
    page: Optional[int] = None,
    page_size: Optional[int] = None,
) -> Any:
    """List projects in a workspace."""
    params: Dict[str, Any] = {}
    if name is not None:
        params["name"] = name
    if archived is not None:
        params["archived"] = str(archived).lower()
    if page is not None:
        params["page"] = page
    if page_size is not None:
        params["page-size"] = page_size
    return _request("GET", f"/workspaces/{workspace_id}/projects", params=params or None)


@mcp.tool()
def create_project(
    workspace_id: str,
    name: str,
    client_id: Optional[str] = None,
    is_public: Optional[bool] = None,
    billable: Optional[bool] = None,
    color: Optional[str] = None,
    note: Optional[str] = None,
) -> Any:
    """Create a project in a workspace."""
    body: Dict[str, Any] = {"name": name}
    if client_id is not None:
        body["clientId"] = client_id
    if is_public is not None:
        body["isPublic"] = is_public
    if billable is not None:
        body["billable"] = billable
    if color is not None:
        body["color"] = color
    if note is not None:
        body["note"] = note
    return _request("POST", f"/workspaces/{workspace_id}/projects", json=body)


@mcp.tool()
def update_project(
    workspace_id: str,
    project_id: str,
    name: Optional[str] = None,
    client_id: Optional[str] = None,
    is_public: Optional[bool] = None,
    billable: Optional[bool] = None,
    color: Optional[str] = None,
    note: Optional[str] = None,
    archived: Optional[bool] = None,
) -> Any:
    """Update a project."""
    body: Dict[str, Any] = {}
    if name is not None:
        body["name"] = name
    if client_id is not None:
        body["clientId"] = client_id
    if is_public is not None:
        body["isPublic"] = is_public
    if billable is not None:
        body["billable"] = billable
    if color is not None:
        body["color"] = color
    if note is not None:
        body["note"] = note
    if archived is not None:
        body["archived"] = archived
    return _request("PUT", f"/workspaces/{workspace_id}/projects/{project_id}", json=body)


@mcp.tool()
def delete_project(workspace_id: str, project_id: str) -> Any:
    """Delete a project."""
    return _request("DELETE", f"/workspaces/{workspace_id}/projects/{project_id}")


# Clients
@mcp.tool()
def list_clients(workspace_id: str, name: Optional[str] = None, archived: Optional[bool] = None) -> Any:
    """List clients in a workspace."""
    params: Dict[str, Any] = {}
    if name is not None:
        params["name"] = name
    if archived is not None:
        params["archived"] = str(archived).lower()
    return _request("GET", f"/workspaces/{workspace_id}/clients", params=params or None)


@mcp.tool()
def create_client(workspace_id: str, name: str) -> Any:
    """Create a client."""
    return _request("POST", f"/workspaces/{workspace_id}/clients", json={"name": name})


# Tags
@mcp.tool()
def list_tags(workspace_id: str, name: Optional[str] = None, archived: Optional[bool] = None) -> Any:
    """List tags in a workspace."""
    params: Dict[str, Any] = {}
    if name is not None:
        params["name"] = name
    if archived is not None:
        params["archived"] = str(archived).lower()
    return _request("GET", f"/workspaces/{workspace_id}/tags", params=params or None)


@mcp.tool()
def create_tag(workspace_id: str, name: str) -> Any:
    """Create a tag."""
    return _request("POST", f"/workspaces/{workspace_id}/tags", json={"name": name})


# Tasks
@mcp.tool()
def list_tasks(
    workspace_id: str,
    project_id: str,
    name: Optional[str] = None,
    is_active: Optional[bool] = None,
) -> Any:
    """List tasks within a project."""
    params: Dict[str, Any] = {}
    if name is not None:
        params["name"] = name
    if is_active is not None:
        params["is-active"] = str(is_active).lower()
    return _request(
        "GET",
        f"/workspaces/{workspace_id}/projects/{project_id}/tasks",
        params=params or None,
    )


@mcp.tool()
def create_task(
    workspace_id: str,
    project_id: str,
    name: str,
    assignee_id: Optional[str] = None,
    estimate: Optional[str] = None,
) -> Any:
    """Create a task within a project."""
    body: Dict[str, Any] = {"name": name}
    if assignee_id is not None:
        body["assigneeId"] = assignee_id
    if estimate is not None:
        body["estimate"] = estimate
    return _request("POST", f"/workspaces/{workspace_id}/projects/{project_id}/tasks", json=body)


# Time entries
@mcp.tool()
def list_time_entries(
    workspace_id: str,
    user_id: Optional[str] = None,
    description: Optional[str] = None,
    project_id: Optional[str] = None,
    start: Optional[str] = None,
    end: Optional[str] = None,
    page: Optional[int] = None,
    page_size: Optional[int] = None,
    in_progress: Optional[bool] = None,
) -> Any:
    """List time entries in a workspace.

    Notes:
      - start/end should be ISO-8601 timestamps.
      - If user_id is provided, uses /user/{userId}/time-entries endpoint.
    """
    params: Dict[str, Any] = {}
    if description is not None:
        params["description"] = description
    if project_id is not None:
        params["project"] = project_id
    if start is not None:
        params["start"] = start
    if end is not None:
        params["end"] = end
    if page is not None:
        params["page"] = page
    if page_size is not None:
        params["page-size"] = page_size
    if in_progress is not None:
        params["in-progress"] = str(in_progress).lower()

    if user_id:
        return _request("GET", f"/workspaces/{workspace_id}/user/{user_id}/time-entries", params=params or None)
    return _request("GET", f"/workspaces/{workspace_id}/time-entries", params=params or None)


@mcp.tool()
def create_time_entry(
    workspace_id: str,
    start: str,
    description: Optional[str] = None,
    end: Optional[str] = None,
    project_id: Optional[str] = None,
    task_id: Optional[str] = None,
    tag_ids: Optional[list] = None,
    billable: Optional[bool] = None,
) -> Any:
    """Create a time entry.

    Provide start (ISO-8601). Provide end to create a finished entry; omit end to start a running timer.
    """
    body: Dict[str, Any] = {
        "start": start,
    }
    if end is not None:
        body["end"] = end
    if description is not None:
        body["description"] = description
    if project_id is not None:
        body["projectId"] = project_id
    if task_id is not None:
        body["taskId"] = task_id
    if tag_ids is not None:
        body["tagIds"] = tag_ids
    if billable is not None:
        body["billable"] = billable
    return _request("POST", f"/workspaces/{workspace_id}/time-entries", json=body)


@mcp.tool()
def update_time_entry(
    workspace_id: str,
    time_entry_id: str,
    start: Optional[str] = None,
    end: Optional[str] = None,
    description: Optional[str] = None,
    project_id: Optional[str] = None,
    task_id: Optional[str] = None,
    tag_ids: Optional[list] = None,
    billable: Optional[bool] = None,
) -> Any:
    """Update a time entry."""
    body: Dict[str, Any] = {}
    if start is not None:
        body["start"] = start
    if end is not None:
        body["end"] = end
    if description is not None:
        body["description"] = description
    if project_id is not None:
        body["projectId"] = project_id
    if task_id is not None:
        body["taskId"] = task_id
    if tag_ids is not None:
        body["tagIds"] = tag_ids
    if billable is not None:
        body["billable"] = billable
    return _request("PUT", f"/workspaces/{workspace_id}/time-entries/{time_entry_id}", json=body)


@mcp.tool()
def delete_time_entry(workspace_id: str, time_entry_id: str) -> Any:
    """Delete a time entry."""
    return _request("DELETE", f"/workspaces/{workspace_id}/time-entries/{time_entry_id}")


@mcp.tool()
def stop_running_timer(workspace_id: str, user_id: str, end: Optional[str] = None) -> Any:
    """Stop the currently running timer for a user.

    If end is omitted, Clockify will set end to now.
    """
    body: Dict[str, Any] = {}
    if end is not None:
        body["end"] = end
    return _request("PATCH", f"/workspaces/{workspace_id}/user/{user_id}/time-entries", json=body or None)


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
