from typing import Any, Dict, List, Optional

from .jira_client import JiraClient


def search_issues(jql: str, start_at: int = 0, max_results: int = 50, fields: Optional[List[str]] = None,
                 expand: Optional[List[str]] = None, properties: Optional[List[str]] = None,
                 fields_by_keys: Optional[bool] = None, validate_query: Optional[str] = None,
                 fail_fast: Optional[bool] = None) -> Any:
    """POST /search

    Uses POST variant to avoid GET deprecation/removal.
    """
    body: Dict[str, Any] = {
        "jql": jql,
        "startAt": start_at,
        "maxResults": max_results,
    }
    if fields is not None:
        body["fields"] = fields
    if expand is not None:
        body["expand"] = expand
    if properties is not None:
        body["properties"] = properties
    if fields_by_keys is not None:
        body["fieldsByKeys"] = fields_by_keys
    if validate_query is not None:
        body["validateQuery"] = validate_query
    if fail_fast is not None:
        body["failFast"] = fail_fast

    return JiraClient().request("POST", "/search", json_body=body)


def get_issue_picker_suggestions(query: str, current_jql: Optional[str] = None, current_issue_key: Optional[str] = None,
                                 current_project_id: Optional[str] = None, show_sub_tasks: Optional[bool] = None,
                                 show_sub_task_parent: Optional[bool] = None) -> Any:
    """GET /issue/picker"""
    params: Dict[str, Any] = {"query": query}
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

    return JiraClient().request("GET", "/issue/picker", params=params)


def check_issues_against_jql(issue_ids: List[int], jqls: List[str]) -> Any:
    """POST /jql/match"""
    body = {"issueIds": issue_ids, "jqls": jqls}
    return JiraClient().request("POST", "/jql/match", json_body=body)
