from typing import Any, Dict, List, Optional, Union

from .http_client import JiraClient


def bulk_fetch_changelogs(issue_ids_or_keys: List[str], field_ids: Optional[List[str]] = None, max_results: Optional[int] = None, next_page_token: Optional[str] = None) -> Union[Dict[str, Any], list, str]:
    """POST /changelog/bulkfetch"""
    client = JiraClient()
    body: Dict[str, Any] = {"issueIdsOrKeys": issue_ids_or_keys}
    if field_ids is not None:
        body["fieldIds"] = field_ids
    if max_results is not None:
        body["maxResults"] = max_results
    if next_page_token is not None:
        body["nextPageToken"] = next_page_token
    return client.request("POST", "/changelog/bulkfetch", json=body)


def get_events() -> Union[Dict[str, Any], list, str]:
    """GET /events"""
    client = JiraClient()
    return client.request("GET", "/events")


def create_issue(fields: Dict[str, Any], update: Optional[Dict[str, Any]] = None, transition: Optional[Dict[str, Any]] = None, properties: Optional[List[Dict[str, Any]]] = None, history_metadata: Optional[Dict[str, Any]] = None, update_history: Optional[bool] = None) -> Union[Dict[str, Any], list, str]:
    """POST /issue"""
    client = JiraClient()
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
    return client.request("POST", "/issue", params=params or None, json=body)


def get_issue(issue_id_or_key: str, fields: Optional[List[str]] = None, fields_by_keys: Optional[bool] = None, expand: Optional[str] = None, properties: Optional[List[str]] = None, update_history: Optional[bool] = None) -> Union[Dict[str, Any], list, str]:
    """GET /issue/{issueIdOrKey}"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if fields is not None:
        params["fields"] = ",".join(fields)
    if fields_by_keys is not None:
        params["fieldsByKeys"] = str(fields_by_keys).lower()
    if expand is not None:
        params["expand"] = expand
    if properties is not None:
        params["properties"] = ",".join(properties)
    if update_history is not None:
        params["updateHistory"] = str(update_history).lower()
    return client.request("GET", f"/issue/{issue_id_or_key}", params=params or None)


def update_issue(issue_id_or_key: str, fields: Optional[Dict[str, Any]] = None, update: Optional[Dict[str, Any]] = None, properties: Optional[List[Dict[str, Any]]] = None, history_metadata: Optional[Dict[str, Any]] = None, notify_users: Optional[bool] = None, override_screen_security: Optional[bool] = None, override_editable_flag: Optional[bool] = None, return_issue: Optional[bool] = None, expand: Optional[str] = None) -> Union[Dict[str, Any], list, str]:
    """PUT /issue/{issueIdOrKey}"""
    client = JiraClient()
    body: Dict[str, Any] = {}
    if fields is not None:
        body["fields"] = fields
    if update is not None:
        body["update"] = update
    if properties is not None:
        body["properties"] = properties
    if history_metadata is not None:
        body["historyMetadata"] = history_metadata
    params: Dict[str, Any] = {}
    if notify_users is not None:
        params["notifyUsers"] = str(notify_users).lower()
    if override_screen_security is not None:
        params["overrideScreenSecurity"] = str(override_screen_security).lower()
    if override_editable_flag is not None:
        params["overrideEditableFlag"] = str(override_editable_flag).lower()
    if return_issue is not None:
        params["returnIssue"] = str(return_issue).lower()
    if expand is not None:
        params["expand"] = expand
    return client.request("PUT", f"/issue/{issue_id_or_key}", params=params or None, json=body or {})


def delete_issue(issue_id_or_key: str, delete_subtasks: Optional[bool] = None) -> Union[Dict[str, Any], list, str]:
    """DELETE /issue/{issueIdOrKey}"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if delete_subtasks is not None:
        params["deleteSubtasks"] = str(delete_subtasks).lower()
    return client.request("DELETE", f"/issue/{issue_id_or_key}", params=params or None)


def assign_issue(issue_id_or_key: str, account_id: Optional[str] = None) -> Union[Dict[str, Any], list, str]:
    """PUT /issue/{issueIdOrKey}/assignee"""
    client = JiraClient()
    body: Dict[str, Any] = {}
    # Jira uses accountId; setting null unassigns
    body["accountId"] = account_id
    return client.request("PUT", f"/issue/{issue_id_or_key}/assignee", json=body)


def get_issue_changelog(issue_id_or_key: str, start_at: Optional[int] = None, max_results: Optional[int] = None) -> Union[Dict[str, Any], list, str]:
    """GET /issue/{issueIdOrKey}/changelog"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if start_at is not None:
        params["startAt"] = start_at
    if max_results is not None:
        params["maxResults"] = max_results
    return client.request("GET", f"/issue/{issue_id_or_key}/changelog", params=params or None)


def get_issue_editmeta(issue_id_or_key: str) -> Union[Dict[str, Any], list, str]:
    """GET /issue/{issueIdOrKey}/editmeta"""
    client = JiraClient()
    return client.request("GET", f"/issue/{issue_id_or_key}/editmeta")


def get_issue_transitions(issue_id_or_key: str, expand: Optional[str] = None, transition_id: Optional[str] = None, skip_remote_only_condition: Optional[bool] = None, include_unavailable_transitions: Optional[bool] = None) -> Union[Dict[str, Any], list, str]:
    """GET /issue/{issueIdOrKey}/transitions"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    if transition_id is not None:
        params["transitionId"] = transition_id
    if skip_remote_only_condition is not None:
        params["skipRemoteOnlyCondition"] = str(skip_remote_only_condition).lower()
    if include_unavailable_transitions is not None:
        params["includeUnavailableTransitions"] = str(include_unavailable_transitions).lower()
    return client.request("GET", f"/issue/{issue_id_or_key}/transitions", params=params or None)


def transition_issue(issue_id_or_key: str, transition: Dict[str, Any], fields: Optional[Dict[str, Any]] = None, update: Optional[Dict[str, Any]] = None, history_metadata: Optional[Dict[str, Any]] = None, properties: Optional[List[Dict[str, Any]]] = None, expand: Optional[str] = None) -> Union[Dict[str, Any], list, str]:
    """POST /issue/{issueIdOrKey}/transitions"""
    client = JiraClient()
    body: Dict[str, Any] = {"transition": transition}
    if fields is not None:
        body["fields"] = fields
    if update is not None:
        body["update"] = update
    if history_metadata is not None:
        body["historyMetadata"] = history_metadata
    if properties is not None:
        body["properties"] = properties
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    return client.request("POST", f"/issue/{issue_id_or_key}/transitions", params=params or None, json=body)


def get_create_meta(project_ids_or_keys: Optional[List[str]] = None, issuetype_ids: Optional[List[str]] = None, expand: Optional[str] = None) -> Union[Dict[str, Any], list, str]:
    """GET /issue/createmeta"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if project_ids_or_keys is not None:
        params["projectIdsOrKeys"] = ",".join(project_ids_or_keys)
    if issuetype_ids is not None:
        params["issuetypeIds"] = ",".join(issuetype_ids)
    if expand is not None:
        params["expand"] = expand
    return client.request("GET", "/issue/createmeta", params=params or None)
