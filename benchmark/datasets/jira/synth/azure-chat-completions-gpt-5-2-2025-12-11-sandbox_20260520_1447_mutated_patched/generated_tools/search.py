from typing import Any, Dict, List, Optional

from .jira_client import JiraClient


def search_issues(jql_query: str, start_index: int = 0, page_size: int = 50, fields: Optional[List[str]] = None, expand: Optional[List[str]] = None, fieldsByKeys: Optional[bool] = None, validateQuery: Optional[str] = None, properties: Optional[List[str]] = None):
    """POST /search"""
    client = JiraClient()
    body: Dict[str, Any] = {
        "jql": jql_query,
        "startAt": start_index,
        "maxResults": page_size,
    }
    if fields is not None:
        body["fields"] = fields
    if expand is not None:
        body["expand"] = expand
    if fieldsByKeys is not None:
        body["fieldsByKeys"] = fieldsByKeys
    if validateQuery is not None:
        body["validateQuery"] = validateQuery
    if properties is not None:
        body["properties"] = properties
    return client.request("POST", "/search", json=body)


def issue_picker(query: str, currentJQL: Optional[str] = None, currentIssueKey: Optional[str] = None, currentProjectId: Optional[str] = None, showSubTasks: Optional[bool] = None, showSubTaskParent: Optional[bool] = None):
    """GET /issue/picker"""
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


def match_issues_to_jql(issueIds: List[int], jqls: List[str]):
    """POST /jql_query/match"""
    client = JiraClient()
    return client.request("POST", "/jql_query/match", json={"issueIds": issueIds, "jqls": jqls})
