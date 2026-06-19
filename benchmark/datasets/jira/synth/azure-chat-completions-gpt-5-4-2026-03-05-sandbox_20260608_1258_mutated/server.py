from mcp.server.fastmcp import FastMCP

from generated_tools import admin, config, issues, projects

mcp = FastMCP("jira-cloud")


@mcp.tool()
def create_issue(fields: dict, update: dict | None = None, transition: dict | None = None, properties: list | None = None, history_metadata: dict | None = None, update_history: bool | None = None):
    return issues.create_issue(fields, update, transition, properties, history_metadata, update_history)


@mcp.tool()
def get_issue(issue_id_or_key: str, fields: str | None = None, expand: str | None = None, properties: str | None = None):
    return issues.get_issue(issue_id_or_key, fields, expand, properties)


@mcp.tool()
def update_issue(issue_id_or_key: str, fields: dict | None = None, update: dict | None = None, history_metadata: dict | None = None, properties: list | None = None, notify_users: bool | None = None, override_screen_security: bool | None = None, override_editable_flag: bool | None = None, return_issue: bool | None = None):
    return issues.update_issue(issue_id_or_key, fields, update, history_metadata, properties, notify_users, override_screen_security, override_editable_flag, return_issue)


@mcp.tool()
def delete_issue(issue_id_or_key: str, delete_subtasks: bool | None = None):
    return issues.delete_issue(issue_id_or_key, delete_subtasks)


@mcp.tool()
def assign_issue(issue_id_or_key: str, account_id: str | None = None):
    return issues.assign_issue(issue_id_or_key, account_id)


@mcp.tool()
def get_transitions(issue_id_or_key: str, expand: str | None = None, transition_id: str | None = None):
    return issues.get_transitions(issue_id_or_key, expand, transition_id)


@mcp.tool()
def transition_issue(issue_id_or_key: str, transition: dict, fields: dict | None = None, update: dict | None = None, history_metadata: dict | None = None):
    return issues.transition_issue(issue_id_or_key, transition, fields, update, history_metadata)


@mcp.tool()
def search_projects(query: str | None = None, start_at: int | None = None, max_results: int | None = None, order_by: str | None = None, type_key: str | None = None, category_id: int | None = None, action: str | None = None, expand: str | None = None, status: str | None = None, properties: str | None = None):
    return projects.search_projects(start_at, max_results, order_by, query, type_key, category_id, action, expand, status, properties)


@mcp.tool()
def get_project(project_id_or_key: str, expand: str | None = None, properties: str | None = None):
    return projects.get_project(project_id_or_key, expand, properties)


@mcp.tool()
def create_project(body: dict):
    return projects.create_project(body)


@mcp.tool()
def update_project(project_id_or_key: str, body: dict):
    return projects.update_project(project_id_or_key, body)


@mcp.tool()
def delete_project(project_id_or_key: str, enable_undo: bool | None = None):
    return projects.delete_project(project_id_or_key, enable_undo)


@mcp.tool()
def get_issue_comments(issue_id_or_key: str, start_at: int | None = None, max_results: int | None = None, order_by: str | None = None, expand: str | None = None):
    return issues.get_issue_comments(issue_id_or_key, start_at, max_results, order_by, expand)


@mcp.tool()
def add_comment(issue_id_or_key: str, body: dict, visibility: dict | None = None, properties: list | None = None, expand: str | None = None):
    return issues.add_comment(issue_id_or_key, body, visibility, properties, expand)


@mcp.tool()
def update_comment(issue_id_or_key: str, comment_id: str, body: dict, visibility: dict | None = None, properties: list | None = None, notify_users: bool | None = None, override_editable_flag: bool | None = None, expand: str | None = None):
    return issues.update_comment(issue_id_or_key, comment_id, body, visibility, properties, notify_users, override_editable_flag, expand)


@mcp.tool()
def delete_comment(issue_id_or_key: str, comment_id: str):
    return issues.delete_comment(issue_id_or_key, comment_id)


@mcp.tool()
def get_issue_worklogs(issue_id_or_key: str, start_at: int | None = None, max_results: int | None = None, started_after: int | None = None, started_before: int | None = None, expand: str | None = None):
    return issues.get_issue_worklogs(issue_id_or_key, start_at, max_results, started_after, started_before, expand)


@mcp.tool()
def add_worklog(issue_id_or_key: str, time_spent_seconds: int | None = None, time_spent: str | None = None, started: str | None = None, comment: dict | None = None, visibility: dict | None = None, properties: list | None = None, notify_users: bool | None = None, adjust_estimate: str | None = None, new_estimate: str | None = None, reduce_by: str | None = None, expand: str | None = None, override_editable_flag: bool | None = None):
    return issues.add_worklog(issue_id_or_key, time_spent_seconds, time_spent, started, comment, visibility, properties, notify_users, adjust_estimate, new_estimate, reduce_by, expand, override_editable_flag)


@mcp.tool()
def get_issue_watchers(issue_id_or_key: str):
    return issues.get_issue_watchers(issue_id_or_key)


@mcp.tool()
def add_watcher(issue_id_or_key: str, account_id: str | None = None):
    return issues.add_watcher(issue_id_or_key, account_id)


@mcp.tool()
def remove_watcher(issue_id_or_key: str, account_id: str | None = None, username: str | None = None):
    return issues.remove_watcher(issue_id_or_key, account_id, username)


@mcp.tool()
def add_attachment(issue_id_or_key: str, file_paths: list[str]):
    return issues.add_attachment(issue_id_or_key, file_paths)


@mcp.tool()
def get_user(account_id: str | None = None, username: str | None = None, key: str | None = None, expand: str | None = None):
    return admin.get_user(account_id, username, key, expand)


@mcp.tool()
def bulk_get_users(account_ids: list[str], start_at: int | None = None, max_results: int | None = None):
    return admin.bulk_get_users(account_ids, start_at, max_results)


@mcp.tool()
def get_group_members(group_id: str | None = None, groupname: str | None = None, include_inactive_users: bool | None = None, start_at: int | None = None, max_results: int | None = None):
    return admin.get_group_members(group_id, groupname, include_inactive_users, start_at, max_results)


@mcp.tool()
def find_groups(query: str | None = None, exclude: list[str] | None = None, exclude_id: list[str] | None = None, max_results: int | None = None, case_insensitive: bool | None = None, account_id: str | None = None, username: str | None = None):
    return admin.find_groups(query, exclude, exclude_id, max_results, case_insensitive, account_id, username)


@mcp.tool()
def create_filter(name: str, jql: str | None = None, description: str | None = None, favourite: bool | None = None, share_permissions: list | None = None, edit_permissions: list | None = None, expand: str | None = None, override_share_permissions: bool | None = None):
    return config.create_filter(name, jql, description, favourite, share_permissions, edit_permissions, expand, override_share_permissions)


@mcp.tool()
def search_filters(filter_name: str | None = None, account_id: str | None = None, owner: str | None = None, groupname: str | None = None, group_id: str | None = None, project_id: int | None = None, ids: list[int] | None = None, order_by: str | None = None, start_at: int | None = None, max_results: int | None = None, expand: str | None = None):
    return config.search_filters(filter_name, account_id, owner, groupname, group_id, project_id, ids, order_by, start_at, max_results, expand)


@mcp.tool()
def get_issue_types():
    return config.get_issue_types()


@mcp.tool()
def get_priorities():
    return config.get_priorities()


@mcp.tool()
def search_statuses(project_id: str | None = None, start_at: int | None = None, max_results: int | None = None, search_string: str | None = None, status_category: str | None = None):
    return config.search_statuses(project_id, start_at, max_results, search_string, status_category)


if __name__ == "__main__":
    mcp.run()
