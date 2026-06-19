from typing import Any, Dict, List, Optional

from .jira_client import JiraClient, clean_params


def comment_list_by_ids(ids: List[int], expand: Optional[str] = None) -> Dict[str, Any]:
    """POST /comment/list - Get comments by IDs."""
    client = JiraClient()
    params = clean_params({"expand": expand})
    return client.request("POST", "/comment/list", params=params, json_body={"ids": ids})  # type: ignore[return-value]


def issue_comments_get(issue_id_or_key: str, start_at: Optional[int] = None, max_results: Optional[int] = None, order_by: Optional[str] = None, expand: Optional[str] = None) -> Dict[str, Any]:
    """GET /issue/{issueIdOrKey}/comment - Get comments for an issue."""
    client = JiraClient()
    params = clean_params({"startAt": start_at, "maxResults": max_results, "orderBy": order_by, "expand": expand})
    return client.request("GET", f"/issue/{issue_id_or_key}/comment", params=params)  # type: ignore[return-value]


def issue_comment_add(issue_id_or_key: str, body: Any, visibility: Optional[Dict[str, Any]] = None, expand: Optional[str] = None, properties: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
    """POST /issue/{issueIdOrKey}/comment - Add a comment."""
    client = JiraClient()
    params = clean_params({"expand": expand})
    payload: Dict[str, Any] = {"body": body}
    if visibility is not None:
        payload["visibility"] = visibility
    if properties is not None:
        payload["properties"] = properties
    return client.request("POST", f"/issue/{issue_id_or_key}/comment", params=params, json_body=payload)  # type: ignore[return-value]


def issue_comment_get(issue_id_or_key: str, comment_id: str, expand: Optional[str] = None) -> Dict[str, Any]:
    """GET /issue/{issueIdOrKey}/comment/{id} - Get a comment."""
    client = JiraClient()
    params = clean_params({"expand": expand})
    return client.request("GET", f"/issue/{issue_id_or_key}/comment/{comment_id}", params=params)  # type: ignore[return-value]


def issue_comment_update(
    issue_id_or_key: str,
    comment_id: str,
    body: Any,
    visibility: Optional[Dict[str, Any]] = None,
    notify_users: Optional[bool] = None,
    override_editable_flag: Optional[bool] = None,
    expand: Optional[str] = None,
    properties: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    """PUT /issue/{issueIdOrKey}/comment/{id} - Update a comment."""
    client = JiraClient()
    params = clean_params({"notifyUsers": notify_users, "overrideEditableFlag": override_editable_flag, "expand": expand})
    payload: Dict[str, Any] = {"body": body}
    if visibility is not None:
        payload["visibility"] = visibility
    if properties is not None:
        payload["properties"] = properties
    return client.request("PUT", f"/issue/{issue_id_or_key}/comment/{comment_id}", params=params, json_body=payload)  # type: ignore[return-value]


def issue_comment_delete(issue_id_or_key: str, comment_id: str) -> Dict[str, Any]:
    """DELETE /issue/{issueIdOrKey}/comment/{id} - Delete a comment."""
    client = JiraClient()
    return client.request("DELETE", f"/issue/{issue_id_or_key}/comment/{comment_id}")  # type: ignore[return-value]
