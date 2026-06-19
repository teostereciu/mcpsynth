from mcp.server.fastmcp import FastMCP

from generated_tools.issues import (
    list_user_issues,
    list_repo_issues,
    get_issue,
    create_issue,
    update_issue,
)
from generated_tools.issue_comments import (
    list_repo_issue_comments,
    list_issue_comments,
    get_issue_comment,
    create_issue_comment,
    update_issue_comment,
    delete_issue_comment,
    pin_issue_comment,
    unpin_issue_comment,
)
from generated_tools.pull_requests import (
    list_pull_requests,
    get_pull_request,
    create_pull_request,
    update_pull_request,
    merge_pull_request,
)
from generated_tools.repos import (
    list_org_repos,
    get_repo,
    create_org_repo,
    update_repo,
)
from generated_tools.contents import (
    get_repo_content,
    create_or_update_file,
    delete_file,
)
from generated_tools.releases import (
    list_releases,
    get_latest_release,
    create_release,
    generate_release_notes,
)
from generated_tools.actions_workflows import (
    list_workflows,
    get_workflow,
    disable_workflow,
    enable_workflow,
    create_workflow_dispatch,
    get_workflow_usage,
)
from generated_tools.actions_runs import (
    list_workflow_runs,
    get_workflow_run,
    cancel_workflow_run,
    rerun_workflow_run,
    rerun_workflow_job,
)
from generated_tools.search import (
    search_code,
    search_issues_and_pull_requests,
    search_repositories,
)
from generated_tools.branch_protection import (
    get_branch_protection,
    update_branch_protection,
    delete_branch_protection,
)


mcp = FastMCP("github-rest")

# Issues
mcp.tool()(list_user_issues)
mcp.tool()(list_repo_issues)
mcp.tool()(get_issue)
mcp.tool()(create_issue)
mcp.tool()(update_issue)

# Issue comments
mcp.tool()(list_repo_issue_comments)
mcp.tool()(list_issue_comments)
mcp.tool()(get_issue_comment)
mcp.tool()(create_issue_comment)
mcp.tool()(update_issue_comment)
mcp.tool()(delete_issue_comment)
mcp.tool()(pin_issue_comment)
mcp.tool()(unpin_issue_comment)

# Pull requests
mcp.tool()(list_pull_requests)
mcp.tool()(get_pull_request)
mcp.tool()(create_pull_request)
mcp.tool()(update_pull_request)
mcp.tool()(merge_pull_request)

# Repos
mcp.tool()(list_org_repos)
mcp.tool()(get_repo)
mcp.tool()(create_org_repo)
mcp.tool()(update_repo)

# Contents
mcp.tool()(get_repo_content)
mcp.tool()(create_or_update_file)
mcp.tool()(delete_file)

# Releases
mcp.tool()(list_releases)
mcp.tool()(get_latest_release)
mcp.tool()(create_release)
mcp.tool()(generate_release_notes)

# Actions workflows
mcp.tool()(list_workflows)
mcp.tool()(get_workflow)
mcp.tool()(disable_workflow)
mcp.tool()(enable_workflow)
mcp.tool()(create_workflow_dispatch)
mcp.tool()(get_workflow_usage)

# Actions runs
mcp.tool()(list_workflow_runs)
mcp.tool()(get_workflow_run)
mcp.tool()(cancel_workflow_run)
mcp.tool()(rerun_workflow_run)
mcp.tool()(rerun_workflow_job)

# Search
mcp.tool()(search_code)
mcp.tool()(search_issues_and_pull_requests)
mcp.tool()(search_repositories)

# Branch protection
mcp.tool()(get_branch_protection)
mcp.tool()(update_branch_protection)
mcp.tool()(delete_branch_protection)


if __name__ == "__main__":
    mcp.run()
