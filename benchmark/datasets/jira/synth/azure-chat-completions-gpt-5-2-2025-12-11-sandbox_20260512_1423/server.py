from mcp.server.fastmcp import FastMCP

from generated_tools import (
    issues,
    search,
    comments,
    projects,
    users,
    groups,
    worklogs,
    watchers,
    issue_links,
    issue_link_types,
    attachments,
    priorities,
    issue_types,
    statuses,
    myself,
)

mcp = FastMCP("jira-cloud")


# ---- Issues ----
@mcp.tool()
def jira_create_issue(fields: dict, update: dict | None = None, update_history: bool | None = None,
                      transition: dict | None = None, properties: list[dict] | None = None,
                      history_metadata: dict | None = None):
    return issues.create_issue(fields, update=update, update_history=update_history, transition=transition,
                               properties=properties, history_metadata=history_metadata)


@mcp.tool()
def jira_get_issue(issue_id_or_key: str, fields: list[str] | None = None, expand: str | None = None,
                   properties: list[str] | None = None):
    return issues.get_issue(issue_id_or_key, fields=fields, expand=expand, properties=properties)


@mcp.tool()
def jira_update_issue(issue_id_or_key: str, fields: dict | None = None, update: dict | None = None,
                      notify_users: bool | None = None, override_screen_security: bool | None = None,
                      override_editable_flag: bool | None = None):
    return issues.update_issue(
        issue_id_or_key,
        fields=fields,
        update=update,
        notify_users=notify_users,
        override_screen_security=override_screen_security,
        override_editable_flag=override_editable_flag,
    )


@mcp.tool()
def jira_delete_issue(issue_id_or_key: str, delete_subtasks: bool | None = None):
    return issues.delete_issue(issue_id_or_key, delete_subtasks=delete_subtasks)


@mcp.tool()
def jira_assign_issue(issue_id_or_key: str, account_id: str | None = None):
    return issues.assign_issue(issue_id_or_key, account_id=account_id)


@mcp.tool()
def jira_get_issue_transitions(issue_id_or_key: str, expand: str | None = None, transition_id: str | None = None,
                               skip_remote_only_condition: bool | None = None,
                               include_unavailable_transitions: bool | None = None):
    return issues.get_issue_transitions(
        issue_id_or_key,
        expand=expand,
        transition_id=transition_id,
        skip_remote_only_condition=skip_remote_only_condition,
        include_unavailable_transitions=include_unavailable_transitions,
    )


@mcp.tool()
def jira_transition_issue(issue_id_or_key: str, transition: dict, fields: dict | None = None,
                         update: dict | None = None, history_metadata: dict | None = None,
                         properties: list[dict] | None = None):
    return issues.transition_issue(
        issue_id_or_key,
        transition=transition,
        fields=fields,
        update=update,
        history_metadata=history_metadata,
        properties=properties,
    )


@mcp.tool()
def jira_get_issue_changelog(issue_id_or_key: str, start_at: int | None = None, max_results: int | None = None):
    return issues.get_issue_changelog(issue_id_or_key, start_at=start_at, max_results=max_results)


@mcp.tool()
def jira_get_create_meta(project_ids_or_keys: list[str] | None = None, issuetype_ids: list[str] | None = None,
                         expand: str | None = None):
    return issues.get_create_meta(project_ids_or_keys=project_ids_or_keys, issuetype_ids=issuetype_ids, expand=expand)


# ---- Search ----
@mcp.tool()
def jira_search_issues(jql: str, start_at: int = 0, max_results: int = 50, fields: list[str] | None = None,
                       expand: list[str] | None = None, properties: list[str] | None = None,
                       fields_by_keys: bool | None = None, validate_query: str | None = None):
    return search.search_issues(
        jql=jql,
        start_at=start_at,
        max_results=max_results,
        fields=fields,
        expand=expand,
        properties=properties,
        fields_by_keys=fields_by_keys,
        validate_query=validate_query,
    )


@mcp.tool()
def jira_issue_picker(query: str, current_jql: str | None = None, current_issue_key: str | None = None,
                      current_project_id: str | None = None, show_sub_tasks: bool | None = None,
                      show_sub_task_parent: bool | None = None):
    return search.issue_picker(
        query=query,
        current_jql=current_jql,
        current_issue_key=current_issue_key,
        current_project_id=current_project_id,
        show_sub_tasks=show_sub_tasks,
        show_sub_task_parent=show_sub_task_parent,
    )


@mcp.tool()
def jira_jql_match(issue_ids: list[int], jqls: list[str]):
    return search.jql_match(issue_ids=issue_ids, jqls=jqls)


# ---- Comments ----
@mcp.tool()
def jira_get_comments(issue_id_or_key: str, start_at: int = 0, max_results: int = 50,
                      order_by: str | None = None, expand: str | None = None):
    return comments.get_comments(issue_id_or_key, start_at=start_at, max_results=max_results, order_by=order_by, expand=expand)


@mcp.tool()
def jira_add_comment(issue_id_or_key: str, body: object, visibility: dict | None = None,
                     properties: list[dict] | None = None, expand: str | None = None):
    return comments.add_comment(issue_id_or_key, body=body, visibility=visibility, properties=properties, expand=expand)


@mcp.tool()
def jira_get_comment(issue_id_or_key: str, comment_id: str, expand: str | None = None):
    return comments.get_comment(issue_id_or_key, comment_id=comment_id, expand=expand)


@mcp.tool()
def jira_update_comment(issue_id_or_key: str, comment_id: str, body: object, visibility: dict | None = None,
                        properties: list[dict] | None = None, notify_users: bool | None = None,
                        override_editable_flag: bool | None = None, expand: str | None = None):
    return comments.update_comment(
        issue_id_or_key,
        comment_id=comment_id,
        body=body,
        visibility=visibility,
        properties=properties,
        notify_users=notify_users,
        override_editable_flag=override_editable_flag,
        expand=expand,
    )


@mcp.tool()
def jira_delete_comment(issue_id_or_key: str, comment_id: str):
    return comments.delete_comment(issue_id_or_key, comment_id=comment_id)


# ---- Worklogs ----
@mcp.tool()
def jira_get_issue_worklogs(issue_id_or_key: str, start_at: int = 0, max_results: int = 50,
                            started_after: int | None = None, started_before: int | None = None,
                            expand: str | None = None):
    return worklogs.get_issue_worklogs(
        issue_id_or_key,
        start_at=start_at,
        max_results=max_results,
        started_after=started_after,
        started_before=started_before,
        expand=expand,
    )


@mcp.tool()
def jira_add_worklog(issue_id_or_key: str, time_spent_seconds: int | None = None, time_spent: str | None = None,
                     started: str | None = None, comment: object = None, visibility: dict | None = None,
                     properties: list[dict] | None = None, notify_users: bool | None = None,
                     adjust_estimate: str | None = None, new_estimate: str | None = None, reduce_by: str | None = None,
                     expand: str | None = None, override_editable_flag: bool | None = None):
    return worklogs.add_worklog(
        issue_id_or_key,
        time_spent_seconds=time_spent_seconds,
        time_spent=time_spent,
        started=started,
        comment=comment,
        visibility=visibility,
        properties=properties,
        notify_users=notify_users,
        adjust_estimate=adjust_estimate,
        new_estimate=new_estimate,
        reduce_by=reduce_by,
        expand=expand,
        override_editable_flag=override_editable_flag,
    )


@mcp.tool()
def jira_get_worklog(issue_id_or_key: str, worklog_id: str, expand: str | None = None):
    return worklogs.get_worklog(issue_id_or_key, worklog_id=worklog_id, expand=expand)


@mcp.tool()
def jira_update_worklog(issue_id_or_key: str, worklog_id: str, payload: dict,
                        notify_users: bool | None = None, adjust_estimate: str | None = None,
                        new_estimate: str | None = None, expand: str | None = None,
                        override_editable_flag: bool | None = None):
    return worklogs.update_worklog(
        issue_id_or_key,
        worklog_id=worklog_id,
        payload=payload,
        notify_users=notify_users,
        adjust_estimate=adjust_estimate,
        new_estimate=new_estimate,
        expand=expand,
        override_editable_flag=override_editable_flag,
    )


@mcp.tool()
def jira_delete_worklog(issue_id_or_key: str, worklog_id: str, notify_users: bool | None = None,
                        adjust_estimate: str | None = None, new_estimate: str | None = None,
                        increase_by: str | None = None, override_editable_flag: bool | None = None):
    return worklogs.delete_worklog(
        issue_id_or_key,
        worklog_id=worklog_id,
        notify_users=notify_users,
        adjust_estimate=adjust_estimate,
        new_estimate=new_estimate,
        increase_by=increase_by,
        override_editable_flag=override_editable_flag,
    )


# ---- Attachments ----
@mcp.tool()
def jira_get_attachment_settings():
    return attachments.get_attachment_meta()


@mcp.tool()
def jira_get_attachment(attachment_id: str):
    return attachments.get_attachment(attachment_id)


@mcp.tool()
def jira_add_attachment(issue_id_or_key: str, file_path: str):
    return attachments.add_attachment(issue_id_or_key, file_path=file_path)


@mcp.tool()
def jira_delete_attachment(attachment_id: str):
    return attachments.delete_attachment(attachment_id)


# ---- Watchers ----
@mcp.tool()
def jira_get_issue_watchers(issue_id_or_key: str):
    return watchers.get_issue_watchers(issue_id_or_key)


@mcp.tool()
def jira_add_watcher(issue_id_or_key: str, account_id: str | None = None):
    return watchers.add_watcher(issue_id_or_key, account_id=account_id)


@mcp.tool()
def jira_remove_watcher(issue_id_or_key: str, account_id: str | None = None, username: str | None = None):
    return watchers.remove_watcher(issue_id_or_key, account_id=account_id, username=username)


# ---- Issue links ----
@mcp.tool()
def jira_create_issue_link(type_name: str, inward_issue_key: str, outward_issue_key: str, comment: dict | None = None):
    return issue_links.create_issue_link(type_name, inward_issue_key, outward_issue_key, comment=comment)


@mcp.tool()
def jira_get_issue_link(link_id: str):
    return issue_links.get_issue_link(link_id)


@mcp.tool()
def jira_delete_issue_link(link_id: str):
    return issue_links.delete_issue_link(link_id)


@mcp.tool()
def jira_get_issue_link_types():
    return issue_link_types.get_issue_link_types()


# ---- Projects ----
@mcp.tool()
def jira_project_search(start_at: int = 0, max_results: int = 50, order_by: str | None = None,
                        ids: list[int] | None = None, keys: list[str] | None = None, query: str | None = None,
                        type_key: str | None = None, category_id: int | None = None, action: str | None = None,
                        expand: str | None = None):
    return projects.project_search(
        start_at=start_at,
        max_results=max_results,
        order_by=order_by,
        ids=ids,
        keys=keys,
        query=query,
        type_key=type_key,
        category_id=category_id,
        action=action,
        expand=expand,
    )


@mcp.tool()
def jira_get_project(project_id_or_key: str, expand: str | None = None, properties: list[str] | None = None):
    return projects.get_project(project_id_or_key, expand=expand, properties=properties)


@mcp.tool()
def jira_create_project(payload: dict):
    return projects.create_project(payload)


@mcp.tool()
def jira_update_project(project_id_or_key: str, payload: dict):
    return projects.update_project(project_id_or_key, payload)


@mcp.tool()
def jira_delete_project(project_id_or_key: str, enable_undo: bool | None = None):
    return projects.delete_project(project_id_or_key, enable_undo=enable_undo)


# ---- Users & Groups ----
@mcp.tool()
def jira_get_myself(expand: str | None = None):
    return myself.get_myself(expand=expand)


@mcp.tool()
def jira_get_user(account_id: str | None = None, username: str | None = None, key: str | None = None,
                  expand: str | None = None):
    return users.get_user(account_id=account_id, username=username, key=key, expand=expand)


@mcp.tool()
def jira_user_search(query: str, start_at: int = 0, max_results: int = 50,
                     include_active: bool | None = None, include_inactive: bool | None = None):
    return users.user_search(query=query, start_at=start_at, max_results=max_results,
                             include_active=include_active, include_inactive=include_inactive)


@mcp.tool()
def jira_get_user_groups(account_id: str):
    return users.get_user_groups(account_id)


@mcp.tool()
def jira_groups_picker(query: str | None = None, max_results: int | None = None, exclude: list[str] | None = None,
                       exclude_id: list[str] | None = None, case_insensitive: bool | None = None):
    return groups.groups_picker(query=query, max_results=max_results, exclude=exclude, exclude_id=exclude_id,
                                case_insensitive=case_insensitive)


@mcp.tool()
def jira_group_members(group_id: str | None = None, group_name: str | None = None, include_inactive_users: bool = False,
                       start_at: int = 0, max_results: int = 50):
    return groups.group_members(group_id=group_id, group_name=group_name, include_inactive_users=include_inactive_users,
                                start_at=start_at, max_results=max_results)


@mcp.tool()
def jira_add_user_to_group(account_id: str, group_id: str | None = None, group_name: str | None = None):
    return groups.add_user_to_group(account_id=account_id, group_id=group_id, group_name=group_name)


@mcp.tool()
def jira_remove_user_from_group(account_id: str, group_id: str | None = None, group_name: str | None = None):
    return groups.remove_user_from_group(account_id=account_id, group_id=group_id, group_name=group_name)


# ---- Metadata helpers ----
@mcp.tool()
def jira_get_priorities():
    return priorities.get_priorities()


@mcp.tool()
def jira_get_priority(priority_id: str):
    return priorities.get_priority(priority_id)


@mcp.tool()
def jira_get_issue_types():
    return issue_types.get_issue_types()


@mcp.tool()
def jira_get_issue_type(issue_type_id: str):
    return issue_types.get_issue_type(issue_type_id)


@mcp.tool()
def jira_search_statuses(project_id: str | None = None, start_at: int = 0, max_results: int = 50,
                         search_string: str | None = None, status_category: str | None = None):
    return statuses.search_statuses(project_id=project_id, start_at=start_at, max_results=max_results,
                                    search_string=search_string, status_category=status_category)


def main():
    mcp.run()


if __name__ == "__main__":
    main()
