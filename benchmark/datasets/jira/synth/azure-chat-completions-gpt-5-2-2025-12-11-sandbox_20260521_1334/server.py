from mcp.server.fastmcp import FastMCP

from generated_tools.attachments import (
    add_attachment,
    delete_attachment,
    get_attachment_content,
    get_attachment_expand_human,
    get_attachment_expand_raw,
    get_attachment_metadata,
    get_attachment_settings,
    get_attachment_thumbnail,
)
from generated_tools.comments import (
    add_comment,
    delete_comment,
    get_comment,
    get_comments,
    get_comments_by_ids,
    update_comment,
)
from generated_tools.components import (
    create_component,
    delete_component,
    find_components_for_projects,
    get_component,
    get_component_related_issue_counts,
    get_project_components,
    update_component,
)
from generated_tools.filters import (
    create_filter,
    delete_filter,
    get_favorite_filters,
    get_filter,
    get_filter_columns,
    get_my_filters,
    remove_filter_favourite,
    reset_filter_columns,
    search_filters,
    set_filter_columns,
    set_filter_favourite,
    update_filter,
)
from generated_tools.groups import (
    add_user_to_group,
    bulk_get_groups,
    create_group,
    delete_group,
    find_groups,
    get_users_from_group,
    remove_user_from_group,
)
from generated_tools.issue_links import create_issue_link, delete_issue_link, get_issue_link
from generated_tools.issue_types import (
    create_issue_type,
    delete_issue_type,
    get_issue_type,
    get_issue_type_alternatives,
    get_issue_types,
    get_issue_types_for_project,
    update_issue_type,
)
from generated_tools.issues import (
    assign_issue,
    create_issue,
    delete_issue,
    get_issue,
    get_transitions,
    transition_issue,
    update_issue,
)
from generated_tools.priorities import (
    create_priority,
    delete_priority,
    get_priorities,
    get_priority,
    move_priorities,
    search_priorities,
    set_default_priority,
    update_priority,
)
from generated_tools.projects import (
    create_project,
    delete_project,
    get_project,
    get_recent_projects,
    search_projects,
    update_project,
)
from generated_tools.search import (
    check_issues_against_jql,
    get_issue_picker_suggestions,
    search_issues,
)
from generated_tools.statuses import (
    bulk_create_statuses,
    bulk_delete_statuses,
    bulk_get_statuses,
    bulk_get_statuses_by_names,
    bulk_update_statuses,
    get_issue_type_usages_by_status_and_project,
    get_project_usages_by_status,
    get_workflow_usages_by_status,
    search_statuses,
)
from generated_tools.tasks import cancel_task, get_task
from generated_tools.users import (
    bulk_get_users,
    get_account_ids_for_users,
    get_user,
    get_user_groups,
    search_users,
)
from generated_tools.versions import (
    create_version,
    delete_version,
    get_project_versions,
    get_project_versions_paginated,
    get_version,
    merge_versions,
    move_version,
    update_version,
)
from generated_tools.watchers import (
    add_watcher,
    delete_watcher,
    get_is_watching_issue_bulk,
    get_issue_watchers,
)
from generated_tools.worklogs import (
    add_worklog,
    delete_worklog,
    get_worklog,
    get_worklogs,
    update_worklog,
)

mcp = FastMCP("jira-cloud")

# Issues
mcp.tool()(create_issue)
mcp.tool()(get_issue)
mcp.tool()(update_issue)
mcp.tool()(delete_issue)
mcp.tool()(assign_issue)
mcp.tool()(get_transitions)
mcp.tool()(transition_issue)

# Search
mcp.tool()(search_issues)
mcp.tool()(get_issue_picker_suggestions)
mcp.tool()(check_issues_against_jql)

# Comments
mcp.tool()(get_comments)
mcp.tool()(add_comment)
mcp.tool()(get_comment)
mcp.tool()(update_comment)
mcp.tool()(delete_comment)
mcp.tool()(get_comments_by_ids)

# Worklogs
mcp.tool()(get_worklogs)
mcp.tool()(add_worklog)
mcp.tool()(get_worklog)
mcp.tool()(update_worklog)
mcp.tool()(delete_worklog)

# Watchers
mcp.tool()(get_issue_watchers)
mcp.tool()(add_watcher)
mcp.tool()(delete_watcher)
mcp.tool()(get_is_watching_issue_bulk)

# Issue links
mcp.tool()(create_issue_link)
mcp.tool()(get_issue_link)
mcp.tool()(delete_issue_link)

# Attachments
mcp.tool()(get_attachment_settings)
mcp.tool()(get_attachment_metadata)
mcp.tool()(delete_attachment)
mcp.tool()(get_attachment_content)
mcp.tool()(get_attachment_thumbnail)
mcp.tool()(add_attachment)
mcp.tool()(get_attachment_expand_human)
mcp.tool()(get_attachment_expand_raw)

# Projects
mcp.tool()(search_projects)
mcp.tool()(get_project)
mcp.tool()(create_project)
mcp.tool()(update_project)
mcp.tool()(delete_project)
mcp.tool()(get_recent_projects)

# Components
mcp.tool()(find_components_for_projects)
mcp.tool()(create_component)
mcp.tool()(get_component)
mcp.tool()(update_component)
mcp.tool()(delete_component)
mcp.tool()(get_component_related_issue_counts)
mcp.tool()(get_project_components)

# Versions
mcp.tool()(get_project_versions_paginated)
mcp.tool()(get_project_versions)
mcp.tool()(create_version)
mcp.tool()(get_version)
mcp.tool()(update_version)
mcp.tool()(delete_version)
mcp.tool()(merge_versions)
mcp.tool()(move_version)

# Users
mcp.tool()(get_user)
mcp.tool()(bulk_get_users)
mcp.tool()(get_account_ids_for_users)
mcp.tool()(get_user_groups)
mcp.tool()(search_users)

# Groups
mcp.tool()(create_group)
mcp.tool()(delete_group)
mcp.tool()(bulk_get_groups)
mcp.tool()(get_users_from_group)
mcp.tool()(add_user_to_group)
mcp.tool()(remove_user_from_group)
mcp.tool()(find_groups)

# Filters
mcp.tool()(create_filter)
mcp.tool()(get_filter)
mcp.tool()(update_filter)
mcp.tool()(delete_filter)
mcp.tool()(get_favorite_filters)
mcp.tool()(get_my_filters)
mcp.tool()(search_filters)
mcp.tool()(get_filter_columns)
mcp.tool()(set_filter_columns)
mcp.tool()(reset_filter_columns)
mcp.tool()(set_filter_favourite)
mcp.tool()(remove_filter_favourite)

# Priorities
mcp.tool()(get_priorities)
mcp.tool()(get_priority)
mcp.tool()(search_priorities)
mcp.tool()(create_priority)
mcp.tool()(update_priority)
mcp.tool()(delete_priority)
mcp.tool()(set_default_priority)
mcp.tool()(move_priorities)

# Statuses
mcp.tool()(bulk_get_statuses)
mcp.tool()(bulk_get_statuses_by_names)
mcp.tool()(search_statuses)
mcp.tool()(bulk_create_statuses)
mcp.tool()(bulk_update_statuses)
mcp.tool()(bulk_delete_statuses)
mcp.tool()(get_issue_type_usages_by_status_and_project)
mcp.tool()(get_project_usages_by_status)
mcp.tool()(get_workflow_usages_by_status)

# Issue types
mcp.tool()(get_issue_types)
mcp.tool()(get_issue_type)
mcp.tool()(create_issue_type)
mcp.tool()(update_issue_type)
mcp.tool()(delete_issue_type)
mcp.tool()(get_issue_type_alternatives)
mcp.tool()(get_issue_types_for_project)

# Tasks
mcp.tool()(get_task)
mcp.tool()(cancel_task)


if __name__ == "__main__":
    mcp.run()
