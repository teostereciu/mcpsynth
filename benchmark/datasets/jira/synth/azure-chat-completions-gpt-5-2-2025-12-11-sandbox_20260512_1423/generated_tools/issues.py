from typing import Any, Dict, List, Optional

from ._client import get_client


def create_issue(fields: Dict[str, Any], update: Optional[Dict[str, Any]] = None, update_history: Optional[bool] = None,
                 transition: Optional[Dict[str, Any]] = None, properties: Optional[List[Dict[str, Any]]] = None,
                 history_metadata: Optional[Dict[str, Any]] = None) -> Any:
    """POST /issue"""
    params = {}
    if update_history is not None:
        params["updateHistory"] = str(bool(update_history)).lower()
    body: Dict[str, Any] = {"fields": fields}
    if update is not None:
        body["update"] = update
    if transition is not None:
        body["transition"] = transition
    if properties is not None:
        body["properties"] = properties
    if history_metadata is not None:
        body["historyMetadata"] = history_metadata
    return get_client().request("POST", "/issue", params=params or None, json_body=body)


def get_issue(issue_id_or_key: str, fields: Optional[List[str]] = None, expand: Optional[str] = None,
              properties: Optional[List[str]] = None, update_history: Optional[bool] = None) -> Any:
    """GET /issue/{issueIdOrKey}"""
    params: Dict[str, Any] = {}
    if fields:
        params["fields"] = ",".join(fields)
    if expand:
        params["expand"] = expand
    if properties:
        params["properties"] = ",".join(properties)
    if update_history is not None:
        params["updateHistory"] = str(bool(update_history)).lower()
    return get_client().request("GET", f"/issue/{issue_id_or_key}", params=params or None)


def update_issue(issue_id_or_key: str, fields: Optional[Dict[str, Any]] = None, update: Optional[Dict[str, Any]] = None,
                 notify_users: Optional[bool] = None, override_screen_security: Optional[bool] = None,
                 override_editable_flag: Optional[bool] = None) -> Any:
    """PUT /issue/{issueIdOrKey}"""
    params: Dict[str, Any] = {}
    if notify_users is not None:
        params["notifyUsers"] = str(bool(notify_users)).lower()
    if override_screen_security is not None:
        params["overrideScreenSecurity"] = str(bool(override_screen_security)).lower()
    if override_editable_flag is not None:
        params["overrideEditableFlag"] = str(bool(override_editable_flag)).lower()
    body: Dict[str, Any] = {}
    if fields is not None:
        body["fields"] = fields
    if update is not None:
        body["update"] = update
    return get_client().request("PUT", f"/issue/{issue_id_or_key}", params=params or None, json_body=body or {})


def delete_issue(issue_id_or_key: str, delete_subtasks: Optional[bool] = None) -> Any:
    """DELETE /issue/{issueIdOrKey}"""
    params: Dict[str, Any] = {}
    if delete_subtasks is not None:
        params["deleteSubtasks"] = str(bool(delete_subtasks)).lower()
    return get_client().request("DELETE", f"/issue/{issue_id_or_key}", params=params or None)


def assign_issue(issue_id_or_key: str, account_id: Optional[str] = None) -> Any:
    """PUT /issue/{issueIdOrKey}/assignee"""
    body: Dict[str, Any] = {}
    # Jira: accountId null unassigns
    body["accountId"] = account_id
    return get_client().request("PUT", f"/issue/{issue_id_or_key}/assignee", json_body=body)


def get_issue_transitions(issue_id_or_key: str, expand: Optional[str] = None, transition_id: Optional[str] = None,
                          skip_remote_only_condition: Optional[bool] = None, include_unavailable_transitions: Optional[bool] = None) -> Any:
    """GET /issue/{issueIdOrKey}/transitions"""
    params: Dict[str, Any] = {}
    if expand:
        params["expand"] = expand
    if transition_id:
        params["transitionId"] = transition_id
    if skip_remote_only_condition is not None:
        params["skipRemoteOnlyCondition"] = str(bool(skip_remote_only_condition)).lower()
    if include_unavailable_transitions is not None:
        params["includeUnavailableTransitions"] = str(bool(include_unavailable_transitions)).lower()
    return get_client().request("GET", f"/issue/{issue_id_or_key}/transitions", params=params or None)


def transition_issue(issue_id_or_key: str, transition: Dict[str, Any], fields: Optional[Dict[str, Any]] = None,
                     update: Optional[Dict[str, Any]] = None, history_metadata: Optional[Dict[str, Any]] = None,
                     properties: Optional[List[Dict[str, Any]]] = None) -> Any:
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
    return get_client().request("POST", f"/issue/{issue_id_or_key}/transitions", json_body=body)


def get_issue_changelog(issue_id_or_key: str, start_at: Optional[int] = None, max_results: Optional[int] = None) -> Any:
    """GET /issue/{issueIdOrKey}/changelog"""
    params: Dict[str, Any] = {}
    if start_at is not None:
        params["startAt"] = start_at
    if max_results is not None:
        params["maxResults"] = max_results
    return get_client().request("GET", f"/issue/{issue_id_or_key}/changelog", params=params or None)


def get_create_meta(project_ids_or_keys: Optional[List[str]] = None, issuetype_ids: Optional[List[str]] = None,
                    expand: Optional[str] = None) -> Any:
    """GET /issue/createmeta"""
    params: Dict[str, Any] = {}
    if project_ids_or_keys:
        params["projectIdsOrKeys"] = ",".join(project_ids_or_keys)
    if issuetype_ids:
        params["issuetypeIds"] = ",".join(issuetype_ids)
    if expand:
        params["expand"] = expand
    return get_client().request("GET", "/issue/createmeta", params=params or None)
