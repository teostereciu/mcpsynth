"""
Jira Cloud REST API v3 — MCP Server
Runs over stdio using FastMCP.

Environment variables required:
  JIRA_BASE_URL   — e.g. https://your-org.atlassian.net
  JIRA_EMAIL      — your Atlassian account email
  JIRA_API_TOKEN  — your Atlassian API token
"""

from mcp.server.fastmcp import FastMCP

# ── Import all domain tool functions ──────────────────────────────────────────
# Issues
from generated_tools.issues import (
    get_issue,
    create_issue,
    update_issue,
    delete_issue,
    assign_issue,
    get_issue_transitions,
    transition_issue,
    get_issue_metadata,
    get_create_issue_metadata,
    bulk_create_issues,
    get_issue_changelog,
    get_issue_watchers,
    add_watcher,
    remove_watcher,
    get_issue_votes,
    add_vote,
    remove_vote,
    get_issue_remote_links,
    add_remote_link,
    delete_remote_link,
    notify_issue,
)

# Search / JQL
from generated_tools.search import (
    search_issues,
    search_issues_get,
    get_field_reference,
    parse_jql,
    get_jql_autocomplete_suggestions,
)

# Comments
from generated_tools.comments import (
    get_issue_comments,
    get_comment,
    add_comment,
    update_comment,
    delete_comment,
)

# Worklogs
from generated_tools.worklogs import (
    get_issue_worklogs,
    get_worklog,
    add_worklog,
    update_worklog,
    delete_worklog,
    get_updated_worklogs,
    get_deleted_worklogs,
)

# Attachments
from generated_tools.attachments import (
    get_attachment_metadata,
    delete_attachment,
    get_attachment_settings,
    upload_attachment,
    get_issue_attachments,
    get_attachment_thumbnail,
)

# Issue Links
from generated_tools.issue_links import (
    get_issue_link,
    create_issue_link,
    delete_issue_link,
    get_issue_link_types,
    get_issue_link_type,
    create_issue_link_type,
    update_issue_link_type,
    delete_issue_link_type,
)

# Projects
from generated_tools.projects import (
    get_all_projects,
    search_projects,
    get_project,
    create_project,
    update_project,
    delete_project,
    archive_project,
    restore_project,
    get_project_statuses,
    get_project_issue_types,
    get_project_roles,
    get_project_role,
    add_actors_to_project_role,
    delete_actor_from_project_role,
    get_project_categories,
    get_project_category,
    create_project_category,
    get_project_property,
    set_project_property,
    delete_project_property,
)

# Components
from generated_tools.components import (
    get_project_components,
    get_project_components_list,
    get_component,
    create_component,
    update_component,
    delete_component,
    get_component_issue_count,
)

# Versions
from generated_tools.versions import (
    get_project_versions,
    get_project_versions_paginated,
    get_version,
    create_version,
    update_version,
    delete_version,
    merge_versions,
    get_version_related_issues,
    get_version_unresolved_issue_count,
    move_version,
)

# Users
from generated_tools.users import (
    get_current_user,
    get_user,
    find_users,
    find_users_for_picker,
    find_assignable_users,
    find_users_with_permissions,
    get_user_groups,
    get_account_ids_for_users,
    get_all_users,
)

# Groups
from generated_tools.groups import (
    get_group,
    create_group,
    delete_group,
    get_group_members,
    add_user_to_group,
    remove_user_from_group,
    find_groups,
    bulk_get_groups,
)

# Filters
from generated_tools.filters import (
    get_filter,
    create_filter,
    update_filter,
    delete_filter,
    get_my_filters,
    get_favourite_filters,
    search_filters,
    get_filter_columns,
    set_filter_columns,
    reset_filter_columns,
    get_filter_sharing,
    add_filter_sharing,
    delete_filter_sharing,
)

# Issue Types
from generated_tools.issue_types import (
    get_all_issue_types,
    get_issue_type,
    create_issue_type,
    update_issue_type,
    delete_issue_type,
    get_issue_type_alternatives,
    get_issue_types_for_project,
    get_issue_type_screen_schemes,
    get_issue_type_schemes,
)

# Priorities & Statuses
from generated_tools.priorities import (
    get_priorities,
    get_priority,
    search_priorities,
    create_priority,
    update_priority,
    delete_priority,
    set_default_priority,
    move_priorities,
    get_statuses,
    get_status,
    get_status_categories,
    get_status_category,
    search_statuses,
)

# Fields
from generated_tools.fields import (
    get_all_fields,
    get_custom_fields,
    create_custom_field,
    update_custom_field,
    delete_custom_field,
    get_field_contexts,
    get_field_options,
    create_field_option,
    update_field_option,
    delete_field_option,
)

# Permissions
from generated_tools.permissions import (
    get_my_permissions,
    get_all_permissions,
    get_bulk_permissions,
    get_permitted_projects,
    get_permission_schemes,
    get_permission_scheme,
    get_project_permission_scheme,
)

# Boards & Sprints
from generated_tools.boards_sprints import (
    get_boards,
    get_board,
    create_board,
    delete_board,
    get_board_issues,
    get_board_sprints,
    get_board_backlog,
    get_board_epics,
    get_sprint,
    create_sprint,
    update_sprint,
    delete_sprint,
    get_sprint_issues,
    move_issues_to_sprint,
    move_issues_to_backlog,
    start_sprint,
    close_sprint,
)

# Dashboards
from generated_tools.dashboards import (
    get_dashboards,
    search_dashboards,
    get_dashboard,
    create_dashboard,
    update_dashboard,
    delete_dashboard,
    copy_dashboard,
    get_dashboard_gadgets,
    add_dashboard_gadget,
    update_dashboard_gadget,
    remove_dashboard_gadget,
    get_dashboard_item_property,
    set_dashboard_item_property,
)

# Screens
from generated_tools.screens import (
    get_screens,
    get_screen,
    create_screen,
    update_screen,
    delete_screen,
    get_screen_tabs,
    create_screen_tab,
    update_screen_tab,
    delete_screen_tab,
    get_screen_tab_fields,
    add_field_to_screen_tab,
    remove_field_from_screen_tab,
    get_available_screen_fields,
    get_screen_schemes,
)

# Workflows
from generated_tools.workflows import (
    get_workflows,
    search_workflows,
    get_workflow_transitions,
    get_workflow_schemes,
    get_workflow_scheme,
    create_workflow_scheme,
    update_workflow_scheme,
    delete_workflow_scheme,
    get_project_workflow_scheme,
    get_all_workflow_statuses,
)

# Issue Properties, Security, Labels, Resolutions
from generated_tools.issue_properties import (
    get_issue_properties,
    get_issue_property,
    set_issue_property,
    delete_issue_property,
    bulk_set_issue_properties,
    bulk_delete_issue_properties,
    get_issue_security_schemes,
    get_issue_security_scheme,
    get_issue_security_level,
    get_project_issue_security_scheme,
    get_all_labels,
    get_resolutions,
    get_resolution,
    search_resolutions,
)

# Server Info, Config, Notifications
from generated_tools.server_info import (
    get_server_info,
    get_application_roles,
    get_application_role,
    get_audit_records,
    get_configuration,
    get_global_settings,
    get_time_tracking_configuration,
    get_time_tracking_providers,
    get_avatars,
    get_system_avatars,
    get_issue_navigator_default_columns,
    get_my_preferences,
    get_locale,
    get_notification_schemes,
    get_notification_scheme,
    get_project_notification_scheme,
)

# ── Build the unified MCP server ──────────────────────────────────────────────
mcp = FastMCP("jira-cloud")

# Register every tool function with the main server
_ALL_TOOLS = [
    # Issues
    get_issue, create_issue, update_issue, delete_issue, assign_issue,
    get_issue_transitions, transition_issue, get_issue_metadata,
    get_create_issue_metadata, bulk_create_issues, get_issue_changelog,
    get_issue_watchers, add_watcher, remove_watcher,
    get_issue_votes, add_vote, remove_vote,
    get_issue_remote_links, add_remote_link, delete_remote_link, notify_issue,
    # Search
    search_issues, search_issues_get, get_field_reference,
    parse_jql, get_jql_autocomplete_suggestions,
    # Comments
    get_issue_comments, get_comment, add_comment, update_comment, delete_comment,
    # Worklogs
    get_issue_worklogs, get_worklog, add_worklog, update_worklog, delete_worklog,
    get_updated_worklogs, get_deleted_worklogs,
    # Attachments
    get_attachment_metadata, delete_attachment, get_attachment_settings,
    upload_attachment, get_issue_attachments, get_attachment_thumbnail,
    # Issue Links
    get_issue_link, create_issue_link, delete_issue_link,
    get_issue_link_types, get_issue_link_type,
    create_issue_link_type, update_issue_link_type, delete_issue_link_type,
    # Projects
    get_all_projects, search_projects, get_project, create_project,
    update_project, delete_project, archive_project, restore_project,
    get_project_statuses, get_project_issue_types,
    get_project_roles, get_project_role,
    add_actors_to_project_role, delete_actor_from_project_role,
    get_project_categories, get_project_category, create_project_category,
    get_project_property, set_project_property, delete_project_property,
    # Components
    get_project_components, get_project_components_list, get_component,
    create_component, update_component, delete_component, get_component_issue_count,
    # Versions
    get_project_versions, get_project_versions_paginated, get_version,
    create_version, update_version, delete_version, merge_versions,
    get_version_related_issues, get_version_unresolved_issue_count, move_version,
    # Users
    get_current_user, get_user, find_users, find_users_for_picker,
    find_assignable_users, find_users_with_permissions,
    get_user_groups, get_account_ids_for_users, get_all_users,
    # Groups
    get_group, create_group, delete_group, get_group_members,
    add_user_to_group, remove_user_from_group, find_groups, bulk_get_groups,
    # Filters
    get_filter, create_filter, update_filter, delete_filter,
    get_my_filters, get_favourite_filters, search_filters,
    get_filter_columns, set_filter_columns, reset_filter_columns,
    get_filter_sharing, add_filter_sharing, delete_filter_sharing,
    # Issue Types
    get_all_issue_types, get_issue_type, create_issue_type,
    update_issue_type, delete_issue_type, get_issue_type_alternatives,
    get_issue_types_for_project, get_issue_type_screen_schemes, get_issue_type_schemes,
    # Priorities & Statuses
    get_priorities, get_priority, search_priorities,
    create_priority, update_priority, delete_priority,
    set_default_priority, move_priorities,
    get_statuses, get_status, get_status_categories, get_status_category, search_statuses,
    # Fields
    get_all_fields, get_custom_fields, create_custom_field,
    update_custom_field, delete_custom_field, get_field_contexts,
    get_field_options, create_field_option, update_field_option, delete_field_option,
    # Permissions
    get_my_permissions, get_all_permissions, get_bulk_permissions,
    get_permitted_projects, get_permission_schemes,
    get_permission_scheme, get_project_permission_scheme,
    # Boards & Sprints
    get_boards, get_board, create_board, delete_board,
    get_board_issues, get_board_sprints, get_board_backlog, get_board_epics,
    get_sprint, create_sprint, update_sprint, delete_sprint,
    get_sprint_issues, move_issues_to_sprint, move_issues_to_backlog,
    start_sprint, close_sprint,
    # Dashboards
    get_dashboards, search_dashboards, get_dashboard,
    create_dashboard, update_dashboard, delete_dashboard, copy_dashboard,
    get_dashboard_gadgets, add_dashboard_gadget,
    update_dashboard_gadget, remove_dashboard_gadget,
    get_dashboard_item_property, set_dashboard_item_property,
    # Screens
    get_screens, get_screen, create_screen, update_screen, delete_screen,
    get_screen_tabs, create_screen_tab, update_screen_tab, delete_screen_tab,
    get_screen_tab_fields, add_field_to_screen_tab, remove_field_from_screen_tab,
    get_available_screen_fields, get_screen_schemes,
    # Workflows
    get_workflows, search_workflows, get_workflow_transitions,
    get_workflow_schemes, get_workflow_scheme,
    create_workflow_scheme, update_workflow_scheme, delete_workflow_scheme,
    get_project_workflow_scheme, get_all_workflow_statuses,
    # Issue Properties, Security, Labels, Resolutions
    get_issue_properties, get_issue_property, set_issue_property, delete_issue_property,
    bulk_set_issue_properties, bulk_delete_issue_properties,
    get_issue_security_schemes, get_issue_security_scheme,
    get_issue_security_level, get_project_issue_security_scheme,
    get_all_labels, get_resolutions, get_resolution, search_resolutions,
    # Server Info
    get_server_info, get_application_roles, get_application_role,
    get_audit_records, get_configuration, get_global_settings,
    get_time_tracking_configuration, get_time_tracking_providers,
    get_avatars, get_system_avatars, get_issue_navigator_default_columns,
    get_my_preferences, get_locale,
    get_notification_schemes, get_notification_scheme, get_project_notification_scheme,
]

for _fn in _ALL_TOOLS:
    mcp.tool()(_fn)


if __name__ == "__main__":
    mcp.run(transport="stdio")
