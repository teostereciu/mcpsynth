"""FastMCP server exposing Notion API tools."""

from __future__ import annotations

from fastmcp import FastMCP

from . import blocks, comments, databases, pages, search, users

mcp = FastMCP("notion-mcp")

# Pages
mcp.tool()(pages.create_page)
mcp.tool()(pages.retrieve_page)
mcp.tool()(pages.update_page)
mcp.tool()(pages.retrieve_page_property_item)
mcp.tool()(pages.move_page)

# Databases
mcp.tool()(databases.create_database)
mcp.tool()(databases.retrieve_database)
mcp.tool()(databases.update_database)
mcp.tool()(databases.query_database)
mcp.tool()(databases.list_databases)

# Blocks
mcp.tool()(blocks.retrieve_block)
mcp.tool()(blocks.list_block_children)
mcp.tool()(blocks.append_block_children)
mcp.tool()(blocks.update_block)
mcp.tool()(blocks.delete_block)

# Comments
mcp.tool()(comments.create_comment)
mcp.tool()(comments.retrieve_comment)
mcp.tool()(comments.list_comments)

# Users
mcp.tool()(users.list_users)
mcp.tool()(users.retrieve_user)
mcp.tool()(users.retrieve_me)

# Search
mcp.tool()(search.search)
