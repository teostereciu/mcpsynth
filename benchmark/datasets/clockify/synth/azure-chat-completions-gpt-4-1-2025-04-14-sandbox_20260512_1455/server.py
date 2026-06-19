import os
from mcp.server.fastmcp import FastMCP
import generated_tools.workspaces as workspaces
import generated_tools.users as users
import generated_tools.projects as projects
import generated_tools.time_entries as time_entries
import generated_tools.clients as clients
import generated_tools.tags as tags
import generated_tools.tasks as tasks

TOOLS = {
    "list_workspaces": workspaces.list_workspaces,
    "get_workspace_details": workspaces.get_workspace_details,
    "get_current_user": users.get_current_user,
    "list_workspace_users": users.list_workspace_users,
    "list_projects": projects.list_projects,
    "create_project": projects.create_project,
    "update_project": projects.update_project,
    "delete_project": projects.delete_project,
    "list_time_entries": time_entries.list_time_entries,
    "create_time_entry": time_entries.create_time_entry,
    "update_time_entry": time_entries.update_time_entry,
    "delete_time_entry": time_entries.delete_time_entry,
    "stop_running_timer": time_entries.stop_running_timer,
    "list_clients": clients.list_clients,
    "create_client": clients.create_client,
    "list_tags": tags.list_tags,
    "create_tag": tags.create_tag,
    "list_tasks": tasks.list_tasks,
    "create_task": tasks.create_task,
}

def list_tools():
    return list(TOOLS.keys())

if __name__ == "__main__":
    FastMCP(
        tools=TOOLS,
        list_tools=list_tools,
    ).run_stdio()