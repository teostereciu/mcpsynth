from mcp.server.fastmcp import FastMCP

from generated_tools.attachments import (
    attachment_content_get,
    attachment_delete,
    attachment_expand_human,
    attachment_expand_raw,
    attachment_get,
    attachment_settings_get,
    attachment_thumbnail_get,
    issue_attachments_add,
)
from generated_tools.comments import (
    comment_list_by_ids,
    issue_comment_add,
    issue_comment_delete,
    issue_comment_get,
    issue_comment_update,
    issue_comments_get,
)
from generated_tools.components import (
    component_create,
    component_delete,
    component_get,
    component_related_issue_counts,
    component_update,
    components_find,
    project_components_get,
)
from generated_tools.filters import (
    filter_create,
    filter_delete,
    filter_favourite_set,
    filter_favourite_unset,
    filter_get,
    filter_update,
    filters_favourite,
    filters_my,
    filters_search,
)
from generated_tools.groups import (
    group_add_user,
    group_create,
    group_delete,
    group_get,
    group_members,
    group_remove_user,
    groups_bulk,
    groups_picker,
)
from generated_tools.issue_links import issue_link_create, issue_link_delete, issue_link_get
from generated_tools.issue_types import (
    issue_type_alternatives,
    issue_type_create,
    issue_type_delete,
    issue_type_get,
    issue_type_update,
    issue_types_for_project,
    issue_types_get_all,
)
from generated_tools.issues import (
    issue_assign,
    issue_changelog_get,
    issue_create,
    issue_createmeta,
    issue_delete,
    issue_get,
    issue_transition,
    issue_transitions_get,
    issue_update,
)
from generated_tools.priorities import (
    priorities_get_all,
    priority_create,
    priority_delete,
    priority_get,
    priority_move,
    priority_search,
    priority_set_default,
    priority_update,
)
from generated_tools.projects import (
    project_create,
    project_delete,
    project_get,
    project_statuses_get,
    project_update,
    projects_get_all,
    projects_search,
)
from generated_tools.resolutions import (
    resolution_create,
    resolution_delete,
    resolution_get,
    resolution_move,
    resolution_search,
    resolution_set_default,
    resolution_update,
    resolutions_get_all,
)
from generated_tools.search import issue_picker, jql_match, search_issues, search_issues_post
from generated_tools.statuses import (
    statuses_by_names,
    statuses_create,
    statuses_delete,
    statuses_get,
    statuses_search,
    statuses_update,
)
from generated_tools.users import (
    user_create,
    user_delete,
    user_get,
    user_groups_get,
    users_bulk_get,
    users_get_all,
    users_search,
)
from generated_tools.versions import (
    project_versions,
    project_versions_paginated,
    version_create,
    version_delete,
    version_get,
    version_merge,
    version_move,
    version_related_issue_counts,
    version_update,
)
from generated_tools.watchers import issue_is_watching_bulk, issue_watcher_add, issue_watcher_delete, issue_watchers_get
from generated_tools.worklogs import (
    issue_worklog_add,
    issue_worklog_delete,
    issue_worklog_get,
    issue_worklog_update,
    issue_worklogs_bulk_delete,
    issue_worklogs_get,
)


mcp = FastMCP("jira-cloud")

# Issues
mcp.tool()(issue_create)
mcp.tool()(issue_get)
mcp.tool()(issue_update)
mcp.tool()(issue_delete)
mcp.tool()(issue_assign)
mcp.tool()(issue_transitions_get)
mcp.tool()(issue_transition)
mcp.tool()(issue_changelog_get)
mcp.tool()(issue_createmeta)

# Comments
mcp.tool()(issue_comments_get)
mcp.tool()(issue_comment_add)
mcp.tool()(issue_comment_get)
mcp.tool()(issue_comment_update)
mcp.tool()(issue_comment_delete)
mcp.tool()(comment_list_by_ids)

# Worklogs
mcp.tool()(issue_worklogs_get)
mcp.tool()(issue_worklog_add)
mcp.tool()(issue_worklog_get)
mcp.tool()(issue_worklog_update)
mcp.tool()(issue_worklog_delete)
mcp.tool()(issue_worklogs_bulk_delete)

# Attachments
mcp.tool()(attachment_settings_get)
mcp.tool()(attachment_get)
mcp.tool()(attachment_delete)
mcp.tool()(attachment_content_get)
mcp.tool()(attachment_thumbnail_get)
mcp.tool()(attachment_expand_human)
mcp.tool()(attachment_expand_raw)
mcp.tool()(issue_attachments_add)

# Watchers
mcp.tool()(issue_watchers_get)
mcp.tool()(issue_watcher_add)
mcp.tool()(issue_watcher_delete)
mcp.tool()(issue_is_watching_bulk)

# Issue links
mcp.tool()(issue_link_create)
mcp.tool()(issue_link_get)
mcp.tool()(issue_link_delete)

# Search / JQL
mcp.tool()(search_issues)
mcp.tool()(search_issues_post)
mcp.tool()(issue_picker)
mcp.tool()(jql_match)

# Projects
mcp.tool()(projects_get_all)
mcp.tool()(projects_search)
mcp.tool()(project_get)
mcp.tool()(project_create)
mcp.tool()(project_update)
mcp.tool()(project_delete)
mcp.tool()(project_statuses_get)

# Components
mcp.tool()(components_find)
mcp.tool()(component_create)
mcp.tool()(component_get)
mcp.tool()(component_update)
mcp.tool()(component_delete)
mcp.tool()(component_related_issue_counts)
mcp.tool()(project_components_get)

# Versions
mcp.tool()(project_versions_paginated)
mcp.tool()(project_versions)
mcp.tool()(version_create)
mcp.tool()(version_get)
mcp.tool()(version_update)
mcp.tool()(version_delete)
mcp.tool()(version_merge)
mcp.tool()(version_move)
mcp.tool()(version_related_issue_counts)

# Users
mcp.tool()(user_get)
mcp.tool()(user_create)
mcp.tool()(user_delete)
mcp.tool()(users_bulk_get)
mcp.tool()(user_groups_get)
mcp.tool()(users_get_all)
mcp.tool()(users_search)

# Groups
mcp.tool()(group_get)
mcp.tool()(group_create)
mcp.tool()(group_delete)
mcp.tool()(groups_bulk)
mcp.tool()(group_members)
mcp.tool()(group_add_user)
mcp.tool()(group_remove_user)
mcp.tool()(groups_picker)

# Filters
mcp.tool()(filter_create)
mcp.tool()(filter_get)
mcp.tool()(filter_update)
mcp.tool()(filter_delete)
mcp.tool()(filters_favourite)
mcp.tool()(filters_my)
mcp.tool()(filters_search)
mcp.tool()(filter_favourite_set)
mcp.tool()(filter_favourite_unset)

# Issue types
mcp.tool()(issue_types_get_all)
mcp.tool()(issue_type_get)
mcp.tool()(issue_type_create)
mcp.tool()(issue_type_update)
mcp.tool()(issue_type_delete)
mcp.tool()(issue_type_alternatives)
mcp.tool()(issue_types_for_project)

# Priorities
mcp.tool()(priorities_get_all)
mcp.tool()(priority_get)
mcp.tool()(priority_search)
mcp.tool()(priority_create)
mcp.tool()(priority_update)
mcp.tool()(priority_set_default)
mcp.tool()(priority_move)
mcp.tool()(priority_delete)

# Resolutions
mcp.tool()(resolutions_get_all)
mcp.tool()(resolution_get)
mcp.tool()(resolution_search)
mcp.tool()(resolution_create)
mcp.tool()(resolution_update)
mcp.tool()(resolution_set_default)
mcp.tool()(resolution_move)
mcp.tool()(resolution_delete)

# Statuses
mcp.tool()(statuses_get)
mcp.tool()(statuses_by_names)
mcp.tool()(statuses_search)
mcp.tool()(statuses_create)
mcp.tool()(statuses_update)
mcp.tool()(statuses_delete)


if __name__ == "__main__":
    mcp.run()
