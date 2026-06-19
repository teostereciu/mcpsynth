"""
Confluence Cloud MCP Server

Exposes Confluence Cloud REST API (v1 + v2) operations as MCP tools.
Runs over stdio using FastMCP.

Required environment variables:
  CONFLUENCE_BASE_URL  — e.g. https://yoursite.atlassian.net/wiki
  CONFLUENCE_SPACE_KEY — default space key (e.g. SYNTH)
  JIRA_EMAIL           — Atlassian account email
  JIRA_API_TOKEN       — Atlassian API token
"""

from mcp.server.fastmcp import FastMCP

from generated_tools import (
    pages,
    spaces,
    blog_posts,
    attachments,
    labels,
    comments,
    versions,
    content_properties,
    search,
    users,
)

mcp = FastMCP("confluence")

# Register all domain tool groups
pages.register(mcp)
spaces.register(mcp)
blog_posts.register(mcp)
attachments.register(mcp)
labels.register(mcp)
comments.register(mcp)
versions.register(mcp)
content_properties.register(mcp)
search.register(mcp)
users.register(mcp)

if __name__ == "__main__":
    mcp.run(transport="stdio")
