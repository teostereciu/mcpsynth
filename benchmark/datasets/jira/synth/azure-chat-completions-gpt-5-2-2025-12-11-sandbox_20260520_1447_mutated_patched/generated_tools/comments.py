from typing import Any, Dict, List, Optional

from .jira_client import JiraClient


def get_comments(issueIdOrKey: str, start_index: int = 0, page_size: int = 50, orderBy: Optional[str] = None, expand: Optional[str] = None):
    """GET /issue/{issueIdOrKey}/comment"""
    client = JiraClient()
    params: Dict[str, Any] = {"startAt": start_index, "maxResults": page_size}
    if orderBy is not None:
        params["orderBy"] = orderBy
    if expand is not None:
        params["expand"] = expand
    return client.request("GET", f"/issue/{issueIdOrKey}/comment", params=params)


def add_comment(issueIdOrKey: str, body: Any, visibility: Optional[Dict[str, Any]] = None, properties: Optional[List[Dict[str, Any]]] = None, expand: Optional[str] = None):
    """POST /issue/{issueIdOrKey}/comment"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    payload: Dict[str, Any] = {"body": body}
    if visibility is not None:
        payload["visibility"] = visibility
    if properties is not None:
        payload["properties"] = properties
    return client.request("POST", f"/issue/{issueIdOrKey}/comment", params=params or None, json=payload)


def get_comment(issueIdOrKey: str, id: str, expand: Optional[str] = None):
    """GET /issue/{issueIdOrKey}/comment/{id}"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    return client.request("GET", f"/issue/{issueIdOrKey}/comment/{id}", params=params or None)


def update_comment(issueIdOrKey: str, id: str, body: Any, visibility: Optional[Dict[str, Any]] = None, properties: Optional[List[Dict[str, Any]]] = None, notifyUsers: Optional[bool] = None, overrideEditableFlag: Optional[bool] = None, expand: Optional[str] = None):
    """PUT /issue/{issueIdOrKey}/comment/{id}"""
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
    return client.request("PUT", f"/issue/{issueIdOrKey}/comment/{id}", params=params or None, json=payload)


def delete_comment(issueIdOrKey: str, id: str):
    """DELETE /issue/{issueIdOrKey}/comment/{id}"""
    client = JiraClient()
    return client.request("DELETE", f"/issue/{issueIdOrKey}/comment/{id}")


def get_comments_by_ids(ids: List[int], expand: Optional[str] = None):
    """POST /comment/list"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    return client.request("POST", "/comment/list", params=params or None, json={"ids": ids})
