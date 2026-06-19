from typing import Any, Dict, List, Optional

from jira_client import JiraClient


def get_issue(client: JiraClient, issue_id_or_key: str, fields: Optional[List[str]] = None, expand: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {}
    if fields:
        params["fields"] = ",".join(fields)
    if expand:
        params["expand"] = expand
    return client.request("GET", f"/issue/{issue_id_or_key}", params=params)


def create_issue(client: JiraClient, fields: Dict[str, Any], update: Optional[Dict[str, Any]] = None) -> Any:
    payload: Dict[str, Any] = {"fields": fields}
    if update is not None:
        payload["update"] = update
    return client.request("POST", "/issue", json=payload)


def update_issue(client: JiraClient, issue_id_or_key: str, fields: Optional[Dict[str, Any]] = None, update: Optional[Dict[str, Any]] = None, notify_users: Optional[bool] = None) -> Any:
    payload: Dict[str, Any] = {}
    if fields is not None:
        payload["fields"] = fields
    if update is not None:
        payload["update"] = update
    params: Dict[str, Any] = {}
    if notify_users is not None:
        params["notifyUsers"] = str(notify_users).lower()
    return client.request("PUT", f"/issue/{issue_id_or_key}", params=params, json=payload)


def delete_issue(client: JiraClient, issue_id_or_key: str, delete_subtasks: Optional[bool] = None) -> Any:
    params: Dict[str, Any] = {}
    if delete_subtasks is not None:
        params["deleteSubtasks"] = str(delete_subtasks).lower()
    return client.request("DELETE", f"/issue/{issue_id_or_key}", params=params)


def assign_issue(client: JiraClient, issue_id_or_key: str, account_id: Optional[str] = None) -> Any:
    return client.request("PUT", f"/issue/{issue_id_or_key}/assignee", json={"accountId": account_id})


def transitions(client: JiraClient, issue_id_or_key: str) -> Any:
    return client.request("GET", f"/issue/{issue_id_or_key}/transitions")


def transition_issue(client: JiraClient, issue_id_or_key: str, transition_id: str, fields: Optional[Dict[str, Any]] = None, update: Optional[Dict[str, Any]] = None, comment: Optional[Dict[str, Any]] = None) -> Any:
    payload: Dict[str, Any] = {"transition": {"id": transition_id}}
    if fields is not None:
        payload["fields"] = fields
    if update is not None:
        payload["update"] = update
    if comment is not None:
        payload["update"] = payload.get("update", {})
        payload["update"]["comment"] = [{"add": comment}]
    return client.request("POST", f"/issue/{issue_id_or_key}/transitions", json=payload)


def add_comment(client: JiraClient, issue_id_or_key: str, body: Any) -> Any:
    return client.request("POST", f"/issue/{issue_id_or_key}/comment", json={"body": body})


def get_comments(client: JiraClient, issue_id_or_key: str, start_at: int = 0, max_results: int = 50, order_by: Optional[str] = None, expand: Optional[str] = None) -> Any:
    params: Dict[str, Any] = {"startAt": start_at, "maxResults": max_results}
    if order_by:
        params["orderBy"] = order_by
    if expand:
        params["expand"] = expand
    return client.request("GET", f"/issue/{issue_id_or_key}/comment", params=params)


def update_comment(client: JiraClient, issue_id_or_key: str, comment_id: str, body: Any) -> Any:
    return client.request("PUT", f"/issue/{issue_id_or_key}/comment/{comment_id}", json={"body": body})


def delete_comment(client: JiraClient, issue_id_or_key: str, comment_id: str) -> Any:
    return client.request("DELETE", f"/issue/{issue_id_or_key}/comment/{comment_id}")


def add_worklog(client: JiraClient, issue_id_or_key: str, time_spent_seconds: int, comment: Optional[Any] = None, started: Optional[str] = None) -> Any:
    payload: Dict[str, Any] = {"timeSpentSeconds": time_spent_seconds}
    if comment is not None:
        payload["comment"] = comment
    if started is not None:
        payload["started"] = started
    return client.request("POST", f"/issue/{issue_id_or_key}/worklog", json=payload)


def get_worklogs(client: JiraClient, issue_id_or_key: str, start_at: int = 0, max_results: int = 50) -> Any:
    params = {"startAt": start_at, "maxResults": max_results}
    return client.request("GET", f"/issue/{issue_id_or_key}/worklog", params=params)


def delete_worklog(client: JiraClient, issue_id_or_key: str, worklog_id: str) -> Any:
    return client.request("DELETE", f"/issue/{issue_id_or_key}/worklog/{worklog_id}")


def add_watcher(client: JiraClient, issue_id_or_key: str, account_id: str) -> Any:
    # Jira expects a JSON string body with accountId
    return client.request("POST", f"/issue/{issue_id_or_key}/watchers", json=account_id)


def remove_watcher(client: JiraClient, issue_id_or_key: str, account_id: str) -> Any:
    return client.request("DELETE", f"/issue/{issue_id_or_key}/watchers", params={"accountId": account_id})


def create_issue_link(client: JiraClient, inward_issue_key: str, outward_issue_key: str, link_type: str, comment: Optional[Any] = None) -> Any:
    payload: Dict[str, Any] = {
        "type": {"name": link_type},
        "inwardIssue": {"key": inward_issue_key},
        "outwardIssue": {"key": outward_issue_key},
    }
    if comment is not None:
        payload["comment"] = {"body": comment}
    return client.request("POST", "/issueLink", json=payload)


def delete_issue_link(client: JiraClient, link_id: str) -> Any:
    return client.request("DELETE", f"/issueLink/{link_id}")
