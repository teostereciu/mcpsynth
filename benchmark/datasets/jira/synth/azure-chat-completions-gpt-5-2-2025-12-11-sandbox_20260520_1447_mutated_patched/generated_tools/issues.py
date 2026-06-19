from typing import Any, Dict, Optional, Union, List

from .jira_client import JiraClient


def create_issue(fields: Dict[str, Any], update: Optional[Dict[str, Any]] = None, updateHistory: Optional[bool] = None):
    """POST /issue"""
    client = JiraClient()
    params = {}
    if updateHistory is not None:
        params["updateHistory"] = str(updateHistory).lower()
    body: Dict[str, Any] = {"fields": fields}
    if update is not None:
        body["update"] = update
    return client.request("POST", "/issue", params=params or None, json=body)


def get_issue(issueIdOrKey: str, fields: Optional[str] = None, expand: Optional[str] = None, properties: Optional[str] = None, fieldsByKeys: Optional[bool] = None):
    """GET /issue/{issueIdOrKey}"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if fields is not None:
        params["fields"] = fields
    if expand is not None:
        params["expand"] = expand
    if properties is not None:
        params["properties"] = properties
    if fieldsByKeys is not None:
        params["fieldsByKeys"] = str(fieldsByKeys).lower()
    return client.request("GET", f"/issue/{issueIdOrKey}", params=params or None)


def update_issue(issueIdOrKey: str, fields: Optional[Dict[str, Any]] = None, update: Optional[Dict[str, Any]] = None, notifyUsers: Optional[bool] = None):
    """PUT /issue/{issueIdOrKey}"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if notifyUsers is not None:
        params["notifyUsers"] = str(notifyUsers).lower()
    body: Dict[str, Any] = {}
    if fields is not None:
        body["fields"] = fields
    if update is not None:
        body["update"] = update
    return client.request("PUT", f"/issue/{issueIdOrKey}", params=params or None, json=body or {})


def delete_issue(issueIdOrKey: str, deleteSubtasks: Optional[bool] = None):
    """DELETE /issue/{issueIdOrKey}"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if deleteSubtasks is not None:
        params["deleteSubtasks"] = str(deleteSubtasks).lower()
    return client.request("DELETE", f"/issue/{issueIdOrKey}", params=params or None)


def assign_issue(issueIdOrKey: str, accountId: Optional[str] = None):
    """PUT /issue/{issueIdOrKey}/assignee"""
    client = JiraClient()
    body: Dict[str, Any] = {"accountId": accountId}
    return client.request("PUT", f"/issue/{issueIdOrKey}/assignee", json=body)


def get_transitions(issueIdOrKey: str, expand: Optional[str] = None, transitionId: Optional[str] = None, skipRemoteOnlyCondition: Optional[bool] = None, includeUnavailableTransitions: Optional[bool] = None):
    """GET /issue/{issueIdOrKey}/transitions"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    if transitionId is not None:
        params["transitionId"] = transitionId
    if skipRemoteOnlyCondition is not None:
        params["skipRemoteOnlyCondition"] = str(skipRemoteOnlyCondition).lower()
    if includeUnavailableTransitions is not None:
        params["includeUnavailableTransitions"] = str(includeUnavailableTransitions).lower()
    return client.request("GET", f"/issue/{issueIdOrKey}/transitions", params=params or None)


def transition_issue(issueIdOrKey: str, transition: Dict[str, Any], fields: Optional[Dict[str, Any]] = None, update: Optional[Dict[str, Any]] = None, historyMetadata: Optional[Dict[str, Any]] = None, properties: Optional[List[Dict[str, Any]]] = None):
    """POST /issue/{issueIdOrKey}/transitions"""
    client = JiraClient()
    body: Dict[str, Any] = {"transition": transition}
    if fields is not None:
        body["fields"] = fields
    if update is not None:
        body["update"] = update
    if historyMetadata is not None:
        body["historyMetadata"] = historyMetadata
    if properties is not None:
        body["properties"] = properties
    return client.request("POST", f"/issue/{issueIdOrKey}/transitions", json=body)
