from mcp.server.fastmcp import FastMCP

from generated_tools.repositories import (
    repo_get,
    repo_delete,
    repo_search,
    repo_migrate,
    repo_edit,
    repo_fork,
    repo_create_for_authenticated_user,
    user_repos_list as repos_user_repos_list,
    org_repos_list as repos_org_repos_list,
    repo_branches_list,
    repo_branch_get,
    repo_branch_create,
    repo_commits_list,
    repo_commit_get,
    repo_releases_list,
    repo_release_get,
    repo_release_create,
)
from generated_tools.issues import (
    issues_search_accessible,
    repo_issues_list,
    repo_issue_get,
    repo_issue_create,
    repo_issue_update,
    repo_issue_close,
    repo_issue_labels_add,
    repo_issue_comment_add,
    repo_issue_comments_list,
)
from generated_tools.pull_requests import (
    repo_pulls_list,
    repo_pull_get,
    repo_pull_create,
    repo_pull_merge,
)
from generated_tools.users import (
    user_me,
    user_get,
    users_search,
    user_repos_list,
    my_repos_list,
)
from generated_tools.organizations import (
    orgs_list,
    org_get,
    org_repos_list,
)
from generated_tools.misc import (
    version,
    nodeinfo,
    gitignore_templates_list,
    gitignore_template_get,
    licenses_list,
    license_get,
    markdown_render,
    markdown_render_raw,
)

mcp = FastMCP("forgejo-codeberg")

# Repositories
mcp.tool()(repo_get)
mcp.tool()(repo_delete)
mcp.tool()(repo_search)
mcp.tool()(repo_migrate)
mcp.tool()(repo_edit)
mcp.tool()(repo_fork)
mcp.tool()(repo_create_for_authenticated_user)
mcp.tool()(repos_user_repos_list)
mcp.tool()(repos_org_repos_list)

# Branches / Commits / Releases
mcp.tool()(repo_branches_list)
mcp.tool()(repo_branch_get)
mcp.tool()(repo_branch_create)
mcp.tool()(repo_commits_list)
mcp.tool()(repo_commit_get)
mcp.tool()(repo_releases_list)
mcp.tool()(repo_release_get)
mcp.tool()(repo_release_create)

# Issues
mcp.tool()(issues_search_accessible)
mcp.tool()(repo_issues_list)
mcp.tool()(repo_issue_get)
mcp.tool()(repo_issue_create)
mcp.tool()(repo_issue_update)
mcp.tool()(repo_issue_close)
mcp.tool()(repo_issue_labels_add)
mcp.tool()(repo_issue_comment_add)
mcp.tool()(repo_issue_comments_list)

# Pull Requests
mcp.tool()(repo_pulls_list)
mcp.tool()(repo_pull_get)
mcp.tool()(repo_pull_create)
mcp.tool()(repo_pull_merge)

# Users
mcp.tool()(user_me)
mcp.tool()(user_get)
mcp.tool()(users_search)
mcp.tool()(user_repos_list)
mcp.tool()(my_repos_list)

# Organizations
mcp.tool()(orgs_list)
mcp.tool()(org_get)
mcp.tool()(org_repos_list)

# Misc
mcp.tool()(version)
mcp.tool()(nodeinfo)
mcp.tool()(gitignore_templates_list)
mcp.tool()(gitignore_template_get)
mcp.tool()(licenses_list)
mcp.tool()(license_get)
mcp.tool()(markdown_render)
mcp.tool()(markdown_render_raw)


if __name__ == "__main__":
    mcp.run()
