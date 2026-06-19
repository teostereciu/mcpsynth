import os

from mcp.server.fastmcp import FastMCP

from generated_tools import (
    actions_runs,
    actions_workflows,
    branch_protection,
    contents,
    issue_comments,
    issues,
    pulls,
    releases,
    repos,
    search,
)
from generated_tools._client import parse_owner_repo


mcp = FastMCP("github-rest")


def _default_owner_repo():
    owner, repo = parse_owner_repo(os.getenv("GITHUB_TEST_REPO"))
    return owner, repo


# Issues
mcp.tool()(issues.list_my_issues)
mcp.tool()(issues.list_repo_issues)
mcp.tool()(issues.create_issue)
mcp.tool()(issues.get_issue)
mcp.tool()(issues.update_issue)

# Issue comments
mcp.tool()(issue_comments.list_repo_issue_comments)
mcp.tool()(issue_comments.list_issue_comments)
mcp.tool()(issue_comments.create_issue_comment)
mcp.tool()(issue_comments.get_issue_comment)
mcp.tool()(issue_comments.update_issue_comment)
mcp.tool()(issue_comments.delete_issue_comment)

# Pull requests
mcp.tool()(pulls.list_pulls)
mcp.tool()(pulls.create_pull)
mcp.tool()(pulls.get_pull)
mcp.tool()(pulls.update_pull)
mcp.tool()(pulls.list_pull_commits)
mcp.tool()(pulls.list_pull_files)
mcp.tool()(pulls.merge_pull)
mcp.tool()(pulls.update_pull_branch)

# Repos
mcp.tool()(repos.get_repo)
mcp.tool()(repos.list_org_repos)
mcp.tool()(repos.create_org_repo)
mcp.tool()(repos.delete_repo)
mcp.tool()(repos.fork_repo)

# Contents
mcp.tool()(contents.get_content)
mcp.tool()(contents.put_file_contents)
mcp.tool()(contents.delete_file)

# Releases
mcp.tool()(releases.list_releases)
mcp.tool()(releases.create_release)
mcp.tool()(releases.generate_release_notes)
mcp.tool()(releases.get_latest_release)

# Actions workflows
mcp.tool()(actions_workflows.list_workflows)
mcp.tool()(actions_workflows.get_workflow)
mcp.tool()(actions_workflows.enable_workflow)
mcp.tool()(actions_workflows.disable_workflow)
mcp.tool()(actions_workflows.dispatch_workflow)
mcp.tool()(actions_workflows.get_workflow_usage)

# Actions runs
mcp.tool()(actions_runs.list_workflow_runs)
mcp.tool()(actions_runs.get_workflow_run)
mcp.tool()(actions_runs.cancel_workflow_run)
mcp.tool()(actions_runs.rerun_workflow_run)
mcp.tool()(actions_runs.rerun_job)

# Search
mcp.tool()(search.search_code)
mcp.tool()(search.search_issues)
mcp.tool()(search.search_repositories)

# Branch protection
mcp.tool()(branch_protection.get_branch_protection)
mcp.tool()(branch_protection.update_branch_protection)


@mcp.tool()
def get_test_repo() -> dict:
    """Return the configured test repository (from GITHUB_TEST_REPO) split into owner/repo."""
    owner, repo = _default_owner_repo()
    return {"owner": owner, "repo": repo, "owner_repo": os.getenv("GITHUB_TEST_REPO")}


if __name__ == "__main__":
    mcp.run()
