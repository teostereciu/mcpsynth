import os
from typing import Any, Dict, Optional

import requests

BASE_URL = os.environ.get("JIRA_BASE_URL", "").rstrip("/")
EMAIL = os.environ.get("JIRA_EMAIL", "")
API_TOKEN = os.environ.get("JIRA_API_TOKEN", "")
API_ROOT = f"{BASE_URL}/rest/api/3"


def _client() -> requests.Session:
    session = requests.Session()
    session.auth = (EMAIL, API_TOKEN)
    session.headers.update({"Accept": "application/json"})
    return session


def _request(method: str, path: str, *, params: Optional[Dict[str, Any]] = None, json_body: Any = None, headers: Optional[Dict[str, str]] = None, files: Any = None) -> Any:
    if not BASE_URL or not EMAIL or not API_TOKEN:
        return {"error": "Missing JIRA_BASE_URL, JIRA_EMAIL, or JIRA_API_TOKEN environment variables."}
    try:
        session = _client()
        req_headers = {}
        if headers:
            req_headers.update(headers)
        if json_body is not None and files is None:
            req_headers.setdefault("Content-Type", "application/json")
        response = session.request(method, f"{API_ROOT}{path}", params=params, json=json_body if files is None else None, headers=req_headers, files=files)
        if response.status_code == 204:
            return {"success": True, "status_code": 204}
        content_type = response.headers.get("Content-Type", "")
        data = response.json() if "application/json" in content_type else {"text": response.text, "status_code": response.status_code}
        if response.ok:
            return data
        return {"error": data, "status_code": response.status_code}
    except requests.RequestException as exc:
        return {"error": str(exc)}


def create_issue(fields: Dict[str, Any], update: Optional[Dict[str, Any]] = None, transition: Optional[Dict[str, Any]] = None, properties: Optional[list] = None, history_metadata: Optional[Dict[str, Any]] = None, update_history: Optional[bool] = None) -> Any:
    body: Dict[str, Any] = {"fields": fields}
    if update is not None:
        body["update"] = update
    if transition is not None:
        body["transition"] = transition
    if properties is not None:
        body["properties"] = properties
    if history_metadata is not None:
        body["historyMetadata"] = history_metadata
    params = {}
    if update_history is not None:
        params["updateHistory"] = str(update_history).lower()
    return _request("POST", "/issue", params=params or None, json_body=body)


def get_issue(issue_id_or_key: str, fields: Optional[list] = None, expand: Optional[str] = None, properties: Optional[list] = None, update_history: Optional[bool] = None) -> Any:
    params: Dict[str, Any] = {}
    if fields is not None:
        params["fields"] = ",".join(fields)
    if expand is not None:
        params["expand"] = expand
    if properties is not None:
        params["properties"] = ",".join(properties)
    if update_history is not None:
        params["updateHistory"] = str(update_history).lower()
    return _request("GET", f"/issue/{issue_id_or_key}", params=params or None)


def update_issue(issue_id_or_key: str, fields: Optional[Dict[str, Any]] = None, update: Optional[Dict[str, Any]] = None, history_metadata: Optional[Dict[str, Any]] = None, properties: Optional[list] = None, notify_users: Optional[bool] = None, override_screen_security: Optional[bool] = None, override_editable_flag: Optional[bool] = None, return_issue: Optional[bool] = None) -> Any:
    body: Dict[str, Any] = {}
    if fields is not None:
        body["fields"] = fields
    if update is not None:
        body["update"] = update
    if history_metadata is not None:
        body["historyMetadata"] = history_metadata
    if properties is not None:
        body["properties"] = properties
    params: Dict[str, Any] = {}
    if notify_users is not None:
        params["notifyUsers"] = str(notify_users).lower()
    if override_screen_security is not None:
        params["overrideScreenSecurity"] = str(override_screen_security).lower()
    if override_editable_flag is not None:
        params["overrideEditableFlag"] = str(override_editable_flag).lower()
    if return_issue is not None:
        params["returnIssue"] = str(return_issue).lower()
    return _request("PUT", f"/issue/{issue_id_or_key}", params=params or None, json_body=body)


def delete_issue(issue_id_or_key: str, delete_subtasks: Optional[bool] = None) -> Any:
    params = {}
    if delete_subtasks is not None:
        params["deleteSubtasks"] = str(delete_subtasks).lower()
    return _request("DELETE", f"/issue/{issue_id_or_key}", params=params or None)


def assign_issue(issue_id_or_key: str, account_id: Optional[str] = None) -> Any:
    return _request("PUT", f"/issue/{issue_id_or_key}/assignee", json_body={"accountId": account_id})


def get_issue_transitions(issue_id_or_key: str, expand: Optional[str] = None, transition_id: Optional[str] = None) -> Any:
    params = {}
    if expand is not None:
        params["expand"] = expand
    if transition_id is not None:
        params["transitionId"] = transition_id
    return _request("GET", f"/issue/{issue_id_or_key}/transitions", params=params or None)


def transition_issue(issue_id_or_key: str, transition: Dict[str, Any], fields: Optional[Dict[str, Any]] = None, update: Optional[Dict[str, Any]] = None, history_metadata: Optional[Dict[str, Any]] = None) -> Any:
    body: Dict[str, Any] = {"transition": transition}
    if fields is not None:
        body["fields"] = fields
    if update is not None:
        body["update"] = update
    if history_metadata is not None:
        body["historyMetadata"] = history_metadata
    return _request("POST", f"/issue/{issue_id_or_key}/transitions", json_body=body)


def get_issue_changelog(issue_id_or_key: str, start_at: Optional[int] = None, max_results: Optional[int] = None) -> Any:
    params = {}
    if start_at is not None:
        params["startAt"] = start_at
    if max_results is not None:
        params["maxResults"] = max_results
    return _request("GET", f"/issue/{issue_id_or_key}/changelog", params=params or None)


def get_create_issue_meta(project_ids_or_keys: Optional[list] = None, issuetype_ids: Optional[list] = None, expand: Optional[str] = None) -> Any:
    params = {}
    if project_ids_or_keys is not None:
        params["projectIdsOrKeys"] = ",".join(project_ids_or_keys)
    if issuetype_ids is not None:
        params["issuetypeIds"] = ",".join(issuetype_ids)
    if expand is not None:
        params["expand"] = expand
    return _request("GET", "/issue/createmeta", params=params or None)


def get_edit_issue_meta(issue_id_or_key: str) -> Any:
    return _request("GET", f"/issue/{issue_id_or_key}/editmeta")


def list_comments(issue_id_or_key: str, start_at: Optional[int] = None, max_results: Optional[int] = None, order_by: Optional[str] = None, expand: Optional[str] = None) -> Any:
    params = {}
    if start_at is not None:
        params["startAt"] = start_at
    if max_results is not None:
        params["maxResults"] = max_results
    if order_by is not None:
        params["orderBy"] = order_by
    if expand is not None:
        params["expand"] = expand
    return _request("GET", f"/issue/{issue_id_or_key}/comment", params=params or None)


def add_comment(issue_id_or_key: str, body: Any, visibility: Optional[Dict[str, Any]] = None, properties: Optional[list] = None, expand: Optional[str] = None) -> Any:
    params = {"expand": expand} if expand is not None else None
    payload: Dict[str, Any] = {"body": body}
    if visibility is not None:
        payload["visibility"] = visibility
    if properties is not None:
        payload["properties"] = properties
    return _request("POST", f"/issue/{issue_id_or_key}/comment", params=params, json_body=payload)


def get_comment(issue_id_or_key: str, comment_id: str, expand: Optional[str] = None) -> Any:
    params = {"expand": expand} if expand is not None else None
    return _request("GET", f"/issue/{issue_id_or_key}/comment/{comment_id}", params=params)


def update_comment(issue_id_or_key: str, comment_id: str, body: Any, visibility: Optional[Dict[str, Any]] = None, properties: Optional[list] = None, notify_users: Optional[bool] = None, override_editable_flag: Optional[bool] = None, expand: Optional[str] = None) -> Any:
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
    return _request("PUT", f"/issue/{issue_id_or_key}/comment/{comment_id}", params=params or None, json_body=payload)


def delete_comment(issue_id_or_key: str, comment_id: str) -> Any:
    return _request("DELETE", f"/issue/{issue_id_or_key}/comment/{comment_id}")


def list_worklogs(issue_id_or_key: str, start_at: Optional[int] = None, max_results: Optional[int] = None, started_after: Optional[int] = None, started_before: Optional[int] = None, expand: Optional[str] = None) -> Any:
    params = {}
    if start_at is not None:
        params["startAt"] = start_at
    if max_results is not None:
        params["maxResults"] = max_results
    if started_after is not None:
        params["startedAfter"] = started_after
    if started_before is not None:
        params["startedBefore"] = started_before
    if expand is not None:
        params["expand"] = expand
    return _request("GET", f"/issue/{issue_id_or_key}/worklog", params=params or None)


def add_worklog(issue_id_or_key: str, time_spent_seconds: Optional[int] = None, time_spent: Optional[str] = None, started: Optional[str] = None, comment: Any = None, visibility: Optional[Dict[str, Any]] = None, properties: Optional[list] = None, notify_users: Optional[bool] = None, adjust_estimate: Optional[str] = None, new_estimate: Optional[str] = None, reduce_by: Optional[str] = None, expand: Optional[str] = None, override_editable_flag: Optional[bool] = None) -> Any:
    params: Dict[str, Any] = {}
    if notify_users is not None:
        params["notifyUsers"] = str(notify_users).lower()
    if adjust_estimate is not None:
        params["adjustEstimate"] = adjust_estimate
    if new_estimate is not None:
        params["newEstimate"] = new_estimate
    if reduce_by is not None:
        params["reduceBy"] = reduce_by
    if expand is not None:
        params["expand"] = expand
    if override_editable_flag is not None:
        params["overrideEditableFlag"] = str(override_editable_flag).lower()
    payload: Dict[str, Any] = {}
    if time_spent_seconds is not None:
        payload["timeSpentSeconds"] = time_spent_seconds
    if time_spent is not None:
        payload["timeSpent"] = time_spent
    if started is not None:
        payload["started"] = started
    if comment is not None:
        payload["comment"] = comment
    if visibility is not None:
        payload["visibility"] = visibility
    if properties is not None:
        payload["properties"] = properties
    return _request("POST", f"/issue/{issue_id_or_key}/worklog", params=params or None, json_body=payload)


def get_worklog(issue_id_or_key: str, worklog_id: str, expand: Optional[str] = None) -> Any:
    params = {"expand": expand} if expand is not None else None
    return _request("GET", f"/issue/{issue_id_or_key}/worklog/{worklog_id}", params=params)


def get_issue_watchers(issue_id_or_key: str) -> Any:
    return _request("GET", f"/issue/{issue_id_or_key}/watchers")


def add_watcher(issue_id_or_key: str, account_id: Optional[str] = None) -> Any:
    return _request("POST", f"/issue/{issue_id_or_key}/watchers", json_body=account_id)


def remove_watcher(issue_id_or_key: str, account_id: Optional[str] = None, username: Optional[str] = None) -> Any:
    params = {}
    if account_id is not None:
        params["accountId"] = account_id
    if username is not None:
        params["username"] = username
    return _request("DELETE", f"/issue/{issue_id_or_key}/watchers", params=params or None)


def bulk_is_watching(issue_ids: list[str]) -> Any:
    return _request("POST", "/issue/watching", json_body={"issueIds": issue_ids})


def get_attachment_settings() -> Any:
    return _request("GET", "/attachment/meta")


def get_attachment(attachment_id: str) -> Any:
    return _request("GET", f"/attachment/{attachment_id}")


def delete_attachment(attachment_id: str) -> Any:
    return _request("DELETE", f"/attachment/{attachment_id}")


def add_attachment(issue_id_or_key: str, file_path: str) -> Any:
    if not os.path.exists(file_path):
        return {"error": f"File not found: {file_path}"}
    with open(file_path, "rb") as fh:
        files = {"file": fh}
        return _request("POST", f"/issue/{issue_id_or_key}/attachments", headers={"X-Atlassian-Token": "no-check"}, files=files)


def create_issue_link(inward_issue_key: str, outward_issue_key: str, link_type_name: str, comment: Optional[Dict[str, Any]] = None) -> Any:
    payload: Dict[str, Any] = {
        "inwardIssue": {"key": inward_issue_key},
        "outwardIssue": {"key": outward_issue_key},
        "type": {"name": link_type_name},
    }
    if comment is not None:
        payload["comment"] = comment
    return _request("POST", "/issueLink", json_body=payload)


def get_issue_link(link_id: str) -> Any:
    return _request("GET", f"/issueLink/{link_id}")


def delete_issue_link(link_id: str) -> Any:
    return _request("DELETE", f"/issueLink/{link_id}")
