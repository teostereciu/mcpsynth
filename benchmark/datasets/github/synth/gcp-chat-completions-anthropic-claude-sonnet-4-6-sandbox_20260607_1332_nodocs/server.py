"""
GitHub REST API MCP Server
Runs over stdio using FastMCP.
"""
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    name="github-api",
    instructions=(
        "This server exposes tools for the GitHub REST API. "
        "Set GITHUB_TOKEN to authenticate. "
        "Set GITHUB_API_BASE_URL to override the base URL (e.g. for GitHub Enterprise). "
        "All tools return JSON-serializable results. Errors are returned as dicts with an 'error' key."
    ),
)

# Register all domain modules
from generated_tools import (
    issues,
    pulls,
    repos,
    releases,
    actions,
    search,
    webhooks,
    users,
    gists,
    notifications,
    checks,
    projects,
    code_scanning,
    meta,
    deployments,
)

issues.register(mcp)
pulls.register(mcp)
repos.register(mcp)
releases.register(mcp)
actions.register(mcp)
search.register(mcp)
webhooks.register(mcp)
users.register(mcp)
gists.register(mcp)
notifications.register(mcp)
checks.register(mcp)
projects.register(mcp)
code_scanning.register(mcp)
meta.register(mcp)
deployments.register(mcp)

if __name__ == "__main__":
    mcp.run(transport="stdio")
