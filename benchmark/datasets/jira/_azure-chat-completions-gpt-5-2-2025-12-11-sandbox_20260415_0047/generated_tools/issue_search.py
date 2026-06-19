from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .jira_client import JiraClient


@mcp.tool()
def jira_search_issues(
    jql: str,
    start_at: int = 0,
    max_results: int = 50,
    fields: Optional[list[str]] = None,
    expand: Optional[list[str]] = None,
    validate_query: Optional[str] = None,
    fields_by_keys: Optional[bool] = None,
    properties: Optional[list[str]] = None,
) -> Dict[str, Any]:
    """Search for issues using JQL.

    Uses POST /rest/api/3/search.
    """

    client = JiraClient()
    payload: Dict[str, Any] = {"jql": jql, "startAt": start_at, "maxResults": max_results}
    if fields is not None:
        payload["fields"] = fields
    if expand is not None:
        payload["expand"] = expand
    if validate_query is not None:
        payload["validateQuery"] = validate_query
    if fields_by_keys is not None:
        payload["fieldsByKeys"] = fields_by_keys
    if properties is not None:
        payload["properties"] = properties
    return client.request("POST", "/search", json=payload)


@mcp.tool()
def jira_issue_picker(
    query: str,
    current_jql: Optional[str] = None,
    current_issue_key: Optional[str] = None,
    current_project_id: Optional[str] = None,
    show_sub_tasks: Optional[bool] = None,
    show_sub_task_parent: Optional[bool] = None,
) -> Dict[str, Any]:
    """Get issue picker suggestions.

    GET /rest/api/3/issue/picker
    """

    client = JiraClient()
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
    return client.request("GET", "/issue/picker", params=params)


@mcp.tool()
def jira_jql_match(issue_ids: list[int], jqls: list[str]) -> Dict[str, Any]:
    """Check issues against JQL.

    POST /rest/api/3/jql/match
    """

    client = JiraClient()
    return client.request("POST", "/jql/match", json={"issueIds": issue_ids, "jqls": jqls})
