"""
MCP tools for Jira Agile Boards and Sprints (Jira Software / Agile API).
Uses the /rest/agile/1.0 endpoint.
"""

import os
import requests
from requests.auth import HTTPBasicAuth
from typing import Any, Dict, List, Optional
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("jira-boards-sprints")

JIRA_BASE_URL = os.environ.get("JIRA_BASE_URL", "").rstrip("/")
JIRA_EMAIL = os.environ.get("JIRA_EMAIL", "")
JIRA_API_TOKEN = os.environ.get("JIRA_API_TOKEN", "")

AGILE_BASE = f"{JIRA_BASE_URL}/rest/agile/1.0"


def _agile_get(path: str, params: Optional[Dict[str, Any]] = None) -> Any:
    try:
        resp = requests.get(
            f"{AGILE_BASE}{path}",
            params=params,
            auth=HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN),
            headers={"Accept": "application/json"},
            timeout=30,
        )
        if not resp.ok:
            return {"error": resp.text, "status_code": resp.status_code}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def _agile_post(path: str, json: Optional[Any] = None) -> Any:
    try:
        resp = requests.post(
            f"{AGILE_BASE}{path}",
            json=json,
            auth=HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN),
            headers={"Accept": "application/json", "Content-Type": "application/json"},
            timeout=30,
        )
        if resp.status_code == 204:
            return {"status": "success"}
        if not resp.ok:
            return {"error": resp.text, "status_code": resp.status_code}
        if resp.text:
            return resp.json()
        return {"status": "success"}
    except Exception as e:
        return {"error": str(e)}


def _agile_put(path: str, json: Optional[Any] = None) -> Any:
    try:
        resp = requests.put(
            f"{AGILE_BASE}{path}",
            json=json,
            auth=HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN),
            headers={"Accept": "application/json", "Content-Type": "application/json"},
            timeout=30,
        )
        if resp.status_code == 204:
            return {"status": "success"}
        if not resp.ok:
            return {"error": resp.text, "status_code": resp.status_code}
        if resp.text:
            return resp.json()
        return {"status": "success"}
    except Exception as e:
        return {"error": str(e)}


def _agile_delete(path: str) -> Any:
    try:
        resp = requests.delete(
            f"{AGILE_BASE}{path}",
            auth=HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN),
            headers={"Accept": "application/json"},
            timeout=30,
        )
        if resp.status_code in (200, 204):
            return {"status": "success"}
        if not resp.ok:
            return {"error": resp.text, "status_code": resp.status_code}
        return {"status": "success"}
    except Exception as e:
        return {"error": str(e)}


# ── Boards ───────────────────────────────────────────────────────────────────

@mcp.tool()
def get_boards(
    start_at: int = 0,
    max_results: int = 50,
    type_: Optional[str] = None,
    name: Optional[str] = None,
    project_key_or_id: Optional[str] = None,
    account_id_location: Optional[str] = None,
    include_private: bool = False,
) -> Dict[str, Any]:
    """
    Get all Agile boards visible to the current user.

    Args:
        start_at: Index of the first result to return.
        max_results: Maximum number of results to return.
        type_: Filter by board type: 'scrum' or 'kanban'.
        name: Filter by board name (partial match).
        project_key_or_id: Filter by project key or ID.
        account_id_location: Filter by the account ID of the board location.
        include_private: Include private boards.
    """
    params: Dict[str, Any] = {
        "startAt": start_at,
        "maxResults": max_results,
        "includePrivate": include_private,
    }
    if type_:
        params["type"] = type_
    if name:
        params["name"] = name
    if project_key_or_id:
        params["projectKeyOrId"] = project_key_or_id
    if account_id_location:
        params["accountIdLocation"] = account_id_location
    return _agile_get("/board", params=params)


@mcp.tool()
def get_board(board_id: int) -> Dict[str, Any]:
    """
    Get details of a specific Agile board.

    Args:
        board_id: The board ID.
    """
    return _agile_get(f"/board/{board_id}")


@mcp.tool()
def create_board(
    name: str,
    type_: str,
    filter_id: int,
    location: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Create a new Agile board.

    Args:
        name: Board name.
        type_: Board type: 'scrum' or 'kanban'.
        filter_id: ID of the saved filter to use for the board.
        location: Location dict (e.g. {"type": "project", "projectKeyOrId": "PROJ"}).
    """
    body: Dict[str, Any] = {"name": name, "type": type_, "filterId": filter_id}
    if location:
        body["location"] = location
    return _agile_post("/board", json=body)


@mcp.tool()
def delete_board(board_id: int) -> Dict[str, Any]:
    """
    Delete an Agile board.

    Args:
        board_id: The board ID.
    """
    return _agile_delete(f"/board/{board_id}")


@mcp.tool()
def get_board_issues(
    board_id: int,
    start_at: int = 0,
    max_results: int = 50,
    jql: Optional[str] = None,
    fields: Optional[str] = None,
    expand: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Get issues on a board.

    Args:
        board_id: The board ID.
        start_at: Index of the first result to return.
        max_results: Maximum number of results to return.
        jql: Additional JQL to filter issues.
        fields: Comma-separated list of fields to include.
        expand: Comma-separated list of entities to expand.
    """
    params: Dict[str, Any] = {"startAt": start_at, "maxResults": max_results}
    if jql:
        params["jql"] = jql
    if fields:
        params["fields"] = fields
    if expand:
        params["expand"] = expand
    return _agile_get(f"/board/{board_id}/issue", params=params)


@mcp.tool()
def get_board_sprints(
    board_id: int,
    start_at: int = 0,
    max_results: int = 50,
    state: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Get sprints for a board.

    Args:
        board_id: The board ID.
        start_at: Index of the first result to return.
        max_results: Maximum number of results to return.
        state: Filter by sprint state: 'future', 'active', 'closed'.
    """
    params: Dict[str, Any] = {"startAt": start_at, "maxResults": max_results}
    if state:
        params["state"] = state
    return _agile_get(f"/board/{board_id}/sprint", params=params)


@mcp.tool()
def get_board_backlog(
    board_id: int,
    start_at: int = 0,
    max_results: int = 50,
    jql: Optional[str] = None,
    fields: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Get issues in the backlog of a board.

    Args:
        board_id: The board ID.
        start_at: Index of the first result to return.
        max_results: Maximum number of results to return.
        jql: Additional JQL to filter issues.
        fields: Comma-separated list of fields to include.
    """
    params: Dict[str, Any] = {"startAt": start_at, "maxResults": max_results}
    if jql:
        params["jql"] = jql
    if fields:
        params["fields"] = fields
    return _agile_get(f"/board/{board_id}/backlog", params=params)


@mcp.tool()
def get_board_epics(
    board_id: int,
    start_at: int = 0,
    max_results: int = 50,
    done: Optional[bool] = None,
) -> Dict[str, Any]:
    """
    Get epics on a board.

    Args:
        board_id: The board ID.
        start_at: Index of the first result to return.
        max_results: Maximum number of results to return.
        done: Filter by done status (True for done epics, False for active).
    """
    params: Dict[str, Any] = {"startAt": start_at, "maxResults": max_results}
    if done is not None:
        params["done"] = "true" if done else "false"
    return _agile_get(f"/board/{board_id}/epic", params=params)


# ── Sprints ──────────────────────────────────────────────────────────────────

@mcp.tool()
def get_sprint(sprint_id: int) -> Dict[str, Any]:
    """
    Get details of a specific sprint.

    Args:
        sprint_id: The sprint ID.
    """
    return _agile_get(f"/sprint/{sprint_id}")


@mcp.tool()
def create_sprint(
    name: str,
    board_id: int,
    goal: Optional[str] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Create a new sprint on a board.

    Args:
        name: Sprint name.
        board_id: The board ID to create the sprint on.
        goal: Sprint goal description.
        start_date: Sprint start date in ISO 8601 format (e.g. '2024-01-15T00:00:00.000Z').
        end_date: Sprint end date in ISO 8601 format.
    """
    body: Dict[str, Any] = {"name": name, "originBoardId": board_id}
    if goal:
        body["goal"] = goal
    if start_date:
        body["startDate"] = start_date
    if end_date:
        body["endDate"] = end_date
    return _agile_post("/sprint", json=body)


@mcp.tool()
def update_sprint(
    sprint_id: int,
    name: Optional[str] = None,
    state: Optional[str] = None,
    goal: Optional[str] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    complete_date: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Update a sprint (name, state, dates, goal).

    Args:
        sprint_id: The sprint ID.
        name: New sprint name.
        state: New sprint state: 'future', 'active', 'closed'.
        goal: New sprint goal.
        start_date: New start date in ISO 8601 format.
        end_date: New end date in ISO 8601 format.
        complete_date: Completion date in ISO 8601 format.
    """
    body: Dict[str, Any] = {}
    if name is not None:
        body["name"] = name
    if state is not None:
        body["state"] = state
    if goal is not None:
        body["goal"] = goal
    if start_date is not None:
        body["startDate"] = start_date
    if end_date is not None:
        body["endDate"] = end_date
    if complete_date is not None:
        body["completeDate"] = complete_date
    if not body:
        return {"error": "No fields provided to update."}
    return _agile_put(f"/sprint/{sprint_id}", json=body)


@mcp.tool()
def delete_sprint(sprint_id: int) -> Dict[str, Any]:
    """
    Delete a sprint. Only future sprints can be deleted.

    Args:
        sprint_id: The sprint ID.
    """
    return _agile_delete(f"/sprint/{sprint_id}")


@mcp.tool()
def get_sprint_issues(
    sprint_id: int,
    start_at: int = 0,
    max_results: int = 50,
    jql: Optional[str] = None,
    fields: Optional[str] = None,
    expand: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Get issues in a sprint.

    Args:
        sprint_id: The sprint ID.
        start_at: Index of the first result to return.
        max_results: Maximum number of results to return.
        jql: Additional JQL to filter issues.
        fields: Comma-separated list of fields to include.
        expand: Comma-separated list of entities to expand.
    """
    params: Dict[str, Any] = {"startAt": start_at, "maxResults": max_results}
    if jql:
        params["jql"] = jql
    if fields:
        params["fields"] = fields
    if expand:
        params["expand"] = expand
    return _agile_get(f"/sprint/{sprint_id}/issue", params=params)


@mcp.tool()
def move_issues_to_sprint(sprint_id: int, issue_keys: List[str]) -> Dict[str, Any]:
    """
    Move issues to a sprint.

    Args:
        sprint_id: The target sprint ID.
        issue_keys: List of issue keys to move (e.g. ['PROJ-1', 'PROJ-2']).
    """
    return _agile_post(f"/sprint/{sprint_id}/issue", json={"issues": issue_keys})


@mcp.tool()
def move_issues_to_backlog(board_id: int, issue_keys: List[str]) -> Dict[str, Any]:
    """
    Move issues to the backlog of a board.

    Args:
        board_id: The board ID.
        issue_keys: List of issue keys to move to the backlog.
    """
    return _agile_post(f"/board/{board_id}/issue", json={"issues": issue_keys})


@mcp.tool()
def start_sprint(sprint_id: int, start_date: str, end_date: str, goal: Optional[str] = None) -> Dict[str, Any]:
    """
    Start a sprint by transitioning it from 'future' to 'active'.

    Args:
        sprint_id: The sprint ID.
        start_date: Sprint start date in ISO 8601 format.
        end_date: Sprint end date in ISO 8601 format.
        goal: Optional sprint goal.
    """
    body: Dict[str, Any] = {"state": "active", "startDate": start_date, "endDate": end_date}
    if goal:
        body["goal"] = goal
    return _agile_put(f"/sprint/{sprint_id}", json=body)


@mcp.tool()
def close_sprint(sprint_id: int, complete_date: Optional[str] = None) -> Dict[str, Any]:
    """
    Close/complete an active sprint.

    Args:
        sprint_id: The sprint ID.
        complete_date: Completion date in ISO 8601 format. Defaults to now.
    """
    body: Dict[str, Any] = {"state": "closed"}
    if complete_date:
        body["completeDate"] = complete_date
    return _agile_put(f"/sprint/{sprint_id}", json=body)
