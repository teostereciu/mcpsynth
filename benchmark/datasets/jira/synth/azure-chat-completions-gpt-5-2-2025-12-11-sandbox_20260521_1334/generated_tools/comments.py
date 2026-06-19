from typing import Any, Dict, List, Optional

from .jira_client import JiraClient


def get_comments(issue_id_or_key: str, start_at: int = 0, max_results: int = 50,
                 order_by: Optional[str] = None, expand: Optional[str] = None) -> Any:
    """GET /issue/{issueIdOrKey}/comment"""
    params: Dict[str, Any] = {"startAt": start_at, "maxResults": max_results}
    if order_by is not None:
        params["orderBy"] = order_by
    if expand is not None:
        params["expand"] = expand
    return JiraClient().request("GET", f"/issue/{issue_id_or_key}/comment", params=params)


def add_comment(issue_id_or_key: str, body: Any, visibility: Optional[Dict[str, Any]] = None,
                properties: Optional[List[Dict[str, Any]]] = None, expand: Optional[str] = None) -> Any:
    """POST /issue/{issueIdOrKey}/comment"""
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    payload: Dict[str, Any] = {"body": body}
    if visibility is not None:
        payload["visibility"] = visibility
    if properties is not None:
        payload["properties"] = properties
    return JiraClient().request("POST", f"/issue/{issue_id_or_key}/comment", params=params or None, json_body=payload)


def get_comment(issue_id_or_key: str, comment_id: str, expand: Optional[str] = None) -> Any:
    """GET /issue/{issueIdOrKey}/comment/{id}"""
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    return JiraClient().request("GET", f"/issue/{issue_id_or_key}/comment/{comment_id}", params=params or None)


def update_comment(issue_id_or_key: str, comment_id: str, body: Any,
                   notify_users: Optional[bool] = None, override_editable_flag: Optional[bool] = None,
                   visibility: Optional[Dict[str, Any]] = None, properties: Optional[List[Dict[str, Any]]] = None,
                   expand: Optional[str] = None) -> Any:
    """PUT /issue/{issueIdOrKey}/comment/{id}"""
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

    return JiraClient().request("PUT", f"/issue/{issue_id_or_key}/comment/{comment_id}", params=params or None, json_body=payload)


def delete_comment(issue_id_or_key: str, comment_id: str) -> Any:
    """DELETE /issue/{issueIdOrKey}/comment/{id}"""
    return JiraClient().request("DELETE", f"/issue/{issue_id_or_key}/comment/{comment_id}")


def get_comments_by_ids(ids: List[int], expand: Optional[str] = None) -> Any:
    """POST /comment/list"""
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    return JiraClient().request("POST", "/comment/list", params=params or None, json_body={"ids": ids})
