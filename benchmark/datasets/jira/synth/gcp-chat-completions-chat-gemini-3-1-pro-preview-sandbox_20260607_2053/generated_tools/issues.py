import json
from typing import Any, Dict, List, Optional
from server import mcp, make_request

@mcp.tool()
def get_issue(issue_id_or_key: str, expand: Optional[str] = None, fields: Optional[str] = None) -> Dict[str, Any]:
    """
    Returns the details for an issue.
    """
    params = {}
    if expand:
        params["expand"] = expand
    if fields:
        params["fields"] = fields
    return make_request("GET", f"/issue/{issue_id_or_key}", params=params)

@mcp.tool()
def create_issue(fields: Dict[str, Any], update: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Creates an issue or a subtask.
    """
    payload = {"fields": fields}
    if update:
        payload["update"] = update
    return make_request("POST", "/issue", json=payload)

@mcp.tool()
def edit_issue(issue_id_or_key: str, fields: Optional[Dict[str, Any]] = None, update: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Edits an issue.
    """
    payload = {}
    if fields:
        payload["fields"] = fields
    if update:
        payload["update"] = update
    return make_request("PUT", f"/issue/{issue_id_or_key}", json=payload)

@mcp.tool()
def delete_issue(issue_id_or_key: str, delete_subtasks: str = "false") -> Dict[str, Any]:
    """
    Deletes an issue.
    """
    return make_request("DELETE", f"/issue/{issue_id_or_key}", params={"deleteSubtasks": delete_subtasks})

@mcp.tool()
def assign_issue(issue_id_or_key: str, account_id: Optional[str]) -> Dict[str, Any]:
    """
    Assigns an issue to a user. Use account_id=None to unassign.
    """
    payload = {"accountId": account_id} if account_id else {"accountId": None}
    return make_request("PUT", f"/issue/{issue_id_or_key}/assignee", json=payload)

@mcp.tool()
def get_transitions(issue_id_or_key: str) -> Dict[str, Any]:
    """
    Returns either all transitions or a transition that can be performed by the user on an issue.
    """
    return make_request("GET", f"/issue/{issue_id_or_key}/transitions")

@mcp.tool()
def transition_issue(issue_id_or_key: str, transition_id: str, fields: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Performs an issue transition and, optionally, updates the issue's fields.
    """
    payload = {"transition": {"id": transition_id}}
    if fields:
        payload["fields"] = fields
    return make_request("POST", f"/issue/{issue_id_or_key}/transitions", json=payload)
