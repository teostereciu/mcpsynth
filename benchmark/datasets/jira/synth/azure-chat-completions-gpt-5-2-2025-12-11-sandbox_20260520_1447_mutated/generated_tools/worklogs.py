from typing import Any, Dict, List, Optional

from .jira_client import JiraClient


def get_issue_worklogs(issueIdOrKey: str, start_index: int = 0, page_size: int = 50, startedAfter: Optional[int] = None, startedBefore: Optional[int] = None, expand: Optional[str] = None):
    """GET /issue/{issueIdOrKey}/worklog"""
    client = JiraClient()
    params: Dict[str, Any] = {"start_index": start_index, "page_size": page_size}
    if startedAfter is not None:
        params["startedAfter"] = startedAfter
    if startedBefore is not None:
        params["startedBefore"] = startedBefore
    if expand is not None:
        params["expand"] = expand
    return client.request("GET", f"/issue/{issueIdOrKey}/worklog", params=params)


def add_worklog(issueIdOrKey: str, timeSpentSeconds: Optional[int] = None, timeSpent: Optional[str] = None, started: Optional[str] = None, comment: Any = None, visibility: Optional[Dict[str, Any]] = None, notifyUsers: Optional[bool] = None, adjustEstimate: Optional[str] = None, newEstimate: Optional[str] = None, reduceBy: Optional[str] = None, overrideEditableFlag: Optional[bool] = None, expand: Optional[str] = None):
    """POST /issue/{issueIdOrKey}/worklog"""
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
    if overrideEditableFlag is not None:
        params["overrideEditableFlag"] = str(overrideEditableFlag).lower()
    if expand is not None:
        params["expand"] = expand

    body: Dict[str, Any] = {}
    if comment is not None:
        body["comment"] = comment
    if started is not None:
        body["started"] = started
    if timeSpentSeconds is not None:
        body["timeSpentSeconds"] = timeSpentSeconds
    if timeSpent is not None:
        body["timeSpent"] = timeSpent
    if visibility is not None:
        body["visibility"] = visibility

    return client.request("POST", f"/issue/{issueIdOrKey}/worklog", params=params or None, json=body)


def get_worklog(issueIdOrKey: str, id: str, expand: Optional[str] = None):
    """GET /issue/{issueIdOrKey}/worklog/{id}"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    return client.request("GET", f"/issue/{issueIdOrKey}/worklog/{id}", params=params or None)


def update_worklog(issueIdOrKey: str, id: str, payload: Dict[str, Any], notifyUsers: Optional[bool] = None, adjustEstimate: Optional[str] = None, newEstimate: Optional[str] = None, overrideEditableFlag: Optional[bool] = None, expand: Optional[str] = None):
    """PUT /issue/{issueIdOrKey}/worklog/{id}"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if notifyUsers is not None:
        params["notifyUsers"] = str(notifyUsers).lower()
    if adjustEstimate is not None:
        params["adjustEstimate"] = adjustEstimate
    if newEstimate is not None:
        params["newEstimate"] = newEstimate
    if overrideEditableFlag is not None:
        params["overrideEditableFlag"] = str(overrideEditableFlag).lower()
    if expand is not None:
        params["expand"] = expand
    return client.request("PUT", f"/issue/{issueIdOrKey}/worklog/{id}", params=params or None, json=payload)


def delete_worklog(issueIdOrKey: str, id: str, notifyUsers: Optional[bool] = None, adjustEstimate: Optional[str] = None, newEstimate: Optional[str] = None, increaseBy: Optional[str] = None, overrideEditableFlag: Optional[bool] = None):
    """DELETE /issue/{issueIdOrKey}/worklog/{id}"""
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
    return client.request("DELETE", f"/issue/{issueIdOrKey}/worklog/{id}", params=params or None)
