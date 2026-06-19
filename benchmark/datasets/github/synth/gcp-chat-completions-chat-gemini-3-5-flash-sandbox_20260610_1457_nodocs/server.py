import logging
from mcp.server.fastmcp import FastMCP

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mcp-github-server")

# Initialize FastMCP server
mcp = FastMCP("GitHub REST API")

# Import tools
from generated_tools.issues import (
    list_issues,
    get_issue,
    create_issue,
    update_issue,
    add_issue_labels,
    remove_issue_label,
    add_issue_assignees,
    remove_issue_assignees,
    list_issue_comments,
    create_issue_comment,
    update_issue_comment,
    delete_issue_comment
)

from generated_tools.pull_requests import (
    list_pull_requests,
    get_pull_request,
    create_pull_request,
    update_pull_request,
    create_pull_request_review,
    merge_pull_request
)

from generated_tools.repositories import (
    get_repository,
    create_repository,
    create_fork,
    list_branches,
    get_branch,
    list_commits,
    get_commit,
    get_repository_content,
    create_or_update_file_contents,
    delete_file
)

from generated_tools.releases import (
    list_releases,
    get_release,
    get_latest_release,
    create_release,
    update_release,
    delete_release
)

from generated_tools.actions import (
    list_workflows,
    get_workflow,
    list_workflow_runs,
    get_workflow_run,
    trigger_workflow_dispatch
)

from generated_tools.search import (
    search_code
)

from generated_tools.webhooks import (
    list_repository_webhooks,
    get_repository_webhook,
    create_repository_webhook,
    update_repository_webhook,
    delete_repository_webhook
)

from generated_tools.branch_protection import (
    get_branch_protection,
    update_branch_protection,
    delete_branch_protection
)

# Register tools with FastMCP
tools_to_register = [
    # Issues
    list_issues,
    get_issue,
    create_issue,
    update_issue,
    add_issue_labels,
    remove_issue_label,
    add_issue_assignees,
    remove_issue_assignees,
    list_issue_comments,
    create_issue_comment,
    update_issue_comment,
    delete_issue_comment,
    
    # Pull Requests
    list_pull_requests,
    get_pull_request,
    create_pull_request,
    update_pull_request,
    create_pull_request_review,
    merge_pull_request,
    
    # Repositories
    get_repository,
    create_repository,
    create_fork,
    list_branches,
    get_branch,
    list_commits,
    get_commit,
    get_repository_content,
    create_or_update_file_contents,
    delete_file,
    
    # Releases
    list_releases,
    get_release,
    get_latest_release,
    create_release,
    update_release,
    delete_release,
    
    # Actions
    list_workflows,
    get_workflow,
    list_workflow_runs,
    get_workflow_run,
    trigger_workflow_dispatch,
    
    # Search
    search_code,
    
    # Webhooks
    list_repository_webhooks,
    get_repository_webhook,
    create_repository_webhook,
    update_repository_webhook,
    delete_repository_webhook,
    
    # Branch Protection
    get_branch_protection,
    update_branch_protection,
    delete_branch_protection
]

for tool_func in tools_to_register:
    mcp.tool()(tool_func)

if __name__ == "__main__":
    logger.info("Starting GitHub MCP Server...")
    mcp.run()
