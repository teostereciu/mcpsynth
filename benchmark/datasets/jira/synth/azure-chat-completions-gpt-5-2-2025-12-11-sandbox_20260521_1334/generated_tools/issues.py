from typing import Any, Dict, List, Optional

from .jira_client import JiraClient


def create_issue(fields: Dict[str, Any], update: Optional[Dict[str, Any]] = None, update_history: Optional[bool] = None,
                 transition: Optional[Dict[str, Any]] = None, properties: Optional[List[Dict[str, Any]]] = None,
                 history_metadata: Optional[Dict[str, Any]] = None) -> Any:
    """POST /issue"""
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

    return JiraClient().request("POST", "/issue", params=params or None, json_body=body)


def get_issue(issue_id_or_key: str, fields: Optional[List[str]] = None, expand: Optional[str] = None,
              properties: Optional[List[str]] = None, fields_by_keys: Optional[bool] = None,
              update_history: Optional[bool] = None) -> Any:
    """GET /issue/{issueIdOrKey}"""
    params: Dict[str, Any] = {}
    if fields is not None:
        params["fields"] = ",".join(fields)
    if expand is not None:
        params["expand"] = expand
    if properties is not None:
        params["properties"] = ",".join(properties)
    if fields_by_keys is not None:
        params["fieldsByKeys"] = str(fields_by_keys).lower()
    if update_history is not None:
        params["updateHistory"] = str(update_history).lower()

    return JiraClient().request("GET", f"/issue/{issue_id_or_key}", params=params or None)


def update_issue(issue_id_or_key: str, fields: Optional[Dict[str, Any]] = None, update: Optional[Dict[str, Any]] = None,
                 notify_users: Optional[bool] = None, override_screen_security: Optional[bool] = None,
                 override_editable_flag: Optional[bool] = None, return_issue: Optional[bool] = None,
                 expand: Optional[str] = None) -> Any:
    """PUT /issue/{issueIdOrKey}"""
    body: Dict[str, Any] = {}
    if fields is not None:
        body["fields"] = fields
    if update is not None:
        body["update"] = update

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

    return JiraClient().request("PUT", f"/issue/{issue_id_or_key}", params=params or None, json_body=body or {})


def delete_issue(issue_id_or_key: str, delete_subtasks: Optional[bool] = None) -> Any:
    """DELETE /issue/{issueIdOrKey}"""
    params: Dict[str, Any] = {}
    if delete_subtasks is not None:
        params["deleteSubtasks"] = str(delete_subtasks).lower()
    return JiraClient().request("DELETE", f"/issue/{issue_id_or_key}", params=params or None)


def assign_issue(issue_id_or_key: str, account_id: Optional[str] = None) -> Any:
    """PUT /issue/{issueIdOrKey}/assignee"""
    body: Dict[str, Any] = {"accountId": account_id}
    return JiraClient().request("PUT", f"/issue/{issue_id_or_key}/assignee", json_body=body)


def get_transitions(issue_id_or_key: str, expand: Optional[str] = None, transition_id: Optional[str] = None,
                    skip_remote_only_condition: Optional[bool] = None, include_unavailable_transitions: Optional[bool] = None) -> Any:
    """GET /issue/{issueIdOrKey}/transitions"""
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    if transition_id is not None:
        params["transitionId"] = transition_id
    if skip_remote_only_condition is not None:
        params["skipRemoteOnlyCondition"] = str(skip_remote_only_condition).lower()
    if include_unavailable_transitions is not None:
        params["includeUnavailableTransitions"] = str(include_unavailable_transitions).lower()
    return JiraClient().request("GET", f"/issue/{issue_id_or_key}/transitions", params=params or None)


def transition_issue(issue_id_or_key: str, transition: Dict[str, Any], fields: Optional[Dict[str, Any]] = None,
                     update: Optional[Dict[str, Any]] = None, history_metadata: Optional[Dict[str, Any]] = None,
                     properties: Optional[List[Dict[str, Any]]] = None, update_history: Optional[bool] = None) -> Any:
    """POST /issue/{issueIdOrKey}/transitions"""
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
    if update_history is not None:
        params["updateHistory"] = str(update_history).lower()

    return JiraClient().request("POST", f"/issue/{issue_id_or_key}/transitions", params=params or None, json_body=body)
