"""GitHub REST API MCP Server — entry point."""
import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("github-rest-api")

# Register all domain tool modules
from generated_tools.issues import register_issues_tools
from generated_tools.pulls import register_pulls_tools
from generated_tools.repos import register_repos_tools
from generated_tools.branches import register_branches_tools
from generated_tools.releases import register_releases_tools
from generated_tools.actions import register_actions_tools
from generated_tools.search import register_search_tools
from generated_tools.webhooks import register_webhooks_tools
from generated_tools.commits import register_commits_tools
from generated_tools.git_refs import register_git_refs_tools
from generated_tools.users import register_users_tools
from generated_tools.orgs import register_orgs_tools
from generated_tools.teams import register_teams_tools
from generated_tools.gists import register_gists_tools
from generated_tools.deployments import register_deployments_tools

register_issues_tools(mcp)
register_pulls_tools(mcp)
register_repos_tools(mcp)
register_branches_tools(mcp)
register_releases_tools(mcp)
register_actions_tools(mcp)
register_search_tools(mcp)
register_webhooks_tools(mcp)
register_commits_tools(mcp)
register_git_refs_tools(mcp)
register_users_tools(mcp)
register_orgs_tools(mcp)
register_teams_tools(mcp)
register_gists_tools(mcp)
register_deployments_tools(mcp)

if __name__ == "__main__":
    mcp.run(transport="stdio")
