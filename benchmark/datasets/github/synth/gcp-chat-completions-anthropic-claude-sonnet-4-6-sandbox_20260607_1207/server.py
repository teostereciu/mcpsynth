"""GitHub REST API MCP Server — entry point."""
import os
from mcp.server.fastmcp import FastMCP

# Import all domain registration functions
from generated_tools.issues import register_issues_tools
from generated_tools.pulls import register_pulls_tools
from generated_tools.repos import register_repos_tools
from generated_tools.branches import register_branches_tools
from generated_tools.releases import register_releases_tools
from generated_tools.actions import register_actions_tools
from generated_tools.search import register_search_tools
from generated_tools.webhooks import register_webhooks_tools
from generated_tools.commits import register_commits_tools
from generated_tools.users import register_users_tools
from generated_tools.git_objects import register_git_objects_tools
from generated_tools.deploy_keys import register_deploy_keys_tools

mcp = FastMCP(
    name="github-rest-api",
    instructions=(
        "MCP server for the GitHub REST API. "
        "Provides tools for managing issues, pull requests, repositories, branches, "
        "releases, GitHub Actions, code search, webhooks, commits, users, and more. "
        "Set GITHUB_TOKEN env var for authentication. "
        "Set GITHUB_API_BASE_URL for GitHub Enterprise (default: https://api.github.com)."
    ),
)

# Register all tool domains
register_issues_tools(mcp)
register_pulls_tools(mcp)
register_repos_tools(mcp)
register_branches_tools(mcp)
register_releases_tools(mcp)
register_actions_tools(mcp)
register_search_tools(mcp)
register_webhooks_tools(mcp)
register_commits_tools(mcp)
register_users_tools(mcp)
register_git_objects_tools(mcp)
register_deploy_keys_tools(mcp)

if __name__ == "__main__":
    mcp.run(transport="stdio")
