from typing import Any, Dict, List, Optional

from .jira_client import JiraClient


def create_issue(
    fields: Dict[str, Any],
    *,
    update: Optional[Dict[str, Any]] = None,
    updateHistory: Optional[bool] = None,
    properties: Optional[List[Dict[str, Any]]] = None,
    transition: Optional[Dict[str, Any]] = None,
    historyMetadata: Optional[Dict[str, Any]] = None,
) -> Any:
    """POST /rest/api/3/issue

    Creates an issue. Provide Jira 'fields' object.
    """
    client = JiraClient()
    params = {}
    if updateHistory is not None:
        params["updateHistory"] = str(updateHistory).lower()
    body: Dict[str, Any] = {"fields": fields}
    if update is not None:
        body["update"] = update
    if properties is not None:
        body["properties"] = properties
    if transition is not None:
        body["transition"] = transition
    if historyMetadata is not None:
        body["historyMetadata"] = historyMetadata
    return client.request("POST", "/issue", params=params or None, json_body=body)


def get_issue(
    issueIdOrKey: str,
    *,
    fields: Optional[List[str]] = None,
    fieldsByKeys: Optional[bool] = None,
    expand: Optional[str] = None,
    properties: Optional[List[str]] = None,
    updateHistory: Optional[bool] = None,
) -> Any:
    """GET /rest/api/3/issue/{issueIdOrKey}"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if fields is not None:
        params["fields"] = ",".join(fields)
    if fieldsByKeys is not None:
        params["fieldsByKeys"] = str(fieldsByKeys).lower()
    if expand is not None:
        params["expand"] = expand
    if properties is not None:
        params["properties"] = ",".join(properties)
    if updateHistory is not None:
        params["updateHistory"] = str(updateHistory).lower()
    return client.request("GET", f"/issue/{issueIdOrKey}", params=params or None)


def update_issue(
    issueIdOrKey: str,
    *,
    fields: Optional[Dict[str, Any]] = None,
    update: Optional[Dict[str, Any]] = None,
    notifyUsers: Optional[bool] = None,
    overrideScreenSecurity: Optional[bool] = None,
    overrideEditableFlag: Optional[bool] = None,
) -> Any:
    """PUT /rest/api/3/issue/{issueIdOrKey}"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if notifyUsers is not None:
        params["notifyUsers"] = str(notifyUsers).lower()
    if overrideScreenSecurity is not None:
        params["overrideScreenSecurity"] = str(overrideScreenSecurity).lower()
    if overrideEditableFlag is not None:
        params["overrideEditableFlag"] = str(overrideEditableFlag).lower()
    body: Dict[str, Any] = {}
    if fields is not None:
        body["fields"] = fields
    if update is not None:
        body["update"] = update
    return client.request("PUT", f"/issue/{issueIdOrKey}", params=params or None, json_body=body or {})


def delete_issue(
    issueIdOrKey: str,
    *,
    deleteSubtasks: Optional[bool] = None,
) -> Any:
    """DEL /rest/api/3/issue/{issueIdOrKey}"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if deleteSubtasks is not None:
        params["deleteSubtasks"] = str(deleteSubtasks).lower()
    return client.request("DELETE", f"/issue/{issueIdOrKey}", params=params or None)


def assign_issue(
    issueIdOrKey: str,
    *,
    accountId: Optional[str] = None,
) -> Any:
    """PUT /rest/api/3/issue/{issueIdOrKey}/assignee"""
    client = JiraClient()
    body: Dict[str, Any] = {"accountId": accountId}
    return client.request("PUT", f"/issue/{issueIdOrKey}/assignee", json_body=body)


def get_transitions(issueIdOrKey: str, *, expand: Optional[str] = None, transitionId: Optional[str] = None) -> Any:
    """GET /rest/api/3/issue/{issueIdOrKey}/transitions"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    if transitionId is not None:
        params["transitionId"] = transitionId
    return client.request("GET", f"/issue/{issueIdOrKey}/transitions", params=params or None)


def transition_issue(
    issueIdOrKey: str,
    transition: Dict[str, Any],
    *,
    fields: Optional[Dict[str, Any]] = None,
    update: Optional[Dict[str, Any]] = None,
    historyMetadata: Optional[Dict[str, Any]] = None,
    properties: Optional[List[Dict[str, Any]]] = None,
) -> Any:
    """POST /rest/api/3/issue/{issueIdOrKey}/transitions"""
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
    return client.request("POST", f"/issue/{issueIdOrKey}/transitions", json_body=body)
