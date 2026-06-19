from mcp.server.fastmcp import FastMCP

from generated_tools import (
    issues,
    search,
    comments,
    worklogs,
    attachments,
    watchers,
    issue_links,
    issue_link_types,
    projects,
    components,
    versions,
    users,
    groups,
    priorities,
    statuses,
    issue_types,
    filters,
    myself,
)

mcp = FastMCP("jira-cloud")

# Issues
mcp.tool()(issues.create_issue)
mcp.tool()(issues.get_issue)
mcp.tool()(issues.update_issue)
mcp.tool()(issues.delete_issue)
mcp.tool()(issues.assign_issue)
mcp.tool()(issues.get_transitions)
mcp.tool()(issues.transition_issue)

# Search
mcp.tool()(search.search_issues)
mcp.tool()(search.issue_picker)
mcp.tool()(search.match_issues_to_jql)

# Comments
mcp.tool()(comments.get_comments)
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

# Attachments
mcp.tool()(attachments.get_attachment_meta)
mcp.tool()(attachments.get_attachment)
mcp.tool()(attachments.delete_attachment)
mcp.tool()(attachments.add_attachment)

# Watchers
mcp.tool()(watchers.get_issue_watchers)
mcp.tool()(watchers.add_watcher)
mcp.tool()(watchers.delete_watcher)
mcp.tool()(watchers.bulk_is_watching)

# Issue links
mcp.tool()(issue_links.create_issue_link)
mcp.tool()(issue_links.get_issue_link)
mcp.tool()(issue_links.delete_issue_link)

# Issue link types
mcp.tool()(issue_link_types.list_issue_link_types)
mcp.tool()(issue_link_types.get_issue_link_type)
mcp.tool()(issue_link_types.create_issue_link_type)
mcp.tool()(issue_link_types.update_issue_link_type)
mcp.tool()(issue_link_types.delete_issue_link_type)

# Projects
mcp.tool()(projects.list_projects)
mcp.tool()(projects.search_projects)
mcp.tool()(projects.get_project)
mcp.tool()(projects.create_project)
mcp.tool()(projects.update_project)
mcp.tool()(projects.delete_project)

# Components
mcp.tool()(components.search_components)
mcp.tool()(components.create_component)
mcp.tool()(components.get_component)
mcp.tool()(components.update_component)
mcp.tool()(components.delete_component)
mcp.tool()(components.get_project_components)

# Versions
mcp.tool()(versions.list_project_versions)
mcp.tool()(versions.list_project_versions_paginated)
mcp.tool()(versions.create_version)
mcp.tool()(versions.get_version)
mcp.tool()(versions.update_version)

# Users
mcp.tool()(users.get_user)
mcp.tool()(users.bulk_get_users)
mcp.tool()(users.search_users)
mcp.tool()(users.get_user_groups)

# Groups
mcp.tool()(groups.find_groups)
mcp.tool()(groups.get_group_members)
mcp.tool()(groups.add_user_to_group)
mcp.tool()(groups.remove_user_from_group)

# Priorities
mcp.tool()(priorities.list_priorities)
mcp.tool()(priorities.get_priority)
mcp.tool()(priorities.search_priorities)

# Statuses
mcp.tool()(statuses.get_statuses)
mcp.tool()(statuses.get_statuses_by_names)
mcp.tool()(statuses.search_statuses)

# Issue types
mcp.tool()(issue_types.list_issue_types)
mcp.tool()(issue_types.get_issue_type)
mcp.tool()(issue_types.get_issue_types_for_project)
mcp.tool()(issue_types.get_alternative_issue_types)

# Filters
mcp.tool()(filters.create_filter)
mcp.tool()(filters.get_filter)
mcp.tool()(filters.update_filter)
mcp.tool()(filters.delete_filter)
mcp.tool()(filters.my_filters)
mcp.tool()(filters.favourite_filters)
mcp.tool()(filters.search_filters)

# Myself
mcp.tool()(myself.get_myself)
mcp.tool()(myself.get_my_preference)
mcp.tool()(myself.set_my_preference)
mcp.tool()(myself.delete_my_preference)


if __name__ == "__main__":
    mcp.run()
