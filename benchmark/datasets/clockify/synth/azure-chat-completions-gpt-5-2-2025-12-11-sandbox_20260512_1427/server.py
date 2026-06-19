from mcp.server.fastmcp import FastMCP

from generated_tools.workspaces import (
    add_user_to_workspace,
    create_workspace,
    get_workspace,
    list_workspaces,
    update_user_cost_rate,
    update_user_hourly_rate,
    update_user_status,
    update_workspace_billable_rate,
    update_workspace_cost_rate,
)
from generated_tools.users import (
    filter_workspace_users,
    find_users_team_manager,
    get_current_user,
    get_workspace_user_profile,
    give_manager_role_to_user,
    remove_users_manager_role,
    update_user_custom_field,
    update_workspace_user_profile,
    upload_user_photo,
    list_workspace_users,
)
from generated_tools.projects import (
    assign_or_remove_users_from_project,
    create_project,
    create_project_from_template,
    delete_project,
    get_project,
    list_projects,
    update_project,
    update_project_estimate,
    update_project_memberships,
    update_project_template,
    update_project_user_billable_rate,
    update_project_user_cost_rate,
)
from generated_tools.clients import (
    create_client,
    delete_client,
    get_client,
    list_clients,
    update_client,
)
from generated_tools.tags import (
    create_tag,
    delete_tag,
    get_tag,
    list_tags,
    update_tag,
)
from generated_tools.tasks import (
    create_task,
    delete_task,
    get_task,
    list_tasks,
    update_task,
    update_task_billable_rate,
    update_task_cost_rate,
)
from generated_tools.time_entries import (
    bulk_edit_time_entries,
    create_time_entry,
    create_time_entry_for_user,
    delete_time_entries_for_user,
    delete_time_entry,
    duplicate_time_entry,
    get_time_entry,
    list_in_progress_time_entries,
    list_time_entries_for_user,
    mark_time_entries_invoiced,
    stop_running_timer,
    update_time_entry,
)

mcp = FastMCP("clockify")

# Workspace
mcp.tool()(list_workspaces)
mcp.tool()(create_workspace)
mcp.tool()(get_workspace)
mcp.tool()(update_workspace_cost_rate)
mcp.tool()(update_workspace_billable_rate)
mcp.tool()(add_user_to_workspace)
mcp.tool()(update_user_status)
mcp.tool()(update_user_cost_rate)
mcp.tool()(update_user_hourly_rate)

# Users
mcp.tool()(upload_user_photo)
mcp.tool()(get_current_user)
mcp.tool()(get_workspace_user_profile)
mcp.tool()(update_workspace_user_profile)
mcp.tool()(list_workspace_users)
mcp.tool()(filter_workspace_users)
mcp.tool()(update_user_custom_field)
mcp.tool()(find_users_team_manager)
mcp.tool()(remove_users_manager_role)
mcp.tool()(give_manager_role_to_user)

# Projects
mcp.tool()(list_projects)
mcp.tool()(create_project)
mcp.tool()(create_project_from_template)
mcp.tool()(delete_project)
mcp.tool()(get_project)
mcp.tool()(update_project)
mcp.tool()(update_project_estimate)
mcp.tool()(update_project_memberships)
mcp.tool()(assign_or_remove_users_from_project)
mcp.tool()(update_project_template)
mcp.tool()(update_project_user_cost_rate)
mcp.tool()(update_project_user_billable_rate)

# Clients
mcp.tool()(list_clients)
mcp.tool()(create_client)
mcp.tool()(delete_client)
mcp.tool()(get_client)
mcp.tool()(update_client)

# Tags
mcp.tool()(list_tags)
mcp.tool()(create_tag)
mcp.tool()(delete_tag)
mcp.tool()(get_tag)
mcp.tool()(update_tag)

# Tasks
mcp.tool()(list_tasks)
mcp.tool()(create_task)
mcp.tool()(update_task_cost_rate)
mcp.tool()(update_task_billable_rate)
mcp.tool()(delete_task)
mcp.tool()(get_task)
mcp.tool()(update_task)

# Time entries
mcp.tool()(create_time_entry)
mcp.tool()(mark_time_entries_invoiced)
mcp.tool()(list_in_progress_time_entries)
mcp.tool()(delete_time_entry)
mcp.tool()(get_time_entry)
mcp.tool()(update_time_entry)
mcp.tool()(delete_time_entries_for_user)
mcp.tool()(list_time_entries_for_user)
mcp.tool()(stop_running_timer)
mcp.tool()(create_time_entry_for_user)
mcp.tool()(bulk_edit_time_entries)
mcp.tool()(duplicate_time_entry)


if __name__ == "__main__":
    mcp.run()
