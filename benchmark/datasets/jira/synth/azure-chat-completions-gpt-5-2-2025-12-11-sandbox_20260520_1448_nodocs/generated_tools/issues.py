from typing import Any, Dict, List, Optional

from jira_client import JiraClient


def get_issue(issue_id_or_key: str, fields: Optional[List[str]] = None, expand: Optional[str] = None) -> Any:
    """GET /issue/{issueIdOrKey}"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if fields:
        params["fields"] = ",".join(fields)
    if expand:
        params["expand"] = expand
    return client.request("GET", f"/issue/{issue_id_or_key}", params=params)


def create_issue(fields: Dict[str, Any], update: Optional[Dict[str, Any]] = None) -> Any:
    """POST /issue"""
    client = JiraClient()
    payload: Dict[str, Any] = {"fields": fields}
    if update is not None:
        payload["update"] = update
    return client.request("POST", "/issue", json=payload)


def update_issue(issue_id_or_key: str, fields: Optional[Dict[str, Any]] = None, update: Optional[Dict[str, Any]] = None) -> Any:
    """PUT /issue/{issueIdOrKey}"""
    client = JiraClient()
    payload: Dict[str, Any] = {}
    if fields is not None:
        payload["fields"] = fields
    if update is not None:
        payload["update"] = update
    return client.request("PUT", f"/issue/{issue_id_or_key}", json=payload)


def delete_issue(issue_id_or_key: str, delete_subtasks: bool = False) -> Any:
    """DELETE /issue/{issueIdOrKey}"""
    client = JiraClient()
    params = {"deleteSubtasks": str(delete_subtasks).lower()}
    return client.request("DELETE", f"/issue/{issue_id_or_key}", params=params)


def assign_issue(issue_id_or_key: str, account_id: Optional[str]) -> Any:
    """PUT /issue/{issueIdOrKey}/assignee"""
    client = JiraClient()
    return client.request("PUT", f"/issue/{issue_id_or_key}/assignee", json={"accountId": account_id})


def get_transitions(issue_id_or_key: str, expand: Optional[str] = None) -> Any:
    """GET /issue/{issueIdOrKey}/transitions"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    return client.request("GET", f"/issue/{issue_id_or_key}/transitions", params=params)


def transition_issue(issue_id_or_key: str, transition_id: str, fields: Optional[Dict[str, Any]] = None, update: Optional[Dict[str, Any]] = None, comment: Optional[Dict[str, Any]] = None) -> Any:
    """POST /issue/{issueIdOrKey}/transitions"""
    client = JiraClient()
    payload: Dict[str, Any] = {"transition": {"id": transition_id}}
    if fields is not None:
        payload["fields"] = fields
    if update is not None:
        payload["update"] = update
    if comment is not None:
        payload["update"] = payload.get("update", {})
        payload["update"].setdefault("comment", []).append({"add": comment})
    return client.request("POST", f"/issue/{issue_id_or_key}/transitions", json=payload)


def add_comment(issue_id_or_key: str, body: Dict[str, Any], visibility: Optional[Dict[str, Any]] = None) -> Any:
    """POST /issue/{issueIdOrKey}/comment"""
    client = JiraClient()
    payload: Dict[str, Any] = {"body": body}
    if visibility is not None:
        payload["visibility"] = visibility
    return client.request("POST", f"/issue/{issue_id_or_key}/comment", json=payload)


def get_comments(issue_id_or_key: str, start_at: int = 0, max_results: int = 50, order_by: Optional[str] = None, expand: Optional[str] = None) -> Any:
    """GET /issue/{issueIdOrKey}/comment"""
    client = JiraClient()
    params: Dict[str, Any] = {"startAt": start_at, "maxResults": max_results}
    if order_by:
        params["orderBy"] = order_by
    if expand:
        params["expand"] = expand
    return client.request("GET", f"/issue/{issue_id_or_key}/comment", params=params)


def update_comment(issue_id_or_key: str, comment_id: str, body: Dict[str, Any], visibility: Optional[Dict[str, Any]] = None) -> Any:
    """PUT /issue/{issueIdOrKey}/comment/{id}"""
    client = JiraClient()
    payload: Dict[str, Any] = {"body": body}
    if visibility is not None:
        payload["visibility"] = visibility
    return client.request("PUT", f"/issue/{issue_id_or_key}/comment/{comment_id}", json=payload)


def delete_comment(issue_id_or_key: str, comment_id: str) -> Any:
    """DELETE /issue/{issueIdOrKey}/comment/{id}"""
    client = JiraClient()
    return client.request("DELETE", f"/issue/{issue_id_or_key}/comment/{comment_id}")


def add_worklog(issue_id_or_key: str, time_spent_seconds: int, comment: Optional[Dict[str, Any]] = None, started: Optional[str] = None) -> Any:
    """POST /issue/{issueIdOrKey}/worklog"""
    client = JiraClient()
    payload: Dict[str, Any] = {"timeSpentSeconds": time_spent_seconds}
    if comment is not None:
        payload["comment"] = comment
    if started is not None:
        payload["started"] = started
    return client.request("POST", f"/issue/{issue_id_or_key}/worklog", json=payload)


def get_worklogs(issue_id_or_key: str, start_at: int = 0, max_results: int = 50, expand: Optional[str] = None) -> Any:
    """GET /issue/{issueIdOrKey}/worklog"""
    client = JiraClient()
    params: Dict[str, Any] = {"startAt": start_at, "maxResults": max_results}
    if expand:
        params["expand"] = expand
    return client.request("GET", f"/issue/{issue_id_or_key}/worklog", params=params)


def add_watcher(issue_id_or_key: str, account_id: str) -> Any:
    """POST /issue/{issueIdOrKey}/watchers"""
    client = JiraClient()
    return client.request(
        "POST",
        f"/issue/{issue_id_or_key}/watchers",
        headers={"Content-Type": "application/json"},
        json=account_id,
    )


def remove_watcher(issue_id_or_key: str, account_id: str) -> Any:
    """DELETE /issue/{issueIdOrKey}/watchers"""
    client = JiraClient()
    return client.request("DELETE", f"/issue/{issue_id_or_key}/watchers", params={"accountId": account_id})


def create_issue_link(type_name: str, inward_issue_key: str, outward_issue_key: str, comment: Optional[Dict[str, Any]] = None) -> Any:
    """POST /issueLink"""
    client = JiraClient()
    payload: Dict[str, Any] = {
        "type": {"name": type_name},
        "inwardIssue": {"key": inward_issue_key},
        "outwardIssue": {"key": outward_issue_key},
    }
    if comment is not None:
        payload["comment"] = comment
    return client.request("POST", "/issueLink", json=payload)


def delete_issue_link(link_id: str) -> Any:
    """DELETE /issueLink/{linkId}"""
    client = JiraClient()
    return client.request("DELETE", f"/issueLink/{link_id}")
