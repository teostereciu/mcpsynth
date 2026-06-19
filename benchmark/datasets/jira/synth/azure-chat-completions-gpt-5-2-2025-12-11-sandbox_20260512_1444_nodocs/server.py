from typing import Any, Dict, List, Optional

from mcp.server.fastmcp import FastMCP

from jira_client import JiraClient
from generated_tools import issues, search, projects, users, meta, filters, components_versions, groups

mcp = FastMCP("jira-cloud")


def _client() -> JiraClient:
    return JiraClient()


@mcp.tool()
def jira_server_info() -> Any:
    return meta.get_server_info(_client())


@mcp.tool()
def jira_myself() -> Any:
    return users.get_myself(_client())


@mcp.tool()
def jira_fields() -> Any:
    return meta.get_fields(_client())


@mcp.tool()
def jira_issue_types() -> Any:
    return meta.get_issue_types(_client())


@mcp.tool()
def jira_priorities() -> Any:
    return meta.get_priorities(_client())


@mcp.tool()
def jira_statuses() -> Any:
    return meta.get_statuses(_client())


@mcp.tool()
def jira_create_issue_metadata(project_ids: Optional[str] = None, project_keys: Optional[str] = None, issuetype_ids: Optional[str] = None, issuetype_names: Optional[str] = None, expand: Optional[str] = None) -> Any:
    return meta.get_create_issue_metadata(_client(), project_ids, project_keys, issuetype_ids, issuetype_names, expand)


# Search
@mcp.tool()
def jira_jql_search(jql: str, start_at: int = 0, max_results: int = 50, fields: Optional[List[str]] = None, expand: Optional[str] = None) -> Any:
    return search.jql_search(_client(), jql, start_at, max_results, fields, expand)


# Projects
@mcp.tool()
def jira_list_projects(expand: Optional[str] = None, recent: Optional[int] = None) -> Any:
    return projects.list_projects(_client(), expand, recent)


@mcp.tool()
def jira_get_project(project_id_or_key: str, expand: Optional[str] = None) -> Any:
    return projects.get_project(_client(), project_id_or_key, expand)


@mcp.tool()
def jira_create_project(key: str, name: str, project_type_key: str, project_template_key: str, lead_account_id: Optional[str] = None, description: Optional[str] = None) -> Any:
    return projects.create_project(_client(), key, name, project_type_key, project_template_key, lead_account_id, description)


@mcp.tool()
def jira_update_project(project_id_or_key: str, updates: Dict[str, Any]) -> Any:
    return projects.update_project(_client(), project_id_or_key, updates)


@mcp.tool()
def jira_delete_project(project_id_or_key: str) -> Any:
    return projects.delete_project(_client(), project_id_or_key)


# Issues
@mcp.tool()
def jira_get_issue(issue_id_or_key: str, fields: Optional[List[str]] = None, expand: Optional[str] = None) -> Any:
    return issues.get_issue(_client(), issue_id_or_key, fields, expand)


@mcp.tool()
def jira_create_issue(fields: Dict[str, Any], update: Optional[Dict[str, Any]] = None) -> Any:
    return issues.create_issue(_client(), fields, update)


@mcp.tool()
def jira_update_issue(issue_id_or_key: str, fields: Optional[Dict[str, Any]] = None, update: Optional[Dict[str, Any]] = None, notify_users: Optional[bool] = None) -> Any:
    return issues.update_issue(_client(), issue_id_or_key, fields, update, notify_users)


@mcp.tool()
def jira_delete_issue(issue_id_or_key: str, delete_subtasks: Optional[bool] = None) -> Any:
    return issues.delete_issue(_client(), issue_id_or_key, delete_subtasks)


@mcp.tool()
def jira_assign_issue(issue_id_or_key: str, account_id: Optional[str] = None) -> Any:
    return issues.assign_issue(_client(), issue_id_or_key, account_id)


@mcp.tool()
def jira_get_transitions(issue_id_or_key: str) -> Any:
    return issues.transitions(_client(), issue_id_or_key)


@mcp.tool()
def jira_transition_issue(issue_id_or_key: str, transition_id: str, fields: Optional[Dict[str, Any]] = None, update: Optional[Dict[str, Any]] = None, comment: Optional[Dict[str, Any]] = None) -> Any:
    return issues.transition_issue(_client(), issue_id_or_key, transition_id, fields, update, comment)


@mcp.tool()
def jira_add_comment(issue_id_or_key: str, body: Any) -> Any:
    return issues.add_comment(_client(), issue_id_or_key, body)


@mcp.tool()
def jira_get_comments(issue_id_or_key: str, start_at: int = 0, max_results: int = 50, order_by: Optional[str] = None, expand: Optional[str] = None) -> Any:
    return issues.get_comments(_client(), issue_id_or_key, start_at, max_results, order_by, expand)


@mcp.tool()
def jira_update_comment(issue_id_or_key: str, comment_id: str, body: Any) -> Any:
    return issues.update_comment(_client(), issue_id_or_key, comment_id, body)


@mcp.tool()
def jira_delete_comment(issue_id_or_key: str, comment_id: str) -> Any:
    return issues.delete_comment(_client(), issue_id_or_key, comment_id)


@mcp.tool()
def jira_add_worklog(issue_id_or_key: str, time_spent_seconds: int, comment: Optional[Any] = None, started: Optional[str] = None) -> Any:
    return issues.add_worklog(_client(), issue_id_or_key, time_spent_seconds, comment, started)


@mcp.tool()
def jira_get_worklogs(issue_id_or_key: str, start_at: int = 0, max_results: int = 50) -> Any:
    return issues.get_worklogs(_client(), issue_id_or_key, start_at, max_results)


@mcp.tool()
def jira_delete_worklog(issue_id_or_key: str, worklog_id: str) -> Any:
    return issues.delete_worklog(_client(), issue_id_or_key, worklog_id)


@mcp.tool()
def jira_add_watcher(issue_id_or_key: str, account_id: str) -> Any:
    return issues.add_watcher(_client(), issue_id_or_key, account_id)


@mcp.tool()
def jira_remove_watcher(issue_id_or_key: str, account_id: str) -> Any:
    return issues.remove_watcher(_client(), issue_id_or_key, account_id)


@mcp.tool()
def jira_create_issue_link(inward_issue_key: str, outward_issue_key: str, link_type: str, comment: Optional[Any] = None) -> Any:
    return issues.create_issue_link(_client(), inward_issue_key, outward_issue_key, link_type, comment)


@mcp.tool()
def jira_delete_issue_link(link_id: str) -> Any:
    return issues.delete_issue_link(_client(), link_id)


# Filters
@mcp.tool()
def jira_get_filter(filter_id: str, expand: Optional[str] = None) -> Any:
    return filters.get_filter(_client(), filter_id, expand)


@mcp.tool()
def jira_my_filters(expand: Optional[str] = None) -> Any:
    return filters.my_filters(_client(), expand)


@mcp.tool()
def jira_create_filter(name: str, jql: str, description: Optional[str] = None, favourite: Optional[bool] = None) -> Any:
    return filters.create_filter(_client(), name, jql, description, favourite)


@mcp.tool()
def jira_update_filter(filter_id: str, updates: Dict[str, Any]) -> Any:
    return filters.update_filter(_client(), filter_id, updates)


@mcp.tool()
def jira_delete_filter(filter_id: str) -> Any:
    return filters.delete_filter(_client(), filter_id)


# Components & Versions
@mcp.tool()
def jira_create_component(project_id: str, name: str, description: Optional[str] = None, lead_account_id: Optional[str] = None) -> Any:
    return components_versions.create_component(_client(), project_id, name, description, lead_account_id)


@mcp.tool()
def jira_get_component(component_id: str) -> Any:
    return components_versions.get_component(_client(), component_id)


@mcp.tool()
def jira_update_component(component_id: str, updates: Dict[str, Any]) -> Any:
    return components_versions.update_component(_client(), component_id, updates)


@mcp.tool()
def jira_delete_component(component_id: str) -> Any:
    return components_versions.delete_component(_client(), component_id)


@mcp.tool()
def jira_create_version(project_id: str, name: str, description: Optional[str] = None, released: Optional[bool] = None) -> Any:
    return components_versions.create_version(_client(), project_id, name, description, released)


@mcp.tool()
def jira_get_version(version_id: str) -> Any:
    return components_versions.get_version(_client(), version_id)


@mcp.tool()
def jira_update_version(version_id: str, updates: Dict[str, Any]) -> Any:
    return components_versions.update_version(_client(), version_id, updates)


@mcp.tool()
def jira_delete_version(version_id: str, move_fix_issues_to: Optional[str] = None, move_affected_issues_to: Optional[str] = None) -> Any:
    return components_versions.delete_version(_client(), version_id, move_fix_issues_to, move_affected_issues_to)


# Users & Groups
@mcp.tool()
def jira_get_user(account_id: str, expand: Optional[str] = None) -> Any:
    return users.get_user(_client(), account_id, expand)


@mcp.tool()
def jira_find_users(query: str, max_results: int = 50, start_at: int = 0) -> Any:
    return users.find_users(_client(), query, max_results, start_at)


@mcp.tool()
def jira_users_assignable_to_project(project_key_or_id: str, query: Optional[str] = None, max_results: int = 50, start_at: int = 0) -> Any:
    return users.get_users_assignable_to_project(_client(), project_key_or_id, query, max_results, start_at)


@mcp.tool()
def jira_find_groups(query: str, max_results: int = 50) -> Any:
    return groups.find_groups(_client(), query, max_results)


@mcp.tool()
def jira_get_group_members(group_id: Optional[str] = None, group_name: Optional[str] = None, include_inactive_users: bool = False, start_at: int = 0, max_results: int = 50) -> Any:
    return groups.get_group_members(_client(), group_id, group_name, include_inactive_users, start_at, max_results)


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
