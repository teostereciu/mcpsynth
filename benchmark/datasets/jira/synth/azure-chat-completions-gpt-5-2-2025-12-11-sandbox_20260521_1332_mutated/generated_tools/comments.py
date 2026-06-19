from typing import Any, Dict, List, Optional

from .jira_client import JiraClient


def list_comments(
    issueIdOrKey: str,
    *,
    startAt: int = 0,
    maxResults: int = 50,
    orderBy: Optional[str] = None,
    expand: Optional[str] = None,
) -> Any:
    """GET /rest/api/3/issue/{issueIdOrKey}/comment"""
    client = JiraClient()
    params: Dict[str, Any] = {"startAt": startAt, "maxResults": maxResults}
    if orderBy is not None:
        params["orderBy"] = orderBy
    if expand is not None:
        params["expand"] = expand
    return client.request("GET", f"/issue/{issueIdOrKey}/comment", params=params)


def add_comment(
    issueIdOrKey: str,
    body: Dict[str, Any],
    *,
    expand: Optional[str] = None,
    visibility: Optional[Dict[str, Any]] = None,
    properties: Optional[List[Dict[str, Any]]] = None,
) -> Any:
    """POST /rest/api/3/issue/{issueIdOrKey}/comment

    'body' should be Atlassian Document Format.
    """
    client = JiraClient()
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    payload: Dict[str, Any] = {"body": body}
    if visibility is not None:
        payload["visibility"] = visibility
    if properties is not None:
        payload["properties"] = properties
    return client.request("POST", f"/issue/{issueIdOrKey}/comment", params=params or None, json_body=payload)


def get_comment(issueIdOrKey: str, commentId: str, *, expand: Optional[str] = None) -> Any:
    """GET /rest/api/3/issue/{issueIdOrKey}/comment/{id}"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    return client.request("GET", f"/issue/{issueIdOrKey}/comment/{commentId}", params=params or None)


def update_comment(
    issueIdOrKey: str,
    commentId: str,
    body: Dict[str, Any],
    *,
    notifyUsers: Optional[bool] = None,
    overrideEditableFlag: Optional[bool] = None,
    expand: Optional[str] = None,
    visibility: Optional[Dict[str, Any]] = None,
    properties: Optional[List[Dict[str, Any]]] = None,
) -> Any:
    """PUT /rest/api/3/issue/{issueIdOrKey}/comment/{id}"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if notifyUsers is not None:
        params["notifyUsers"] = str(notifyUsers).lower()
    if overrideEditableFlag is not None:
        params["overrideEditableFlag"] = str(overrideEditableFlag).lower()
    if expand is not None:
        params["expand"] = expand
    payload: Dict[str, Any] = {"body": body}
    if visibility is not None:
        payload["visibility"] = visibility
    if properties is not None:
        payload["properties"] = properties
    return client.request("PUT", f"/issue/{issueIdOrKey}/comment/{commentId}", params=params or None, json_body=payload)


def delete_comment(issueIdOrKey: str, commentId: str) -> Any:
    """DEL /rest/api/3/issue/{issueIdOrKey}/comment/{id}"""
    client = JiraClient()
    return client.request("DELETE", f"/issue/{issueIdOrKey}/comment/{commentId}")


def get_comments_by_ids(ids: List[int], *, expand: Optional[str] = None) -> Any:
    """POST /rest/api/3/comment/list"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    return client.request("POST", "/comment/list", params=params or None, json_body={"ids": ids})
