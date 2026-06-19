from typing import Any, Dict, List, Optional

from ._client import get_client


def search_issues(jql: str, start_at: int = 0, max_results: int = 50, fields: Optional[List[str]] = None,
                 expand: Optional[List[str]] = None, properties: Optional[List[str]] = None,
                 fields_by_keys: Optional[bool] = None, validate_query: Optional[str] = None) -> Any:
    """POST /search (preferred over deprecated GET)"""
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
    return get_client().request("POST", "/search", json_body=body)


def issue_picker(query: str, current_jql: Optional[str] = None, current_issue_key: Optional[str] = None,
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
        params["showSubTasks"] = str(bool(show_sub_tasks)).lower()
    if show_sub_task_parent is not None:
        params["showSubTaskParent"] = str(bool(show_sub_task_parent)).lower()
    return get_client().request("GET", "/issue/picker", params=params)


def jql_match(issue_ids: List[int], jqls: List[str]) -> Any:
    """POST /jql/match"""
    return get_client().request("POST", "/jql/match", json_body={"issueIds": issue_ids, "jqls": jqls})
