from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .jira_client import JiraClient


@mcp.tool()
def jira_get_transitions(issue_id_or_key: str, expand: Optional[str] = None, transition_id: Optional[str] = None) -> Dict[str, Any]:
    """Get available transitions for an issue.

    GET /rest/api/3/issue/{issueIdOrKey}/transitions
    """

    client = JiraClient()
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    if transition_id:
        params["transitionId"] = transition_id
    return client.request("GET", f"/issue/{issue_id_or_key}/transitions", params=params)


@mcp.tool()
def jira_transition_issue(
    issue_id_or_key: str,
    transition_id: str,
    fields: Optional[Dict[str, Any]] = None,
    update: Optional[Dict[str, Any]] = None,
    history_metadata: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Perform a workflow transition on an issue.

    POST /rest/api/3/issue/{issueIdOrKey}/transitions

    Returns {"ok": true} on success.
    """

    client = JiraClient()
    payload: Dict[str, Any] = {"transition": {"id": transition_id}}
    if fields is not None:
        payload["fields"] = fields
    if update is not None:
        payload["update"] = update
    if history_metadata is not None:
        payload["historyMetadata"] = history_metadata
    return client.request("POST", f"/issue/{issue_id_or_key}/transitions", json=payload)
