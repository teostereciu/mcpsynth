"""Notion MCP Server — entry point.

Runs over stdio and exposes Notion API tools via the MCP protocol.
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
        "This server exposes the Notion API as MCP tools. "
        "Use it to create, read, update, and delete Notion pages, databases, blocks, "
        "comments, views, data sources, file uploads, and users. "
        "All IDs can be provided with or without dashes (UUIDv4 format). "
        "The NOTION_API_KEY environment variable must be set to a valid integration token."
    ),
)

# Register all domain tool groups
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
