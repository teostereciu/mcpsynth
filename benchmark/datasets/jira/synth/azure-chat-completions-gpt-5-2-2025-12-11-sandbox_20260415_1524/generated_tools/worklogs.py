from typing import Any, Dict, List, Optional

from .jira_client import JiraClient, clean_params


def issue_worklogs_get(
    issue_id_or_key: str,
    start_at: Optional[int] = None,
    max_results: Optional[int] = None,
    started_after: Optional[int] = None,
    started_before: Optional[int] = None,
    expand: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /issue/{issueIdOrKey}/worklog - Get worklogs for an issue."""
    client = JiraClient()
    params = clean_params(
        {
            "startAt": start_at,
            "maxResults": max_results,
            "startedAfter": started_after,
            "startedBefore": started_before,
            "expand": expand,
        }
    )
    return client.request("GET", f"/issue/{issue_id_or_key}/worklog", params=params)  # type: ignore[return-value]


def issue_worklog_add(
    issue_id_or_key: str,
    time_spent: Optional[str] = None,
    time_spent_seconds: Optional[int] = None,
    started: Optional[str] = None,
    comment: Optional[Any] = None,
    visibility: Optional[Dict[str, Any]] = None,
    notify_users: Optional[bool] = None,
    adjust_estimate: Optional[str] = None,
    new_estimate: Optional[str] = None,
    reduce_by: Optional[str] = None,
    expand: Optional[str] = None,
    override_editable_flag: Optional[bool] = None,
    properties: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    """POST /issue/{issueIdOrKey}/worklog - Add a worklog."""
    client = JiraClient()
    params = clean_params(
        {
            "notifyUsers": notify_users,
            "adjustEstimate": adjust_estimate,
            "newEstimate": new_estimate,
            "reduceBy": reduce_by,
            "expand": expand,
            "overrideEditableFlag": override_editable_flag,
        }
    )
    payload: Dict[str, Any] = {}
    if time_spent is not None:
        payload["timeSpent"] = time_spent
    if time_spent_seconds is not None:
        payload["timeSpentSeconds"] = time_spent_seconds
    if started is not None:
        payload["started"] = started
    if comment is not None:
        payload["comment"] = comment
    if visibility is not None:
        payload["visibility"] = visibility
    if properties is not None:
        payload["properties"] = properties
    return client.request("POST", f"/issue/{issue_id_or_key}/worklog", params=params, json_body=payload)  # type: ignore[return-value]


def issue_worklog_get(issue_id_or_key: str, worklog_id: str, expand: Optional[str] = None) -> Dict[str, Any]:
    """GET /issue/{issueIdOrKey}/worklog/{id} - Get a worklog."""
    client = JiraClient()
    params = clean_params({"expand": expand})
    return client.request("GET", f"/issue/{issue_id_or_key}/worklog/{worklog_id}", params=params)  # type: ignore[return-value]


def issue_worklog_update(
    issue_id_or_key: str,
    worklog_id: str,
    time_spent: Optional[str] = None,
    time_spent_seconds: Optional[int] = None,
    started: Optional[str] = None,
    comment: Optional[Any] = None,
    visibility: Optional[Dict[str, Any]] = None,
    notify_users: Optional[bool] = None,
    adjust_estimate: Optional[str] = None,
    new_estimate: Optional[str] = None,
    expand: Optional[str] = None,
    override_editable_flag: Optional[bool] = None,
    properties: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    """PUT /issue/{issueIdOrKey}/worklog/{id} - Update a worklog."""
    client = JiraClient()
    params = clean_params(
        {
            "notifyUsers": notify_users,
            "adjustEstimate": adjust_estimate,
            "newEstimate": new_estimate,
            "expand": expand,
            "overrideEditableFlag": override_editable_flag,
        }
    )
    payload: Dict[str, Any] = {}
    if time_spent is not None:
        payload["timeSpent"] = time_spent
    if time_spent_seconds is not None:
        payload["timeSpentSeconds"] = time_spent_seconds
    if started is not None:
        payload["started"] = started
    if comment is not None:
        payload["comment"] = comment
    if visibility is not None:
        payload["visibility"] = visibility
    if properties is not None:
        payload["properties"] = properties
    return client.request("PUT", f"/issue/{issue_id_or_key}/worklog/{worklog_id}", params=params, json_body=payload)  # type: ignore[return-value]


def issue_worklog_delete(
    issue_id_or_key: str,
    worklog_id: str,
    notify_users: Optional[bool] = None,
    adjust_estimate: Optional[str] = None,
    new_estimate: Optional[str] = None,
    increase_by: Optional[str] = None,
    override_editable_flag: Optional[bool] = None,
) -> Dict[str, Any]:
    """DELETE /issue/{issueIdOrKey}/worklog/{id} - Delete a worklog."""
    client = JiraClient()
    params = clean_params(
        {
            "notifyUsers": notify_users,
            "adjustEstimate": adjust_estimate,
            "newEstimate": new_estimate,
            "increaseBy": increase_by,
            "overrideEditableFlag": override_editable_flag,
        }
    )
    return client.request("DELETE", f"/issue/{issue_id_or_key}/worklog/{worklog_id}", params=params)  # type: ignore[return-value]


def issue_worklogs_bulk_delete(
    issue_id_or_key: str,
    ids: List[int],
    adjust_estimate: Optional[str] = None,
    override_editable_flag: Optional[bool] = None,
) -> Dict[str, Any]:
    """DELETE /issue/{issueIdOrKey}/worklog - Bulk delete worklogs."""
    client = JiraClient()
    params = clean_params({"adjustEstimate": adjust_estimate, "overrideEditableFlag": override_editable_flag})
    return client.request("DELETE", f"/issue/{issue_id_or_key}/worklog", params=params, json_body={"ids": ids})  # type: ignore[return-value]
