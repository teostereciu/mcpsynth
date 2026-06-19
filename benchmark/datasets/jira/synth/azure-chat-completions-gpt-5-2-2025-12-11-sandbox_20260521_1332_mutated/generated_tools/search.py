from typing import Any, Dict, List, Optional

from .jira_client import JiraClient


def search_issues(
    jql: str,
    *,
    startAt: int = 0,
    maxResults: int = 50,
    fields: Optional[List[str]] = None,
    expand: Optional[List[str]] = None,
    properties: Optional[List[str]] = None,
    fieldsByKeys: Optional[bool] = None,
    validateQuery: Optional[str] = None,
) -> Any:
    """POST /rest/api/3/search

    Uses JQL to search for issues.
    """
    client = JiraClient()
    body: Dict[str, Any] = {
        "jql": jql,
        "startAt": startAt,
        "maxResults": maxResults,
    }
    if fields is not None:
        body["fields"] = fields
    if expand is not None:
        body["expand"] = expand
    if properties is not None:
        body["properties"] = properties
    if fieldsByKeys is not None:
        body["fieldsByKeys"] = fieldsByKeys
    if validateQuery is not None:
        body["validateQuery"] = validateQuery
    return client.request("POST", "/search", json_body=body)


def issue_picker(
    query: str,
    *,
    currentJQL: Optional[str] = None,
    currentIssueKey: Optional[str] = None,
    currentProjectId: Optional[str] = None,
    showSubTasks: Optional[bool] = None,
    showSubTaskParent: Optional[bool] = None,
) -> Any:
    """GET /rest/api/3/issue/picker"""
    client = JiraClient()
    params: Dict[str, Any] = {"query": query}
    if currentJQL is not None:
        params["currentJQL"] = currentJQL
    if currentIssueKey is not None:
        params["currentIssueKey"] = currentIssueKey
    if currentProjectId is not None:
        params["currentProjectId"] = currentProjectId
    if showSubTasks is not None:
        params["showSubTasks"] = str(showSubTasks).lower()
    if showSubTaskParent is not None:
        params["showSubTaskParent"] = str(showSubTaskParent).lower()
    return client.request("GET", "/issue/picker", params=params)


def match_issues_against_jql(issueIds: List[int], jqls: List[str]) -> Any:
    """POST /rest/api/3/jql_query/match

    Checks whether issues match JQL queries.
    """
    client = JiraClient()
    body = {"issueIds": issueIds, "jqls": jqls}
    return client.request("POST", "/jql_query/match", json_body=body)
