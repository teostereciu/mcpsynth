from typing import Any, Dict, List, Optional

from .jira_client import JiraClient, clean_params


def issue_picker(query: str, current_jql: Optional[str] = None, current_issue_key: Optional[str] = None, current_project_id: Optional[str] = None, show_sub_tasks: Optional[bool] = None, show_sub_task_parent: Optional[bool] = None) -> Dict[str, Any]:
    """GET /issue/picker - Issue picker suggestions."""
    client = JiraClient()
    params = clean_params(
        {
            "query": query,
            "currentJQL": current_jql,
            "currentIssueKey": current_issue_key,
            "currentProjectId": current_project_id,
            "showSubTasks": show_sub_tasks,
            "showSubTaskParent": show_sub_task_parent,
        }
    )
    return client.request("GET", "/issue/picker", params=params)  # type: ignore[return-value]


def jql_match(issue_ids: List[int], jqls: List[str]) -> Dict[str, Any]:
    """POST /jql/match - Check issues against JQL."""
    client = JiraClient()
    return client.request("POST", "/jql/match", json_body={"issueIds": issue_ids, "jqls": jqls})  # type: ignore[return-value]


def search_issues(
    jql: str,
    start_at: Optional[int] = None,
    max_results: Optional[int] = None,
    validate_query: Optional[str] = None,
    fields: Optional[List[str]] = None,
    expand: Optional[str] = None,
    properties: Optional[List[str]] = None,
    fields_by_keys: Optional[bool] = None,
    fail_fast: Optional[bool] = None,
) -> Dict[str, Any]:
    """GET /search - Search issues using JQL (GET)."""
    client = JiraClient()
    params = clean_params(
        {
            "jql": jql,
            "startAt": start_at,
            "maxResults": max_results,
            "validateQuery": validate_query,
            "fields": ",".join(fields) if fields else None,
            "expand": expand,
            "properties": ",".join(properties) if properties else None,
            "fieldsByKeys": fields_by_keys,
            "failFast": fail_fast,
        }
    )
    return client.request("GET", "/search", params=params)  # type: ignore[return-value]


def search_issues_post(
    jql: str,
    start_at: Optional[int] = None,
    max_results: Optional[int] = None,
    validate_query: Optional[str] = None,
    fields: Optional[List[str]] = None,
    expand: Optional[List[str]] = None,
    properties: Optional[List[str]] = None,
    fields_by_keys: Optional[bool] = None,
) -> Dict[str, Any]:
    """POST /search - Search issues using JQL (POST)."""
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
    return client.request("POST", "/search", json_body=body)  # type: ignore[return-value]
