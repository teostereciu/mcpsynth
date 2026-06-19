from mcp.server.fastmcp import FastMCP

from generated_tools.users import get_authenticated_user, get_user, search_users
from generated_tools.orgs import list_my_orgs, get_org, list_org_repos
from generated_tools.repos import list_my_repos, get_repo, create_repo, delete_repo, fork_repo
from generated_tools.issues import (
    list_issues,
    get_issue,
    create_issue,
    update_issue,
    close_issue,
    add_issue_labels,
    create_issue_comment,
)
from generated_tools.pulls import list_pull_requests, get_pull_request, create_pull_request, merge_pull_request
from generated_tools.branches import list_branches, get_branch, create_branch
from generated_tools.commits import list_commits, get_commit
from generated_tools.releases import list_releases, get_release, create_release

mcp = FastMCP("forgejo-codeberg")

# Users
mcp.tool()(get_authenticated_user)
mcp.tool()(get_user)
mcp.tool()(search_users)

# Orgs
mcp.tool()(list_my_orgs)
mcp.tool()(get_org)
mcp.tool()(list_org_repos)

# Repos
mcp.tool()(list_my_repos)
mcp.tool()(get_repo)
mcp.tool()(create_repo)
mcp.tool()(delete_repo)
mcp.tool()(fork_repo)

# Issues
mcp.tool()(list_issues)
mcp.tool()(get_issue)
mcp.tool()(create_issue)
mcp.tool()(update_issue)
mcp.tool()(close_issue)
mcp.tool()(add_issue_labels)
mcp.tool()(create_issue_comment)

# Pull Requests
mcp.tool()(list_pull_requests)
mcp.tool()(get_pull_request)
mcp.tool()(create_pull_request)
mcp.tool()(merge_pull_request)

# Branches
mcp.tool()(list_branches)
mcp.tool()(get_branch)
mcp.tool()(create_branch)

# Commits
mcp.tool()(list_commits)
mcp.tool()(get_commit)

# Releases
mcp.tool()(list_releases)
mcp.tool()(get_release)
mcp.tool()(create_release)

if __name__ == "__main__":
    mcp.run()
