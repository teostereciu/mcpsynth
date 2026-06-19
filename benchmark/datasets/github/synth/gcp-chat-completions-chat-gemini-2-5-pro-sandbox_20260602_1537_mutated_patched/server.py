
import os
from mcp.server.fastmcp import FastMCP
from generated_tools.issues import list_issues_for_authenticated_user, list_organization_issues_for_authenticated_user, list_repository_issues, create_issue, get_issue, update_issue, lock_issue, unlock_issue
from generated_tools.repos import get_repository
from generated_tools.pulls import list_pull_requests, create_pull_request, get_pull_request, update_pull_request, merge_pull_request, list_pull_request_commits, list_pull_request_files, check_if_pull_request_has_been_merged
from generated_tools.releases import list_releases, create_release, get_release, update_release, delete_release, get_latest_release, get_release_by_tag
from generated_tools.actions import list_repository_workflows, get_workflow, disable_workflow, enable_workflow, create_workflow_dispatch_event, list_workflow_runs_for_repository, get_workflow_run, delete_workflow_run, cancel_workflow_run, retry_workflow_run, list_workflow_runs

# Create an MCP server
server = FastMCP()

# Register the tools
server.register_tool(list_issues_for_authenticated_user)
server.register_tool(list_organization_issues_for_authenticated_user)
server.register_tool(list_repository_issues)
server.register_tool(create_issue)
server.register_tool(get_issue)
server.register_tool(update_issue)
server.register_tool(lock_issue)
server.register_tool(unlock_issue)
server.register_tool(get_repository)
server.register_tool(list_pull_requests)
server.register_tool(create_pull_request)
server.register_tool(get_pull_request)
server.register_tool(update_pull_request)
server.register_tool(merge_pull_request)
server.register_tool(list_pull_request_commits)
server.register_tool(list_pull_request_files)
server.register_tool(check_if_pull_request_has_been_merged)
server.register_tool(list_releases)
server.register_tool(create_release)
server.register_tool(get_release)
server.register_tool(update_release)
server.register_tool(delete_release)
server.register_tool(get_latest_release)
server.register_tool(get_release_by_tag)
server.register_tool(list_repository_workflows)
server.register_tool(get_workflow)
server.register_tool(disable_workflow)
server.register_tool(enable_workflow)
server.register_tool(create_workflow_dispatch_event)
server.register_tool(list_workflow_runs_for_repository)
server.register_tool(get_workflow_run)
server.register_tool(delete_workflow_run)
server.register_tool(cancel_workflow_run)
server.register_tool(retry_workflow_run)
server.register_tool(list_workflow_runs)


if __name__ == "__main__":
    server.run()
