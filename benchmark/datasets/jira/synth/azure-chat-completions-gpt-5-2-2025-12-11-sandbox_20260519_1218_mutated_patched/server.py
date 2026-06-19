from typing import Any, Dict, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools._client import JiraClient
from generated_tools import (
    issues,
    search,
    projects,
    comments,
    worklogs,
    attachments,
    watchers,
    issue_links,
    users,
    groups,
    filters,
    issue_types,
    priorities,
    statuses,
    resolutions,
    components,
    versions,
    tasks,
)

mcp = FastMCP("jira-cloud")


def _client() -> JiraClient:
    # JiraClient validates required env vars.
    return JiraClient()


# --- Issues ---


@mcp.tool()
def jira_create_issue(fields: Dict[str, Any], update: Optional[Dict[str, Any]] = None) -> Any:
    """Create an issue."""
    return issues.create_issue(_client(), fields, update=update)


@mcp.tool()
def jira_get_issue(issue_id_or_key: str, fields: Optional[list[str]] = None, expand: Optional[str] = None) -> Any:
    """Get issue details."""
    return issues.get_issue(_client(), issue_id_or_key, fields=fields, expand=expand)


@mcp.tool()
def jira_update_issue(issue_id_or_key: str, fields: Optional[Dict[str, Any]] = None, update: Optional[Dict[str, Any]] = None) -> Any:
    """Update an issue."""
    return issues.update_issue(_client(), issue_id_or_key, fields=fields, update=update)


@mcp.tool()
def jira_delete_issue(issue_id_or_key: str, delete_subtasks: Optional[bool] = None) -> Any:
    """Delete an issue."""
    return issues.delete_issue(_client(), issue_id_or_key, delete_subtasks=delete_subtasks)


@mcp.tool()
def jira_assign_issue(issue_id_or_key: str, account_id: Optional[str] = None) -> Any:
    """Assign an issue to a user (accountId). Pass null to unassign."""
    return issues.assign_issue(_client(), issue_id_or_key, account_id=account_id)


@mcp.tool()
def jira_get_transitions(issue_id_or_key: str, expand: Optional[str] = None) -> Any:
    """Get available transitions for an issue."""
    return issues.get_transitions(_client(), issue_id_or_key, expand=expand)


@mcp.tool()
def jira_transition_issue(issue_id_or_key: str, transition: Dict[str, Any], fields: Optional[Dict[str, Any]] = None) -> Any:
    """Transition an issue."""
    return issues.transition_issue(_client(), issue_id_or_key, transition, fields=fields)


@mcp.tool()
def jira_get_issue_changelog(issue_id_or_key: str, start_at: Optional[int] = None, max_results: Optional[int] = None) -> Any:
    """Get issue changelog."""
    return issues.get_issue_changelog(_client(), issue_id_or_key, start_at=start_at, max_results=max_results)


@mcp.tool()
def jira_get_create_meta(
    project_ids: Optional[list[str]] = None,
    project_keys: Optional[list[str]] = None,
    issuetype_ids: Optional[list[str]] = None,
    issuetype_names: Optional[list[str]] = None,
    expand: Optional[str] = None,
) -> Any:
    """Get create issue metadata."""
    return issues.get_create_meta(
        _client(),
        project_ids=project_ids,
        project_keys=project_keys,
        issuetype_ids=issuetype_ids,
        issuetype_names=issuetype_names,
        expand=expand,
    )


# --- Search ---


@mcp.tool()
def jira_search_issues(jql: str, start_at: Optional[int] = None, max_results: Optional[int] = None, fields: Optional[list[str]] = None) -> Any:
    """Search issues using JQL (GET /search)."""
    return search.search_issues_get(_client(), jql, start_at=start_at, max_results=max_results, fields=fields)


@mcp.tool()
def jira_issue_picker(query: str, current_jql: Optional[str] = None) -> Any:
    """Issue picker suggestions."""
    return search.issue_picker(_client(), query, current_jql=current_jql)


# --- Projects ---


@mcp.tool()
def jira_list_projects(expand: Optional[str] = None) -> Any:
    return projects.list_projects(_client(), expand=expand)


@mcp.tool()
def jira_search_projects(query: Optional[str] = None, start_at: Optional[int] = None, max_results: Optional[int] = None) -> Any:
    return projects.search_projects(_client(), query=query, start_at=start_at, max_results=max_results)


@mcp.tool()
def jira_get_project(project_id_or_key: str, expand: Optional[str] = None) -> Any:
    return projects.get_project(_client(), project_id_or_key, expand=expand)


@mcp.tool()
def jira_create_project(project: Dict[str, Any]) -> Any:
    return projects.create_project(_client(), project)


@mcp.tool()
def jira_update_project(project_id_or_key: str, project: Dict[str, Any]) -> Any:
    return projects.update_project(_client(), project_id_or_key, project)


@mcp.tool()
def jira_delete_project(project_id_or_key: str, enable_undo: Optional[bool] = None) -> Any:
    return projects.delete_project(_client(), project_id_or_key, enable_undo=enable_undo)


# --- Comments ---


@mcp.tool()
def jira_get_comments(issue_id_or_key: str, start_at: Optional[int] = None, max_results: Optional[int] = None) -> Any:
    return comments.get_comments(_client(), issue_id_or_key, start_at=start_at, max_results=max_results)


@mcp.tool()
def jira_add_comment(issue_id_or_key: str, body: Any) -> Any:
    return comments.add_comment(_client(), issue_id_or_key, body)


@mcp.tool()
def jira_update_comment(issue_id_or_key: str, comment_id: str, body: Any, notify_users: Optional[bool] = None) -> Any:
    return comments.update_comment(_client(), issue_id_or_key, comment_id, body, notify_users=notify_users)


@mcp.tool()
def jira_delete_comment(issue_id_or_key: str, comment_id: str) -> Any:
    return comments.delete_comment(_client(), issue_id_or_key, comment_id)


# --- Worklogs ---


@mcp.tool()
def jira_get_worklogs(issue_id_or_key: str, start_at: Optional[int] = None, max_results: Optional[int] = None) -> Any:
    return worklogs.get_worklogs(_client(), issue_id_or_key, start_at=start_at, max_results=max_results)


@mcp.tool()
def jira_add_worklog(issue_id_or_key: str, time_spent: Optional[str] = None, time_spent_seconds: Optional[int] = None, started: Optional[str] = None, comment: Any = None) -> Any:
    return worklogs.add_worklog(
        _client(),
        issue_id_or_key,
        time_spent=time_spent,
        time_spent_seconds=time_spent_seconds,
        started=started,
        comment=comment,
    )


@mcp.tool()
def jira_delete_worklog(issue_id_or_key: str, worklog_id: str) -> Any:
    return worklogs.delete_worklog(_client(), issue_id_or_key, worklog_id)


# --- Attachments ---


@mcp.tool()
def jira_get_attachment_meta() -> Any:
    return attachments.get_attachment_meta(_client())


@mcp.tool()
def jira_add_attachment(issue_id_or_key: str, file_path: str, filename: Optional[str] = None) -> Any:
    return attachments.add_attachment(_client(), issue_id_or_key, file_path, filename=filename)


@mcp.tool()
def jira_get_attachment(attachment_id: str) -> Any:
    return attachments.get_attachment(_client(), attachment_id)


@mcp.tool()
def jira_delete_attachment(attachment_id: str) -> Any:
    return attachments.delete_attachment(_client(), attachment_id)


# --- Watchers ---


@mcp.tool()
def jira_get_watchers(issue_id_or_key: str) -> Any:
    return watchers.get_watchers(_client(), issue_id_or_key)


@mcp.tool()
def jira_add_watcher(issue_id_or_key: str, account_id: Optional[str] = None) -> Any:
    return watchers.add_watcher(_client(), issue_id_or_key, account_id=account_id)


@mcp.tool()
def jira_remove_watcher(issue_id_or_key: str, account_id: str) -> Any:
    return watchers.remove_watcher(_client(), issue_id_or_key, account_id=account_id)


# --- Issue links ---


@mcp.tool()
def jira_create_issue_link(inward_issue_key: str, outward_issue_key: str, link_type_name: str, comment: Optional[Dict[str, Any]] = None) -> Any:
    return issue_links.create_issue_link(
        _client(),
        inward_issue_key=inward_issue_key,
        outward_issue_key=outward_issue_key,
        link_type_name=link_type_name,
        comment=comment,
    )


@mcp.tool()
def jira_delete_issue_link(link_id: str) -> Any:
    return issue_links.delete_issue_link(_client(), link_id)


# --- Users & Groups ---


@mcp.tool()
def jira_get_myself() -> Any:
    return users.get_myself(_client())


@mcp.tool()
def jira_get_user(account_id: Optional[str] = None) -> Any:
    return users.get_user(_client(), account_id=account_id)


@mcp.tool()
def jira_search_users(query: str, start_at: Optional[int] = None, max_results: Optional[int] = None) -> Any:
    return users.search_users(_client(), query, start_at=start_at, max_results=max_results)


@mcp.tool()
def jira_groups_picker(query: Optional[str] = None, max_results: Optional[int] = None) -> Any:
    return groups.groups_picker(_client(), query=query, max_results=max_results)


# --- Filters ---


@mcp.tool()
def jira_search_filters(filter_name: Optional[str] = None, start_at: Optional[int] = None, max_results: Optional[int] = None) -> Any:
    return filters.search_filters(_client(), filter_name=filter_name, start_at=start_at, max_results=max_results)


@mcp.tool()
def jira_get_filter(filter_id: str) -> Any:
    return filters.get_filter(_client(), filter_id)


# --- Metadata (issue types, priorities, statuses, resolutions) ---


@mcp.tool()
def jira_list_issue_types() -> Any:
    return issue_types.list_issue_types(_client())


@mcp.tool()
def jira_list_priorities() -> Any:
    return priorities.list_priorities(_client())


@mcp.tool()
def jira_list_resolutions() -> Any:
    return resolutions.list_resolutions(_client())


@mcp.tool()
def jira_search_statuses(project_id: Optional[str] = None, search_string: Optional[str] = None) -> Any:
    return statuses.search_statuses(_client(), project_id=project_id, search_string=search_string)


# --- Components & Versions ---


@mcp.tool()
def jira_find_components(project_ids_or_keys: Optional[list[str]] = None, query: Optional[str] = None) -> Any:
    return components.find_components(_client(), project_ids_or_keys=project_ids_or_keys, query=query)


@mcp.tool()
def jira_get_project_versions(project_id_or_key: str) -> Any:
    return versions.get_project_versions(_client(), project_id_or_key)


# --- Tasks ---


@mcp.tool()
def jira_get_task(task_id: str) -> Any:
    return tasks.get_task(_client(), task_id)


@mcp.tool()
def jira_cancel_task(task_id: str) -> Any:
    return tasks.cancel_task(_client(), task_id)


if __name__ == "__main__":
    mcp.run()
