from mcp.server.fastmcp import FastMCP

from generated_tools.actions import cancel_workflow_run, get_workflow_run, list_workflow_runs, rerun_workflow
from generated_tools.branches import delete_branch_protection, get_branch_protection, update_branch_protection
from generated_tools.issues import create_issue, create_issue_comment, get_issue, list_issue_comments, list_repository_issues, update_issue
from generated_tools.pulls import create_pull_request, get_pull_request, list_pull_requests, merge_pull_request, update_pull_request
from generated_tools.releases import create_release, generate_release_notes, get_latest_release, list_releases
from generated_tools.repos import create_org_repository, create_or_update_file, delete_file, get_repository, get_repository_content, list_org_repositories
from generated_tools.search import search_code, search_issues_and_pull_requests, search_repositories, search_users
from generated_tools.webhooks import create_repository_webhook, delete_repository_webhook, get_repository_webhook, list_repository_webhooks, update_repository_webhook

mcp = FastMCP("github-rest")

mcp.tool()(list_repository_issues)
mcp.tool()(get_issue)
mcp.tool()(create_issue)
mcp.tool()(update_issue)
mcp.tool()(create_issue_comment)
mcp.tool()(list_issue_comments)

mcp.tool()(list_pull_requests)
mcp.tool()(get_pull_request)
mcp.tool()(create_pull_request)
mcp.tool()(update_pull_request)
mcp.tool()(merge_pull_request)

mcp.tool()(get_repository)
mcp.tool()(list_org_repositories)
mcp.tool()(create_org_repository)
mcp.tool()(get_repository_content)
mcp.tool()(create_or_update_file)
mcp.tool()(delete_file)

mcp.tool()(list_releases)
mcp.tool()(get_latest_release)
mcp.tool()(create_release)
mcp.tool()(generate_release_notes)

mcp.tool()(list_workflow_runs)
mcp.tool()(get_workflow_run)
mcp.tool()(rerun_workflow)
mcp.tool()(cancel_workflow_run)

mcp.tool()(search_repositories)
mcp.tool()(search_code)
mcp.tool()(search_issues_and_pull_requests)
mcp.tool()(search_users)

mcp.tool()(list_repository_webhooks)
mcp.tool()(get_repository_webhook)
mcp.tool()(create_repository_webhook)
mcp.tool()(update_repository_webhook)
mcp.tool()(delete_repository_webhook)

mcp.tool()(get_branch_protection)
mcp.tool()(update_branch_protection)
mcp.tool()(delete_branch_protection)

if __name__ == "__main__":
    mcp.run()
