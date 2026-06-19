from typing import Any, Dict, List, Optional, Union

from .http_client import JiraClient


def get_comments_by_ids(ids: List[int], expand: Optional[str] = None) -> Union[Dict[str, Any], list, str]:
    """POST /comment/list"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    return client.request("POST", "/comment/list", params=params or None, json={"ids": ids})


def get_issue_comments(issue_id_or_key: str, start_at: Optional[int] = None, max_results: Optional[int] = None, order_by: Optional[str] = None, expand: Optional[str] = None) -> Union[Dict[str, Any], list, str]:
    """GET /issue/{issueIdOrKey}/comment"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if start_at is not None:
        params["startAt"] = start_at
    if max_results is not None:
        params["maxResults"] = max_results
    if order_by is not None:
        params["orderBy"] = order_by
    if expand is not None:
        params["expand"] = expand
    return client.request("GET", f"/issue/{issue_id_or_key}/comment", params=params or None)


def add_comment(issue_id_or_key: str, body: Any, visibility: Optional[Dict[str, Any]] = None, properties: Optional[List[Dict[str, Any]]] = None, expand: Optional[str] = None) -> Union[Dict[str, Any], list, str]:
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
    return client.request("POST", f"/issue/{issue_id_or_key}/comment", params=params or None, json=payload)


def get_comment(issue_id_or_key: str, comment_id: str, expand: Optional[str] = None) -> Union[Dict[str, Any], list, str]:
    """GET /issue/{issueIdOrKey}/comment/{id}"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    return client.request("GET", f"/issue/{issue_id_or_key}/comment/{comment_id}", params=params or None)


def update_comment(issue_id_or_key: str, comment_id: str, body: Any, visibility: Optional[Dict[str, Any]] = None, properties: Optional[List[Dict[str, Any]]] = None, notify_users: Optional[bool] = None, override_editable_flag: Optional[bool] = None, expand: Optional[str] = None) -> Union[Dict[str, Any], list, str]:
    """PUT /issue/{issueIdOrKey}/comment/{id}"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if notify_users is not None:
        params["notifyUsers"] = str(notify_users).lower()
    if override_editable_flag is not None:
        params["overrideEditableFlag"] = str(override_editable_flag).lower()
    if expand is not None:
        params["expand"] = expand
    payload: Dict[str, Any] = {"body": body}
    if visibility is not None:
        payload["visibility"] = visibility
    if properties is not None:
        payload["properties"] = properties
    return client.request("PUT", f"/issue/{issue_id_or_key}/comment/{comment_id}", params=params or None, json=payload)


def delete_comment(issue_id_or_key: str, comment_id: str) -> Union[Dict[str, Any], list, str]:
    """DELETE /issue/{issueIdOrKey}/comment/{id}"""
    client = JiraClient()
    return client.request("DELETE", f"/issue/{issue_id_or_key}/comment/{comment_id}")
