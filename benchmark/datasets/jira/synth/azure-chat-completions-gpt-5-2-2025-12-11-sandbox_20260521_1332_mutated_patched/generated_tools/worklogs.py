from typing import Any, Dict, List, Optional

from .jira_client import JiraClient


def list_worklogs(
    issueIdOrKey: str,
    *,
    startAt: int = 0,
    maxResults: int = 50,
    startedAfter: Optional[int] = None,
    startedBefore: Optional[int] = None,
    expand: Optional[str] = None,
) -> Any:
    """GET /rest/api/3/issue/{issueIdOrKey}/worklog"""
    client = JiraClient()
    params: Dict[str, Any] = {"startAt": startAt, "maxResults": maxResults}
    if startedAfter is not None:
        params["startedAfter"] = startedAfter
    if startedBefore is not None:
        params["startedBefore"] = startedBefore
    if expand is not None:
        params["expand"] = expand
    return client.request("GET", f"/issue/{issueIdOrKey}/worklog", params=params)


def add_worklog(
    issueIdOrKey: str,
    *,
    timeSpentSeconds: Optional[int] = None,
    timeSpent: Optional[str] = None,
    started: Optional[str] = None,
    comment: Optional[Dict[str, Any]] = None,
    visibility: Optional[Dict[str, Any]] = None,
    properties: Optional[List[Dict[str, Any]]] = None,
    notifyUsers: Optional[bool] = None,
    adjustEstimate: Optional[str] = None,
    newEstimate: Optional[str] = None,
    reduceBy: Optional[str] = None,
    expand: Optional[str] = None,
    overrideEditableFlag: Optional[bool] = None,
) -> Any:
    """POST /rest/api/3/issue/{issueIdOrKey}/worklog"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if notifyUsers is not None:
        params["notifyUsers"] = str(notifyUsers).lower()
    if adjustEstimate is not None:
        params["adjustEstimate"] = adjustEstimate
    if newEstimate is not None:
        params["newEstimate"] = newEstimate
    if reduceBy is not None:
        params["reduceBy"] = reduceBy
    if expand is not None:
        params["expand"] = expand
    if overrideEditableFlag is not None:
        params["overrideEditableFlag"] = str(overrideEditableFlag).lower()

    body: Dict[str, Any] = {}
    if comment is not None:
        body["comment"] = comment
    if started is not None:
        body["started"] = started
    if timeSpent is not None:
        body["timeSpent"] = timeSpent
    if timeSpentSeconds is not None:
        body["timeSpentSeconds"] = timeSpentSeconds
    if visibility is not None:
        body["visibility"] = visibility
    if properties is not None:
        body["properties"] = properties

    return client.request("POST", f"/issue/{issueIdOrKey}/worklog", params=params or None, json_body=body)


def get_worklog(issueIdOrKey: str, worklogId: str, *, expand: Optional[str] = None) -> Any:
    """GET /rest/api/3/issue/{issueIdOrKey}/worklog/{id}"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    return client.request("GET", f"/issue/{issueIdOrKey}/worklog/{worklogId}", params=params or None)


def update_worklog(
    issueIdOrKey: str,
    worklogId: str,
    *,
    comment: Optional[Dict[str, Any]] = None,
    started: Optional[str] = None,
    timeSpent: Optional[str] = None,
    timeSpentSeconds: Optional[int] = None,
    visibility: Optional[Dict[str, Any]] = None,
    properties: Optional[List[Dict[str, Any]]] = None,
    notifyUsers: Optional[bool] = None,
    adjustEstimate: Optional[str] = None,
    newEstimate: Optional[str] = None,
    expand: Optional[str] = None,
    overrideEditableFlag: Optional[bool] = None,
) -> Any:
    """PUT /rest/api/3/issue/{issueIdOrKey}/worklog/{id}"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if notifyUsers is not None:
        params["notifyUsers"] = str(notifyUsers).lower()
    if adjustEstimate is not None:
        params["adjustEstimate"] = adjustEstimate
    if newEstimate is not None:
        params["newEstimate"] = newEstimate
    if expand is not None:
        params["expand"] = expand
    if overrideEditableFlag is not None:
        params["overrideEditableFlag"] = str(overrideEditableFlag).lower()

    body: Dict[str, Any] = {}
    if comment is not None:
        body["comment"] = comment
    if started is not None:
        body["started"] = started
    if timeSpent is not None:
        body["timeSpent"] = timeSpent
    if timeSpentSeconds is not None:
        body["timeSpentSeconds"] = timeSpentSeconds
    if visibility is not None:
        body["visibility"] = visibility
    if properties is not None:
        body["properties"] = properties

    return client.request("PUT", f"/issue/{issueIdOrKey}/worklog/{worklogId}", params=params or None, json_body=body)


def delete_worklog(
    issueIdOrKey: str,
    worklogId: str,
    *,
    notifyUsers: Optional[bool] = None,
    adjustEstimate: Optional[str] = None,
    newEstimate: Optional[str] = None,
    increaseBy: Optional[str] = None,
    overrideEditableFlag: Optional[bool] = None,
) -> Any:
    """DEL /rest/api/3/issue/{issueIdOrKey}/worklog/{id}"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if notifyUsers is not None:
        params["notifyUsers"] = str(notifyUsers).lower()
    if adjustEstimate is not None:
        params["adjustEstimate"] = adjustEstimate
    if newEstimate is not None:
        params["newEstimate"] = newEstimate
    if increaseBy is not None:
        params["increaseBy"] = increaseBy
    if overrideEditableFlag is not None:
        params["overrideEditableFlag"] = str(overrideEditableFlag).lower()
    return client.request("DELETE", f"/issue/{issueIdOrKey}/worklog/{worklogId}", params=params or None)
