from typing import Any, Dict, List, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools.components_versions import (
    create_component,
    create_version,
    delete_component,
    delete_version,
    get_component,
    get_version,
    update_component,
    update_version,
)
from generated_tools.issues import (
    add_comment,
    add_watcher,
    add_worklog,
    assign_issue,
    create_issue,
    create_issue_link,
    delete_comment,
    delete_issue,
    get_issue,
    get_transitions,
    list_comments,
    list_worklogs,
    remove_watcher,
    search_issues,
    transition_issue,
    update_comment,
    update_issue,
)
from generated_tools.metadata import (
    create_filter,
    delete_filter,
    get_filter,
    get_group_members,
    get_user,
    list_filters,
    list_groups,
    list_issue_types,
    list_priorities,
    list_statuses,
    list_users,
)
from generated_tools.projects import (
    create_project,
    delete_project,
    get_project,
    list_project_components,
    list_project_issue_types,
    list_project_versions,
    list_projects,
    update_project,
)

mcp = FastMCP("jira-cloud")


@mcp.tool()
def jira_create_issue(
    project_key: str,
    summary: str,
    issue_type: str,
    description: Optional[Any] = None,
    fields: Optional[Dict[str, Any]] = None,
) -> Any:
    return create_issue(project_key, summary, issue_type, description, fields)


@mcp.tool()
def jira_get_issue(issue_id_or_key: str, fields: Optional[List[str]] = None, expand: Optional[str] = None) -> Any:
    return get_issue(issue_id_or_key, fields, expand)


@mcp.tool()
def jira_update_issue(issue_id_or_key: str, fields: Dict[str, Any], update: Optional[Dict[str, Any]] = None) -> Any:
    return update_issue(issue_id_or_key, fields, update)


@mcp.tool()
def jira_delete_issue(issue_id_or_key: str, delete_subtasks: bool = False) -> Any:
    return delete_issue(issue_id_or_key, delete_subtasks)


@mcp.tool()
def jira_assign_issue(issue_id_or_key: str, account_id: str) -> Any:
    return assign_issue(issue_id_or_key, account_id)


@mcp.tool()
def jira_get_transitions(issue_id_or_key: str) -> Any:
    return get_transitions(issue_id_or_key)


@mcp.tool()
def jira_transition_issue(issue_id_or_key: str, transition_id: str, fields: Optional[Dict[str, Any]] = None) -> Any:
    return transition_issue(issue_id_or_key, transition_id, fields)


@mcp.tool()
def jira_add_comment(issue_id_or_key: str, body: Any, visibility: Optional[Dict[str, str]] = None) -> Any:
    return add_comment(issue_id_or_key, body, visibility)


@mcp.tool()
def jira_list_comments(issue_id_or_key: str, start_at: int = 0, max_results: int = 50) -> Any:
    return list_comments(issue_id_or_key, start_at, max_results)


@mcp.tool()
def jira_update_comment(issue_id_or_key: str, comment_id: str, body: Any) -> Any:
    return update_comment(issue_id_or_key, comment_id, body)


@mcp.tool()
def jira_delete_comment(issue_id_or_key: str, comment_id: str) -> Any:
    return delete_comment(issue_id_or_key, comment_id)


@mcp.tool()
def jira_add_worklog(issue_id_or_key: str, time_spent: str, comment: Optional[Any] = None, started: Optional[str] = None) -> Any:
    return add_worklog(issue_id_or_key, time_spent, comment, started)


@mcp.tool()
def jira_list_worklogs(issue_id_or_key: str, start_at: int = 0, max_results: int = 50) -> Any:
    return list_worklogs(issue_id_or_key, start_at, max_results)


@mcp.tool()
def jira_add_watcher(issue_id_or_key: str, account_id: str) -> Any:
    return add_watcher(issue_id_or_key, account_id)


@mcp.tool()
def jira_remove_watcher(issue_id_or_key: str, account_id: str) -> Any:
    return remove_watcher(issue_id_or_key, account_id)


@mcp.tool()
def jira_create_issue_link(link_type: str, inward_issue_key: str, outward_issue_key: str, comment: Optional[Any] = None) -> Any:
    return create_issue_link(link_type, inward_issue_key, outward_issue_key, comment)


@mcp.tool()
def jira_search_issues(
    jql: str,
    start_at: int = 0,
    max_results: int = 50,
    fields: Optional[List[str]] = None,
    expand: Optional[str] = None,
) -> Any:
    return search_issues(jql, start_at, max_results, fields, expand)


@mcp.tool()
def jira_list_projects() -> Any:
    return list_projects()


@mcp.tool()
def jira_get_project(project_id_or_key: str, expand: Optional[str] = None) -> Any:
    return get_project(project_id_or_key, expand)


@mcp.tool()
def jira_create_project(
    key: str,
    name: str,
    project_type_key: str,
    project_template_key: str,
    lead_account_id: str,
    description: Optional[str] = None,
) -> Any:
    return create_project(key, name, project_type_key, project_template_key, lead_account_id, description)


@mcp.tool()
def jira_update_project(project_id_or_key: str, updates: Dict[str, Any]) -> Any:
    return update_project(project_id_or_key, updates)


@mcp.tool()
def jira_delete_project(project_id_or_key: str) -> Any:
    return delete_project(project_id_or_key)


@mcp.tool()
def jira_list_project_components(project_id_or_key: str) -> Any:
    return list_project_components(project_id_or_key)


@mcp.tool()
def jira_list_project_versions(project_id_or_key: str) -> Any:
    return list_project_versions(project_id_or_key)


@mcp.tool()
def jira_list_project_issue_types(project_id_or_key: str) -> Any:
    return list_project_issue_types(project_id_or_key)


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
def jira_list_users(query: Optional[str] = None, start_at: int = 0, max_results: int = 50) -> Any:
    return list_users(query, start_at, max_results)


@mcp.tool()
def jira_get_user(account_id: str, expand: Optional[str] = None) -> Any:
    return get_user(account_id, expand)


@mcp.tool()
def jira_list_groups(query: Optional[str] = None, max_results: int = 50) -> Any:
    return list_groups(query, max_results)


@mcp.tool()
def jira_get_group_members(groupname: str, start_at: int = 0, max_results: int = 50) -> Any:
    return get_group_members(groupname, start_at, max_results)


@mcp.tool()
def jira_list_filters(start_at: int = 0, max_results: int = 50) -> Any:
    return list_filters(start_at, max_results)


@mcp.tool()
def jira_get_filter(filter_id: str, expand: Optional[str] = None) -> Any:
    return get_filter(filter_id, expand)


@mcp.tool()
def jira_create_filter(name: str, jql: str, description: Optional[str] = None) -> Any:
    return create_filter(name, jql, description)


@mcp.tool()
def jira_delete_filter(filter_id: str) -> Any:
    return delete_filter(filter_id)


@mcp.tool()
def jira_create_component(project_id_or_key: str, name: str, description: Optional[str] = None) -> Any:
    return create_component(project_id_or_key, name, description)


@mcp.tool()
def jira_get_component(component_id: str) -> Any:
    return get_component(component_id)


@mcp.tool()
def jira_update_component(component_id: str, updates: Dict[str, Any]) -> Any:
    return update_component(component_id, updates)


@mcp.tool()
def jira_delete_component(component_id: str) -> Any:
    return delete_component(component_id)


@mcp.tool()
def jira_create_version(project_id: str, name: str, description: Optional[str] = None, released: Optional[bool] = None) -> Any:
    return create_version(project_id, name, description, released)


@mcp.tool()
def jira_get_version(version_id: str) -> Any:
    return get_version(version_id)


@mcp.tool()
def jira_update_version(version_id: str, updates: Dict[str, Any]) -> Any:
    return update_version(version_id, updates)


@mcp.tool()
def jira_delete_version(version_id: str) -> Any:
    return delete_version(version_id)


if __name__ == "__main__":
    mcp.run()
