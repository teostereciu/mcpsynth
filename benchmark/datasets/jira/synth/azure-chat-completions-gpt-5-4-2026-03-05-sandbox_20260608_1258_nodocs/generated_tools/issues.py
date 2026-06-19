import json
from typing import Any, Dict, List, Optional

from generated_tools.jira_client import jira_client


def create_issue(
    project_key: str,
    summary: str,
    issue_type: str,
    description: Optional[Any] = None,
    fields: Optional[Dict[str, Any]] = None,
) -> Any:
    payload = {"fields": {"project": {"key": project_key}, "summary": summary, "issuetype": {"name": issue_type}}}
    if description is not None:
        payload["fields"]["description"] = description
    if fields:
        payload["fields"].update(fields)
    return jira_client.request("POST", "/issue", json_body=payload)


def get_issue(issue_id_or_key: str, fields: Optional[List[str]] = None, expand: Optional[str] = None) -> Any:
    params = {}
    if fields:
        params["fields"] = ",".join(fields)
    if expand:
        params["expand"] = expand
    return jira_client.request("GET", f"/issue/{issue_id_or_key}", params=params)


def update_issue(issue_id_or_key: str, fields: Dict[str, Any], update: Optional[Dict[str, Any]] = None) -> Any:
    payload: Dict[str, Any] = {"fields": fields}
    if update:
        payload["update"] = update
    return jira_client.request("PUT", f"/issue/{issue_id_or_key}", json_body=payload)


def delete_issue(issue_id_or_key: str, delete_subtasks: bool = False) -> Any:
    return jira_client.request("DELETE", f"/issue/{issue_id_or_key}", params={"deleteSubtasks": delete_subtasks})


def assign_issue(issue_id_or_key: str, account_id: str) -> Any:
    return jira_client.request("PUT", f"/issue/{issue_id_or_key}/assignee", json_body={"accountId": account_id})


def get_transitions(issue_id_or_key: str) -> Any:
    return jira_client.request("GET", f"/issue/{issue_id_or_key}/transitions")


def transition_issue(issue_id_or_key: str, transition_id: str, fields: Optional[Dict[str, Any]] = None) -> Any:
    payload: Dict[str, Any] = {"transition": {"id": transition_id}}
    if fields:
        payload["fields"] = fields
    return jira_client.request("POST", f"/issue/{issue_id_or_key}/transitions", json_body=payload)


def add_comment(issue_id_or_key: str, body: Any, visibility: Optional[Dict[str, str]] = None) -> Any:
    payload: Dict[str, Any] = {"body": body}
    if visibility:
        payload["visibility"] = visibility
    return jira_client.request("POST", f"/issue/{issue_id_or_key}/comment", json_body=payload)


def list_comments(issue_id_or_key: str, start_at: int = 0, max_results: int = 50) -> Any:
    return jira_client.request(
        "GET",
        f"/issue/{issue_id_or_key}/comment",
        params={"startAt": start_at, "maxResults": max_results},
    )


def update_comment(issue_id_or_key: str, comment_id: str, body: Any) -> Any:
    return jira_client.request("PUT", f"/issue/{issue_id_or_key}/comment/{comment_id}", json_body={"body": body})


def delete_comment(issue_id_or_key: str, comment_id: str) -> Any:
    return jira_client.request("DELETE", f"/issue/{issue_id_or_key}/comment/{comment_id}")


def add_worklog(issue_id_or_key: str, time_spent: str, comment: Optional[Any] = None, started: Optional[str] = None) -> Any:
    payload: Dict[str, Any] = {"timeSpent": time_spent}
    if comment is not None:
        payload["comment"] = comment
    if started is not None:
        payload["started"] = started
    return jira_client.request("POST", f"/issue/{issue_id_or_key}/worklog", json_body=payload)


def list_worklogs(issue_id_or_key: str, start_at: int = 0, max_results: int = 50) -> Any:
    return jira_client.request(
        "GET",
        f"/issue/{issue_id_or_key}/worklog",
        params={"startAt": start_at, "maxResults": max_results},
    )


def add_watcher(issue_id_or_key: str, account_id: str) -> Any:
    return jira_client.request(
        "POST",
        f"/issue/{issue_id_or_key}/watchers",
        data=json_string(account_id),
        headers={"Content-Type": "application/json"},
    )


def remove_watcher(issue_id_or_key: str, account_id: str) -> Any:
    return jira_client.request("DELETE", f"/issue/{issue_id_or_key}/watchers", params={"accountId": account_id})


def create_issue_link(link_type: str, inward_issue_key: str, outward_issue_key: str, comment: Optional[Any] = None) -> Any:
    payload: Dict[str, Any] = {
        "type": {"name": link_type},
        "inwardIssue": {"key": inward_issue_key},
        "outwardIssue": {"key": outward_issue_key},
    }
    if comment is not None:
        payload["comment"] = {"body": comment}
    return jira_client.request("POST", "/issueLink", json_body=payload)


def search_issues(
    jql: str,
    start_at: int = 0,
    max_results: int = 50,
    fields: Optional[List[str]] = None,
    expand: Optional[str] = None,
) -> Any:
    payload: Dict[str, Any] = {"jql": jql, "startAt": start_at, "maxResults": max_results}
    if fields:
        payload["fields"] = fields
    if expand:
        payload["expand"] = expand
    return jira_client.request("POST", "/search", json_body=payload)


def json_string(value: str) -> str:
    return json.dumps(value)
