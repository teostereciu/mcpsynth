import os
from typing import Any, Dict, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools.issues import create_issue, get_issue, list_my_issues, list_repo_issues, update_issue
from generated_tools.pulls import (
    create_pull_request,
    get_pull_request,
    list_pull_requests,
    merge_pull_request,
    update_pull_request,
)
from generated_tools.repos import create_org_repo, delete_repo, get_repo, list_org_repos, update_repo
from generated_tools.contents import create_or_update_file_contents, delete_file, get_repo_content
from generated_tools.releases import create_release, generate_release_notes, get_latest_release, list_releases
from generated_tools.actions_workflows import (
    create_workflow_dispatch,
    disable_workflow,
    enable_workflow,
    get_workflow,
    get_workflow_usage,
    list_repo_workflows,
)
from generated_tools.actions_runs import (
    cancel_workflow_run,
    get_workflow_run,
    list_workflow_runs_for_repo,
    rerun_job,
    rerun_workflow_run,
)
from generated_tools.search import search_code, search_issues_and_prs, search_repositories
from generated_tools.branch_protection import delete_branch_protection, get_branch_protection, update_branch_protection

mcp = FastMCP("github-rest")


@mcp.tool()
def github_test_repo() -> Dict[str, Any]:
    """Return the configured test repo (owner/repo) from env, if set."""
    return {"GITHUB_TEST_REPO": os.getenv("GITHUB_TEST_REPO")}


# Issues
mcp.tool()(list_my_issues)
mcp.tool()(list_repo_issues)
mcp.tool()(create_issue)
mcp.tool()(get_issue)
mcp.tool()(update_issue)

# Pull requests
mcp.tool()(list_pull_requests)
mcp.tool()(create_pull_request)
mcp.tool()(get_pull_request)
mcp.tool()(update_pull_request)
mcp.tool()(merge_pull_request)

# Repos
mcp.tool()(get_repo)
mcp.tool()(list_org_repos)
mcp.tool()(create_org_repo)
mcp.tool()(update_repo)
mcp.tool()(delete_repo)

# Contents
mcp.tool()(get_repo_content)
mcp.tool()(create_or_update_file_contents)
mcp.tool()(delete_file)

# Releases
mcp.tool()(list_releases)
mcp.tool()(get_latest_release)
mcp.tool()(generate_release_notes)
mcp.tool()(create_release)

# Actions
mcp.tool()(list_repo_workflows)
mcp.tool()(get_workflow)
mcp.tool()(enable_workflow)
mcp.tool()(disable_workflow)
mcp.tool()(create_workflow_dispatch)
mcp.tool()(get_workflow_usage)

mcp.tool()(list_workflow_runs_for_repo)
mcp.tool()(get_workflow_run)
mcp.tool()(cancel_workflow_run)
mcp.tool()(rerun_workflow_run)
mcp.tool()(rerun_job)

# Search
mcp.tool()(search_code)
mcp.tool()(search_issues_and_prs)
mcp.tool()(search_repositories)

# Branch protection
mcp.tool()(get_branch_protection)
mcp.tool()(update_branch_protection)
mcp.tool()(delete_branch_protection)


if __name__ == "__main__":
    mcp.run()
