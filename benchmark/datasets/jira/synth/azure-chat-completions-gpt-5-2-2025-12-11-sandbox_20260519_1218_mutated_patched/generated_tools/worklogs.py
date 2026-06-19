from typing import Any, Dict, List, Optional

from ._client import JiraClient


def get_worklogs(
    client: JiraClient,
    issue_id_or_key: str,
    *,
    start_at: Optional[int] = None,
    max_results: Optional[int] = None,
    started_after: Optional[int] = None,
    started_before: Optional[int] = None,
    expand: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {}
    if start_at is not None:
        params["startAt"] = start_at
    if max_results is not None:
        params["maxResults"] = max_results
    if started_after is not None:
        params["startedAfter"] = started_after
    if started_before is not None:
        params["startedBefore"] = started_before
    if expand is not None:
        params["expand"] = expand
    return client.request("GET", f"/issue/{issue_id_or_key}/worklog", params=params or None)


def add_worklog(
    client: JiraClient,
    issue_id_or_key: str,
    *,
    time_spent: Optional[str] = None,
    time_spent_seconds: Optional[int] = None,
    started: Optional[str] = None,
    comment: Any = None,
    visibility: Optional[Dict[str, Any]] = None,
    properties: Optional[List[Dict[str, Any]]] = None,
    notify_users: Optional[bool] = None,
    adjust_estimate: Optional[str] = None,
    new_estimate: Optional[str] = None,
    reduce_by: Optional[str] = None,
    expand: Optional[str] = None,
    override_editable_flag: Optional[bool] = None,
) -> Any:
    params: Dict[str, Any] = {}
    if notify_users is not None:
        params["notifyUsers"] = str(notify_users).lower()
    if adjust_estimate is not None:
        params["adjustEstimate"] = adjust_estimate
    if new_estimate is not None:
        params["newEstimate"] = new_estimate
    if reduce_by is not None:
        params["reduceBy"] = reduce_by
    if expand is not None:
        params["expand"] = expand
    if override_editable_flag is not None:
        params["overrideEditableFlag"] = str(override_editable_flag).lower()

    body: Dict[str, Any] = {}
    if time_spent is not None:
        body["timeSpent"] = time_spent
    if time_spent_seconds is not None:
        body["timeSpentSeconds"] = time_spent_seconds
    if started is not None:
        body["started"] = started
    if comment is not None:
        body["comment"] = comment
    if visibility is not None:
        body["visibility"] = visibility
    if properties is not None:
        body["properties"] = properties

    return client.request("POST", f"/issue/{issue_id_or_key}/worklog", params=params or None, json=body)


def get_worklog(
    client: JiraClient,
    issue_id_or_key: str,
    worklog_id: str,
    *,
    expand: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    return client.request("GET", f"/issue/{issue_id_or_key}/worklog/{worklog_id}", params=params or None)


def update_worklog(
    client: JiraClient,
    issue_id_or_key: str,
    worklog_id: str,
    *,
    time_spent: Optional[str] = None,
    time_spent_seconds: Optional[int] = None,
    started: Optional[str] = None,
    comment: Any = None,
    visibility: Optional[Dict[str, Any]] = None,
    properties: Optional[List[Dict[str, Any]]] = None,
    notify_users: Optional[bool] = None,
    adjust_estimate: Optional[str] = None,
    new_estimate: Optional[str] = None,
    expand: Optional[str] = None,
    override_editable_flag: Optional[bool] = None,
) -> Any:
    params: Dict[str, Any] = {}
    if notify_users is not None:
        params["notifyUsers"] = str(notify_users).lower()
    if adjust_estimate is not None:
        params["adjustEstimate"] = adjust_estimate
    if new_estimate is not None:
        params["newEstimate"] = new_estimate
    if expand is not None:
        params["expand"] = expand
    if override_editable_flag is not None:
        params["overrideEditableFlag"] = str(override_editable_flag).lower()

    body: Dict[str, Any] = {}
    if time_spent is not None:
        body["timeSpent"] = time_spent
    if time_spent_seconds is not None:
        body["timeSpentSeconds"] = time_spent_seconds
    if started is not None:
        body["started"] = started
    if comment is not None:
        body["comment"] = comment
    if visibility is not None:
        body["visibility"] = visibility
    if properties is not None:
        body["properties"] = properties

    return client.request("PUT", f"/issue/{issue_id_or_key}/worklog/{worklog_id}", params=params or None, json=body)


def delete_worklog(
    client: JiraClient,
    issue_id_or_key: str,
    worklog_id: str,
    *,
    notify_users: Optional[bool] = None,
    adjust_estimate: Optional[str] = None,
    new_estimate: Optional[str] = None,
    increase_by: Optional[str] = None,
    override_editable_flag: Optional[bool] = None,
) -> Any:
    params: Dict[str, Any] = {}
    if notify_users is not None:
        params["notifyUsers"] = str(notify_users).lower()
    if adjust_estimate is not None:
        params["adjustEstimate"] = adjust_estimate
    if new_estimate is not None:
        params["newEstimate"] = new_estimate
    if increase_by is not None:
        params["increaseBy"] = increase_by
    if override_editable_flag is not None:
        params["overrideEditableFlag"] = str(override_editable_flag).lower()

    return client.request("DELETE", f"/issue/{issue_id_or_key}/worklog/{worklog_id}", params=params or None)


def bulk_delete_worklogs(
    client: JiraClient,
    issue_id_or_key: str,
    ids: List[int],
    *,
    adjust_estimate: Optional[str] = None,
    override_editable_flag: Optional[bool] = None,
) -> Any:
    params: Dict[str, Any] = {}
    if adjust_estimate is not None:
        params["adjustEstimate"] = adjust_estimate
    if override_editable_flag is not None:
        params["overrideEditableFlag"] = str(override_editable_flag).lower()
    return client.request("DELETE", f"/issue/{issue_id_or_key}/worklog", params=params or None, json={"ids": ids})


def bulk_move_worklogs(
    client: JiraClient,
    issue_id_or_key: str,
    ids: List[int],
    destination_issue_id_or_key: str,
    *,
    adjust_estimate: Optional[str] = None,
    override_editable_flag: Optional[bool] = None,
) -> Any:
    params: Dict[str, Any] = {}
    if adjust_estimate is not None:
        params["adjustEstimate"] = adjust_estimate
    if override_editable_flag is not None:
        params["overrideEditableFlag"] = str(override_editable_flag).lower()
    return client.request(
        "POST",
        f"/issue/{issue_id_or_key}/worklog/move",
        params=params or None,
        json={"ids": ids, "issueIdOrKey": destination_issue_id_or_key},
    )
