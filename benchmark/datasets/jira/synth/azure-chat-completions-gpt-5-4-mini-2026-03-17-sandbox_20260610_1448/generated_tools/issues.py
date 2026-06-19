from typing import Any, Dict, Optional
from .jira_client import JiraClient

client = JiraClient()


def create_issue(fields: Dict[str, Any], update: Optional[Dict[str, Any]] = None, transition: Optional[Dict[str, Any]] = None, properties: Optional[list] = None, historyMetadata: Optional[Dict[str, Any]] = None, updateHistory: Optional[bool] = None) -> Any:
    body: Dict[str, Any] = {"fields": fields}
    if update is not None:
        body["update"] = update
    if transition is not None:
        body["transition"] = transition
    if properties is not None:
        body["properties"] = properties
    if historyMetadata is not None:
        body["historyMetadata"] = historyMetadata
    params = {"updateHistory": updateHistory} if updateHistory is not None else None
    return client.request("POST", "/issue", params=params, body=body)


def get_issue(issueIdOrKey: str, fields: Optional[str] = None, expand: Optional[str] = None) -> Any:
    params = {"fields": fields, "expand": expand}
    return client.request("GET", f"/issue/{issueIdOrKey}", params=params)


def edit_issue(issueIdOrKey: str, fields: Optional[Dict[str, Any]] = None, update: Optional[Dict[str, Any]] = None) -> Any:
    body: Dict[str, Any] = {}
    if fields is not None:
        body["fields"] = fields
    if update is not None:
        body["update"] = update
    return client.request("PUT", f"/issue/{issueIdOrKey}", body=body)


def delete_issue(issueIdOrKey: str, deleteSubtasks: Optional[bool] = None) -> Any:
    params = {"deleteSubtasks": deleteSubtasks} if deleteSubtasks is not None else None
    return client.request("DELETE", f"/issue/{issueIdOrKey}", params=params)
