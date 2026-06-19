from mcp.server.fastmcp import FastMCP

from generated_tools import actions, issues, pulls, releases, repos, search, webhooks

mcp = FastMCP("github-rest")

# Repos
mcp.tool()(repos.get_repo)
mcp.tool()(repos.list_user_repos)
mcp.tool()(repos.list_org_repos)
mcp.tool()(repos.create_repo)
mcp.tool()(repos.fork_repo)
mcp.tool()(repos.list_branches)
mcp.tool()(repos.get_branch)
mcp.tool()(repos.update_branch_protection)
mcp.tool()(repos.delete_branch_protection)
mcp.tool()(repos.get_commit)
mcp.tool()(repos.list_commits)
mcp.tool()(repos.get_content)
mcp.tool()(repos.create_or_update_file)
mcp.tool()(repos.delete_file)

# Issues
mcp.tool()(issues.list_repo_issues)
mcp.tool()(issues.get_issue)
mcp.tool()(issues.create_issue)
mcp.tool()(issues.update_issue)
mcp.tool()(issues.lock_issue)
mcp.tool()(issues.unlock_issue)
mcp.tool()(issues.list_issue_comments)
mcp.tool()(issues.create_issue_comment)
mcp.tool()(issues.update_issue_comment)
mcp.tool()(issues.delete_issue_comment)
mcp.tool()(issues.add_labels)
mcp.tool()(issues.set_labels)
mcp.tool()(issues.remove_label)
mcp.tool()(issues.list_labels)
mcp.tool()(issues.create_label)
mcp.tool()(issues.update_label)
mcp.tool()(issues.delete_label)
mcp.tool()(issues.add_assignees)
mcp.tool()(issues.remove_assignees)

# Pull requests
mcp.tool()(pulls.list_pull_requests)
mcp.tool()(pulls.get_pull_request)
mcp.tool()(pulls.create_pull_request)
mcp.tool()(pulls.update_pull_request)
mcp.tool()(pulls.list_pull_reviews)
mcp.tool()(pulls.create_pull_review)
mcp.tool()(pulls.merge_pull_request)
mcp.tool()(pulls.list_pull_files)
mcp.tool()(pulls.list_pull_comments)

# Releases
mcp.tool()(releases.list_releases)
mcp.tool()(releases.get_release)
mcp.tool()(releases.create_release)
mcp.tool()(releases.update_release)
mcp.tool()(releases.delete_release)

# Actions
mcp.tool()(actions.list_workflows)
mcp.tool()(actions.get_workflow)
mcp.tool()(actions.list_workflow_runs)
mcp.tool()(actions.get_workflow_run)
mcp.tool()(actions.rerun_workflow_run)
mcp.tool()(actions.cancel_workflow_run)
mcp.tool()(actions.list_repo_secrets)

# Search
mcp.tool()(search.search_code)
mcp.tool()(search.search_issues)
mcp.tool()(search.search_repositories)

# Webhooks
mcp.tool()(webhooks.list_repo_webhooks)
mcp.tool()(webhooks.get_repo_webhook)
mcp.tool()(webhooks.create_repo_webhook)
mcp.tool()(webhooks.update_repo_webhook)
mcp.tool()(webhooks.delete_repo_webhook)
mcp.tool()(webhooks.ping_repo_webhook)


if __name__ == "__main__":
    mcp.run()
