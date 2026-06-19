from mcp.server.fastmcp import FastMCP

from generated_tools import (
    list_my_issues,
    list_pull_requests,
    list_org_repos,
    create_org_repo,
    get_repo_content,
    create_or_update_file_contents,
    delete_file,
    list_releases,
    create_release,
    generate_release_notes,
    list_workflow_runs,
    rerun_workflow_job,
    search_code,
    get_branch_protection,
    update_branch_protection,
    list_repo_webhooks,
    create_repo_webhook,
    get_repo_webhook,
    update_repo_webhook,
)

mcp = FastMCP("github-rest")

# Issues
mcp.tool()(list_my_issues)

# Pull requests
mcp.tool()(list_pull_requests)

# Repos + contents
mcp.tool()(list_org_repos)
mcp.tool()(create_org_repo)
mcp.tool()(get_repo_content)
mcp.tool()(create_or_update_file_contents)
mcp.tool()(delete_file)

# Releases
mcp.tool()(list_releases)
mcp.tool()(create_release)
mcp.tool()(generate_release_notes)

# Actions
mcp.tool()(list_workflow_runs)
mcp.tool()(rerun_workflow_job)

# Search
mcp.tool()(search_code)

# Branch protection
mcp.tool()(get_branch_protection)
mcp.tool()(update_branch_protection)

# Webhooks
mcp.tool()(list_repo_webhooks)
mcp.tool()(create_repo_webhook)
mcp.tool()(get_repo_webhook)
mcp.tool()(update_repo_webhook)


if __name__ == "__main__":
    mcp.run()
