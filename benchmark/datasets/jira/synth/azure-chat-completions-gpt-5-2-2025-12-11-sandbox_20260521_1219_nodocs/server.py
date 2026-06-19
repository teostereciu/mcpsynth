from typing import Any, Dict, List, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools.issues import (
    add_comment,
    add_watcher,
    add_worklog,
    assign_issue,
    create_issue,
    create_issue_link,
    delete_issue,
    get_comments,
    get_issue,
    get_transitions,
    get_worklogs,
    remove_watcher,
    transition_issue,
    update_issue,
)
from generated_tools.search import jql_search
from generated_tools.projects import create_project, delete_project, get_project, list_projects, update_project
from generated_tools.users_groups import find_users, get_group_members, get_user
from generated_tools.metadata import get_create_meta, list_fields, list_issue_types, list_priorities, list_statuses
from generated_tools.filters import create_filter, delete_filter, get_filter, list_my_filters, update_filter


mcp = FastMCP("jira-cloud")


@mcp.tool()
def jira_get_issue(issue_id_or_key: str, fields: Optional[List[str]] = None, expand: Optional[List[str]] = None) -> Dict[str, Any]:
    return get_issue(issue_id_or_key, fields=fields, expand=expand)


@mcp.tool()
def jira_create_issue(fields: Dict[str, Any], update: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    return create_issue(fields, update=update)


@mcp.tool()
def jira_update_issue(issue_id_or_key: str, fields: Optional[Dict[str, Any]] = None, update: Optional[Dict[str, Any]] = None, notify_users: Optional[bool] = None) -> Dict[str, Any]:
    return update_issue(issue_id_or_key, fields=fields, update=update, notify_users=notify_users)


@mcp.tool()
def jira_delete_issue(issue_id_or_key: str, delete_subtasks: Optional[bool] = None) -> Dict[str, Any]:
    return delete_issue(issue_id_or_key, delete_subtasks=delete_subtasks)


@mcp.tool()
def jira_assign_issue(issue_id_or_key: str, account_id: Optional[str]) -> Dict[str, Any]:
    return assign_issue(issue_id_or_key, account_id=account_id)


@mcp.tool()
def jira_get_transitions(issue_id_or_key: str, expand: Optional[str] = None) -> Dict[str, Any]:
    return get_transitions(issue_id_or_key, expand=expand)


@mcp.tool()
def jira_transition_issue(issue_id_or_key: str, transition_id: str, fields: Optional[Dict[str, Any]] = None, update: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    return transition_issue(issue_id_or_key, transition_id, fields=fields, update=update)


@mcp.tool()
def jira_add_comment(issue_id_or_key: str, body: Any) -> Dict[str, Any]:
    return add_comment(issue_id_or_key, body)


@mcp.tool()
def jira_get_comments(issue_id_or_key: str, start_at: int = 0, max_results: int = 50, order_by: Optional[str] = None, expand: Optional[str] = None) -> Dict[str, Any]:
    return get_comments(issue_id_or_key, start_at=start_at, max_results=max_results, order_by=order_by, expand=expand)


@mcp.tool()
def jira_add_worklog(issue_id_or_key: str, time_spent_seconds: int, comment: Optional[Any] = None, started: Optional[str] = None) -> Dict[str, Any]:
    return add_worklog(issue_id_or_key, time_spent_seconds=time_spent_seconds, comment=comment, started=started)


@mcp.tool()
def jira_get_worklogs(issue_id_or_key: str, start_at: int = 0, max_results: int = 50) -> Dict[str, Any]:
    return get_worklogs(issue_id_or_key, start_at=start_at, max_results=max_results)


@mcp.tool()
def jira_add_watcher(issue_id_or_key: str, account_id: str) -> Dict[str, Any]:
    return add_watcher(issue_id_or_key, account_id)


@mcp.tool()
def jira_remove_watcher(issue_id_or_key: str, account_id: str) -> Dict[str, Any]:
    return remove_watcher(issue_id_or_key, account_id)


@mcp.tool()
def jira_create_issue_link(type_name: str, inward_issue_key: str, outward_issue_key: str, comment: Optional[Any] = None) -> Dict[str, Any]:
    return create_issue_link(type_name, inward_issue_key, outward_issue_key, comment=comment)


@mcp.tool()
def jira_jql_search(jql: str, start_at: int = 0, max_results: int = 50, fields: Optional[List[str]] = None, expand: Optional[List[str]] = None) -> Dict[str, Any]:
    return jql_search(jql, start_at=start_at, max_results=max_results, fields=fields, expand=expand)


@mcp.tool()
def jira_list_projects(expand: Optional[str] = None, recent: Optional[int] = None) -> Any:
    return list_projects(expand=expand, recent=recent)


@mcp.tool()
def jira_get_project(project_id_or_key: str, expand: Optional[str] = None) -> Dict[str, Any]:
    return get_project(project_id_or_key, expand=expand)


@mcp.tool()
def jira_create_project(payload: Dict[str, Any]) -> Dict[str, Any]:
    return create_project(payload)


@mcp.tool()
def jira_update_project(project_id_or_key: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    return update_project(project_id_or_key, payload)


@mcp.tool()
def jira_delete_project(project_id_or_key: str, enable_undo: Optional[bool] = None) -> Dict[str, Any]:
    return delete_project(project_id_or_key, enable_undo=enable_undo)


@mcp.tool()
def jira_get_user(account_id: str, expand: Optional[str] = None) -> Dict[str, Any]:
    return get_user(account_id, expand=expand)


@mcp.tool()
def jira_find_users(query: str, max_results: int = 50, start_at: int = 0) -> Any:
    return find_users(query=query, max_results=max_results, start_at=start_at)


@mcp.tool()
def jira_get_group_members(groupname: str, start_at: int = 0, max_results: int = 50) -> Dict[str, Any]:
    return get_group_members(groupname=groupname, start_at=start_at, max_results=max_results)


@mcp.tool()
def jira_list_issue_types() -> Any:
    return list_issue_types()


@mcp.tool()
def jira_list_priorities() -> Any:
    return list_priorities()


@mcp.tool()
def jira_list_statuses() -> Any:
    return list_statuses()


@mcp.tool()
def jira_list_fields() -> Any:
    return list_fields()


@mcp.tool()
def jira_get_create_meta(project_keys: Optional[str] = None, issuetype_names: Optional[str] = None, expand: Optional[str] = None) -> Dict[str, Any]:
    return get_create_meta(project_keys=project_keys, issuetype_names=issuetype_names, expand=expand)


@mcp.tool()
def jira_get_filter(filter_id: int, expand: Optional[str] = None) -> Dict[str, Any]:
    return get_filter(filter_id, expand=expand)


@mcp.tool()
def jira_list_my_filters(expand: Optional[str] = None) -> Any:
    return list_my_filters(expand=expand)


@mcp.tool()
def jira_create_filter(name: str, jql: str, description: Optional[str] = None, favourite: Optional[bool] = None) -> Dict[str, Any]:
    return create_filter(name=name, jql=jql, description=description, favourite=favourite)


@mcp.tool()
def jira_update_filter(filter_id: int, payload: Dict[str, Any]) -> Dict[str, Any]:
    return update_filter(filter_id, payload)


@mcp.tool()
def jira_delete_filter(filter_id: int) -> Dict[str, Any]:
    return delete_filter(filter_id)


if __name__ == "__main__":
    mcp.run()
