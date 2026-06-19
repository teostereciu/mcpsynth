from typing import Any, Dict, List, Optional, Union

from .http_client import JiraClient


def issue_picker_suggestions(query: Optional[str] = None, current_jql: Optional[str] = None, current_issue_key: Optional[str] = None, current_project_id: Optional[str] = None, show_sub_tasks: Optional[bool] = None, show_sub_task_parent: Optional[bool] = None) -> Union[Dict[str, Any], list, str]:
    """GET /issue/picker"""
    client = JiraClient()
    params: Dict[str, Any] = {}
    if query is not None:
        params["query"] = query
    if current_jql is not None:
        params["currentJQL"] = current_jql
    if current_issue_key is not None:
        params["currentIssueKey"] = current_issue_key
    if current_project_id is not None:
        params["currentProjectId"] = current_project_id
    if show_sub_tasks is not None:
        params["showSubTasks"] = str(show_sub_tasks).lower()
    if show_sub_task_parent is not None:
        params["showSubTaskParent"] = str(show_sub_task_parent).lower()
    return client.request("GET", "/issue/picker", params=params or None)


def jql_match(issue_ids: List[int], jqls: List[str]) -> Union[Dict[str, Any], list, str]:
    """POST /jql/match"""
    client = JiraClient()
    body = {"issueIds": issue_ids, "jqls": jqls}
    return client.request("POST", "/jql/match", json=body)


def search_issues_get(jql: str, start_at: Optional[int] = None, max_results: Optional[int] = None, validate_query: Optional[str] = None, fields: Optional[List[str]] = None, expand: Optional[str] = None, properties: Optional[List[str]] = None, fields_by_keys: Optional[bool] = None, fail_fast: Optional[bool] = None) -> Union[Dict[str, Any], list, str]:
    """GET /search (Deprecated in docs but still useful)"""
    client = JiraClient()
    params: Dict[str, Any] = {"jql": jql}
    if start_at is not None:
        params["startAt"] = start_at
    if max_results is not None:
        params["maxResults"] = max_results
    if validate_query is not None:
        params["validateQuery"] = validate_query
    if fields is not None:
        params["fields"] = ",".join(fields)
    if expand is not None:
        params["expand"] = expand
    if properties is not None:
        params["properties"] = ",".join(properties)
    if fields_by_keys is not None:
        params["fieldsByKeys"] = str(fields_by_keys).lower()
    if fail_fast is not None:
        params["failFast"] = str(fail_fast).lower()
    return client.request("GET", "/search", params=params)


def search_issues_post(jql: str, start_at: Optional[int] = None, max_results: Optional[int] = None, validate_query: Optional[str] = None, fields: Optional[List[str]] = None, expand: Optional[List[str]] = None, properties: Optional[List[str]] = None, fields_by_keys: Optional[bool] = None) -> Union[Dict[str, Any], list, str]:
    """POST /search (Deprecated in docs but still useful)"""
    client = JiraClient()
    body: Dict[str, Any] = {"jql": jql}
    if start_at is not None:
        body["startAt"] = start_at
    if max_results is not None:
        body["maxResults"] = max_results
    if validate_query is not None:
        body["validateQuery"] = validate_query
    if fields is not None:
        body["fields"] = fields
    if expand is not None:
        body["expand"] = expand
    if properties is not None:
        body["properties"] = properties
    if fields_by_keys is not None:
        body["fieldsByKeys"] = fields_by_keys
    return client.request("POST", "/search", json=body)
