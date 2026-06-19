"""Notion MCP Server — entry point.

Runs over stdio using FastMCP and exposes tools for the Notion API.
"""
from mcp.server.fastmcp import FastMCP

from generated_tools import (
    pages,
    databases,
    blocks,
    users,
    comments,
    search,
    data_sources,
    views,
    file_uploads,
)

mcp = FastMCP(
    name="notion",
    instructions=(
        "A comprehensive MCP server for the Notion API. "
        "Supports pages, databases, blocks, comments, users, search, "
        "data sources, views, and file uploads."
    ),
)

# Register all tool groups
pages.register(mcp)
databases.register(mcp)
blocks.register(mcp)
users.register(mcp)
comments.register(mcp)
search.register(mcp)
data_sources.register(mcp)
views.register(mcp)
file_uploads.register(mcp)

if __name__ == "__main__":
    mcp.run(transport="stdio")
