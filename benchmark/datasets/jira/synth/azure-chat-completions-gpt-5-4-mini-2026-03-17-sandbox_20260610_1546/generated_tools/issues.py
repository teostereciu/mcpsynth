from typing import Any, Dict, Optional

from generated_tools.jira_client import JiraClient

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
    return client.request("POST", "/issue", query={"updateHistory": updateHistory}, body=body)


def get_issue(issueIdOrKey: str, fields: Optional[list] = None, expand: Optional[str] = None) -> Any:
    return client.request("GET", f"/issue/{issueIdOrKey}", query={"fields": fields, "expand": expand})


def edit_issue(issueIdOrKey: str, fields: Optional[Dict[str, Any]] = None, update: Optional[Dict[str, Any]] = None, notifyUsers: Optional[bool] = None, overrideScreenSecurity: Optional[bool] = None, overrideEditableFlag: Optional[bool] = None) -> Any:
    body: Dict[str, Any] = {}
    if fields is not None:
        body["fields"] = fields
    if update is not None:
        body["update"] = update
    return client.request("PUT", f"/issue/{issueIdOrKey}", query={"notifyUsers": notifyUsers, "overrideScreenSecurity": overrideScreenSecurity, "overrideEditableFlag": overrideEditableFlag}, body=body)
