from mcp.server.fastmcp import FastMCP

from generated_tools import attachments, comments, filters, groups, issue_links, issue_types, issues, priorities, projects, search, statuses, tasks, users, watchers, worklogs

mcp = FastMCP("jira-cloud")


# Issues
mcp.tool()(issues.create_issue)
mcp.tool()(issues.get_issue)
mcp.tool()(issues.update_issue)
mcp.tool()(issues.delete_issue)
mcp.tool()(issues.assign_issue)
mcp.tool()(issues.get_issue_changelog)
mcp.tool()(issues.bulk_fetch_changelogs)
mcp.tool()(issues.get_issue_editmeta)
mcp.tool()(issues.get_issue_transitions)
mcp.tool()(issues.transition_issue)
mcp.tool()(issues.get_create_meta)
mcp.tool()(issues.get_events)

# Search
mcp.tool()(search.search_issues_get)
mcp.tool()(search.search_issues_post)
mcp.tool()(search.issue_picker_suggestions)
mcp.tool()(search.jql_match)

# Projects
mcp.tool()(projects.get_all_projects)
mcp.tool()(projects.search_projects)
mcp.tool()(projects.get_project)
mcp.tool()(projects.create_project)
mcp.tool()(projects.update_project)
mcp.tool()(projects.delete_project)
mcp.tool()(projects.get_recent_projects)
mcp.tool()(projects.get_project_statuses)

# Comments
mcp.tool()(comments.get_issue_comments)
mcp.tool()(comments.add_comment)
mcp.tool()(comments.get_comment)
mcp.tool()(comments.update_comment)
mcp.tool()(comments.delete_comment)
mcp.tool()(comments.get_comments_by_ids)

# Worklogs
mcp.tool()(worklogs.get_issue_worklogs)
mcp.tool()(worklogs.add_worklog)
mcp.tool()(worklogs.get_worklog)
mcp.tool()(worklogs.update_worklog)
mcp.tool()(worklogs.delete_worklog)

# Tasks
mcp.tool()(tasks.get_task)
mcp.tool()(tasks.cancel_task)

# Attachments
mcp.tool()(attachments.get_attachment_settings)
mcp.tool()(attachments.get_attachment_metadata)
mcp.tool()(attachments.delete_attachment)
mcp.tool()(attachments.get_attachment_archive_metadata_human)
mcp.tool()(attachments.get_attachment_archive_metadata_raw)
mcp.tool()(attachments.add_attachment)

# Watchers
mcp.tool()(watchers.get_issue_watchers)
mcp.tool()(watchers.add_watcher)
mcp.tool()(watchers.delete_watcher)
mcp.tool()(watchers.is_watching_issue_bulk)

# Issue links
mcp.tool()(issue_links.create_issue_link)
mcp.tool()(issue_links.get_issue_link)
mcp.tool()(issue_links.delete_issue_link)

# Users
mcp.tool()(users.get_user)
mcp.tool()(users.bulk_get_users)
mcp.tool()(users.users_search)
mcp.tool()(users.get_user_groups)
mcp.tool()(users.create_user)
mcp.tool()(users.delete_user)

# Groups
mcp.tool()(groups.get_group)
mcp.tool()(groups.create_group)
mcp.tool()(groups.delete_group)
mcp.tool()(groups.bulk_get_groups)
mcp.tool()(groups.get_group_members)
mcp.tool()(groups.add_user_to_group)
mcp.tool()(groups.remove_user_from_group)
mcp.tool()(groups.groups_picker)

# Filters
mcp.tool()(filters.create_filter)
mcp.tool()(filters.get_filter)
mcp.tool()(filters.update_filter)
mcp.tool()(filters.delete_filter)
mcp.tool()(filters.search_filters)
mcp.tool()(filters.get_my_filters)
mcp.tool()(filters.get_favourite_filters)
mcp.tool()(filters.get_filter_columns)
mcp.tool()(filters.set_filter_columns)
mcp.tool()(filters.reset_filter_columns)
mcp.tool()(filters.favourite_filter)
mcp.tool()(filters.unfavourite_filter)

# Issue types
mcp.tool()(issue_types.get_all_issue_types)
mcp.tool()(issue_types.get_issue_type)
mcp.tool()(issue_types.get_issue_types_for_project)
mcp.tool()(issue_types.create_issue_type)
mcp.tool()(issue_types.update_issue_type)
mcp.tool()(issue_types.delete_issue_type)
mcp.tool()(issue_types.get_alternative_issue_types)

# Priorities
mcp.tool()(priorities.get_priorities)
mcp.tool()(priorities.get_priority)
mcp.tool()(priorities.search_priorities)
mcp.tool()(priorities.create_priority)
mcp.tool()(priorities.update_priority)
mcp.tool()(priorities.set_default_priority)
mcp.tool()(priorities.move_priorities)
mcp.tool()(priorities.delete_priority)

# Statuses
mcp.tool()(statuses.bulk_get_statuses)
mcp.tool()(statuses.bulk_update_statuses)
mcp.tool()(statuses.bulk_create_statuses)
mcp.tool()(statuses.bulk_delete_statuses)
mcp.tool()(statuses.bulk_get_statuses_by_names)
mcp.tool()(statuses.search_statuses)
mcp.tool()(statuses.get_status_project_issue_type_usages)
mcp.tool()(statuses.get_status_project_usages)
mcp.tool()(statuses.get_status_workflow_usages)


if __name__ == "__main__":
    mcp.run()
