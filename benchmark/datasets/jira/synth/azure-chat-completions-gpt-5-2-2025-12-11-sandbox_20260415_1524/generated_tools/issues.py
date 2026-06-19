from typing import Any, Dict, Optional

from .jira_client import JiraClient, clean_params


def issue_create(fields: Dict[str, Any], update: Optional[Dict[str, Any]] = None, update_history: Optional[bool] = None) -> Dict[str, Any]:
    """POST /issue - Create an issue.

    fields: Jira issue fields payload.
    update: optional update object.
    update_history: optional query param updateHistory.
    """
    client = JiraClient()
    params = clean_params({"updateHistory": update_history})
    body: Dict[str, Any] = {"fields": fields}
    if update is not None:
        body["update"] = update
    return client.request("POST", "/issue", params=params, json_body=body)  # type: ignore[return-value]


def issue_get(issue_id_or_key: str, fields: Optional[str] = None, expand: Optional[str] = None, properties: Optional[str] = None) -> Dict[str, Any]:
    """GET /issue/{issueIdOrKey} - Get issue details."""
    client = JiraClient()
    params = clean_params({"fields": fields, "expand": expand, "properties": properties})
    return client.request("GET", f"/issue/{issue_id_or_key}", params=params)  # type: ignore[return-value]


def issue_update(issue_id_or_key: str, fields: Optional[Dict[str, Any]] = None, update: Optional[Dict[str, Any]] = None, notify_users: Optional[bool] = None) -> Dict[str, Any]:
    """PUT /issue/{issueIdOrKey} - Update issue fields."""
    client = JiraClient()
    params = clean_params({"notifyUsers": notify_users})
    body: Dict[str, Any] = {}
    if fields is not None:
        body["fields"] = fields
    if update is not None:
        body["update"] = update
    return client.request("PUT", f"/issue/{issue_id_or_key}", params=params, json_body=body)  # type: ignore[return-value]


def issue_delete(issue_id_or_key: str, delete_subtasks: Optional[bool] = None) -> Dict[str, Any]:
    """DELETE /issue/{issueIdOrKey} - Delete issue."""
    client = JiraClient()
    params = clean_params({"deleteSubtasks": delete_subtasks})
    return client.request("DELETE", f"/issue/{issue_id_or_key}", params=params)  # type: ignore[return-value]


def issue_assign(issue_id_or_key: str, account_id: Optional[str] = None) -> Dict[str, Any]:
    """PUT /issue/{issueIdOrKey}/assignee - Assign issue.

    account_id: Atlassian accountId. Use None to unassign.
    """
    client = JiraClient()
    body = {"accountId": account_id}
    return client.request("PUT", f"/issue/{issue_id_or_key}/assignee", json_body=body)  # type: ignore[return-value]


def issue_transitions_get(issue_id_or_key: str, expand: Optional[str] = None, transition_id: Optional[str] = None, skip_remote_only_condition: Optional[bool] = None) -> Dict[str, Any]:
    """GET /issue/{issueIdOrKey}/transitions - Get available transitions."""
    client = JiraClient()
    params = clean_params({"expand": expand, "transitionId": transition_id, "skipRemoteOnlyCondition": skip_remote_only_condition})
    return client.request("GET", f"/issue/{issue_id_or_key}/transitions", params=params)  # type: ignore[return-value]


def issue_transition(issue_id_or_key: str, transition: Dict[str, Any], fields: Optional[Dict[str, Any]] = None, update: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """POST /issue/{issueIdOrKey}/transitions - Perform a transition."""
    client = JiraClient()
    body: Dict[str, Any] = {"transition": transition}
    if fields is not None:
        body["fields"] = fields
    if update is not None:
        body["update"] = update
    return client.request("POST", f"/issue/{issue_id_or_key}/transitions", json_body=body)  # type: ignore[return-value]


def issue_changelog_get(issue_id_or_key: str, start_at: Optional[int] = None, max_results: Optional[int] = None) -> Dict[str, Any]:
    """GET /issue/{issueIdOrKey}/changelog - Get issue changelog."""
    client = JiraClient()
    params = clean_params({"startAt": start_at, "maxResults": max_results})
    return client.request("GET", f"/issue/{issue_id_or_key}/changelog", params=params)  # type: ignore[return-value]


def issue_createmeta(project_id_or_key: Optional[str] = None, issuetype_ids: Optional[str] = None, expand: Optional[str] = None) -> Dict[str, Any]:
    """GET /issue/createmeta - Get create issue metadata."""
    client = JiraClient()
    params = clean_params({"projectIdsOrKeys": project_id_or_key, "issuetypeIds": issuetype_ids, "expand": expand})
    return client.request("GET", "/issue/createmeta", params=params)  # type: ignore[return-value]
