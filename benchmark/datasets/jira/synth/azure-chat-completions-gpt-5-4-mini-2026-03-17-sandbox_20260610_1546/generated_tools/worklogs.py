from typing import Any, Dict, Optional

from generated_tools.jira_client import JiraClient

client = JiraClient()


def get_worklogs(issueIdOrKey: str, startAt: Optional[int] = None, maxResults: Optional[int] = None, startedAfter: Optional[int] = None, startedBefore: Optional[int] = None, expand: Optional[str] = None) -> Any:
    return client.request("GET", f"/issue/{issueIdOrKey}/worklog", query={"startAt": startAt, "maxResults": maxResults, "startedAfter": startedAfter, "startedBefore": startedBefore, "expand": expand})


def add_worklog(issueIdOrKey: str, started: str, timeSpentSeconds: Optional[int] = None, timeSpent: Optional[str] = None, comment: Optional[Any] = None, properties: Optional[list] = None, visibility: Optional[Dict[str, Any]] = None, notifyUsers: Optional[bool] = None, adjustEstimate: Optional[str] = None, newEstimate: Optional[str] = None, reduceBy: Optional[str] = None, expand: Optional[str] = None, overrideEditableFlag: Optional[bool] = None) -> Any:
    body: Dict[str, Any] = {"started": started}
    if timeSpentSeconds is not None:
        body["timeSpentSeconds"] = timeSpentSeconds
    if timeSpent is not None:
        body["timeSpent"] = timeSpent
    if comment is not None:
        body["comment"] = comment
    if properties is not None:
        body["properties"] = properties
    if visibility is not None:
        body["visibility"] = visibility
    return client.request("POST", f"/issue/{issueIdOrKey}/worklog", query={"notifyUsers": notifyUsers, "adjustEstimate": adjustEstimate, "newEstimate": newEstimate, "reduceBy": reduceBy, "expand": expand, "overrideEditableFlag": overrideEditableFlag}, body=body)
