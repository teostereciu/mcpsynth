from mcp.server.fastmcp import FastMCP

from generated_tools import (
    actions_runs,
    actions_workflows,
    branch_protection,
    contents,
    issue_comments,
    issues,
    pull_reviews,
    pulls,
    releases,
    repos,
    search,
    webhooks,
)

mcp = FastMCP("github-rest")

# Issues
mcp.tool()(issues.list_my_issues)
mcp.tool()(issues.list_repo_issues)
mcp.tool()(issues.get_issue)
mcp.tool()(issues.create_issue)
mcp.tool()(issues.update_issue)
mcp.tool()(issues.lock_issue)
mcp.tool()(issues.unlock_issue)

# Issue comments
mcp.tool()(issue_comments.list_repo_issue_comments)
mcp.tool()(issue_comments.list_issue_comments)
mcp.tool()(issue_comments.get_issue_comment)
mcp.tool()(issue_comments.create_issue_comment)
mcp.tool()(issue_comments.update_issue_comment)
mcp.tool()(issue_comments.delete_issue_comment)
mcp.tool()(issue_comments.pin_issue_comment)
mcp.tool()(issue_comments.unpin_issue_comment)

# Pull requests
mcp.tool()(pulls.list_pulls)
mcp.tool()(pulls.get_pull)
mcp.tool()(pulls.create_pull)
mcp.tool()(pulls.update_pull)
mcp.tool()(pulls.merge_pull)

# Pull request reviews
mcp.tool()(pull_reviews.list_pull_reviews)
mcp.tool()(pull_reviews.create_pull_review)
mcp.tool()(pull_reviews.get_pull_review)
mcp.tool()(pull_reviews.submit_pull_review)
mcp.tool()(pull_reviews.dismiss_pull_review)

# Repositories
mcp.tool()(repos.get_repo)
mcp.tool()(repos.list_org_repos)
mcp.tool()(repos.create_org_repo)
mcp.tool()(repos.create_user_repo)
mcp.tool()(repos.fork_repo)
mcp.tool()(repos.list_forks)

# Contents
mcp.tool()(contents.get_content)
mcp.tool()(contents.create_or_update_file)
mcp.tool()(contents.delete_file)

# Releases
mcp.tool()(releases.list_releases)
mcp.tool()(releases.get_latest_release)
mcp.tool()(releases.create_release)
mcp.tool()(releases.generate_release_notes)

# Actions
mcp.tool()(actions_workflows.list_workflows)
mcp.tool()(actions_workflows.get_workflow)
mcp.tool()(actions_workflows.disable_workflow)
mcp.tool()(actions_workflows.enable_workflow)
mcp.tool()(actions_workflows.dispatch_workflow)
mcp.tool()(actions_workflows.get_workflow_timing)

mcp.tool()(actions_runs.list_workflow_runs)
mcp.tool()(actions_runs.get_workflow_run)
mcp.tool()(actions_runs.cancel_workflow_run)
mcp.tool()(actions_runs.rerun_workflow_run)
mcp.tool()(actions_runs.rerun_job)

# Search
mcp.tool()(search.search_code)
mcp.tool()(search.search_issues_and_prs)
mcp.tool()(search.search_repositories)

# Webhooks
mcp.tool()(webhooks.list_repo_webhooks)
mcp.tool()(webhooks.get_repo_webhook)
mcp.tool()(webhooks.create_repo_webhook)
mcp.tool()(webhooks.update_repo_webhook)
mcp.tool()(webhooks.delete_repo_webhook)
mcp.tool()(webhooks.ping_repo_webhook)

# Branch protection
mcp.tool()(branch_protection.get_branch_protection)
mcp.tool()(branch_protection.update_branch_protection)
mcp.tool()(branch_protection.delete_branch_protection)


if __name__ == "__main__":
    mcp.run()
