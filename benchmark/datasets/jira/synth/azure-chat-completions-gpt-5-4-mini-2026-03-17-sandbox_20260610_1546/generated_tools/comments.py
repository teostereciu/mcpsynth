from typing import Any, Dict, Optional

from generated_tools.jira_client import JiraClient

client = JiraClient()


def get_comments(issueIdOrKey: str, startAt: Optional[int] = None, maxResults: Optional[int] = None, orderBy: Optional[str] = None, expand: Optional[str] = None) -> Any:
    return client.request("GET", f"/issue/{issueIdOrKey}/comment", query={"startAt": startAt, "maxResults": maxResults, "orderBy": orderBy, "expand": expand})


def add_comment(issueIdOrKey: str, body: Any, properties: Optional[list] = None, visibility: Optional[Dict[str, Any]] = None, expand: Optional[str] = None) -> Any:
    payload: Dict[str, Any] = {"body": body}
    if properties is not None:
        payload["properties"] = properties
    if visibility is not None:
        payload["visibility"] = visibility
    return client.request("POST", f"/issue/{issueIdOrKey}/comment", query={"expand": expand}, body=payload)
