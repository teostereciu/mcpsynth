from typing import Any, Dict, Optional

from generated_tools.issues import _request


def search_issues(jql: str, fields: Optional[list] = None, start_at: Optional[int] = None, max_results: Optional[int] = None, expand: Optional[list] = None, properties: Optional[list] = None, fields_by_keys: Optional[bool] = None, validate_query: Optional[str] = None) -> Any:
    payload: Dict[str, Any] = {"jql": jql}
    if fields is not None:
        payload["fields"] = fields
    if start_at is not None:
        payload["startAt"] = start_at
    if max_results is not None:
        payload["maxResults"] = max_results
    if expand is not None:
        payload["expand"] = expand
    if properties is not None:
        payload["properties"] = properties
    if fields_by_keys is not None:
        payload["fieldsByKeys"] = fields_by_keys
    if validate_query is not None:
        payload["validateQuery"] = validate_query
    return _request("POST", "/search", json_body=payload)


def issue_picker(query: str, current_jql: Optional[str] = None, current_issue_key: Optional[str] = None, current_project_id: Optional[str] = None, show_subtasks: Optional[bool] = None, show_subtask_parent: Optional[bool] = None) -> Any:
    params = {"query": query}
    if current_jql is not None:
        params["currentJQL"] = current_jql
    if current_issue_key is not None:
        params["currentIssueKey"] = current_issue_key
    if current_project_id is not None:
        params["currentProjectId"] = current_project_id
    if show_subtasks is not None:
        params["showSubTasks"] = str(show_subtasks).lower()
    if show_subtask_parent is not None:
        params["showSubTaskParent"] = str(show_subtask_parent).lower()
    return _request("GET", "/issue/picker", params=params)


def jql_match(issue_ids: list[int], jqls: list[str]) -> Any:
    return _request("POST", "/jql/match", json_body={"issueIds": issue_ids, "jqls": jqls})


def list_fields() -> Any:
    return _request("GET", "/field")


def search_fields(start_at: Optional[int] = None, max_results: Optional[int] = None, field_type: Optional[list] = None, ids: Optional[list] = None, query: Optional[str] = None, order_by: Optional[str] = None, expand: Optional[str] = None, project_ids: Optional[list[int]] = None) -> Any:
    params = {}
    if start_at is not None:
        params["startAt"] = start_at
    if max_results is not None:
        params["maxResults"] = max_results
    if field_type is not None:
        params["type"] = field_type
    if ids is not None:
        params["id"] = ids
    if query is not None:
        params["query"] = query
    if order_by is not None:
        params["orderBy"] = order_by
    if expand is not None:
        params["expand"] = expand
    if project_ids is not None:
        params["projectIds"] = project_ids
    return _request("GET", "/field/search", params=params)


def create_custom_field(name: str, field_type: str, description: Optional[str] = None, searcher_key: Optional[str] = None) -> Any:
    payload: Dict[str, Any] = {"name": name, "type": field_type}
    if description is not None:
        payload["description"] = description
    if searcher_key is not None:
        payload["searcherKey"] = searcher_key
    return _request("POST", "/field", json_body=payload)
