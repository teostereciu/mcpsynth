from fastmcp import FastMCP

from generated_tools.issues import (
    list_issues, get_issue, create_issue, update_issue,
    list_issue_comments, create_issue_comment,
    add_issue_labels, remove_issue_label,
    add_issue_assignees, remove_issue_assignees
)
from generated_tools.pulls import (
    list_pull_requests, get_pull_request, create_pull_request, update_pull_request,
    merge_pull_request, create_pull_request_review
)
from generated_tools.repos import (
    get_repository, create_repository, update_repository, delete_repository,
    create_fork, list_branches, list_commits, get_repository_content,
    create_or_update_file_contents, delete_file
)
from generated_tools.releases import list_releases, create_release
from generated_tools.actions import list_repository_workflows, list_workflow_runs, create_workflow_dispatch
from generated_tools.search import search_code, search_issues, search_repositories
from generated_tools.webhooks import list_repository_webhooks, create_repository_webhook
from generated_tools.branches import get_branch_protection, update_branch_protection

# Initialize FastMCP server
mcp = FastMCP("github-rest-api")

# Register tools
mcp.tool()(list_issues)
mcp.tool()(get_issue)
mcp.tool()(create_issue)
mcp.tool()(update_issue)
mcp.tool()(list_issue_comments)
mcp.tool()(create_issue_comment)
mcp.tool()(add_issue_labels)
mcp.tool()(remove_issue_label)
mcp.tool()(add_issue_assignees)
mcp.tool()(remove_issue_assignees)

mcp.tool()(list_pull_requests)
mcp.tool()(get_pull_request)
mcp.tool()(create_pull_request)
mcp.tool()(update_pull_request)
mcp.tool()(merge_pull_request)
mcp.tool()(create_pull_request_review)

mcp.tool()(get_repository)
mcp.tool()(create_repository)
mcp.tool()(update_repository)
mcp.tool()(delete_repository)
mcp.tool()(create_fork)
mcp.tool()(list_branches)
mcp.tool()(list_commits)
mcp.tool()(get_repository_content)
mcp.tool()(create_or_update_file_contents)
mcp.tool()(delete_file)

mcp.tool()(list_releases)
mcp.tool()(create_release)

mcp.tool()(list_repository_workflows)
mcp.tool()(list_workflow_runs)
mcp.tool()(create_workflow_dispatch)

mcp.tool()(search_code)
mcp.tool()(search_issues)
mcp.tool()(search_repositories)

mcp.tool()(list_repository_webhooks)
mcp.tool()(create_repository_webhook)

mcp.tool()(get_branch_protection)
mcp.tool()(update_branch_protection)

if __name__ == "__main__":
    mcp.run()
