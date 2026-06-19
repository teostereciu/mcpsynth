from typing import Any, Dict, List, Optional, Union

from ._client import JiraClient


def search_issues_get(
    client: JiraClient,
    jql: str,
    *,
    start_at: Optional[int] = None,
    max_results: Optional[int] = None,
    fields: Optional[List[str]] = None,
    expand: Optional[str] = None,
    properties: Optional[List[str]] = None,
    fields_by_keys: Optional[bool] = None,
    validate_query: Optional[str] = None,
    fail_fast: Optional[bool] = None,
) -> Any:
    params: Dict[str, Any] = {"jql": jql}
    if start_at is not None:
        params["startAt"] = start_at
    if max_results is not None:
        params["maxResults"] = max_results
    if fields is not None:
        params["fields"] = ",".join(fields)
    if expand is not None:
        params["expand"] = expand
    if properties is not None:
        params["properties"] = ",".join(properties)
    if fields_by_keys is not None:
        params["fieldsByKeys"] = str(fields_by_keys).lower()
    if validate_query is not None:
        params["validateQuery"] = validate_query
    if fail_fast is not None:
        params["failFast"] = str(fail_fast).lower()

    return client.request("GET", "/search", params=params)


def search_issues_post(
    client: JiraClient,
    jql: str,
    *,
    start_at: Optional[int] = None,
    max_results: Optional[int] = None,
    fields: Optional[List[str]] = None,
    expand: Optional[List[str]] = None,
    properties: Optional[List[str]] = None,
    fields_by_keys: Optional[bool] = None,
    validate_query: Optional[str] = None,
) -> Any:
    body: Dict[str, Any] = {"jql": jql}
    if start_at is not None:
        body["startAt"] = start_at
    if max_results is not None:
        body["maxResults"] = max_results
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

    return client.request("POST", "/search", json=body)


def issue_picker(
    client: JiraClient,
    query: str,
    *,
    current_jql: Optional[str] = None,
    current_issue_key: Optional[str] = None,
    current_project_id: Optional[str] = None,
    show_sub_tasks: Optional[bool] = None,
    show_sub_task_parent: Optional[bool] = None,
) -> Any:
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


def match_issues_against_jql(
    client: JiraClient,
    issue_ids: List[int],
    jqls: List[str],
) -> Any:
    return client.request("POST", "/jql/match", json={"issueIds": issue_ids, "jqls": jqls})


def approximate_count(
    client: JiraClient,
    jql: str,
) -> Any:
    return client.request("POST", "/search/approximate-count", json={"jql": jql})
